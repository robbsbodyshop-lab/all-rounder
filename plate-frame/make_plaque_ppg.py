#!/usr/bin/env python3
"""
Themed swappable plaque for the plate frame: the three Powerpuff Girls as Dia de los
Muertos sugar skulls, simplified for a 0.4 mm nozzle, plus the poster title text.

Output: plaque_powerpuff_dia_de_muertos.3mf (Bambu Studio project, one object with one
part per filament colour) and preview_plaque_ppg.png.

    pip install manifold3d numpy shapely matplotlib
    python3 make_plaque_ppg.py
"""
import math, zipfile, datetime, pathlib, re
import numpy as np
import manifold3d as m3
from manifold3d import CrossSection, Manifold, FillRule
from shapely.geometry import Polygon, Point, box, MultiPolygon
from shapely.ops import unary_union
from shapely.affinity import translate, scale as sscale
from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties

HERE = pathlib.Path(__file__).parent
m3.set_circular_segments(96)

# ---- plaque envelope: taken from make_frame_3mf.py so both files stay in step
src = (HERE / "make_frame_3mf.py").read_text()
ns = {}
exec(src.split("# ----------------------------------------------------------------- helpers")[0]
     .replace("OUT = pathlib.Path(__file__)", "OUT = pathlib.Path('x')"), ns)
P = ns["P"]
PLQ_W = P["PK_W"] - P["PLQ_CLR"]            # 211.4
PLQ_H = P["PK_H"] - P["PLQ_CLR"]            # 23.4
PLQ_T = P["PLQ_T"]                          # 2.0
HOLE_X = P["HOLE_DX"] / 2                   # 88.9
HOLE_DY = (P["HOLE_DY"] / 2) - (P["FRAME_H"] / 2 - P["PK_TOP_GAP"] - P["PK_H"] / 2)   # -4.675
HOLE_D = P["PLQ_HOLE_D"]

ART_T = 0.6          # raised art height
GAP = 0.5            # black outline between major regions
MARGIN = 0.8         # keep art inside the plaque edge by this much
ART_X_MAX = HOLE_X - HOLE_D / 2 - 6.0       # stay clear of screw heads/washers

# filament slots
BLACK, WHITE, ORANGE, BLUE, GREEN, RED, YELLOW = 1, 2, 3, 4, 5, 6, 7
SLOT_NAMES = {WHITE: "White", ORANGE: "Orange", BLUE: "Blue", GREEN: "Green", RED: "Red", YELLOW: "Yellow"}

# ------------------------------------------------------------------ 2-D helpers
def circ(x, y, r):
    return Point(x, y).buffer(r, 48)

def ell(x, y, rx, ry):
    return sscale(circ(0, 0, 1.0), rx, ry, origin=(0, 0)).buffer(0) if False else \
        translate(sscale(Point(0, 0).buffer(1.0, 48), rx, ry, origin=(0, 0)), x, y)

def rect(x0, y0, x1, y1):
    return box(min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1))

def rounded(poly, r):
    return poly.buffer(-r, 16).buffer(r, 16)

def mirror_x(poly):
    return sscale(poly, -1, 1, origin=(0, 0))

