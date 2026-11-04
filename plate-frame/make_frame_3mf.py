#!/usr/bin/env python3
"""
Generate a Bambu Studio-ready 3MF of a US license-plate frame with:
  * a bottom bar that holds a Subaru "Badge of Ownership" strip
    (round loyalty medallion + five lifestyle icon tiles),
  * a top bar with a recessed, swappable plaque that the two top plate screws clamp,
  * a second-filament accent bezel around both pockets,
  * a matching blank plaque as a second object.

All dimensions are millimetres.  Edit the PARAMS block and re-run:
    pip install manifold3d numpy
    python3 make_frame_3mf.py
"""
import math, zipfile, datetime, pathlib, sys
import numpy as np
import manifold3d as m3
from manifold3d import CrossSection, Manifold, JoinType

m3.set_circular_segments(120)

# ----------------------------------------------------------------- PARAMS
P = dict(
    # --- plate / frame envelope
    PLATE_W=304.8, PLATE_H=152.4,          # US plate 12 x 6 in
    HOLE_DX=177.8, HOLE_DY=120.65,         # 7 x 4.75 in hole pattern
    FRAME_W=316.0, FRAME_H=164.0,          # outer size (fits 325 mm H2C X)
    OUTER_R=10.0, INNER_R=4.0,
    THICK=5.5,                             # frame thickness
    SIDE_RAIL=8.0, TOP_BAR=32.0, BOT_BAR=30.0,
    HOLE_D=7.5, CBORE_D=11.0, CBORE_DEPTH=1.0,
    # --- badge strip (medallion measured from Subaru's 1:1 install template,
    #     tiles from photo ratios; see README)
    MED_D=34.4, MED_CLR=1.2,               # loyalty medallion outer ring
    TILE_H=25.0, TILE_PITCH=22.0, N_TILES=5,
    TILE_CLR_H=1.5, TROUGH_EXTRA_L=2.0,    # vertical clearance, extra length
    STRIP_Y=21.0,                          # strip centre-line above bottom edge
    STRIP_DEPTH=2.0, STRIP_WALL=2.5,
    # --- plaque recess (top bar): the plaque spans both top mounting holes and is
    #     clamped by the plate screws, so no lips are needed
    PK_W=212.0, PK_H=24.0, PK_TOP_GAP=5.0, # recess size, gap from top edge
    PK_R=3.0, PK_DEPTH=2.0,
    # --- plaque (sits flush in the recess)
    PLQ_CLR=0.6, PLQ_T=2.0, PLQ_R=2.5, PLQ_HOLE_D=7.5,
    # --- accent skin (filament 2)
    ACC_W=2.0, ACC_T=0.8,
    # --- bed placement (Bambu H2C plate, single nozzle 325 x 320)
    BED_W=325.0, BED_D=320.0,
)
OUT = pathlib.Path(__file__).with_name("subaru_boo_plate_frame_H2C.3mf")

# ----------------------------------------------------------------- helpers
def rrect(w, h, r, cx=0.0, cy=0.0):
    """Rounded rectangle centred at (cx, cy)."""
    r = min(r, w / 2, h / 2)
    core = CrossSection.square((w - 2 * r, h - 2 * r), center=True)
    cs = core.offset(r, JoinType.Round) if r > 0 else core
    return cs.translate((cx, cy))

def circle(d, cx=0.0, cy=0.0):
    return CrossSection.circle(d / 2).translate((cx, cy))

def ext(cs, z0, z1):
    return Manifold.extrude(cs, z1 - z0).translate((0, 0, z0))

# ----------------------------------------------------------------- 2-D layout
W, H, T = P["FRAME_W"], P["FRAME_H"], P["THICK"]
top, bot = H / 2, -H / 2
edge_gap_y = (H - P["PLATE_H"]) / 2            # frame overhang beyond plate
hole_y = P["HOLE_DY"] / 2
hole_x = P["HOLE_DX"] / 2
assert abs(hole_y - (top - edge_gap_y - (P["PLATE_H"] - P["HOLE_DY"]) / 2)) < 1e-9

