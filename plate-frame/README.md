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

`plaque_powerpuff_dia_de_muertos.3mf` is a second Bambu Studio project holding only a
plaque (same 211.4 x 23.4 x 2 mm blank with the two screw holes) with the three girls as
sugar skulls raised 0.6 mm on the face, plus the poster's title text at each end.
Regenerate with `python3 make_plaque_ppg.py`; it reads the plaque size from
`make_frame_3mf.py` so the two stay matched.

Parts and filament slots (five, to match one AMS plus the external spool or a
five-slot setup):

| Part | Slot | Colour |
|---|---|---|
| Plaque base | 1 | black |
| Art White | 2 | white (faces, bone arms and legs, ribs, marigold centres) |
| Art Orange, Text left, Text right | 3 | orange (Blossom hair, bow and dress, marigolds, lettering) |
| Art Blue | 4 | blue (Bubbles hair and dress) |
| Art Green | 5 | green (Buttercup hair and dress) |

Each girl is drawn in her signature colour with a white sugar-skull face: flower-shaped
eye sockets with a coloured iris, heart nose, stitched smile (flat and angry for
Buttercup), cheek dots, white ribs on the dress, bone arms and legs. Delete the
`Text left` and `Text right` parts for characters only, or reassign any part's filament
in the object list.

Print it face up, 0.2 mm layers (0.1 mm for crisper faces), 0.4 nozzle, Arachne wall
generator on (the default) so the 0.6 to 0.8 mm skull details and lettering strokes
print as single lines. The colour changes happen in the top three layers only. Black
outlines between regions are 0.5 mm gaps that show the base.

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
