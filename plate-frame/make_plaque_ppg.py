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
MARGIN = 0.6         # keep art inside the plaque edge by this much
ART_X_MAX = HOLE_X - HOLE_D / 2 - 6.0       # stay clear of screw heads/washers

# filament slots (5): the base colour doubles as Buttercup's hair
BLACK, WHITE, ORANGE, BLUE, GREEN = 1, 2, 3, 4, 5
SLOT_NAMES = {WHITE: "White", ORANGE: "Orange", BLUE: "Blue", GREEN: "Green"}

# ------------------------------------------------------------------ 2-D helpers
from shapely.geometry import LineString

def circ(x, y, r):
    return Point(x, y).buffer(r, 48)

def rect(x0, y0, x1, y1):
    return box(min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1))

def rounded(poly, r):
    return poly.buffer(-r, 16).buffer(r, 16)

def smooth(poly, r):
    """Round convex corners only (outward buffer then back)."""
    return poly.buffer(r, 16).buffer(-r, 16)

def bone(p0, p1, w, rb):
    """Cartoon bone: a thick line with a knob at each end."""
    return unary_union([LineString([p0, p1]).buffer(w / 2, 16), circ(*p0, rb), circ(*p1, rb)])

def arc_pts(cx, cy, r, a0, a1, n=24):
    return [(cx + r * math.cos(a), cy + r * math.sin(a)) for a in np.linspace(a0, a1, n)]

def flower(x, y, r, petals=8, pr=None):
    pr = pr or r * 0.36
    return unary_union([circ(x, y, r)] + [circ(x + r * math.cos(a), y + r * math.sin(a), pr)
                                          for a in np.linspace(0, 2 * math.pi, petals, endpoint=False)])

# ------------------------------------------------------------------ one character
def character(kind):
    """Return {slot: geometry} for one girl centred at x=0, y up, about 22 mm tall."""
    col = {"blossom": ORANGE, "bubbles": BLUE, "buttercup": GREEN}[kind]
    out = {}
    def add(slot, geom):
        if geom is not None and not geom.is_empty:
            out.setdefault(slot, []).append(geom)

    # ---- head and hair silhouettes
    face = circ(0, 1.4, 5.6)
    if kind == "blossom":
        dome = circ(0, 1.9, 6.6)
        strands = unary_union([Polygon([(-6.5, 3.5), (-7.7, -7.6), (-5.3, -8.4), (-3.8, -2.5)]),
                               Polygon([(6.5, 3.5), (7.7, -7.6), (5.3, -8.4), (3.8, -2.5)])])
        hair = smooth(unary_union([dome, strands]), 1.2)
        bangs = rounded(Polygon([(-8, 11), (8, 11), (8, 5.6), (5.0, 5.3), (0, 3.5), (-5.0, 5.3), (-8, 5.6)]), 0.5)
        knot = circ(0, 8.3, 1.1)
        loops = unary_union([smooth(Polygon([(-0.4, 8.3), (-6.3, 10.9), (-5.3, 6.6)]), 0.7),
                             smooth(Polygon([(0.4, 8.3), (6.3, 10.9), (5.3, 6.6)]), 0.7)])
        bow = unary_union([knot, loops])
        hair_outline_only = False
    elif kind == "bubbles":
        dome = circ(0, 2.0, 6.5)
        pigtails = unary_union([circ(-6.3, 4.4, 2.9), circ(6.3, 4.4, 2.9)])
        hair = smooth(unary_union([dome, pigtails]), 0.8)
        bangs = rounded(Polygon([(-9, 11), (9, 11), (9, 5.8), (3.5, 5.4), (0, 4.5), (-3.5, 5.4), (-9, 5.8)]), 0.7)
        bow = None
        hair_outline_only = False
    else:
        dome = circ(0, 2.1, 6.6)
        flips = unary_union([smooth(Polygon([(-5.8, 3.8), (-8.2, 1.4), (-5.6, -0.4)]), 0.9),
                             smooth(Polygon([(5.8, 3.8), (8.2, 1.4), (5.6, -0.4)]), 0.9)])
        hair = smooth(unary_union([dome, flips]), 0.6)
        bangs = rounded(Polygon([(-8, 11), (8, 11), (8, 5.0), (3.0, 4.9), (-0.4, 3.4), (-2.4, 4.9), (-8, 5.0)]), 0.5)
        bow = None
        hair_outline_only = False

    hair_region = hair.difference(face).union(hair.intersection(face).intersection(bangs))
    face_region = face.difference(hair_region)

    # ---- body: dress, bone arms and legs
    dress = rounded(Polygon([(-2.8, -2.6), (2.8, -2.6), (4.0, -8.4), (-4.0, -8.4)]), 0.5)
    dress = dress.difference(face.buffer(GAP))
    arms = unary_union([bone((-3.3, -4.3), (-5.3, -7.5), 0.95, 0.55), bone((3.3, -4.3), (5.3, -7.5), 0.95, 0.55)])
    legs = unary_union([bone((-1.6, -9.35), (-1.6, -10.35), 1.0, 0.6), bone((1.6, -9.35), (1.6, -10.35), 1.0, 0.6)])
    bones = unary_union([arms, legs]).difference(dress.buffer(GAP))
    hair_region = hair_region.difference(unary_union([dress, bones]).buffer(GAP))
    if bow is not None:
        hair_region = hair_region.difference(bow.buffer(GAP))
        face_region = face_region.difference(bow.buffer(GAP))

    # ---- raised regions with outline gaps
    if hair_outline_only:
        add(col, hair_region.buffer(-GAP / 2, 8).difference(hair_region.buffer(-GAP / 2 - 0.75, 8)))
    else:
        add(col, hair_region.buffer(-GAP / 2, 8))
    if bow is not None:
        add(col, bow)
    add(col, dress.buffer(-GAP / 2, 8))
    add(WHITE, bones)

    # ---- sugar-skull face
    eyes = []
    for sx in (-1, 1):
        e = flower(sx * 2.3, 2.0, 1.85, 8, 0.62)
        if kind == "buttercup":   # angry brow: clip the upper inner part of each socket
            e = e.difference(Polygon([(0, 4.9), (sx * 0.2, 2.6), (sx * 4.9, 4.9)]))
        eyes.append(e)
    nose = unary_union([circ(-0.42, 0.05, 0.42), circ(0.42, 0.05, 0.42), Polygon([(-0.8, -0.05), (0.8, -0.05), (0, -0.95)])])
    if kind == "buttercup":
        mouth_line = LineString([(-2.2, -1.9), (2.2, -1.9)])
    else:
        mouth_line = LineString(arc_pts(0, 0.6, 3.0, math.radians(235), math.radians(305)))
    mouth = mouth_line.buffer(0.27, 8)
    for t in (0.12, 0.37, 0.63, 0.88):
        pt = mouth_line.interpolate(t, normalized=True)
        mouth = mouth.union(rect(pt.x - 0.2, pt.y - 0.65, pt.x + 0.2, pt.y + 0.65))
    voids = unary_union(eyes + [nose, mouth])
    face_white = face_region.buffer(-GAP / 2, 8).difference(voids)
    # coloured cheek dots and forehead dot (adjacent colours, no gap needed)
    dots = [circ(sx * 4.1, -0.5, 0.5) for sx in (-1, 1)] + [circ(sx * 3.4, -1.9, 0.42) for sx in (-1, 1)]
    dots = [d for d in dots if face_white.buffer(-0.3).contains(d)]
    face_white = face_white.difference(unary_union(dots)) if dots else face_white
    add(WHITE, face_white)
    for d in dots:
        add(col, d)
    for sx in (-1, 1):   # iris inside the socket
        add(col, circ(sx * 2.3, 2.0 if kind != "buttercup" else 1.75, 1.0))

    # ---- skeleton ribs on the dress (white, touching the dress colour)
    ribs = unary_union([rect(-2.1, y - 0.4, 2.1, y + 0.4) for y in (-5.3, -6.6, -7.9)] + [rect(-0.38, -4.6, 0.38, -8.3)])
    ribs = ribs.intersection(dress.buffer(-0.55))
    out[col] = [g.difference(ribs) for g in out[col]]
    add(WHITE, ribs)

    return {slot: unary_union(gs) for slot, gs in out.items()}