outer = rrect(W, H, P["OUTER_R"])
open_w = W - 2 * P["SIDE_RAIL"]
open_h = H - P["TOP_BAR"] - P["BOT_BAR"]
open_cy = bot + P["BOT_BAR"] + open_h / 2
opening = rrect(open_w, open_h, P["INNER_R"], 0, open_cy)

# badge strip: medallion on the LEFT (viewed from the front), tiles to the right
strip_cy = bot + P["STRIP_Y"]
med_pd = P["MED_D"] + P["MED_CLR"]
trough_h = P["TILE_H"] + P["TILE_CLR_H"]
trough_l = P["N_TILES"] * P["TILE_PITCH"] + P["TROUGH_EXTRA_L"]
strip_total = med_pd + trough_l
med_cx = -strip_total / 2 + med_pd / 2
trough_cx = med_cx + med_pd / 2 - 1.0 + trough_l / 2   # 1 mm overlap into medallion pocket
medallion = circle(med_pd, med_cx, strip_cy)
trough = rrect(trough_l + 1.0, trough_h, 3.0, trough_cx - 0.5, strip_cy)
strip = medallion + trough
boss = strip.offset(P["STRIP_WALL"], JoinType.Round)

body2d = outer - (opening - boss)

# plaque recess; the top mounting holes pass through it
pk_cy = top - P["PK_TOP_GAP"] - P["PK_H"] / 2
pocket = rrect(P["PK_W"], P["PK_H"], P["PK_R"], 0, pk_cy)
pk_top, pk_bot = pk_cy + P["PK_H"] / 2, pk_cy - P["PK_H"] / 2
assert pk_top - hole_y > P["HOLE_D"] / 2 + 2 and hole_y - pk_bot > P["HOLE_D"] / 2 + 2, "holes must sit inside the recess"
assert pk_bot - (top - P["TOP_BAR"]) >= 2.5, "wall below recess"

# accent skin regions (ring bands), kept 1 mm inside the outer edge
inset = body2d.offset(-1.0, JoinType.Round)
# the inner boundaries overlap the window/strip/notch by 0.05 mm so the 2-D band and the
# 3-D prism cuts never leave hair-thin slivers (the 3-D cuts below trim them exactly)
EPS = 0.05
acc_plaque = (pocket.offset(P["ACC_W"], JoinType.Round) - pocket.offset(-EPS, JoinType.Round)) ^ inset
acc_strip = (strip.offset(P["ACC_W"], JoinType.Round) - strip.offset(-EPS, JoinType.Round)) ^ inset
accent2d = acc_plaque + acc_strip

# ----------------------------------------------------------------- 3-D build (front face at z = T, back at z = 0)
body = ext(body2d, 0, T)
cuts = []
cuts.append(ext(pocket, T - P["PK_DEPTH"], T + 1))                          # plaque recess
cuts.append(ext(strip, T - P["STRIP_DEPTH"], T + 1))                        # badge pockets
for sx in (-1, 1):
    for sy in (-1, 1):
        cx, cy = sx * hole_x, sy * hole_y
        cuts.append(ext(circle(P["HOLE_D"], cx, cy), -1, T + 1))
        if sy < 0:   # counterbores only on the bottom holes; the top screw heads sit on the plaque
            cuts.append(ext(circle(P["CBORE_D"], cx, cy), T - P["CBORE_DEPTH"], T + 1))
cuts.append(ext(accent2d, T - P["ACC_T"], T + 1))                           # make room for accent skin
body = body - Manifold.batch_boolean(cuts, m3.OpType.Add)

accent = ext(accent2d, T - P["ACC_T"], T)
accent = accent - Manifold.batch_boolean(
    [ext(pocket, T - 2, T + 1), ext(strip, T - 2, T + 1)]
    + [ext(circle(P["CBORE_D"], sx * hole_x, -hole_y), T - 2, T + 1) for sx in (-1, 1)],
    m3.OpType.Add)