# ------------------------------------------------------------------ one character
def character(kind):
    """Return {slot: shapely geometry} for one girl centred at x=0 (y up)."""
    col = {"blossom": ORANGE, "bubbles": BLUE, "buttercup": GREEN}[kind]
    regions = {}          # major regions, outlined with GAP
    details = {}          # small features placed without gaps

    face = circ(0, 1.6, 5.4)
    # hair -------------------------------------------------------------
    if kind == "blossom":
        hair = unary_union([circ(0, 2.3, 6.3), rounded(rect(-6.3, -4.6, 6.3, 2.3), 1.2)])
        # bangs only decide which part of the hair/face overlap stays hair (see below)
        bow = unary_union([
            rounded(Polygon([(0.2, 7.4), (-5.4, 10.9), (-4.4, 6.6)]), 0.5),
            rounded(Polygon([(-0.2, 7.4), (5.4, 10.9), (4.4, 6.6)]), 0.5),
            circ(0, 7.9, 1.0)])
    elif kind == "bubbles":
        cap = circ(0, 2.5, 6.2)
        pig = unary_union([ell(-6.6, 1.3, 2.0, 3.6), ell(6.6, 1.3, 2.0, 3.6)])
        fringe = rect(-7, 4.9, 7, 9)          # straight fringe: hair keeps the face above y=4.9
        hair = unary_union([cap, pig, cap.intersection(fringe)])
        bow = None
    else:
        cap = circ(0, 2.4, 6.3)
        flips = unary_union([ell(-6.3, 4.6, 1.7, 1.2), ell(6.3, 4.6, 1.7, 1.2)])
        bangs = Polygon([(-6, 7.5), (6, 7.5), (6, 4.2), (2.2, 3.3), (-0.8, 4.4), (-6, 4.4)])
        hair = unary_union([cap, flips, bangs])
        bow = None
    hair_region = hair
    face_region = face.difference(hair_region) if kind != "blossom" else face.difference(hair_region)
    # for bubbles/buttercup the fringe/bangs are part of hair and win over the face
    hair_region = hair_region.difference(face) .union(hair_region.intersection(face).intersection(
        {"blossom": Polygon([(-7, 9.5), (7, 9.5), (7, 5.6), (1.6, 3.7), (-0.4, 4.4), (-2.6, 3.8), (-7, 5.6)]),
         "bubbles": rect(-7, 4.9, 7, 9),
         "buttercup": Polygon([(-6, 7.5), (6, 7.5), (6, 4.2), (2.2, 3.3), (-0.8, 4.4), (-6, 4.4)])}[kind]))
    face_region = face.difference(hair_region)

    # body -------------------------------------------------------------
    dress = Polygon([(-2.7, -3.2), (2.7, -3.2), (3.7, -8.6), (-3.7, -8.6)])
    legs = unary_union([rounded(rect(-2.9, -8.4, -0.7, -10.9), 0.4), rounded(rect(0.7, -8.4, 2.9, -10.9), 0.4)])
    arms = unary_union([ell(-4.2, -5.3, 1.0, 1.9), ell(4.2, -5.3, 1.0, 1.9)])
    body = unary_union([dress, legs, arms]).difference(face)
    hair_region = hair_region.difference(body.buffer(0.01))

    # assemble major regions, each shrunk by GAP/2 so neighbours get a black outline
    major = [(col, hair_region if kind != "bubbles" else None), (WHITE, face_region), (col, body)]
    if kind == "bubbles":
        regions.setdefault(ORANGE if False else BLUE, [])   # placeholder, replaced below
    out = {}
    def add(slot, geom):
        if geom is None or geom.is_empty:
            return
        out.setdefault(slot, []).append(geom)
    hair_slot = {"blossom": ORANGE, "bubbles": YELLOW, "buttercup": GREEN}[kind]
    if bow is not None:   # the bow sits on top of hair and face
        hair_region = hair_region.difference(bow.buffer(GAP))
        face_region = face_region.difference(bow.buffer(GAP))
        add(RED, bow)
    add(hair_slot, hair_region.buffer(-GAP / 2, 8))
    add(WHITE, face_region.buffer(-GAP / 2, 8))
    add(col, body.buffer(-GAP / 2, 8))

    # face details (voids) --------------------------------------------
    voids = []
    eyes = []
    for sx in (-1, 1):
        e = circ(sx * 2.1, 2.4, 1.75)
        if kind == "buttercup":   # angry: clip the inner-upper part of each eye
            e = e.difference(Polygon([(sx * 0.0, 4.6), (sx * 0.0, 2.9), (sx * 4.5, 4.6)]))
        eyes.append(e)
        voids.append(e)
    nose = Polygon([(-0.55, 0.65), (0.55, 0.65), (0, -0.35)])
    voids.append(nose)
    mouth = rect(-2.0, -1.45, 2.0, -0.95)
    for x in (-1.1, 0.0, 1.1):
        mouth = mouth.union(rect(x - 0.2, -1.85, x + 0.2, -0.55))
    voids.append(mouth)
    # sugar-skull dots around the eyes, only where they fall on the face
    face_shrunk = out[WHITE][0]
    for sx in (-1, 1):
        for k in range(8):
            a = k * math.pi / 4
            d = circ(sx * 2.1 + 2.55 * math.cos(a), 2.4 + 2.55 * math.sin(a), 0.28)
            if face_shrunk.buffer(-0.35).contains(d) and not unary_union(eyes).buffer(0.45).intersects(d):
                voids.append(d)
    void_u = unary_union(voids)
    out[WHITE] = [g.difference(void_u) for g in out[WHITE]]
    # coloured pupil dot inside each eye
    for sx in (-1, 1):
        add(col, circ(sx * 2.1, 2.4 if kind != "buttercup" else 2.2, 0.7))

    # skeleton: white ribs on the dress, bones in the legs (touching, no gap)
    ribs = unary_union([rect(-1.9, y - 0.4, 1.9, y + 0.4) for y in (-4.8, -6.3, -7.8)]
                       + [rect(-0.4, -4.4, 0.4, -8.2)])
    ribs = ribs.intersection(dress.buffer(-0.5))
    bones = unary_union([rect(sx * 1.8 - 0.3, -8.9, sx * 1.8 + 0.3, -10.4) for sx in (-1, 1)])
    for slot in list(out):
        if slot == col:
            out[slot] = [g.difference(ribs).difference(bones) for g in out[slot]]
    add(WHITE, ribs)
    add(WHITE, bones)

    return {slot: unary_union(gs) for slot, gs in out.items()}

