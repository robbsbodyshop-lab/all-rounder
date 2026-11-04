# Subaru Badge-of-Ownership license plate frame (Bambu H2C)

`subaru_boo_plate_frame_H2C.3mf` is a Bambu Studio project file. Open it directly in
Bambu Studio (File > Open Project). It contains one plate with two objects:

| Object | Parts | Filament slot | Orientation on bed |
|---|---|---|---|
| Plate frame | Frame body, Accent bezels | 1, 2 | front face **down** on the textured plate |
| Blank plaque | Blank plaque | 1 | front face up |

A themed plaque with the Powerpuff Girls lives in a second file, see below.

Regenerate after editing the `P` dict in `make_frame_3mf.py`:

```
pip install manifold3d numpy trimesh
python3 make_frame_3mf.py
```

## What the frame does

* Fits a standard US plate (304.8 x 152.4 mm) with the 7 in x 4.75 in hole pattern.
  Four 7.5 mm through-holes; the bottom pair has 11 mm x 1 mm counterbores for the screw
  heads, the top pair passes through the plaque recess. The plate sits behind the frame
  and is clamped by the mounting screws.
* **Bottom bar**: a 2 mm deep pocket shaped for the Badge of Ownership strip. Round
  pocket 35.6 mm for the loyalty medallion (left side, viewed from the front) and a
  112 x 26.5 mm trough for five lifestyle-icon tiles. The badges' own adhesive holds them
  in; the pocket only locates them.
* **Top bar**: a 212 x 24 x 2 mm recess in place of the Subaru logo. The plaque spans
  both top mounting holes and the two plate screws clamp it, so swapping a plaque means
  loosening those two screws. No lips or clips.
* **Accent bezels**: a 0.8 mm skin (2 mm band) around both pockets, split out as its
  own part so the AMS can print it in a second colour. Set it to filament 1 if you want a
  single-colour frame.

## Swapping plaques

1. Back the two top plate screws out far enough to free the plaque (the bottom screws
   can stay).
2. Lift the old plaque out of the recess and drop the new one in, holes over the screws.
3. Tighten the top screws. The screw heads bear on the plaque; use screws with a washer
   or flange head of at least 10 mm.

Custom plaque blank: 211.4 x 23.4 x 2.0 mm, corner radius 2.5, two 7.5 mm holes at
+/-88.9 mm horizontally and 4.675 mm below the plaque's centre line. It sits flush with
the frame face. Add raised or engraved text to the `Blank plaque` object in Bambu Studio
(Text tool) or remodel from the STL; raised text can be any height since nothing covers
the plaque. If you want the plaque proud of the frame, make it thicker than 2 mm.

## Themed plaque: Powerpuff Girls, Dia de los Muertos

`plaque_powerpuff_dia_de_muertos.3mf` holds the plaque blank with the poster's scene
in five colours: Bubbles, Blossom and Buttercup as full-body sugar-skull figures (each
girl one silhouette in her colour with a white skull face, ribs and bone limbs inside),
papel picado bunting along the top, a dotted border along the bottom, marigolds, two
little skulls and a three-colour Powerpuff heart at each end. No lettering.
Regenerate with `python3 make_plaque_ppg.py`; it reads the plaque size from
`make_frame_3mf.py` through `plaque_lib.py` so the files stay matched.

| Part | Slot | Colour |
|---|---|---|
| Plaque base | 1 | black |
| Art White | 2 | white (faces, bones, skulls, bunting string, border dots, white flags, marigold centres) |
| Art Orange | 3 | orange (Blossom, marigolds, orange flags, left band of the hearts) |
| Art Blue | 4 | blue (Bubbles, blue flags, middle band of the hearts) |
| Art Green | 5 | green (Buttercup, green flags, right band of the hearts) |

Art is raised 0.6 mm. Black outlines are 0.5 mm gaps that show the base; the
smallest features are the 0.6 mm bone arms, the 0.8 mm border dots and the 0.6 mm
holes punched in the flags. Print face up, 0.2 mm layers (0.1 mm for crisper faces),
Arachne on. Colour changes happen in the top three layers only.

## Themed plaque: Gruß vom Krampus

`plaque_gruss_vom_krampus.3mf` holds the same plaque blank with "Gruß vom Krampus" in
Fraktur (UnifrakturCook Bold, SIL Open Font License, bundled in `fonts/`) across the
middle and a Krampus silhouette facing inward at each end: horns, open goat muzzle with
the tongue out, basket on the back, birch rod in hand, cloven hooves and an arrow tail.
Regenerate with `python3 make_plaque_krampus.py`. Shared helpers for the themed plaques
live in `plaque_lib.py`.

| Part | Slot | Colour |
|---|---|---|
| Plaque base | 1 | black |
| Lettering | 2 | white |
| Krampus silhouettes | 3 | red |

Art is raised 0.6 mm; thinnest features are the 0.6 mm birch twigs. Swap the slot
numbers in the object list if you want red lettering and white silhouettes.

## Key dimensions (mm)

| | |
|---|---|
| Frame outer | 316 x 164 x 5.5 |
| Opening | 300 x 102 (side rails 8, top bar 32, bottom bar 30) |
| Bottom boss around the strip | up to 41.3 above the bottom edge |
| Medallion pocket | dia 35.6, centre 21 above the bottom edge, 56 left of centre |
| Tile trough | 112 x 26.5, corner radius 3 |
| Hole centres | +/-88.9 horizontal, +/-60.3 vertical from frame centre |
| Plaque recess | 212 x 24 x 2, from 5 to 29 below the top edge |

## Where the badge sizes come from

* Medallion outer diameter 34.4 mm: circle fitted to the 1:1 cut-out template in Subaru
  Canada's official installation sheet (badgeofownership.ca, `subaru-boo-installation.pdf`).
* Tile height 25 mm and pitch about 22 mm: ratios measured from the official vector
  illustration in that sheet and from the photo of your badge strip, scaled by the
  medallion. These are estimates. Before printing, measure one tile and the medallion
  with calipers and compare with `MED_D`, `TILE_H` and `TILE_PITCH` in the script. The
  pockets carry 1.2 mm (medallion) and 1.5 mm (tile height) of clearance and the trough
  is 2 mm longer than five tiles.

## Printing

* Printer: Bambu Lab H2C, 0.4 nozzle. The frame is 316 mm wide and sits centred on the
  plate. If your printer profile shows a smaller printable area, rotate the frame a few
  degrees in Bambu Studio.
* Suggested: 0.2 mm layers, 3 walls, 5 top/bottom layers, 25% gyroid, no supports.
  The badge pockets, plaque recess and counterbores print as short bridges (max 36 mm)
  because the frame is face down.
* Material: ASA or PETG for outdoor UV and heat. PLA will warp on a dark car in summer.
* Filament 1 = frame colour, filament 2 = accent colour. The colour change only happens
  in the first 4 layers, so purge waste is small.

## Legal note

The top and bottom bars cover about 26 mm and 24 mm of the plate's top and bottom edges
(more around the medallion boss). Some states prohibit frames that cover the state name
or registration stickers. Shrink `TOP_BAR`, `BOT_BAR` and `PK_H` in the script if that
applies to you (the recess must still clear the top holes by 2 mm).