# plaque: flat plate with the two screw holes, sits flush in the recess
plq_w = P["PK_W"] - P["PLQ_CLR"]
plq_h = P["PK_H"] - P["PLQ_CLR"]
plq_hole_dy = hole_y - pk_cy                     # hole offset from plaque centre
plaque2d = rrect(plq_w, plq_h, P["PLQ_R"]) - circle(P["PLQ_HOLE_D"], -hole_x, plq_hole_dy) - circle(P["PLQ_HOLE_D"], hole_x, plq_hole_dy)
plaque = ext(plaque2d, 0, P["PLQ_T"])

# ----------------------------------------------------------------- checks
def stats(name, man):
    assert man.status() == m3.Error.NoError, (name, man.status())
    assert man.genus() >= 0
    bb = man.bounding_box()
    print(f"{name:8s} tris={man.num_tri():6d} vol={man.volume():9.1f} mm3  "
          f"bbox=({bb[0]:.1f},{bb[1]:.1f},{bb[2]:.1f})-({bb[3]:.1f},{bb[4]:.1f},{bb[5]:.1f})")
    return bb
stats("body", body); stats("accent", accent); stats("plaque", plaque)
ov = (body ^ accent).volume()
assert ov < 1e-6, f"body/accent overlap {ov}"
print("body/accent overlap volume:", ov)
assert plq_w < P["PK_W"] and plq_h < P["PK_H"] and P["PLQ_T"] <= P["PK_DEPTH"]
print(f"plaque {plq_w} x {plq_h} x {P['PLQ_T']} mm, screw holes {P['PLQ_HOLE_D']} mm at x=+/-{hole_x} y={plq_hole_dy:+.3f} from plaque centre")
print(f"strip pocket: medallion dia {med_pd} at x={med_cx:.1f}, trough {trough_l}x{trough_h} mm, total {strip_total:.1f} mm")

# ----------------------------------------------------------------- 3MF writing (Bambu Studio project layout)
def clean_mesh(man):
    """Merge coincident vertices, drop zero-area triangles, verify closed topology."""
    mesh = man.simplify(0.001).to_mesh()
    v = np.asarray(mesh.vert_properties)[:, :3]
    f = np.asarray(mesh.tri_verts)
    key = np.round(v, 5)
    uniq, inv = np.unique(key, axis=0, return_inverse=True)
    f2 = inv.reshape(-1)[f]
    keep = (f2[:, 0] != f2[:, 1]) & (f2[:, 1] != f2[:, 2]) & (f2[:, 2] != f2[:, 0])
    f2 = f2[keep]
    e = np.sort(np.vstack([f2[:, [0, 1]], f2[:, [1, 2]], f2[:, [2, 0]]]), axis=1)
    _, cnt = np.unique(e, axis=0, return_counts=True)
    if (cnt != 2).any():                       # merging broke something: keep the raw (index-closed) mesh
        return v, f
    return uniq, f2

def mesh_xml(obj_id, man, name):
    v, f = clean_mesh(man)
    out = [f'  <object id="{obj_id}" type="model">\n   <mesh>\n    <vertices>\n']
    out += [f'     <vertex x="{x:.4f}" y="{y:.4f}" z="{z:.4f}"/>\n' for x, y, z in v]
    out.append('    </vertices>\n    <triangles>\n')
    out += [f'     <triangle v1="{a}" v2="{b}" v3="{c}"/>\n' for a, b, c in f]
    out.append('    </triangles>\n   </mesh>\n  </object>\n')
    return "".join(out), len(f)

def tf(mat):
    """3x4 affine -> 3MF transform string (column major, 12 numbers)."""
    return " ".join(f"{mat[r][c]:.6g}" for c in range(4) for r in range(3))

IDENT = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]
# Frame goes face-DOWN on the bed: rotate 180 deg about X, then lift by T and centre on the bed.
cx, cy = P["BED_W"] / 2, P["BED_D"] / 2 + 55.0
FLIP = [[1, 0, 0, cx], [0, -1, 0, cy], [0, 0, -1, T]]
# Plaque face-UP, below the frame
PLQ_TF = [[1, 0, 0, cx], [0, 1, 0, cy - H / 2 - 32.0], [0, 0, 1, 0]]