# ------------------------------------------------------------------ text
def text_geom(s, cap_h, font=FontProperties(fname="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf")):
    tp = TextPath((0, 0), s, size=10, prop=font)
    ref = TextPath((0, 0), "H", size=10, prop=font)
    k = cap_h / (ref.get_extents().height)
    polys = []
    for pts in tp.to_polygons():
        if len(pts) >= 3:
            polys.append(Polygon(pts * k))
    polys.sort(key=lambda p: p.area, reverse=True)
    geom = None
    for p in polys:
        if geom is None:
            geom = p
        elif geom.contains(p.representative_point()):
            geom = geom.difference(p)
        else:
            geom = geom.union(p)
    b = geom.bounds
    return translate(geom, -(b[0] + b[2]) / 2, -(b[1] + b[3]) / 2)   # centred

# ------------------------------------------------------------------ layout
chars = {"bubbles": -21.5, "blossom": 0.0, "buttercup": 21.5}
layers = {}
for kind, cx in chars.items():
    for slot, g in character(kind).items():
        layers.setdefault(slot, []).append(translate(g, cx, 0))
layers = {slot: unary_union(gs) for slot, gs in layers.items()}

CAP = 4.4
text_parts = {
    "Text left": unary_union([translate(text_geom("LAS TRES", CAP), -56, 3.2),
                              translate(text_geom("CHICAS", CAP), -56, -3.2)]),
    "Text right": unary_union([translate(text_geom("DÍA DE LOS", CAP), 56, 3.2),
                               translate(text_geom("MUERTOS", CAP), 56, -3.2)]),
}

# ------------------------------------------------------------------ checks
limit = box(-ART_X_MAX, -PLQ_H / 2 + MARGIN, ART_X_MAX, PLQ_H / 2 - MARGIN)
all_art = list(layers.items()) + [(ORANGE, g) for g in text_parts.values()]
for slot, g in all_art:
    assert limit.contains(g), f"slot {slot} art leaves the safe area: {g.bounds}"
names = list(layers) 
for i, a in enumerate(names):
    for b in names[i + 1:]:
        inter = layers[a].intersection(layers[b]).area
        assert inter < 1e-6, f"overlap between slots {a} and {b}: {inter}"
# thin-feature audit: anything that vanishes under a 0.3 mm inset is a single-line feature
for slot, g in all_art:
    polys = list(g.geoms) if hasattr(g, "geoms") else [g]
    thin = [p for p in polys if p.buffer(-0.3).is_empty]
    print(f"slot {slot}: {len(polys)} islands, {len(thin)} thinner than 0.6 mm, "
          f"bbox x {g.bounds[0]:.1f}..{g.bounds[2]:.1f} y {g.bounds[1]:.1f}..{g.bounds[3]:.1f}")

