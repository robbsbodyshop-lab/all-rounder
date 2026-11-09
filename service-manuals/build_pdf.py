#!/usr/bin/env python3
"""Build a printable shop-manual PDF from a Markdown source file.

Usage:
    python3 service-manuals/build_pdf.py <manual.md> <output.pdf>

The Markdown dialect is a small, predictable subset so technicians can edit
the source on GitHub and rebuild the PDF without extra dependencies
(only reportlab is required):

    ---                     front matter (key: value) for the cover page
    ## Heading              section heading (h1)
    ### Heading             sub-heading (h2)
    #### Heading            minor heading (h3)
    1. Step text            numbered step (continuation lines indented 3+ spaces;
                            "   - item" inside a step becomes a sub-bullet)
    - Bullet                bullet item
    - [ ] Check item        checklist item with a tick box
    > **WARNING:** text     WARNING / CAUTION / NOTE call-out box
    | a | b |               pipe table (first row is the header)
    [[FLOW: A: x > B: y]]   horizontal process-flow diagram ("tag: label" per box)
    [[SIGNOFF]]             technician sign-off block
    <!-- pagebreak -->      force a new page
    **bold**  *italic*  `mono`  [VERIFY]   inline markup
"""

import re
import sys
from pathlib import Path

from reportlab.graphics.shapes import Drawing, Line, Polygon, Rect, String
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.platypus import (
    CondPageBreak,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

# --------------------------------------------------------------------------
# Fonts
# --------------------------------------------------------------------------
LIB = "/usr/share/fonts/truetype/liberation/"
DJV = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("Body", LIB + "LiberationSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Body-Bold", LIB + "LiberationSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Body-Italic", LIB + "LiberationSans-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Body-BoldItalic", LIB + "LiberationSans-BoldItalic.ttf"))
pdfmetrics.registerFont(TTFont("Mono", DJV + "DejaVuSansMono.ttf"))
pdfmetrics.registerFont(TTFont("Symbols", DJV + "DejaVuSans.ttf"))
pdfmetrics.registerFontFamily(
    "Body", normal="Body", bold="Body-Bold", italic="Body-Italic", boldItalic="Body-BoldItalic"
)

# --------------------------------------------------------------------------
# Palette
# --------------------------------------------------------------------------
INK = colors.HexColor("#1b2430")
MUTED = colors.HexColor("#5b6675")
RULE = colors.HexColor("#c9d1db")
NAVY = colors.HexColor("#14284b")
ACCENT = colors.HexColor("#1f5fa8")
TABLE_HEAD = colors.HexColor("#e6ecf4")
ZEBRA = colors.HexColor("#f6f8fb")
CALLOUTS = {
    "WARNING": (colors.HexColor("#b3261e"), colors.HexColor("#fdecea")),
    "CAUTION": (colors.HexColor("#a15c00"), colors.HexColor("#fff4e0")),
    "NOTE": (colors.HexColor("#1f5fa8"), colors.HexColor("#eaf2fb")),
}
VERIFY_BG = "#ffe08a"

PAGE_W, PAGE_H = letter
MARGIN = 0.75 * inch
CONTENT_W = PAGE_W - 2 * MARGIN

