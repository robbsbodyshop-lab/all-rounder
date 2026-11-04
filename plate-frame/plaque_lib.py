"""Shared helpers for the themed plaques: plaque blank, text outlines, mesh export,
Bambu Studio 3MF writer and a flat colour preview."""
import math, zipfile, datetime, pathlib
import numpy as np
import manifold3d as m3
from manifold3d import CrossSection, Manifold, FillRule
from shapely.geometry import Polygon, Point, box, LineString
from shapely.ops import unary_union
from shapely.affinity import translate, scale as sscale
from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties

HERE = pathlib.Path(__file__).parent
m3.set_circular_segments(96)
BLACK = 1

def frame_params():
    src = (HERE / "make_frame_3mf.py").read_text()
    ns = {}
    exec(src.split("# ----------------------------------------------------------------- helpers")[0]
         .replace("OUT = pathlib.Path(__file__)", "OUT = pathlib.Path('x')"), ns)
    return ns["P"]

class Blank:
    """The plaque blank that fits the frame's top-bar recess."""
    def __init__(self):
        P = self.P = frame_params()
        self.w = P["PK_W"] - P["PLQ_CLR"]
        self.h = P["PK_H"] - P["PLQ_CLR"]
        self.t = P["PLQ_T"]
        self.hole_x = P["HOLE_DX"] / 2
        self.hole_dy = (P["HOLE_DY"] / 2) - (P["FRAME_H"] / 2 - P["PK_TOP_GAP"] - P["PK_H"] / 2)
        self.hole_d = P["PLQ_HOLE_D"]
        self.art_x_max = self.hole_x - self.hole_d / 2 - 6.0     # clear of screw heads
        self.geom = rounded(rect(-self.w / 2, -self.h / 2, self.w / 2, self.h / 2), P["PLQ_R"]) \
            .difference(circ(-self.hole_x, self.hole_dy, self.hole_d / 2)) \
            .difference(circ(self.hole_x, self.hole_dy, self.hole_d / 2))

    def safe_box(self, margin=0.6):
        return box(-self.art_x_max, -self.h / 2 + margin, self.art_x_max, self.h / 2 - margin)

# ---------------------------------------------------------------- 2-D helpers
def circ(x, y, r):
    return Point(x, y).buffer(r, 48)

def ellipse(x, y, rx, ry):
    return translate(sscale(Point(0, 0).buffer(1.0, 48), rx, ry, origin=(0, 0)), x, y)

def rect(x0, y0, x1, y1):
    return box(min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1))

def rounded(poly, r):
    return poly.buffer(-r, 16).buffer(r, 16)

def smooth(poly, r):
    return poly.buffer(r, 16).buffer(-r, 16)

def stroke(points, w):
    return LineString(points).buffer(w / 2, 8)

def tapered(points, w0, w1, n=24):
    """A stroke whose width goes from w0 to w1 along the path (union of discs)."""
    line = LineString(points)
    discs = []
    for i in range(n + 1):
        t = i / n
        p = line.interpolate(t, normalized=True)
        discs.append(circ(p.x, p.y, (w0 + (w1 - w0) * t) / 2))
    hull = unary_union([discs[i].union(discs[i + 1]).convex_hull for i in range(n)])
    return hull

def mirror_x(g):
    return sscale(g, -1, 1, origin=(0, 0))

def text_geom(s, cap_h, font_file):
    font = FontProperties(fname=str(font_file))
    tp = TextPath((0, 0), s, size=10, prop=font)
    ref = TextPath((0, 0), "H", size=10, prop=font)
    k = cap_h / ref.get_extents().height
    polys = [Polygon(pts * k) for pts in tp.to_polygons() if len(pts) >= 3]
    polys = [p.buffer(0) for p in polys]
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
    return translate(geom, -(b[0] + b[2]) / 2, -(b[1] + b[3]) / 2)

def islands(g):
    return list(g.geoms) if hasattr(g, "geoms") else [g]

def thin_report(name, g, w=0.6):
    polys = islands(g)
    thin = [p for p in polys if p.buffer(-w / 2).is_empty]
    print(f"{name:12s}: {len(polys):3d} islands, {len(thin)} thinner than {w} mm, "
          f"x {g.bounds[0]:.1f}..{g.bounds[2]:.1f}  y {g.bounds[1]:.1f}..{g.bounds[3]:.1f}")

# ---------------------------------------------------------------- 3-D
def to_cs(g):
    contours = []
    for p in islands(g):
        contours.append(np.asarray(p.exterior.coords)[:-1])
        for r in p.interiors:
            contours.append(np.asarray(r.coords)[:-1])
    return CrossSection(contours, FillRule.EvenOdd)

def ext(cs, z0, z1):
    return Manifold.extrude(cs, z1 - z0).translate((0, 0, z0))

def clean_mesh(man):
    mesh = man.simplify(0.001).to_mesh()
    v = np.asarray(mesh.vert_properties)[:, :3]; f = np.asarray(mesh.tri_verts)
    uniq, inv = np.unique(np.round(v, 5), axis=0, return_inverse=True)
    f2 = inv.reshape(-1)[f]
    f2 = f2[(f2[:, 0] != f2[:, 1]) & (f2[:, 1] != f2[:, 2]) & (f2[:, 2] != f2[:, 0])]
    e = np.sort(np.vstack([f2[:, [0, 1]], f2[:, [1, 2]], f2[:, [2, 0]]]), axis=1)
    _, cnt = np.unique(e, axis=0, return_counts=True)
    return (v, f) if (cnt != 2).any() else (uniq, f2)