# ------------------------------------------------------------------ 3-D
def to_cs(g):
    polys = list(g.geoms) if hasattr(g, "geoms") else [g]
    contours = []
    for p in polys:
        contours.append(np.asarray(p.exterior.coords)[:-1])
        for r in p.interiors:
            contours.append(np.asarray(r.coords)[:-1])
    return CrossSection(contours, FillRule.EvenOdd)

def ext(cs, z0, z1):
    return Manifold.extrude(cs, z1 - z0).translate((0, 0, z0))

base2d = rounded(rect(-PLQ_W / 2, -PLQ_H / 2, PLQ_W / 2, PLQ_H / 2), P["PLQ_R"]) \
    .difference(circ(-HOLE_X, HOLE_DY, HOLE_D / 2)).difference(circ(HOLE_X, HOLE_DY, HOLE_D / 2))
base = ext(to_cs(base2d), 0, PLQ_T)
parts = [("Plaque base", BLACK, base)]
for slot in sorted(layers):
    parts.append((f"Art {SLOT_NAMES[slot]}", slot, ext(to_cs(layers[slot]), PLQ_T, PLQ_T + ART_T)))
for name, g in text_parts.items():
    parts.append((name, ORANGE, ext(to_cs(g), PLQ_T, PLQ_T + ART_T)))
for name, slot, man in parts:
    assert man.status() == m3.Error.NoError, (name, man.status())
    print(f"{name:14s} slot {slot} tris={man.num_tri():6d} vol={man.volume():8.1f} mm3")

# ------------------------------------------------------------------ preview
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path as MPath
COLORS = {BLACK: "#141416", WHITE: "#f4f1ea", ORANGE: "#f07a1d", BLUE: "#2f6fd6", GREEN: "#3f9a3a", RED: "#d9262e", YELLOW: "#f2c12e"}
fig, ax = plt.subplots(figsize=(22, 3.6))
def draw(g, color, z=1):
    verts, codes = [], []
    for p in (g.geoms if hasattr(g, "geoms") else [g]):
        for ring in [p.exterior] + list(p.interiors):
            pts = np.asarray(ring.coords)
            verts += list(pts); codes += [MPath.MOVETO] + [MPath.LINETO] * (len(pts) - 2) + [MPath.CLOSEPOLY]
    ax.add_patch(PathPatch(MPath(verts, codes), facecolor=color, edgecolor="none", zorder=z))
draw(base2d, COLORS[BLACK], 1)
for slot, g in layers.items():
    draw(g, COLORS[slot], 2)
for g in text_parts.values():
    draw(g, COLORS[ORANGE], 2)
ax.set_xlim(-PLQ_W / 2 - 2, PLQ_W / 2 + 2); ax.set_ylim(-PLQ_H / 2 - 2, PLQ_H / 2 + 2)
ax.set_aspect("equal"); ax.set_facecolor("#d8d8d8"); ax.set_title("Themed plaque, front view, 1 mm grid"); ax.grid(True, lw=0.2)
fig.tight_layout(); fig.savefig(HERE / "preview_plaque_ppg.png", dpi=130)
fig, ax = plt.subplots(figsize=(12, 5))
draw(base2d, COLORS[BLACK], 1)
for slot, g in layers.items():
    draw(g, COLORS[slot], 2)
ax.set_xlim(-34, 34); ax.set_ylim(-12.5, 12.5); ax.set_aspect("equal"); ax.set_facecolor("#d8d8d8")
ax.set_xticks(range(-34, 35, 2)); ax.set_yticks(range(-12, 13, 2)); ax.grid(True, lw=0.3); ax.set_title("Characters, zoom (mm)")
fig.tight_layout(); fig.savefig(HERE / "preview_plaque_ppg_zoom.png", dpi=130)

# ------------------------------------------------------------------ 3MF
def clean_mesh(man):
    mesh = man.simplify(0.001).to_mesh()
    v = np.asarray(mesh.vert_properties)[:, :3]; f = np.asarray(mesh.tri_verts)
    uniq, inv = np.unique(np.round(v, 5), axis=0, return_inverse=True)
    f2 = inv.reshape(-1)[f]
    f2 = f2[(f2[:, 0] != f2[:, 1]) & (f2[:, 1] != f2[:, 2]) & (f2[:, 2] != f2[:, 0])]
    e = np.sort(np.vstack([f2[:, [0, 1]], f2[:, [1, 2]], f2[:, [2, 0]]]), axis=1)
    _, cnt = np.unique(e, axis=0, return_counts=True)
    return (v, f) if (cnt != 2).any() else (uniq, f2)