# --------------------------------------------------------------------------
# Paragraph styles
# --------------------------------------------------------------------------
BASE = ParagraphStyle("base", fontName="Body", fontSize=9.6, leading=13, textColor=INK)
S = {
    "body": ParagraphStyle("body", parent=BASE, spaceAfter=5),
    "h1": ParagraphStyle(
        "h1", parent=BASE, fontName="Body-Bold", fontSize=15, leading=19,
        textColor=NAVY, spaceBefore=10, spaceAfter=6,
    ),
    "h2": ParagraphStyle(
        "h2", parent=BASE, fontName="Body-Bold", fontSize=11.5, leading=15,
        textColor=ACCENT, spaceBefore=9, spaceAfter=4,
    ),
    "h3": ParagraphStyle(
        "h3", parent=BASE, fontName="Body-Bold", fontSize=10, leading=13,
        textColor=INK, spaceBefore=6, spaceAfter=3,
    ),
    "cell": ParagraphStyle("cell", parent=BASE, fontSize=8.6, leading=11),
    "cellhead": ParagraphStyle(
        "cellhead", parent=BASE, fontName="Body-Bold", fontSize=8.6, leading=11, textColor=NAVY
    ),
    "stepnum": ParagraphStyle(
        "stepnum", parent=BASE, fontName="Body-Bold", fontSize=9.6, alignment=TA_CENTER,
        textColor=colors.white,
    ),
    "step": ParagraphStyle("step", parent=BASE),
    "substep": ParagraphStyle("substep", parent=BASE, leftIndent=12, bulletIndent=2),
    "bullet": ParagraphStyle("bullet", parent=BASE, leftIndent=14, bulletIndent=3, spaceAfter=2),
    "calloutlabel": ParagraphStyle(
        "calloutlabel", parent=BASE, fontName="Body-Bold", fontSize=9, alignment=TA_CENTER,
        textColor=colors.white,
    ),
    "callout": ParagraphStyle("callout", parent=BASE, fontSize=9.2, leading=12.4),
    "cover_title": ParagraphStyle(
        "cover_title", parent=BASE, fontName="Body-Bold", fontSize=28, leading=33,
        textColor=colors.white,
    ),
    "cover_sub": ParagraphStyle(
        "cover_sub", parent=BASE, fontSize=14, leading=18, textColor=colors.HexColor("#cfe0f5"),
    ),
    "cover_meta_k": ParagraphStyle(
        "cover_meta_k", parent=BASE, fontName="Body-Bold", fontSize=9.4, textColor=MUTED,
    ),
    "cover_meta_v": ParagraphStyle("cover_meta_v", parent=BASE, fontSize=10.5, leading=14),
}

# --------------------------------------------------------------------------
# Inline markup
# --------------------------------------------------------------------------

def inline(text: str) -> str:
    """Convert the inline Markdown subset to reportlab paragraph markup."""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # protect code spans first
    codes = []

    def _code(m):
        codes.append(m.group(1))
        return f"\x00{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", _code, text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", text)
    text = text.replace(
        "[VERIFY]",
        f'<font name="Body-Bold" size="7.4" backColor="{VERIFY_BG}" color="#5a3d00">'
        "&nbsp;VERIFY&nbsp;</font>",
    )
    text = text.replace("☐", '<font name="Symbols">☐</font>')
    text = text.replace("→", '<font name="Symbols">→</font>')
    text = re.sub(
        r"\x00(\d+)\x00",
        lambda m: f'<font name="Mono" size="8.6">{codes[int(m.group(1))]}</font>',
        text,
    )
    return text


def P(text, style="body"):
    return Paragraph(inline(text), S[style])


# --------------------------------------------------------------------------
# Block builders
# --------------------------------------------------------------------------

def build_table(rows):
    header, body = rows[0], rows[1:]
    ncols = len(header)
    weights = []
    for c in range(ncols):
        longest = max(len(r[c]) if c < len(r) else 0 for r in rows)
        weights.append(min(max(longest, 6), 70) + 4)
    total = sum(weights)
    widths = [CONTENT_W * w / total for w in weights]
    data = [[Paragraph(inline(h), S["cellhead"]) for h in header]]
    for r in body:
        r = r + [""] * (ncols - len(r))
        data.append([Paragraph(inline(c), S["cell"]) for c in r])
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEAD),
        ("LINEBELOW", (0, 0), (-1, 0), 0.9, NAVY),
        ("LINEBELOW", (0, 1), (-1, -1), 0.4, RULE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]
    for i in range(2, len(data), 2):
        style.append(("BACKGROUND", (0, i), (-1, i), ZEBRA))
    t.setStyle(TableStyle(style))
    return [t, Spacer(1, 7)]


def build_callout(kind, text):
    edge, fill = CALLOUTS[kind]
    label = Paragraph(kind, S["calloutlabel"])
    body = [Paragraph(inline(p), S["callout"]) for p in text.split("\n\n") if p.strip()]
    t = Table([[label, body]], colWidths=[0.95 * inch, CONTENT_W - 0.95 * inch], hAlign="LEFT")
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, 0), edge),
                ("BACKGROUND", (1, 0), (1, 0), fill),
                ("BOX", (0, 0), (-1, -1), 0.8, edge),
                ("VALIGN", (0, 0), (0, 0), "MIDDLE"),
                ("VALIGN", (1, 0), (1, 0), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("LEFTPADDING", (1, 0), (1, 0), 7),
            ]
        )
    )
    return [KeepTogether([t]), Spacer(1, 6)]


