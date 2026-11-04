#!/usr/bin/env python3
"""
Powerpuff Girls x Dia de los Muertos plaque: full-body sugar-skull figures of Bubbles,
Blossom and Buttercup, papel picado bunting, marigolds, little skulls, a dotted border
and a three-colour Powerpuff heart at each end. Five filament slots.

    python3 make_plaque_ppg.py
"""
from plaque_lib import *

WHITE, ORANGE, BLUE, GREEN = 2, 3, 4, 5
ART_T, GAP = 0.6, 0.5
blank = Blank()
XMAX = blank.art_x_max            # 79.15
YMAX = blank.h / 2 - 0.6          # 11.1

# ------------------------------------------------------------------ canvas: paint in order, outlines by GAP
class Canvas:
    def __init__(self):
        self.layers = {}
    def paint(self, slot, geom, gap=GAP):
        """Add geom on top of everything painted so far, keeping a black outline of `gap`."""
        if geom is None or geom.is_empty:
            return
        geom = geom.buffer(0)
        cut = geom.buffer(gap, 8) if gap else geom
        for k in self.layers:
            self.layers[k] = self.layers[k].difference(cut)
        self.layers[slot] = unary_union([self.layers.get(slot, Polygon()), geom])
    def paint_group(self, items, gap=GAP):
        """Several colours that touch each other (no gaps between them) but get one outline."""
        items = [(slot, g.buffer(0)) for slot, g in items if g is not None and not g.is_empty]
        footprint = unary_union([g for _, g in items])
        cut = footprint.buffer(gap, 8)
        for k in self.layers:
            self.layers[k] = self.layers[k].difference(cut)
        for slot, g in items:
            self.layers[slot] = unary_union([self.layers.get(slot, Polygon()), g])

# ------------------------------------------------------------------ one girl, full body
def girl(kind):
    """Return [(slot, geom), ...] for one girl centred at x=0, y up, 22 mm tall.
    Everything in her colour is one silhouette; the white face and bones sit inside it."""
    col = {"blossom": ORANGE, "bubbles": BLUE, "buttercup": GREEN}[kind]
    face = circ(0, 2.6, 5.4)                                       # top 8.0, chin -2.8
    # hair
    if kind == "blossom":
        dome = circ(0, 3.0, 6.3)
        strands = unary_union([Polygon([(-6.2, 4.0), (-6.6, -8.0), (-4.6, -8.5), (-3.8, -1.5)]),
                               Polygon([(6.2, 4.0), (6.6, -8.0), (4.6, -8.5), (3.8, -1.5)])])
        hair = smooth(unary_union([dome, strands]), 1.0)
        bangs = rounded(Polygon([(-8, 12), (8, 12), (8, 7.0), (4.8, 6.9), (0, 5.0), (-4.8, 6.9), (-8, 7.0)]), 0.45)
        from shapely.affinity import rotate
        bow = unary_union([circ(0, 8.7, 1.05),
                           rotate(ellipse(-3.3, 9.3, 3.0, 1.5), 22, origin=(-3.3, 9.3)),
                           rotate(ellipse(3.3, 9.3, 3.0, 1.5), -22, origin=(3.3, 9.3))])
        bow = bow.intersection(rect(-9, 0, 9, 10.9))
        hair = hair.union(bow)
    elif kind == "bubbles":
        dome = circ(0, 3.2, 6.2)
        pigtails = unary_union([ellipse(-6.4, 2.8, 2.1, 3.2), ellipse(6.4, 2.8, 2.1, 3.2)])
        hair = smooth(unary_union([dome, pigtails]), 0.8)
        bangs = rounded(Polygon([(-9, 12), (9, 12), (9, 7.6), (3.2, 7.3), (0, 6.2), (-3.2, 7.3), (-9, 7.6)]), 0.6)
    else:
        dome = circ(0, 3.2, 6.2)
        flips = unary_union([smooth(Polygon([(-5.6, 6.0), (-8.2, 4.0), (-5.6, 2.2)]), 0.8),
                             smooth(Polygon([(5.6, 6.0), (8.2, 4.0), (5.6, 2.2)]), 0.8)])
        hair = smooth(unary_union([dome, flips]), 0.6)
        bangs = rounded(Polygon([(-8, 12), (8, 12), (8, 7.2), (2.8, 7.1), (-0.4, 5.3), (-2.4, 7.1), (-8, 7.2)]), 0.45)
    hair_region = hair.difference(face).union(hair.intersection(face).intersection(bangs))
    face_region = face.difference(hair_region)
    # body silhouette: dress, stub arms, stub legs
    dress = rounded(Polygon([(-2.9, -1.6), (2.9, -1.6), (4.1, -8.2), (-4.1, -8.2)]), 0.5)
    arms = unary_union([smooth(Polygon([(-2.6, -2.4), (-5.4, -6.6), (-4.0, -7.4), (-2.4, -4.4)]), 0.5),
                        smooth(Polygon([(2.6, -2.4), (5.4, -6.6), (4.0, -7.4), (2.4, -4.4)]), 0.5)])
    legs = unary_union([rounded(rect(-3.0, -8.0, -0.6, -10.9), 0.5), rounded(rect(0.6, -8.0, 3.0, -10.9), 0.5)])
    body = unary_union([dress, arms, legs])
    silhouette = unary_union([hair_region, body])
    silhouette = silhouette.difference(face.buffer(GAP)).union(hair_region)   # hair stays over the face edge
    # face details (voids) and white face
    eyes = []
    for sx in (-1, 1):
        e = flower(sx * 2.2, 3.1, 1.75, 8, 0.58)
        if kind == "buttercup":
            e = e.difference(Polygon([(0, 6.2), (sx * 0.2, 2.1), (sx * 4.6, 5.2), (sx * 4.6, 6.2)]))
        eyes.append(e)
    nose = unary_union([circ(-0.42, 1.0, 0.42), circ(0.42, 1.0, 0.42), Polygon([(-0.8, 0.9), (0.8, 0.9), (0, 0.05)])])
    if kind == "buttercup":
        mouth_line = LineString([(-2.2, -0.9), (2.2, -0.9)])
    else:
        mouth_line = LineString([(math.cos(a) * 3.0, 1.4 + math.sin(a) * 3.0) for a in np.linspace(math.radians(232), math.radians(308), 20)])
    mouth = mouth_line.buffer(0.26, 8)
    for t in (0.15, 0.5, 0.85):
        pt = mouth_line.interpolate(t, normalized=True)
        mouth = mouth.union(rect(pt.x - 0.2, pt.y - 0.6, pt.x + 0.2, pt.y + 0.6))
    face_white = face_region.buffer(-GAP / 2, 8).difference(unary_union(eyes + [nose, mouth]))
    irises = unary_union([circ(sx * 2.2, 3.1 if kind != "buttercup" else 2.8, 0.95) for sx in (-1, 1)])
    face_white = face_white.difference(irises)          # the angry-brow clip can leave the iris on white
    # skeleton details inside the silhouette (white islands)
    ribs = unary_union([rect(-2.0, y - 0.38, 2.0, y + 0.38) for y in (-3.6, -4.9, -6.2)] + [rect(-0.36, -2.9, 0.36, -7.0)])
    ribs = ribs.intersection(dress.buffer(-0.6))
    bones = unary_union([rect(sx * 1.8 - 0.32, -8.6, sx * 1.8 + 0.32, -10.3) for sx in (-1, 1)]
                        + [stroke([(sx * 3.2, -3.4), (sx * 4.6, -6.0)], 0.55) for sx in (-1, 1)])
    silhouette = silhouette.difference(unary_union([ribs, bones]))
    return [(col, silhouette), (WHITE, face_white), (col, irises), (WHITE, unary_union([ribs, bones]))]