def mesh_xml(obj_id, man):
    v, f = clean_mesh(man)
    out = [f'  <object id="{obj_id}" type="model">\n   <mesh>\n    <vertices>\n']
    out += [f'     <vertex x="{x:.4f}" y="{y:.4f}" z="{z:.4f}"/>\n' for x, y, z in v]
    out.append('    </vertices>\n    <triangles>\n')
    out += [f'     <triangle v1="{a}" v2="{b}" v3="{c}"/>\n' for a, b, c in f]
    out.append('    </triangles>\n   </mesh>\n  </object>\n')
    return "".join(out), len(f)

def tf(mat):
    return " ".join(f"{mat[r][c]:.6g}" for c in range(4) for r in range(3))

IDENT = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]
PLACE = [[1, 0, 0, P["BED_W"] / 2], [0, 1, 0, P["BED_D"] / 2], [0, 0, 1, 0]]
mesh_blocks, comp_lines, part_lines = [], [], []
for i, (name, slot, man) in enumerate(parts, start=1):
    xml, ntri = mesh_xml(i, man)
    mesh_blocks.append(xml)
    comp_lines.append(f'    <component objectid="{i}" transform="{tf(IDENT)}"/>\n')
    part_lines.append(
        f'    <part id="{i}" subtype="normal_part">\n'
        f'      <metadata key="name" value="{name}"/>\n'
        f'      <metadata key="matrix" value="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1"/>\n'
        f'      <metadata key="extruder" value="{slot}"/>\n'
        f'      <mesh_stat face_count="{ntri}" edges_fixed="0" degenerate_facets="0" facets_removed="0" facets_reversed="0" backwards_edges="0"/>\n'
        f'    </part>\n')
OBJ = len(parts) + 1
today = datetime.date.today().isoformat()
model = f'''<?xml version="1.0" encoding="UTF-8"?>
<model unit="millimeter" xml:lang="en-US" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" xmlns:BambuStudio="http://schemas.bambulab.com/package/2021">
 <metadata name="Application">make_plaque_ppg.py</metadata>
 <metadata name="BambuStudio:3mfVersion">1</metadata>
 <metadata name="Title">Powerpuff Girls Dia de los Muertos plaque</metadata>
 <metadata name="CreationDate">{today}</metadata>
 <metadata name="ModificationDate">{today}</metadata>
 <resources>
{"".join(mesh_blocks)}  <object id="{OBJ}" type="model">
   <components>
{"".join(comp_lines)}   </components>
  </object>
 </resources>
 <build>
  <item objectid="{OBJ}" transform="{tf(PLACE)}" printable="1"/>
 </build>
</model>
'''
settings = f'''<?xml version="1.0" encoding="UTF-8"?>
<config>
  <object id="{OBJ}">
    <metadata key="name" value="PPG Dia de los Muertos plaque"/>
    <metadata key="extruder" value="1"/>
{"".join(part_lines)}  </object>
  <plate>
    <metadata key="plater_id" value="1"/>
    <metadata key="plater_name" value="Themed plaque"/>
    <metadata key="locked" value="false"/>
    <model_instance>
      <metadata key="object_id" value="{OBJ}"/>
      <metadata key="instance_id" value="0"/>
      <metadata key="identify_id" value="201"/>
    </model_instance>
  </plate>
  <assemble>
   <assemble_item object_id="{OBJ}" instance_id="0" transform="{tf(PLACE)}" offset="0 0 0" />
  </assemble>
</config>
'''
content_types = '''<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
 <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
 <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/>
</Types>'''
rels = '''<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Target="/3D/3dmodel.model" Id="rel-1" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/>
</Relationships>'''
OUT = HERE / "plaque_powerpuff_dia_de_muertos.3mf"
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("[Content_Types].xml", content_types)
    z.writestr("_rels/.rels", rels)
    z.writestr("3D/3dmodel.model", model)
    z.writestr("Metadata/model_settings.config", settings)
print("wrote", OUT, OUT.stat().st_size, "bytes")
