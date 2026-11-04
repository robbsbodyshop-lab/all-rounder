#!/usr/bin/env python3
"""
"Gruß vom Krampus" plaque: Fraktur lettering in the middle, a Krampus silhouette facing
inward at each end. Raised 0.6 mm on the black plaque blank.

    python3 make_plaque_krampus.py
"""
from plaque_lib import *

WHITE, RED = 2, 3
ART_T, GAP = 0.6, 0.5
FONT = HERE / "fonts" / "UnifrakturCook-Bold.ttf"
blank = Blank()

def krampus():
    """Silhouette facing right, about 22 mm tall. Horns, open goat muzzle with the tongue
    hanging down, basket on the back, birch rod in the front hand, hooves, arrow tail."""
    # ---- head
    cranium = circ(2.4, 6.3, 2.4)
    muzzle = smooth(Polygon([(3.2, 7.6), (7.0, 6.1), (7.3, 5.2), (7.0, 4.7), (4.0, 4.7), (3.0, 5.0)]), 0.35)
    mouth = Polygon([(4.0, 4.9), (7.8, 4.9), (7.8, 3.0), (4.0, 4.1)])                 # open mouth (void)
    jaw = smooth(Polygon([(3.5, 4.3), (6.5, 2.9), (6.0, 2.1), (3.2, 3.2)]), 0.25)
    tongue = tapered([(4.4, 4.5), (6.2, 4.2), (7.2, 3.4), (7.5, 1.8), (6.9, 0.3)], 1.0, 0.62)
    jaw = jaw.difference(tongue.buffer(GAP))
    beard = Polygon([(3.3, 3.3), (4.6, 2.7), (3.5, 1.0)]).difference(tongue.buffer(GAP))
    horn1 = tapered([(1.2, 8.2), (0.5, 9.4), (-0.7, 10.2), (-2.2, 10.55)], 1.5, 0.6)
    horn2 = tapered([(3.0, 8.4), (3.0, 9.6), (2.2, 10.3), (0.8, 10.6)], 1.5, 0.6)
    ear = Polygon([(0.8, 7.6), (-1.2, 8.6), (0.2, 6.6)])
    mane = unary_union([Polygon([(0.2, 6.0), (-1.6, 6.8), (-0.4, 5.0)]), Polygon([(-0.2, 4.8), (-2.0, 5.2), (-0.6, 3.8)])])
    eye = circ(3.5, 6.5, 0.45)
    head = unary_union([cranium, muzzle, horn1, horn2, ear, mane]).difference(mouth).union(unary_union([jaw, beard, tongue]))
    # ---- body
    torso = smooth(Polygon([(1.4, 6.2), (-0.8, 6.6), (-2.6, 5.4), (-3.4, 3.0), (-3.2, -0.2), (-2.4, -2.8),
                            (-0.2, -3.8), (2.4, -3.5), (3.4, -1.2), (3.2, 1.6), (2.4, 3.8), (1.8, 5.0)]), 0.8)
    basket = smooth(Polygon([(-3.6, 4.6), (-6.8, 5.0), (-6.2, -1.2), (-3.4, -1.6)]), 0.4)
    basket = basket.difference(torso.buffer(GAP))
    strap = stroke([(-1.2, 5.8), (-3.4, 5.4), (-4.6, 4.9)], 0.7)
    arm = tapered([(2.0, 2.6), (4.6, 0.8), (6.2, -2.4)], 1.8, 1.3)
    hand = circ(6.3, -2.7, 0.85)
    handle = stroke([(6.8, -1.4), (6.0, -3.6)], 0.9)
    twigs = unary_union([stroke([(6.1, -3.5), p], 0.62) for p in [(7.4, -6.6), (8.4, -5.8), (9.0, -4.6), (9.1, -3.2)]])
    tail = unary_union([stroke([(-2.2, -1.8), (-4.4, -3.0), (-5.6, -5.4)], 0.8),
                        Polygon([(-6.5, -4.8), (-6.8, -6.9), (-4.8, -6.1)])])
    leg_b = tapered([(-1.2, -3.0), (-2.9, -5.9), (-2.0, -8.2), (-2.5, -9.8)], 2.2, 1.5)
    leg_f = tapered([(1.5, -3.0), (3.0, -5.8), (2.0, -8.2), (2.4, -9.8)], 2.2, 1.5)
    hooves = unary_union([Polygon([(cx - 1.4, -9.5), (cx + 1.3, -9.5), (cx + 1.2, -10.9), (cx - 1.5, -10.9)])
                          for cx in (-2.5, 2.4)])
    clefts = unary_union([stroke([(cx - 0.1, -10.9), (cx - 0.1, -10.1)], 0.45) for cx in (-2.5, 2.4)])
    fur = unary_union([Polygon([(-2.9, -4.8), (-4.6, -5.2), (-3.2, -6.4)]), Polygon([(-3.0, 2.2), (-4.6, 1.2), (-3.0, 0.6)]),
                       Polygon([(0.6, -3.6), (0.0, -5.2), (1.8, -3.8)])])
    body = unary_union([torso, basket, strap, arm, hand, handle, twigs, tail, leg_b, leg_f, hooves, fur])
    fig = unary_union([head, body]).difference(unary_union([eye, clefts]))
    fig = fig.buffer(0.05, 8).buffer(-0.05, 8)
    return fig