# ------------------------------------------------------------------ ornaments
def heart(cx, cy, w):
    """Classic heart: a square rotated 45 degrees with a disc on each upper edge."""
    from shapely.affinity import rotate
    sq = w / 1.7071
    d = sq / (2 * math.sqrt(2))
    square = rotate(rect(cx - sq / 2, cy - sq / 2, cx + sq / 2, cy + sq / 2), 45, origin=(cx, cy))
    h = unary_union([square, circ(cx - d, cy + d, sq / 2), circ(cx + d, cy + d, sq / 2)])
    h = translate(h, 0, -d * 0.4)
    bw = w / 3.4
    bands = [rect(cx - w, cy - w, cx - bw / 2, cy + w), rect(cx - bw / 2, cy - w, cx + bw / 2, cy + w),
             rect(cx + bw / 2, cy - w, cx + w, cy + w)]
    return [(ORANGE, h.intersection(bands[0]).buffer(-GAP / 2)), (BLUE, h.intersection(bands[1]).buffer(-GAP / 2)),
            (GREEN, h.intersection(bands[2]).buffer(-GAP / 2))]

def marigold(x, y, r):
    outer = unary_union([circ(x + r * 0.78 * math.cos(a), y + r * 0.78 * math.sin(a), r * 0.36)
                         for a in np.linspace(0, 2 * math.pi, 10, endpoint=False)] + [circ(x, y, r * 0.8)])
    inner = unary_union([circ(x + r * 0.42 * math.cos(a), y + r * 0.42 * math.sin(a), r * 0.2)
                         for a in np.linspace(math.pi / 10, 2 * math.pi + math.pi / 10, 10, endpoint=False)])
    centre = circ(x, y, r * 0.2)
    return [(ORANGE, outer.difference(centre.buffer(0.01))), (WHITE, centre)]

