# Service Manuals

Printable shop procedures, written in [ASD-STE100 Simplified Technical English](https://www.asd-ste100.org/)
style: one action per step, imperative verbs, short sentences, and WARNING / CAUTION / NOTE call-outs.

| Manual | Source | PDF |
|---|---|---|
| 2019 Lincoln Navigator — A/C compressor removal and installation | [`manual.md`](2019-lincoln-navigator-ac-compressor/manual.md) | [`2019-navigator-ac-compressor.pdf`](2019-lincoln-navigator-ac-compressor/2019-navigator-ac-compressor.pdf) |

## Editing and rebuilding

Each manual is a Markdown file. Edit it on GitHub or locally, then rebuild the PDF:

```bash
pip install reportlab   # only dependency
python3 service-manuals/build_pdf.py \
  service-manuals/2019-lincoln-navigator-ac-compressor/manual.md \
  service-manuals/2019-lincoln-navigator-ac-compressor/2019-navigator-ac-compressor.pdf
```

`build_pdf.py` documents the small Markdown dialect it understands (call-out boxes, numbered
steps, tables, check-lists, a process-flow strip and a sign-off block).

## The VERIFY tag

A yellow **VERIFY** tag marks a value that could not be confirmed from an official Ford or Lincoln
source when the manual was written. Look the value up in Ford service information
(motorcraftservice.com) for the VIN before you rely on it. When you confirm a value, remove the tag,
note the source in the References section, and rebuild the PDF.