def traced_krampus(path=HERE / "krampus_silhouette_source.jpg", height=21.8, min_feature=0.45):
    """Trace the supplied silhouette image and scale it to `height` mm. The birch switch
    in the source is drawn with hair-thin strands that no nozzle can print, so that
    region is masked out and a solid fan of twigs is drawn from the hand instead.
    Anything thinner than `min_feature` (bell strings, fur wisps) is dropped."""
    import cv2
    img = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
    mask = (img < 110).astype(np.uint8) * 255
    mask[430:720, :1012] = 0                                          # the birch strands
    cnts, hier = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    polys = []
    for i, c in enumerate(cnts):
        if hier[0][i][3] == -1 and cv2.contourArea(c) > 200:
            holes = []
            j = hier[0][i][2]
            while j != -1:
                if cv2.contourArea(cnts[j]) > 200:
                    holes.append([tuple(pt[0]) for pt in cnts[j]])
                j = hier[0][j][0]
            polys.append(Polygon([tuple(pt[0]) for pt in c], holes).buffer(0))
    g = max(islands(unary_union(polys)), key=lambda q: q.area)
    minx, miny, maxx, maxy = g.bounds
    k = height / (maxy - miny)
    cx, cy = (minx + maxx) / 2, (miny + maxy) / 2
    g = translate(sscale(g, k, -k, origin=(0, 0)), -cx * k, cy * k)   # image y points down
    r = min_feature / 2
    g = g.buffer(-r, 8).buffer(r, 8)
    g = max(islands(g), key=lambda q: q.area).simplify(0.02)
    hand = ((1038 - cx) * k, -(676 - cy) * k)                          # where the switch handle meets the hand
    # birch bundle: a wedge pointing up and away from the hand, with notches at the tip
    from shapely.affinity import rotate
    L, w0, w1 = 4.6, 1.3, 3.8
    wedge = Polygon([(0, -w0 / 2), (L, -w1 / 2), (L, w1 / 2), (0, w0 / 2)])
    notches = unary_union([Polygon([(L + 0.1, y - 0.28), (L - 1.6, y), (L + 0.1, y + 0.28)]) for y in (-1.15, 0.0, 1.15)])
    bundle = wedge.difference(notches)
    bundle = translate(rotate(bundle, 150, origin=(0, 0)), hand[0] + 0.3, hand[1] + 0.2)
    twigs = unary_union([bundle, circ(*hand, 0.75)])
    g = unary_union([g, twigs])
    b = g.bounds
    return translate(g, -(b[0] + b[2]) / 2, -(b[1] + b[3]) / 2)

K = traced_krampus()                 # faces left in the source image
K = mirror_x(K)                      # left-hand copy faces the lettering
kx = blank.art_x_max - (K.bounds[2] - K.bounds[0]) / 2 - 0.5
left = translate(K, -kx - (K.bounds[0] + K.bounds[2]) / 2, 0)
right = mirror_x(left)
silhouettes = unary_union([left, right])

inner = min(abs(left.bounds[2]), abs(right.bounds[0]))
text = text_geom("Gruß vom Krampus", 8.0, FONT)
max_w, max_h = 2 * (inner - 3.0), blank.h - 2 * 0.8
b = text.bounds
k = min(max_w / (b[2] - b[0]), max_h / (b[3] - b[1]))
text = sscale(text, k, k, origin=(0, 0))
print(f"text scaled by {k:.3f}: {text.bounds[2]-text.bounds[0]:.1f} x {text.bounds[3]-text.bounds[1]:.1f} mm")

layers = [(RED, silhouettes), (WHITE, text)]
safe = blank.safe_box(0.5)
for slot, g in layers:
    assert safe.contains(g), f"slot {slot} leaves the safe area {g.bounds}"
assert silhouettes.intersection(text).area < 1e-6
thin_report("krampus", K); thin_report("text", text)

parts = [("Plaque base", BLACK, ext(to_cs(blank.geom), 0, blank.t))]
parts.append(("Krampus silhouettes", RED, ext(to_cs(silhouettes), blank.t, blank.t + ART_T)))
parts.append(("Lettering", WHITE, ext(to_cs(text), blank.t, blank.t + ART_T)))
for name, slot, man in parts:
    print(f"{name:20s} slot {slot} tris={man.num_tri():6d} vol={man.volume():8.1f} mm3")

COLORS = {BLACK: "#141416", WHITE: "#f4f1ea", RED: "#c8102e"}
preview(HERE / "preview_plaque_krampus.png", blank, layers, COLORS, "Gruß vom Krampus plaque, front view (mm)", grid=10)
preview(HERE / "preview_plaque_krampus_zoom.png", blank, layers, COLORS, "Krampus silhouette (mm)",
        xlim=(-82, -56), figsize=(9, 8), grid=2)
write_3mf(HERE / "plaque_gruss_vom_krampus.3mf", parts, "Gruss vom Krampus plaque", "Gruss vom Krampus plaque",
          blank.P["BED_W"], blank.P["BED_D"], app="make_plaque_krampus.py")