def skull(x, y, s=1.0):
    cr = unary_union([circ(x, y + 0.5 * s, 1.35 * s), rounded(rect(x - 0.95 * s, y - 1.5 * s, x + 0.95 * s, y + 0.2 * s), 0.3 * s)])
    voids = unary_union([circ(x - 0.55 * s, y + 0.55 * s, 0.42 * s), circ(x + 0.55 * s, y + 0.55 * s, 0.42 * s),
                         Polygon([(x - 0.25 * s, y - 0.25 * s), (x + 0.25 * s, y - 0.25 * s), (x, y - 0.65 * s)])])
    return [(WHITE, cr.difference(voids))]

def flag(x, y_top, w, h, slot):
    f = Polygon([(x - w / 2, y_top), (x + w / 2, y_top), (x + w / 2, y_top - h * 0.7), (x, y_top - h), (x - w / 2, y_top - h * 0.7)])
    if slot == WHITE:
        f = f.difference(circ(x, y_top - h * 0.42, w * 0.18))
    else:
        f = f.difference(unary_union([circ(x - w * 0.2, y_top - h * 0.3, w * 0.09), circ(x + w * 0.2, y_top - h * 0.3, w * 0.09),
                                      circ(x, y_top - h * 0.55, w * 0.11)]))
    return (slot, f)

# ------------------------------------------------------------------ compose
cv = Canvas()
# background: dotted border along the bottom, bunting string and flags along the top
dots = unary_union([circ(x, -YMAX + 0.5, 0.42) for x in np.arange(-78, 78.01, 2.2)])
cv.paint(WHITE, dots, gap=0)
string_y = YMAX - 0.6
cv.paint(WHITE, stroke([(-XMAX + 0.4, string_y), (XMAX - 0.4, string_y)], 0.5), gap=0)
flag_colors = [ORANGE, BLUE, WHITE, GREEN]
flags = []
for i, x in enumerate(np.arange(-77.0, 77.01, 4.3)):
    flags.append(flag(x, string_y - 0.35, 3.5, 2.9, flag_colors[i % 4]))
for slot, f in flags:
    cv.paint(slot, f, gap=0)
# side ornaments: heart emblems, marigolds, small skulls
for sx in (-1, 1):
    cv.paint_group(heart(sx * 50.0, -1.0, 14.0))
    cv.paint_group(marigold(sx * 66.5, -2.0, 4.4))
    cv.paint_group(marigold(sx * 75.5, -3.2, 2.6))
    cv.paint_group(marigold(sx * 37.5, -6.4, 2.3))
    cv.paint_group(skull(sx * 37.5, 2.6, 1.15))
# the girls on top of everything
for kind, cx in (("bubbles", -23.0), ("blossom", 0.0), ("buttercup", 23.0)):
    cv.paint_group([(slot, translate(g, cx, 0)) for slot, g in girl(kind)])

layers = [(slot, g) for slot, g in cv.layers.items() if not g.is_empty]
safe = blank.safe_box(0.45)
for slot, g in layers:
    assert safe.contains(g), f"slot {slot} leaves the safe area {g.bounds}"
    thin_report(f"slot {slot}", g)
for i in range(len(layers)):
    for j in range(i + 1, len(layers)):
        assert layers[i][1].intersection(layers[j][1]).area < 1e-6, "colour overlap"

parts = [("Plaque base", BLACK, ext(to_cs(blank.geom), 0, blank.t))]
names = {WHITE: "Art White", ORANGE: "Art Orange", BLUE: "Art Blue", GREEN: "Art Green"}
for slot, g in sorted(layers):
    parts.append((names[slot], slot, ext(to_cs(g), blank.t, blank.t + ART_T)))
for name, slot, man in parts:
    print(f"{name:14s} slot {slot} tris={man.num_tri():6d} vol={man.volume():8.1f} mm3")

COLORS = {BLACK: "#141416", WHITE: "#f4f1ea", ORANGE: "#f07a1d", BLUE: "#2f6fd6", GREEN: "#3f9a3a"}
preview(HERE / "preview_plaque_ppg.png", blank, layers, COLORS, "Powerpuff Dia de los Muertos plaque, front view (mm)", grid=10)
preview(HERE / "preview_plaque_ppg_zoom.png", blank, layers, COLORS, "Characters (mm)", xlim=(-42, 42), figsize=(15, 4.8), grid=2)
preview(HERE / "preview_plaque_ppg_side.png", blank, layers, COLORS, "Right end (mm)", xlim=(28, 84), figsize=(12, 5.4), grid=2)
write_3mf(HERE / "plaque_powerpuff_dia_de_muertos.3mf", parts, "Powerpuff Girls Dia de los Muertos plaque",
          "PPG Dia de los Muertos plaque", blank.P["BED_W"], blank.P["BED_D"], app="make_plaque_ppg.py")