def marigold(x, y):
    petals = unary_union([circ(x + 1.55 * math.cos(a), y + 1.55 * math.sin(a), 0.72)
                          for a in np.linspace(0, 2 * math.pi, 10, endpoint=False)] + [circ(x, y, 1.6)])
    inner = unary_union([circ(x + 0.75 * math.cos(a), y + 0.75 * math.sin(a), 0.42)
                         for a in np.linspace(math.pi / 10, 2 * math.pi, 10, endpoint=False)])
    return {ORANGE: petals.difference(circ(x, y, 0.5).buffer(0.25)), WHITE: circ(x, y, 0.5)}

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
chars = {"bubbles": -23.0, "blossom": 0.0, "buttercup": 23.0}
layers = {}
for kind, cx in chars.items():
    for slot, g in character(kind).items():
        layers.setdefault(slot, []).append(translate(g, cx, 0))
for mx in (-37.0, 37.0):
    for slot, g in marigold(mx, 0.0).items():
        layers.setdefault(slot, []).append(g)
layers = {slot: unary_union(gs) for slot, gs in layers.items()}

CAP = 4.0
TX = (41.5 + ART_X_MAX) / 2
text_parts = {
    "Text left": unary_union([translate(text_geom("LAS TRES", CAP), -TX, 3.0),
                              translate(text_geom("CHICAS", CAP), -TX, -3.0)]),
    "Text right": unary_union([translate(text_geom("D\u00cdA DE LOS", CAP), TX, 3.0),
                               translate(text_geom("MUERTOS", CAP), TX, -3.0)]),
}
for g in text_parts.values():
    assert min(abs(g.bounds[0]), abs(g.bounds[2])) > 41.0, "text runs into the marigolds"

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
COLORS = {BLACK: "#141416", WHITE: "#f4f1ea", ORANGE: "#f07a1d", BLUE: "#2f6fd6", GREEN: "#3f9a3a"}
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
fig, ax = plt.subplots(figsize=(14, 4.6))
draw(base2d, COLORS[BLACK], 1)
for slot, g in layers.items():
    draw(g, COLORS[slot], 2)
ax.set_xlim(-42, 42); ax.set_ylim(-12.5, 12.5); ax.set_aspect("equal"); ax.set_facecolor("#d8d8d8")
ax.set_xticks(range(-42, 43, 2)); ax.set_yticks(range(-12, 13, 2)); ax.grid(True, lw=0.3); ax.set_title("Characters, zoom (mm)")
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
