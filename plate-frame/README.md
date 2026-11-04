# Subaru Badge-of-Ownership license plate frame (Bambu H2C)

`subaru_boo_plate_frame_H2C.3mf` is a Bambu Studio project file. Open it directly in
Bambu Studio (File > Open Project). It contains one plate with two objects:

| Object | Parts | Filament slot | Orientation on bed |
|---|---|---|---|
| Plate frame | Frame body, Accent bezels | 1, 2 | front face **down** on the textured plate |
| Blank plaque | Blank plaque | 1 | front face up |

Regenerate after editing the `P` dict in `make_frame_3mf.py`:

```
pip install manifold3d numpy trimesh
python3 make_frame_3mf.py
```

## What the frame does

* Fits a standard US plate (304.8 x 152.4 mm) with the 7 in x 4.75 in hole pattern.
  Four 7.5 mm through-holes with 11 mm x 1 mm counterbores for the screw heads. The
  plate sits behind the frame and is clamped by the mounting screws.
* **Bottom bar**: a 2 mm deep pocket shaped for the Badge of Ownership strip. Round
  pocket 35.6 mm for the loyalty medallion (left side, viewed from the front) and a
  112 x 26.5 mm trough for five lifestyle-icon tiles. The badges' own adhesive holds them
  in; the pocket only locates them.
* **Top bar**: a 160 x 20 mm front-loading plaque pocket in place of the Subaru logo.
  Retaining lips: 2.5 mm along the top edge, 1.0 mm along the bottom edge. Visible
  window 160 x 16.5 mm. A 16 mm fingernail notch below the pocket exposes the plaque's
  bottom edge.
* **Accent bezels**: a 0.8 mm skin (2 mm band) around both pockets, split out as its
  own part so the AMS can print it in a second colour. Set it to filament 1 if you want a
  single-colour frame.

## Swapping plaques

1. Push the plaque's top edge up under the 2.5 mm top lip.
2. Swing the bottom edge into the pocket (it clears the 1 mm bottom lip by 0.4 mm).
3. Let it drop. Gravity seats the bottom edge behind the bottom lip; the top edge stays
   1.1 mm under the top lip.
4. To remove, lift the plaque 1.4 mm with a fingernail in the notch and swing the bottom
   out.

Custom plaque blank: 159.4 x 18.6 x 2.0 mm, 0.6 mm chamfer on the back edges. Add
raised or engraved text to the `Blank plaque` object in Bambu Studio (Text tool) or
remodel from the STL. Keep raised text under 1 mm tall so it clears the lips.

## Key dimensions (mm)

| | |
|---|---|
| Frame outer | 316 x 164 x 5.5 |
| Opening | 300 x 106 (side rails 8, top bar 28, bottom bar 30) |
| Bottom boss around the strip | up to 41.3 above the bottom edge |
| Medallion pocket | dia 35.6, centre 21 above the bottom edge, 56 left of centre |
| Tile trough | 112 x 26.5, corner radius 3 |
| Hole centres | +/-88.9 horizontal, +/-60.3 vertical from frame centre |

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
  The badge pockets, plaque cavity and counterbores print as short bridges (max 36 mm)
  because the frame is face down.
* Material: ASA or PETG for outdoor UV and heat. PLA will warp on a dark car in summer.
* Filament 1 = frame colour, filament 2 = accent colour. The colour change only happens
  in the first 4 layers, so purge waste is small.

## Legal note

The top and bottom bars cover about 22 mm and 24 mm of the plate's top and bottom edges
(more around the medallion boss). Some states prohibit frames that cover the state name
or registration stickers. Shrink `TOP_BAR`, `BOT_BAR` and `PK_H` in the script if that
applies to you.