def _mesh_xml(obj_id, man):
    v, f = clean_mesh(man)
    out = [f'  <object id="{obj_id}" type="model">\n   <mesh>\n    <vertices>\n']
    out += [f'     <vertex x="{x:.4f}" y="{y:.4f}" z="{z:.4f}"/>\n' for x, y, z in v]
    out.append('    </vertices>\n    <triangles>\n')
    out += [f'     <triangle v1="{a}" v2="{b}" v3="{c}"/>\n' for a, b, c in f]
    out.append('    </triangles>\n   </mesh>\n  </object>\n')
    return "".join(out), len(f)

def _tf(mat):
    return " ".join(f"{mat[r][c]:.6g}" for c in range(4) for r in range(3))

def write_3mf(out_path, parts, title, object_name, bed_w, bed_d, app="plaque_lib.py"):
    """parts: list of (name, filament_slot, Manifold). One object, one part per entry."""
    for name, slot, man in parts:
        assert man.status() == m3.Error.NoError, (name, man.status())
    ident = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]
    place = [[1, 0, 0, bed_w / 2], [0, 1, 0, bed_d / 2], [0, 0, 1, 0]]
    meshes, comps, plines = [], [], []
    for i, (name, slot, man) in enumerate(parts, start=1):
        xml, ntri = _mesh_xml(i, man)
        meshes.append(xml)
        comps.append(f'    <component objectid="{i}" transform="{_tf(ident)}"/>\n')
        plines.append(
            f'    <part id="{i}" subtype="normal_part">\n'
            f'      <metadata key="name" value="{name}"/>\n'
            f'      <metadata key="matrix" value="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1"/>\n'
            f'      <metadata key="extruder" value="{slot}"/>\n'
            f'      <mesh_stat face_count="{ntri}" edges_fixed="0" degenerate_facets="0" facets_removed="0" facets_reversed="0" backwards_edges="0"/>\n'
            f'    </part>\n')
    obj = len(parts) + 1
    today = datetime.date.today().isoformat()
    model = f'''<?xml version="1.0" encoding="UTF-8"?>
<model unit="millimeter" xml:lang="en-US" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" xmlns:BambuStudio="http://schemas.bambulab.com/package/2021">
 <metadata name="Application">{app}</metadata>
 <metadata name="BambuStudio:3mfVersion">1</metadata>
 <metadata name="Title">{title}</metadata>
 <metadata name="CreationDate">{today}</metadata>
 <metadata name="ModificationDate">{today}</metadata>
 <resources>
{"".join(meshes)}  <object id="{obj}" type="model">
   <components>
{"".join(comps)}   </components>
  </object>
 </resources>
 <build>
  <item objectid="{obj}" transform="{_tf(place)}" printable="1"/>
 </build>
</model>
'''
    settings = f'''<?xml version="1.0" encoding="UTF-8"?>
<config>
  <object id="{obj}">
    <metadata key="name" value="{object_name}"/>
    <metadata key="extruder" value="1"/>
{"".join(plines)}  </object>
  <plate>
    <metadata key="plater_id" value="1"/>
    <metadata key="plater_name" value="{object_name}"/>
    <metadata key="locked" value="false"/>
    <model_instance>
      <metadata key="object_id" value="{obj}"/>
      <metadata key="instance_id" value="0"/>
      <metadata key="identify_id" value="301"/>
    </model_instance>
  </plate>
  <assemble>
   <assemble_item object_id="{obj}" instance_id="0" transform="{_tf(place)}" offset="0 0 0" />
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
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", rels)
        z.writestr("3D/3dmodel.model", model)
        z.writestr("Metadata/model_settings.config", settings)
    print("wrote", out_path, out_path.stat().st_size, "bytes")

# ---------------------------------------------------------------- preview
def preview(path, blank, layers, colors, title, xlim=None, figsize=(22, 3.6), grid=2):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import PathPatch
    from matplotlib.path import Path as MPath
    fig, ax = plt.subplots(figsize=figsize)
    def draw(g, color):
        verts, codes = [], []
        for p in islands(g):
            for ring in [p.exterior] + list(p.interiors):
                pts = np.asarray(ring.coords)
                verts += list(pts); codes += [MPath.MOVETO] + [MPath.LINETO] * (len(pts) - 2) + [MPath.CLOSEPOLY]
        ax.add_patch(PathPatch(MPath(verts, codes), facecolor=color, edgecolor="none"))
    draw(blank.geom, colors[BLACK])
    for slot, g in layers:
        draw(g, colors[slot])
    if xlim is None:
        xlim = (-blank.w / 2 - 2, blank.w / 2 + 2)
    ax.set_xlim(*xlim); ax.set_ylim(-blank.h / 2 - 1, blank.h / 2 + 1)
    ax.set_aspect("equal"); ax.set_facecolor("#d8d8d8"); ax.set_title(title)
    ax.set_xticks(range(int(xlim[0]), int(xlim[1]) + 1, grid)); ax.grid(True, lw=0.25)
    fig.tight_layout(); fig.savefig(path, dpi=130); plt.close(fig)