body_xml, body_tris = mesh_xml(1, body, "Frame body")
acc_xml, acc_tris = mesh_xml(2, accent, "Accent bezels")
plq_xml, plq_tris = mesh_xml(4, plaque, "Blank plaque")

today = datetime.date.today().isoformat()
model = f'''<?xml version="1.0" encoding="UTF-8"?>
<model unit="millimeter" xml:lang="en-US" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" xmlns:BambuStudio="http://schemas.bambulab.com/package/2021">
 <metadata name="Application">make_frame_3mf.py</metadata>
 <metadata name="BambuStudio:3mfVersion">1</metadata>
 <metadata name="Title">Subaru Badge of Ownership plate frame</metadata>
 <metadata name="CreationDate">{today}</metadata>
 <metadata name="ModificationDate">{today}</metadata>
 <resources>
{body_xml}{acc_xml}  <object id="3" type="model">
   <components>
    <component objectid="1" transform="{tf(IDENT)}"/>
    <component objectid="2" transform="{tf(IDENT)}"/>
   </components>
  </object>
{plq_xml} </resources>
 <build>
  <item objectid="3" transform="{tf(FLIP)}" printable="1"/>
  <item objectid="4" transform="{tf(PLQ_TF)}" printable="1"/>
 </build>
</model>
'''

def part(pid, name, extruder, tris):
    return (f'    <part id="{pid}" subtype="normal_part">\n'
            f'      <metadata key="name" value="{name}"/>\n'
            f'      <metadata key="matrix" value="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1"/>\n'
            f'      <metadata key="extruder" value="{extruder}"/>\n'
            f'      <mesh_stat face_count="{tris}" edges_fixed="0" degenerate_facets="0" facets_removed="0" facets_reversed="0" backwards_edges="0"/>\n'
            f'    </part>\n')

settings = f'''<?xml version="1.0" encoding="UTF-8"?>
<config>
  <object id="3">
    <metadata key="name" value="Plate frame (face down)"/>
    <metadata key="extruder" value="1"/>
    <metadata face_count="{body_tris + acc_tris}"/>
{part(1, "Frame body", 1, body_tris)}{part(2, "Accent bezels", 2, acc_tris)}  </object>
  <object id="4">
    <metadata key="name" value="Blank plaque"/>
    <metadata key="extruder" value="1"/>
    <metadata face_count="{plq_tris}"/>
{part(4, "Blank plaque", 1, plq_tris)}  </object>
  <plate>
    <metadata key="plater_id" value="1"/>
    <metadata key="plater_name" value="Frame + plaque"/>
    <metadata key="locked" value="false"/>
    <model_instance>
      <metadata key="object_id" value="3"/>
      <metadata key="instance_id" value="0"/>
      <metadata key="identify_id" value="101"/>
    </model_instance>
    <model_instance>
      <metadata key="object_id" value="4"/>
      <metadata key="instance_id" value="0"/>
      <metadata key="identify_id" value="102"/>
    </model_instance>
  </plate>
  <assemble>
   <assemble_item object_id="3" instance_id="0" transform="{tf(FLIP)}" offset="0 0 0" />
   <assemble_item object_id="4" instance_id="0" transform="{tf(PLQ_TF)}" offset="0 0 0" />
  </assemble>
</config>
'''

content_types = '''<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
 <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
 <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/>
 <Default Extension="png" ContentType="image/png"/>
</Types>'''
rels = '''<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Target="/3D/3dmodel.model" Id="rel-1" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/>
</Relationships>'''

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("[Content_Types].xml", content_types)
    z.writestr("_rels/.rels", rels)
    z.writestr("3D/3dmodel.model", model)
    z.writestr("Metadata/model_settings.config", settings)
print("wrote", OUT, OUT.stat().st_size, "bytes")

# also dump STLs for quick inspection in any viewer
try:
    import trimesh
    for nm, man in (("frame_body", body), ("accent_bezels", accent), ("blank_plaque", plaque)):
        v, f = clean_mesh(man)
        trimesh.Trimesh(v, f).export(OUT.with_name(f"{nm}.stl"))
except ImportError:
    pass