def build_steps(items):
    """items: list of (number, text, [subbullets])"""
    data = []
    for num, text, subs in items:
        cell = [Paragraph(inline(text), S["step"])]
        for sub in subs:
            cell.append(Paragraph(inline(sub), S["substep"], bulletText="•"))
        data.append([Paragraph(num, S["stepnum"]), cell])
    t = Table(data, colWidths=[0.34 * inch, CONTENT_W - 0.34 * inch], hAlign="LEFT")
    style = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (0, -1), 0),
        ("RIGHTPADDING", (0, 0), (0, -1), 0),
        ("LEFTPADDING", (1, 0), (1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LINEBELOW", (1, 0), (1, -2), 0.3, RULE),
    ]
    for i in range(len(data)):
        style.append(("BACKGROUND", (0, i), (0, i), ACCENT))
    t.setStyle(TableStyle(style))
    return [t, Spacer(1, 6)]


def build_checklist(items):
    data = [
        [Paragraph('<font name="Symbols" size="11">☐</font>', S["cell"]), Paragraph(inline(i), S["body"])]
        for i in items
    ]
    t = Table(data, colWidths=[0.3 * inch, CONTENT_W - 0.3 * inch], hAlign="LEFT")
    t.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 1),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                ("LEFTPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    return [t, Spacer(1, 6)]


def build_flow(stages):
    n = len(stages)
    gap = 12
    box_w = (CONTENT_W - gap * (n - 1)) / n
    box_h = 40
    d = Drawing(CONTENT_W, box_h + 6)
    for i, label in enumerate(stages):
        x = i * (box_w + gap)
        tag = ""
        if ":" in label:  # "A: Recover refrigerant" -> tag "A"
            tag, label = (p.strip() for p in label.split(":", 1))
        d.add(Rect(x, 3, box_w, box_h, rx=5, ry=5, fillColor=TABLE_HEAD, strokeColor=ACCENT,
                   strokeWidth=0.9))
        if tag:
            d.add(String(x + 7, box_h - 9, tag, fontName="Body-Bold", fontSize=8.4,
                         fillColor=ACCENT))
        words, lines, cur = label.split(), [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if pdfmetrics.stringWidth(trial, "Body-Bold", 8.2) > box_w - 10 and cur:
                lines.append(cur)
                cur = w
            else:
                cur = trial
        lines.append(cur)
        y = 3 + box_h / 2 + (len(lines) - 1) * 4.6 - 6
        for ln in lines:
            d.add(String(x + box_w / 2, y, ln, fontName="Body-Bold", fontSize=8.2,
                         fillColor=INK, textAnchor="middle"))
            y -= 9.2
        if i < n - 1:
            ax = x + box_w + 1.5
            ay = 3 + box_h / 2
            d.add(Line(ax, ay, ax + gap - 4, ay, strokeColor=ACCENT, strokeWidth=1.2))
            d.add(Polygon([ax + gap - 3, ay, ax + gap - 7, ay + 3, ax + gap - 7, ay - 3],
                          fillColor=ACCENT, strokeColor=ACCENT))
    return [d, Spacer(1, 8)]


def build_signoff():
    rows = [
        ["Repair order no.", "", "Date", ""],
        ["VIN (last 8)", "", "Mileage", ""],
        ["Technician", "", "EPA 609 cert. no.", ""],
        ["Refrigerant recovered (g / oz)", "", "Refrigerant charged (g / oz)", ""],
        ["Oil drained from old compressor (mL)", "", "Oil in new compressor (mL)", ""],
        ["Center-vent outlet temp. (°F)", "", "Ambient temp. / humidity", ""],
        ["Supervisor / QC check", "", "Signature", ""],
    ]
    data = [[Paragraph(inline(c), S["cellhead"] if j % 2 == 0 else S["cell"]) for j, c in enumerate(r)]
            for r in rows]
    w = CONTENT_W
    t = Table(data, colWidths=[w * 0.27, w * 0.23, w * 0.27, w * 0.23], rowHeights=24, hAlign="LEFT")
    t.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, RULE),
                ("BACKGROUND", (0, 0), (0, -1), TABLE_HEAD),
                ("BACKGROUND", (2, 0), (2, -1), TABLE_HEAD),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    return [KeepTogether([t]), Spacer(1, 8)]


# --------------------------------------------------------------------------
# Parser
# --------------------------------------------------------------------------

def parse(md: str):
    meta = {}
    lines = md.splitlines()
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            if ":" in lines[i]:
                k, v = lines[i].split(":", 1)
                meta[k.strip()] = v.strip()
            i += 1
        i += 1

    story = []
    para = []

    def flush_para():
        if para:
            story.append(P(" ".join(s.strip() for s in para)))
            para.clear()

    while i < len(lines):
        line = lines[i]
        s = line.strip()

        if not s:
            flush_para()
            i += 1
            continue
        if s == "<!-- pagebreak -->":
            flush_para()
            story.append(PageBreak())
            i += 1
            continue
        if s.startswith("<!--"):
            i += 1
            continue
        if s.startswith("#### "):
            flush_para()
            story.append(CondPageBreak(0.9 * inch))
            story.append(P(s[5:], "h3"))
            i += 1
            continue
        if s.startswith("### "):
            flush_para()
            story.append(CondPageBreak(1.2 * inch))
            story.append(P(s[4:], "h2"))
            i += 1
            continue
        if s.startswith("## "):
            flush_para()
            story.append(CondPageBreak(1.6 * inch))
            story.append(P(s[3:], "h1"))
            story.append(_rule())
            i += 1
            continue
        if s.startswith("# "):  # document title is on the cover; skip
            i += 1
            continue
        m = re.match(r"\[\[FLOW:(.+)\]\]", s)
        if m:
            flush_para()
            story += build_flow([x.strip() for x in m.group(1).split(">")])
            i += 1
            continue
        if s == "[[SIGNOFF]]":
            flush_para()
            story += build_signoff()
            i += 1
            continue
        if s.startswith(">"):
            flush_para()
            block = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                block.append(lines[i].strip()[1:].strip())
                i += 1
            text = "\n".join(block)
            m = re.match(r"\*\*(WARNING|CAUTION|NOTE):\*\*\s*(.*)", text, re.S)
            kind, body = (m.group(1), m.group(2)) if m else ("NOTE", text)
            body = re.sub(r"(?<!\n)\n(?!\n)", " ", body)
            story += build_callout(kind, body)
            continue
        if s.startswith("|"):
            flush_para()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            story += build_table(rows)
            continue
        if re.match(r"\d+\.\s", s):
            flush_para()
            items = []
            while i < len(lines):
                cur = lines[i]
                m = re.match(r"\s*(\d+)\.\s+(.*)", cur)
                if m and not cur.startswith("   "):
                    items.append([m.group(1), m.group(2), []])
                    i += 1
                elif cur.startswith("   ") and cur.strip() and items:
                    sub = cur.strip()
                    if sub.startswith("- "):
                        items[-1][2].append(sub[2:])
                    elif items[-1][2]:
                        items[-1][2][-1] += " " + sub
                    else:
                        items[-1][1] += " " + sub
                    i += 1
                elif not cur.strip() and i + 1 < len(lines) and re.match(r"\d+\.\s", lines[i + 1].strip()):
                    i += 1
                else:
                    break
            story += build_steps(items)
            continue
        if s.startswith("- [ ] "):
            flush_para()
            items = []
            while i < len(lines) and lines[i].strip().startswith("- [ ] "):
                items.append(lines[i].strip()[6:])
                i += 1
            story += build_checklist(items)
            continue
        if s.startswith("- "):
            flush_para()
            while i < len(lines) and (lines[i].strip().startswith("- ") or
                                      (lines[i].startswith("  ") and lines[i].strip())):
                if lines[i].strip().startswith("- "):
                    story.append(Paragraph(inline(lines[i].strip()[2:]), S["bullet"], bulletText="•"))
                else:  # continuation line
                    prev = story.pop()
                    story.append(Paragraph(prev.text + " " + inline(lines[i].strip()), S["bullet"],
                                           bulletText="•"))
                i += 1
            story.append(Spacer(1, 4))
            continue
        para.append(line)
        i += 1
    flush_para()
    return meta, story


def _rule():
    t = Table([[""]], colWidths=[CONTENT_W], rowHeights=[2])
    t.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, -1), 1.2, NAVY)]))
    return t


# --------------------------------------------------------------------------
# Cover page and page furniture
# --------------------------------------------------------------------------

def cover(meta):
    band = Table(
        [
            [Paragraph(inline(meta.get("kicker", "SERVICE MANUAL")), ParagraphStyle(
                "k", parent=BASE, fontName="Body-Bold", fontSize=10, textColor=colors.HexColor("#9fc2ec"),
                leading=14))],
            [Paragraph(inline(meta.get("title", "")), S["cover_title"])],
            [Paragraph(inline(meta.get("subtitle", "")), S["cover_sub"])],
        ],
        colWidths=[CONTENT_W],
    )
    band.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), NAVY),
                ("LEFTPADDING", (0, 0), (-1, -1), 22),
                ("RIGHTPADDING", (0, 0), (-1, -1), 22),
                ("TOPPADDING", (0, 0), (0, 0), 26),
                ("BOTTOMPADDING", (0, -1), (-1, -1), 28),
            ]
        )
    )
    keys = [k for k in meta if k.startswith("meta.")]
    meta_rows = [
        [Paragraph(inline(k[5:].replace("_", " ").upper()), S["cover_meta_k"]),
         Paragraph(inline(meta[k]), S["cover_meta_v"])]
        for k in keys
    ]
    mt = Table(meta_rows, colWidths=[1.9 * inch, CONTENT_W - 1.9 * inch], hAlign="LEFT")
    mt.setStyle(
        TableStyle(
            [
                ("LINEBELOW", (0, 0), (-1, -1), 0.4, RULE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    out = [Spacer(1, 0.6 * inch), band, Spacer(1, 0.4 * inch), mt, Spacer(1, 0.35 * inch)]
    if meta.get("cover_warning"):
        out += build_callout("WARNING", meta["cover_warning"])
    if meta.get("cover_note"):
        out += build_callout("NOTE", meta["cover_note"])
    out.append(PageBreak())
    return out


class NumberedCanvas(rl_canvas.Canvas):
    """Canvas that knows the total page count ("Page X of Y")."""

    header_left = ""
    header_right = ""
    footer_left = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved = []

    def showPage(self):
        self._saved.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._saved)
        for state in self._saved:
            self.__dict__.update(state)
            self._furniture(total)
            super().showPage()
        super().save()

    def _furniture(self, total):
        n = self._pageNumber
        self.saveState()
        if n > 1:
            y = PAGE_H - 0.5 * inch
            self.setFont("Body-Bold", 7.6)
            self.setFillColor(NAVY)
            self.drawString(MARGIN, y, self.header_left.upper())
            self.setFont("Body", 7.6)
            self.setFillColor(MUTED)
            self.drawRightString(PAGE_W - MARGIN, y, self.header_right)
            self.setStrokeColor(RULE)
            self.setLineWidth(0.6)
            self.line(MARGIN, y - 5, PAGE_W - MARGIN, y - 5)
        y = 0.45 * inch
        self.setStrokeColor(RULE)
        self.line(MARGIN, y + 10, PAGE_W - MARGIN, y + 10)
        self.setFont("Body", 7.2)
        self.setFillColor(MUTED)
        self.drawString(MARGIN, y, self.footer_left)
        self.setFont("Body-Bold", 7.6)
        self.setFillColor(INK)
        self.drawRightString(PAGE_W - MARGIN, y, f"Page {n} of {total}")
        self.restoreState()


def main(src, dst):
    md = Path(src).read_text(encoding="utf-8")
    meta, story = parse(md)
    NumberedCanvas.header_left = meta.get("header", meta.get("title", ""))
    NumberedCanvas.header_right = meta.get("revision", "")
    NumberedCanvas.footer_left = meta.get("footer", "")
    doc = SimpleDocTemplate(
        dst,
        pagesize=letter,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
        title=meta.get("title", ""),
        author=meta.get("author", ""),
        subject=meta.get("subtitle", ""),
    )
    doc.build(cover(meta) + story, canvasmaker=NumberedCanvas)
    print(f"wrote {dst}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
