#!/usr/bin/env python3
"""Generates the gantry design drawings as SVG (pure Python). Run: python3 make_drawings.py
Model units are millimetres; each view has its own scale (model y is up). All strokes use
currentColor so the drawings render on light or dark grounds."""
import math, os
HERE = os.path.dirname(os.path.abspath(__file__))

def esc(s): return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

STYLE = """
<style>
  .l{stroke:currentColor;fill:none;stroke-width:1.1;stroke-linecap:round;stroke-linejoin:round}
  .t{stroke:currentColor;fill:none;stroke-width:0.55;stroke-linecap:round}
  .k{stroke:currentColor;fill:none;stroke-width:1.8;stroke-linejoin:round}
  .d{stroke:currentColor;fill:none;stroke-width:0.8;stroke-dasharray:5 3}
  .c{stroke:currentColor;fill:none;stroke-width:0.6;stroke-dasharray:14 3 3 3}
  .h{stroke:currentColor;fill:none;stroke-width:0.7;stroke-dasharray:2 2}
  .st{fill:currentColor;fill-opacity:0.22;stroke:currentColor;stroke-width:1.1}
  .conc{fill:url(#conc);stroke:currentColor;stroke-width:1.1}
  .grout{fill:url(#grout);stroke:currentColor;stroke-width:0.8}
  .bag{fill:currentColor;fill-opacity:0.08;stroke:currentColor;stroke-width:0.8;stroke-dasharray:5 3}
  text{font-family:Inter,Helvetica,Arial,sans-serif;fill:currentColor}
  .n{font-size:11px}.s{font-size:9.5px}.b{font-size:13px;font-weight:700}.tt{font-size:16px;font-weight:700}
  .w{font-size:9px}
</style>
<defs>
  <pattern id="conc" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
    <line x1="0" y1="0" x2="0" y2="9" stroke="currentColor" stroke-width="0.6" stroke-opacity="0.75"/>
    <circle cx="5" cy="3" r="0.7" fill="currentColor" fill-opacity="0.6"/>
  </pattern>
  <pattern id="grout" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
    <line x1="0" y1="0" x2="0" y2="5" stroke="currentColor" stroke-width="0.5" stroke-opacity="0.7"/>
    <line x1="0" y1="2.5" x2="5" y2="2.5" stroke="currentColor" stroke-width="0.5" stroke-opacity="0.7"/>
  </pattern>
  <marker id="ar" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto-start-reverse" markerUnits="userSpaceOnUse">
    <path d="M0,1 L7,4 L0,7 z" fill="currentColor"/></marker>
</defs>
"""

class Sheet:
    def __init__(self, w, h, number, title):
        self.w, self.h, self.number, self.title = w, h, number, title
        self.parts = []
    def raw(self, s): self.parts.append(s)
    def heading(self, x, y, s): self.raw(f'<text x="{x}" y="{y}" class="tt">{esc(s)}</text>')
    def view(self, ox, oy, scale): return View(self, ox, oy, scale)
    def titleblock(self, notes=()):
        w, h = self.w, self.h
        self.raw(f'<rect x="1" y="1" width="{w-2}" height="{h-2}" class="t"/>')
        bw, bh, lw = 520, 78, 370
        x0, y0 = w - bw - 10, h - bh - 10
        self.raw(f'<rect x="{x0}" y="{y0}" width="{bw}" height="{bh}" class="l"/>')
        self.raw(f'<line x1="{x0}" y1="{y0+26}" x2="{x0+bw}" y2="{y0+26}" class="t"/>')
        self.raw(f'<line x1="{x0+lw}" y1="{y0}" x2="{x0+lw}" y2="{y0+bh}" class="t"/>')
        self.raw(f'<text x="{x0+8}" y="{y0+18}" class="b">BAG GANTRY — 15 m, 7 HANGERS</text>')
        self.raw(f'<text x="{x0+8}" y="{y0+44}" class="n">{esc(self.title)}</text>')
        self.raw(f'<text x="{x0+8}" y="{y0+60}" class="s">Dimensions mm, not to scale. Steel AS 1163 C350L0 / AS/NZS 3678-350.</text>')
        self.raw(f'<text x="{x0+8}" y="{y0+72}" class="s">HDG AS/NZS 4680. Concrete N32. Bolts Gr 8.8 HDG. Welds SP, AS/NZS 1554.1.</text>')
        self.raw(f'<text x="{x0+lw+8}" y="{y0+18}" class="b">{esc(self.number)}</text>')
        self.raw(f'<text x="{x0+lw+8}" y="{y0+44}" class="s">Rev P1 — PRELIMINARY</text>')
        self.raw(f'<text x="{x0+lw+8}" y="{y0+58}" class="s">Not for construction until</text>')
        self.raw(f'<text x="{x0+lw+8}" y="{y0+72}" class="s">certified by an engineer.</text>')
        for i, n in enumerate(notes):
            self.raw(f'<text x="14" y="{h-14-12*(len(notes)-1-i)}" class="s">{esc(n)}</text>')
    def note(self, x, y, s, cls="s"): self.raw(f'<text x="{x}" y="{y}" class="{cls}">{esc(s)}</text>')
    def save(self, name):
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}">'
               + STYLE + "\n".join(self.parts) + "</svg>")
        p = os.path.join(HERE, name)
        with open(p, "w") as f: f.write(svg)
        print("wrote", p)

class View:
    def __init__(self, sheet, ox, oy, s): self.sh, self.ox, self.oy, self.s = sheet, ox, oy, s
    def X(self, x): return self.ox + x * self.s
    def Y(self, y): return self.oy - y * self.s
    def line(self, x1, y1, x2, y2, cls="l"):
        self.sh.raw(f'<line x1="{self.X(x1):.1f}" y1="{self.Y(y1):.1f}" x2="{self.X(x2):.1f}" y2="{self.Y(y2):.1f}" class="{cls}"/>')
    def rect(self, x, y, w, h, cls="l", rx=0):
        self.sh.raw(f'<rect x="{self.X(x):.1f}" y="{self.Y(y+h):.1f}" width="{w*self.s:.1f}" height="{h*self.s:.1f}" class="{cls}"'
                    + (f' rx="{rx*self.s:.1f}"' if rx else "") + '/>')
    def circle(self, cx, cy, r, cls="l"):
        self.sh.raw(f'<circle cx="{self.X(cx):.1f}" cy="{self.Y(cy):.1f}" r="{r*self.s:.1f}" class="{cls}"/>')
    def poly(self, pts, cls="l", closed=True):
        d = " ".join(f"{self.X(x):.1f},{self.Y(y):.1f}" for x, y in pts)
        self.sh.raw(f'<{"polygon" if closed else "polyline"} points="{d}" class="{cls}"/>')
    def text(self, x, y, s, cls="n", anchor="middle", rot=0, dx=0, dy=0):
        X, Y = self.X(x) + dx, self.Y(y) + dy
        tr = f' transform="rotate({rot} {X:.1f} {Y:.1f})"' if rot else ""
        self.sh.raw(f'<text x="{X:.1f}" y="{Y:.1f}" class="{cls}" text-anchor="{anchor}"{tr}>{esc(s)}</text>')
    def dim(self, x1, y1, x2, y2, off, label=None, cls="t"):
        """Linear dimension: horizontal if y1 == y2 (dimension line at y1 + off), else vertical (line at x1 + off)."""
        if y1 == y2:
            yd = y1 + off
            for x in (x1, x2): self.line(x, y1 + 0.15 * off, x, yd + 0.08 * off, cls)
            self.sh.raw(f'<line x1="{self.X(x1):.1f}" y1="{self.Y(yd):.1f}" x2="{self.X(x2):.1f}" y2="{self.Y(yd):.1f}" class="{cls}" marker-start="url(#ar)" marker-end="url(#ar)"/>')
            self.text((x1 + x2) / 2, yd, label if label is not None else f"{abs(x2-x1):.0f}", "s", dy=-3)
        else:
            xd = x1 + off
            for y in (y1, y2): self.line(x1 + 0.15 * off, y, xd + 0.08 * off, y, cls)
            self.sh.raw(f'<line x1="{self.X(xd):.1f}" y1="{self.Y(y1):.1f}" x2="{self.X(xd):.1f}" y2="{self.Y(y2):.1f}" class="{cls}" marker-start="url(#ar)" marker-end="url(#ar)"/>')
            self.text(xd, (y1 + y2) / 2, label if label is not None else f"{abs(y2-y1):.0f}", "s", rot=-90, dy=-3)
    def leader(self, x, y, tx, ty, s, anchor="start", cls="n"):
        self.sh.raw(f'<line x1="{self.X(tx):.1f}" y1="{self.Y(ty):.1f}" x2="{self.X(x):.1f}" y2="{self.Y(y):.1f}" class="t" marker-end="url(#ar)"/>')
        lines = s if isinstance(s, (list, tuple)) else [s]
        for i, ln in enumerate(lines):
            self.text(tx, ty, ln, cls, anchor=anchor, dx=(4 if anchor == "start" else -4), dy=4 + 12 * i)
    def weld(self, x, y, size, note=""):
        X, Y = self.X(x), self.Y(y)
        self.sh.raw(f'<path d="M{X:.1f},{Y:.1f} l0,-8 l8,8 z" fill="currentColor"/>')
        self.sh.raw(f'<path d="M{X:.1f},{Y:.1f} l0,8 l8,-8 z" fill="currentColor"/>')
        self.sh.raw(f'<line x1="{X-10:.1f}" y1="{Y:.1f}" x2="{X+30:.1f}" y2="{Y:.1f}" class="t"/>')
        self.sh.raw(f'<text x="{X+11:.1f}" y="{Y-3:.1f}" class="w">{esc(size)}</text>')
        if note: self.sh.raw(f'<text x="{X+34:.1f}" y="{Y+4:.1f}" class="w">{esc(note)}</text>')
    def bolt_v(self, x, ytop, d, grip):
        """Bolt, axis vertical, head on top of the grip, nut below."""
        hw, hh = d * 0.8, d * 0.65
        self.rect(x - hw, ytop, 2 * hw, hh, "st"); self.rect(x - d / 2, ytop - grip - hh, d, grip + hh, "l"); self.rect(x - hw, ytop - grip - hh, 2 * hw, hh, "st")
    def bolt_h(self, y, xl, d, grip):
        """Bolt, axis horizontal, head at left of the grip, nut at right."""
        hw, hh = d * 0.8, d * 0.65
        self.rect(xl - hh, y - hw, hh, 2 * hw, "st"); self.rect(xl - hh, y - d / 2, grip + 2 * hh, d, "l"); self.rect(xl + grip, y - hw, hh, 2 * hw, "st")

# ------------------------------------------------------------------------------------------ geometry (mm)
COLS = [0, 4500, 10500, 15000]; HANG = [1500 + 2000 * i for i in range(7)]; SPL = [5000, 10000]
B = 250; SOFFIT = 3000; TOP = 3250; GROUT = 40; BP_T = 32; CAP_T = 20; SHOE_T = 16
COL_BASE = GROUT + BP_T; COL_TOP = SOFFIT - SHOE_T - CAP_T
PAD = 1800; PAD_D = 600; BLIND = 50; BP = 550; G_ANCH = 450; HEF = 450

def ga_sheet():
    sh = Sheet(1700, 1000, "GA-01", "GENERAL ARRANGEMENT — ELEVATION, PLAN, SECTION A-A")
    s = 0.066; v = sh.view(110, 400, s)
    sh.heading(110, 40, "ELEVATION (looking at the bag line)")
    v.line(-1300, 0, 16300, 0, "k"); v.text(-1250, 0, "FFL ±0", "s", anchor="start", dy=-4)
    for xc in COLS:
        v.rect(xc - PAD / 2, -PAD_D, PAD, PAD_D, "d")
        v.rect(xc - BP / 2, 0, BP, GROUT, "grout"); v.rect(xc - BP / 2, GROUT, BP, BP_T, "st")
        v.rect(xc - B / 2, COL_BASE, B, COL_TOP - COL_BASE, "st")
        v.rect(xc - 210, COL_TOP, 420, CAP_T + SHOE_T, "st")
        v.rect(xc - B / 2 - 25, COL_BASE + BP_T, B + 50, 2000 - COL_BASE - BP_T, "h")
    v.rect(-B / 2, SOFFIT, 15000 + B, B, "st")
    for xs in SPL: v.rect(xs - 20, SOFFIT - 85, 40, B + 170, "st")
    for xh in HANG:
        v.rect(xh - 150, SOFFIT - 16, 300, 16, "st"); v.rect(xh - 50, SOFFIT - 126, 100, 110, "st")
        v.line(xh, SOFFIT - 126, xh, SOFFIT - 700, "l"); v.circle(xh, SOFFIT - 160, 30, "l")
        v.rect(xh - 180, 300, 360, SOFFIT - 700 - 300, "bag", rx=90)
    v.text(7500, TOP + 250, "SPINE BEAM 250x250x9.0 SHS C350L0, continuous, 3 x 5.0 m lengths, bolted flange-plate splices at 5.0 and 10.0 m", "s", dy=-2)
    v.dim(0, TOP, 4500, TOP, 550); v.dim(4500, TOP, 10500, TOP, 550); v.dim(10500, TOP, 15000, TOP, 550)
    v.dim(0, TOP, 15000, TOP, 950, "15 000 overall (column centres)")
    for a, b in zip(HANG[:-1], HANG[1:]): v.dim(a, -PAD_D - 150, b, -PAD_D - 150, -350)
    v.dim(0, -PAD_D - 150, 1500, -PAD_D - 150, -350); v.dim(13500, -PAD_D - 150, 15000, -PAD_D - 150, -350)
    v.dim(15000, 0, 15000, SOFFIT, 1500, "3 000 soffit"); v.dim(15000, 0, 15000, TOP, 2300, "3 250 top of steel")
    v.dim(15000, -PAD_D, 15000, 0, 1500, "600")
    v.dim(-700, 0, -700, 2000, -300, "2 000 padding")
    v.line(12500, -300, 12500, TOP + 400, "c"); v.text(12500, TOP + 450, "A", "b"); v.text(12500, -450, "A", "b")
    sh.note(110, 492, "HANGERS: 7 off at 2 000 c/c, 200x300x16 plate + 20 mm lug, 3.25 t bolt-type bow shackle + 2 t bearing swivel each. Posted SWL 100 kg per hanger. See DET-02.")
    sh.note(110, 507, "COLUMNS: 4 off 250x250x12.5 SHS C350L0, fixed base on 550x550x32 plate with 4 x M24 cast-in anchors into 1 800 sq x 600 deep N32 pad footings. See DET-01.")
    sh.note(110, 522, "BAGS SHOWN: 1.8 m Muay Thai bags, bottom 300 above floor on 0.7 m shackle/swivel/chain sets. Columns padded 25 mm closed-cell foam to 2.0 m. Clear headroom to roof structure 3.6 m min.")
    # PLAN
    p = sh.view(110, 790, s)
    sh.heading(110, 570, "PLAN")
    for xc in COLS:
        p.rect(xc - PAD / 2, -PAD / 2, PAD, PAD, "d"); p.rect(xc - BP / 2, -BP / 2, BP, BP, "l"); p.rect(xc - B / 2, -B / 2, B, B, "st")
        for dx in (-G_ANCH / 2, G_ANCH / 2):
            for dy in (-G_ANCH / 2, G_ANCH / 2): p.circle(xc + dx, dy, 15, "l")
    p.rect(-B / 2, -B / 2, 15000 + B, B, "l")
    for xh in HANG: p.circle(xh, 0, 180, "bag"); p.circle(xh, 0, 1000, "h")
    for xs in SPL: p.rect(xs - 20, -210, 40, 420, "st")
    p.line(-1300, 0, 16300, 0, "c")
    p.dim(4500 - PAD / 2, -PAD / 2 - 150, 4500 + PAD / 2, -PAD / 2 - 150, -300, "1 800 sq pad")
    p.dim(-1100, -1000, -1100, 1000, -250, "2 000 clear zone")
    p.leader(5500, 1000, 6400, 1500, ["Dashed circles: 1.0 m radius swing envelope of a hard-hit bag.", "Keep 2.0 m clear each side of the bag line and 1.5 m beyond the end bags."], anchor="start", cls="s")
    p.leader(10500 + G_ANCH / 2, G_ANCH / 2, 11500, 1450, ["Anchor group 4 x M24 at 450 x 450 gauge on 550 x 550 x 32 base plate"], anchor="start", cls="s")
    # SECTION A-A
    q = sh.view(1480, 430, 0.09)
    sh.heading(1370, 40, "SECTION A-A")
    q.line(-1300, 0, 1300, 0, "k")
    q.rect(-PAD / 2, -PAD_D, PAD, PAD_D, "conc"); q.rect(-PAD / 2 - 100, -PAD_D - BLIND, PAD + 200, BLIND, "grout")
    q.rect(-PAD / 2 - 400, -150, 400, 150, "conc"); q.rect(PAD / 2, -150, 400, 150, "conc")
    q.rect(-BP / 2, 0, BP, GROUT, "grout"); q.rect(-BP / 2, GROUT, BP, BP_T, "st")
    q.rect(-B / 2, COL_BASE, B, COL_TOP - COL_BASE, "st"); q.rect(-210, COL_TOP, 420, CAP_T + SHOE_T, "st"); q.rect(-B / 2, SOFFIT, B, B, "st")
    for dx in (-G_ANCH / 2, G_ANCH / 2): q.rect(dx - 12, -HEF, 24, HEF + 150, "l"); q.rect(dx - 50, -HEF - 16, 100, 16, "st")
    q.rect(-180, 300, 360, SOFFIT - 700 - 300, "bag", rx=90); q.line(0, SOFFIT - 126, 0, SOFFIT - 700, "d")
    q.rect(-B / 2 - 25, COL_BASE + BP_T, B + 50, 2000 - COL_BASE - BP_T, "h")
    q.dim(-PAD / 2, -PAD_D - 250, PAD / 2, -PAD_D - 250, -200, "1 800")
    q.dim(PAD / 2 + 200, -PAD_D, PAD / 2 + 200, 0, 250, "600"); q.dim(PAD / 2 + 200, 0, PAD / 2 + 200, SOFFIT, 250, "3 000")
    q.dim(-B / 2, TOP + 150, B / 2, TOP + 150, 150, "250")
    q.leader(B / 2, 1400, 600, 1700, ["250x250x12.5 SHS"], anchor="start", cls="s")
    q.leader(-G_ANCH / 2, -300, -650, -350, ["M24 8.8 cast-in", "anchors, h_ef 450"], anchor="end", cls="s")
    q.leader(-PAD / 2 - 250, -75, -700, -900, ["Slab doweled", "to pad, N12 @ 300"], anchor="end", cls="s")
    sh.titleblock(["Beam soffit 3.0 m suits 1.8 m Muay Thai bags (bottom 0.3 m) and 1.2-1.5 m boxing bags on 0.6-0.9 m chain sets. Design bag mass 100 kg per hanger.",
                   "Six-bag layout: use hangers 1-3 and 5-7; the 7.5 m position then suits a double-end or speed bag. Do not tie the frame to walls or roof without a separate check."])
    sh.save("GA-01-general-arrangement.svg")

def base_sheet():
    sh = Sheet(1500, 1000, "DET-01", "COLUMN BASE PLATE, ANCHORS AND PAD FOOTING")
    # base plate plan
    v = sh.view(140, 330, 0.42)
    sh.heading(60, 40, "BASE PLATE — PLAN")
    v.rect(0, 0, BP, BP, "l"); v.rect((BP - B) / 2, (BP - B) / 2, B, B, "st")
    for dx in (50, 50 + G_ANCH):
        for dy in (50, 50 + G_ANCH): v.circle(dx, dy, 15, "l"); v.rect(dx - 32, dy - 32, 64, 64, "t")
    v.line(-40, BP / 2, BP + 40, BP / 2, "c"); v.line(BP / 2, -40, BP / 2, BP + 40, "c")
    v.dim(0, -60, 50, -60, -90, "50"); v.dim(50, -60, 50 + G_ANCH, -60, -90, "450 gauge"); v.dim(50 + G_ANCH, -60, BP, -60, -90, "50")
    v.dim(0, -60, BP, -60, -200, "550 x 550 x 32 PL Gr 350")
    v.dim(BP + 60, 0, BP + 60, BP, 90, "550"); v.dim(BP + 60, (BP - B) / 2, BP + 60, (BP + B) / 2, 220, "250 SHS")
    v.leader(50 + G_ANCH, 50 + G_ANCH, BP + 130, BP + 80, ["4 x Ø30 holes for M24 anchors, 65x65x8 HDG", "plate washers, nut + lock nut (or wedge-lock washers)"], anchor="start", cls="s")
    v.leader((BP + B) / 2, BP / 2 + 60, BP + 130, BP - 100, ["10 mm CFW all round, SP category,", "column to base plate (shop weld)"], anchor="start", cls="s")
    v.weld((BP + B) / 2 + 6, BP / 2 - 120, "10", "all round")
    # section
    q = sh.view(1000, 560, 0.3)
    sh.heading(700, 40, "SECTION THROUGH BASE AND PAD")
    q.line(-PAD / 2 - 500, 0, PAD / 2 + 500, 0, "k")
    q.rect(-PAD / 2, -PAD_D, PAD, PAD_D, "conc"); q.rect(-PAD / 2 - 100, -PAD_D - BLIND, PAD + 200, BLIND, "grout")
    q.rect(-PAD / 2 - 500, -150, 500, 150, "conc"); q.rect(PAD / 2, -150, 500, 150, "conc")
    q.rect(-BP / 2, 0, BP, GROUT, "grout"); q.rect(-BP / 2, GROUT, BP, BP_T, "st")
    q.rect(-B / 2, COL_BASE, B, 520, "st"); q.line(-B / 2 + 12.5, COL_BASE, -B / 2 + 12.5, COL_BASE + 520, "t"); q.line(B / 2 - 12.5, COL_BASE, B / 2 - 12.5, COL_BASE + 520, "t")
    for yb, off in ((-PAD_D + 75 + 8, 16), (-50 - 8, -16)):
        q.line(-PAD / 2 + 50, yb, PAD / 2 - 50, yb, "k")
        for xb in range(-800, 801, 200): q.circle(xb, yb + off, 8, "st")
    for dx in (-G_ANCH / 2, G_ANCH / 2):
        q.rect(dx - 12, -HEF, 24, HEF + GROUT + BP_T + 80, "st"); q.rect(dx - 50, -HEF - 16, 100, 16, "st")
        q.rect(dx - 22, -HEF - 16 - 22, 44, 22, "st"); q.rect(dx - 22, -HEF, 44, 22, "st")
        q.rect(dx - 32, COL_BASE, 64, 8, "st"); q.rect(dx - 22, COL_BASE + 8, 44, 22, "st"); q.rect(dx - 22, COL_BASE + 30, 44, 14, "st")
        q.rect(dx - 22, GROUT - 22, 44, 22, "st")
        q.circle(dx - 40, -120, 8, "st"); q.circle(dx + 40, -120, 8, "st")
    for sx in (-1, 1): q.line(sx * (PAD / 2 - 300), -75, sx * (PAD / 2 + 450), -75, "k")
    q.dim(1400, -PAD_D, 1400, 0, 60, "600")
    q.dim(1400, -HEF, 1400, 0, 130, "450 h_ef"); q.dim(1400, -PAD_D, 1400, -HEF - 16, 130, "134")
    q.dim(575, 0, 575, GROUT, 60, "40 grout"); q.dim(575, GROUT, 575, COL_BASE, 180, "32 PL")
    q.dim(-PAD / 2, -PAD_D - BLIND - 120, PAD / 2, -PAD_D - BLIND - 120, -120, "1 800")
    q.dim(-G_ANCH / 2, COL_BASE + 560, G_ANCH / 2, COL_BASE + 560, 80, "450 gauge")
    q.leader(G_ANCH / 2 + 12, COL_BASE + 40, 700, 350, ["M24 Gr 8.8 HDG threaded rod x 650 long, 150 projection;", "levelling nut under plate; snug + 1/2 turn after grout", "cures 3 days; nut + lock nut"], anchor="start", cls="s")
    q.leader(G_ANCH / 2 + 50, -HEF - 8, 700, -300, ["100x100x16 anchor plate Gr 250,", "double nut below, single nut above", "(no welding to Gr 8.8 rod)"], anchor="start", cls="s")
    q.leader(-PAD / 2 - 300, -75, -1450, -250, ["N12 dowels @ 300 c/c, 450 each", "side, epoxied into existing slab"], anchor="end", cls="s")
    q.leader(0, GROUT / 2, -400, 380, ["Non-shrink cementitious grout ≥ 50 MPa,", "40 mm bed, full contact under plate"], anchor="end", cls="s")
    q.leader(-B / 2, 300, -450, 620, ["250x250x12.5 SHS column,", "10 CFW all round to plate"], anchor="end", cls="s")
    q.leader(-300, -PAD_D + 83, -300, -PAD_D - BLIND - 300, ["N16 @ 200 c/c each way, top and bottom, cover 50 (75 to blinding);", "4 x N16 U-bar hairpins around each anchor pair, 1 000 legs"], anchor="end", cls="s")
    q.leader(300, -PAD_D - 25, 500, -PAD_D - 300, ["50 mm N20 blinding on compacted subgrade", "(allowable bearing ≥ 100 kPa, verify on site)"], anchor="start", cls="s")
    q.weld(-B / 2 - 6, COL_BASE + 12, "10")
    # footing plan
    f = sh.view(120, 880, 0.12)
    sh.heading(60, 470, "PAD FOOTING — PLAN (top mesh not shown)")
    f.rect(0, 0, PAD, PAD, "l")
    for i in range(1, 9): f.line(50, i * 200 - 50, PAD - 50, i * 200 - 50, "l"); f.line(i * 200 - 50, 50, i * 200 - 50, PAD - 50, "l")
    f.rect((PAD - BP) / 2, (PAD - BP) / 2, BP, BP, "d")
    for dx in (-G_ANCH / 2, G_ANCH / 2):
        for dy in (-G_ANCH / 2, G_ANCH / 2): f.circle(PAD / 2 + dx, PAD / 2 + dy, 12, "st")
    for dy in (-G_ANCH / 2, G_ANCH / 2):
        f.poly([(PAD / 2 - 700, PAD / 2 + dy - 60), (PAD / 2 + 300, PAD / 2 + dy - 60), (PAD / 2 + 300, PAD / 2 + dy + 60), (PAD / 2 - 700, PAD / 2 + dy + 60)], "k", closed=False)
    for sx in range(4):
        y = 150 + sx * 500
        f.line(-450, y, 300, y, "k"); f.line(PAD - 300, y, PAD + 450, y, "k"); f.line(y, -450, y, 300, "k"); f.line(y, PAD - 300, y, PAD + 450, "k")
    f.dim(0, PAD + 520, PAD, PAD + 520, 150, "1 800"); f.dim(PAD + 520, 0, PAD + 520, PAD, 150, "1 800")
    f.leader(PAD / 2 + 300, PAD / 2 + G_ANCH / 2 + 60, PAD + 750, PAD - 100, ["N16 U-bar hairpins around anchors", "(2 per pair, 1 000 legs)"], anchor="start", cls="s")
    f.leader(PAD + 300, 650, PAD + 750, 450, ["N12 dowels @ 300 c/c, all sides"], anchor="start", cls="s")
    sh.titleblock(["Anchor rods set in a plywood template to ±2 mm before the pour. Do not weld to Gr 8.8 rods. Pad top flush with FFL; slab saw-cut 1.9 m square and reinstated.",
                   "If an existing slab is proposed instead of pads it must be ≥ 300 mm thick and ≥ 25 MPa (cored and tested); assessment by the certifying engineer is required."])
    sh.save("DET-01-base-plate-and-footing.svg")

def hanger_sheet():
    sh = Sheet(1500, 1000, "DET-02", "HANGER LUG AND BAG HARDWARE")
    v = sh.view(520, 470, 0.75)
    sh.heading(60, 40, "HANGER — ELEVATION ALONG BEAM")
    v.rect(-260, 0, 520, B, "st"); v.line(-260, 9, 260, 9, "t"); v.line(-260, B - 9, 260, B - 9, "t")
    v.rect(-150, -16, 300, 16, "st")
    v.poly([(-50, -16), (50, -16), (50, -76)] + [(50 * math.cos(a), -76 - 50 * math.sin(a)) for a in [i * math.pi / 12 for i in range(0, 13)]] + [(-50, -76)], "st")
    v.circle(0, -76, 11, "l"); v.line(0, -76, 0, -420, "c")
    v.poly([(-28, -76), (-28, -150)] + [(-28 * math.cos(a), -150 - 28 * math.sin(a) * 1.4) for a in [i * math.pi / 12 for i in range(0, 13)]][::-1] + [(28, -76)], "k", closed=False)
    v.rect(-9, -85, 18, 18, "st"); v.rect(-40, -82, 80, 12, "l")
    v.rect(-12, -195, 24, 45, "l"); v.circle(0, -215, 16, "l"); v.rect(-12, -260, 24, 40, "l"); v.circle(0, -285, 16, "l")
    for i in range(4): v.circle(0, -320 - i * 26, 12, "l")
    v.text(0, -440, "to bag chain set (4 legs, rated by the bag maker)", "s")
    v.dim(-150, 250, 150, 250, 40, "300 hanger plate"); v.dim(-50, 250, 50, 250, 90, "100 lug")
    v.dim(300, 0, 300, B, 60, "250"); v.dim(300, -16, 300, 0, 120, "16"); v.dim(-300, -76, -300, -16, -60, "60"); v.dim(-300, -126, -300, -76, -60, "50")
    v.weld(150 + 4, -8, "8", "all round"); v.weld(50 + 4, -30, "8", "both sides")
    v.leader(130, 8, 330, 300, ["250x250x9.0 SHS spine beam"], anchor="start", cls="s")
    v.leader(120, -10, 330, -180, ["Hanger plate 200 x 300 x 16 Gr 350, 8 CFW all round, shop", "welded before HDG; 200 wide keeps the load line within", "16 mm of the beam webs (no local wall bending)"], anchor="start", cls="s")
    v.leader(45, -95, 330, -330, ["Lug 20 mm PL Gr 350, 100 wide, R50 end,", "Ø22 hole; 8 CFW both sides with returns"], anchor="start", cls="s")
    v.leader(-28, -120, -320, -200, ["3.25 t WLL Grade S bow shackle,", "BOLT TYPE with nut + split pin", "(screw pins unwind under rotation)"], anchor="end", cls="s")
    v.leader(-12, -240, -320, -320, ["2 t WLL bearing-type swivel", "(rated lifting component,", "replace at 5-yearly inspection)"], anchor="end", cls="s")
    e = sh.view(1150, 470, 0.75)
    sh.heading(980, 40, "HANGER — SECTION ACROSS BEAM")
    e.rect(-125, 0, 250, 250, "l"); e.rect(-116, 9, 232, 232, "l")
    e.rect(-100, -16, 200, 16, "st"); e.rect(-10, -126, 20, 110, "st"); e.circle(0, -76, 11, "d")
    e.line(-125, 0, -100, -16, "t"); e.line(125, 0, 100, -16, "t")
    e.dim(-125, 270, 125, 270, 60, "250"); e.dim(-100, -16, 100, -16, -60, "200 plate"); e.dim(-10, -126, 10, -126, -60, "20 lug"); e.dim(150, -16, 150, 0, 40, "16")
    e.leader(100, -8, 200, -160, ["Load path: lug → plate → 8 mm", "fillets → beam bottom wall → webs;", "wall bending lever ≤ 16 mm (checked)"], anchor="start", cls="s")
    e.leader(-125, 120, -300, 120, ["Vent/drain holes for HDG:", "2 x Ø25 each end of every", "closed member, diagonally", "opposite (galvaniser to confirm)"], anchor="end", cls="s")
    x0, y0 = 60, 818
    sh.raw(f'<rect x="{x0}" y="{y0}" width="900" height="132" class="l"/>')
    lines = ["HANGER LOAD RATING (each of 7 hangers)",
             "Posted SWL 100 kg bag mass. Design actions per hanger (characteristic): 3.9 kN vertical (4 x W, swing / snatch / jump envelope), 2.0 kN horizontal in any direction.",
             "ULS 6.1 kN vertical + 3.0 kN horizontal. Rated gear: shackle WLL 3.25 t (31.9 kN), swivel WLL 2 t (19.6 kN). Lug and welds below 6 % utilisation.",
             "Fatigue: 2 x 10^8 cycles per hanger over 50 years; every detail checked for infinite life (AS 4100 Section 11, phi = 0.7).",
             "Proof-load every hanger to 300 kg (3.0 kN) static for 10 min at commissioning and record. Re-inspect hardware 6-monthly; replace shackle and swivel at 5 years."]
    for i, ln in enumerate(lines): sh.note(x0 + 12, y0 + 22 + 22 * i, ln, "b" if i == 0 else "s")
    sh.titleblock(["Optional: a 200-300 kg rated heavy-duty bag spring between swivel and chain set reduces shock and noise; the frame is designed without relying on it.",
                   "Lug plane is parallel to the beam axis. Grind lug hole edges; no sharp corners. Column padding also covers the base plate nuts (toe-stub hazard)."])
    sh.save("DET-02-hanger-lug.svg")

def connection_sheet():
    sh = Sheet(1500, 1000, "DET-03", "BEAM-TO-COLUMN CONNECTION AND BEAM SPLICE")
    v = sh.view(520, 400, 0.55)
    sh.heading(60, 40, "BEAM-TO-COLUMN — ELEVATION")
    v.rect(-125, -400, 250, 400, "st"); v.line(-112.5, -400, -112.5, 0, "t"); v.line(112.5, -400, 112.5, 0, "t")
    v.rect(-210, 0, 420, 20, "st"); v.rect(-210, 20, 420, 16, "st")
    v.rect(-380, 36, 760, 250, "st"); v.line(-380, 45, 380, 45, "t"); v.line(-380, 277, 380, 277, "t")
    for dx in (-170, 170): v.bolt_v(dx, 36, 20, 36)
    v.dim(-170, 300, 170, 300, 60, "340 gauge"); v.dim(-210, 300, 210, 300, 160, "420 x 420 plates")
    v.dim(400, 36, 400, 286, 60, "250")
    v.weld(-125 - 6, -20, "8", "cap PL all round"); v.weld(-210 - 6, 30, "8", "shoe PL all round")
    v.leader(-170, 50, -420, 120, ["4 x M20 Gr 8.8/TB HDG, tensioned", "(turn-of-nut), Ø22 holes, hardened", "washers; nuts below the cap plate"], anchor="end", cls="s")
    v.leader(-125, -250, -420, -250, ["Column 250x250x12.5 SHS;", "cap plate 420x420x20 shop", "welded 8 CFW all round"], anchor="end", cls="s")
    v.leader(300, 250, 420, 420, ["Beam 250x250x9.0 SHS continuous over column;", "shoe plate 420x420x16 shop welded 8 CFW all round"], anchor="start", cls="s")
    p = sh.view(1250, 300, 0.45)
    sh.heading(1020, 40, "CAP / SHOE PLATE — PLAN")
    p.rect(-210, -210, 420, 420, "l"); p.rect(-125, -125, 250, 250, "st")
    for dx in (-170, 170):
        for dy in (-170, 170): p.circle(dx, dy, 11, "l")
    p.dim(-170, -250, 170, -250, -60, "340"); p.dim(-210, -250, 210, -250, -150, "420"); p.dim(250, -170, 250, 170, 60, "340")
    p.leader(-170, 170, -250, 300, ["Ø22 holes, 45 mm from tube face,", "40 mm edge distance"], anchor="end", cls="s")
    q = sh.view(520, 880, 0.5)
    sh.heading(60, 650, "BEAM SPLICE AT 5.0 m AND 10.0 m — ELEVATION")
    q.rect(-500, 0, 480, 250, "st"); q.rect(20, 0, 480, 250, "st")
    q.rect(-20, -85, 20, 420, "st"); q.rect(0, -85, 20, 420, "st")
    for dy in (-45, 125, 295): q.bolt_h(dy, -20, 20, 40)
    q.dim(-20, 350, 20, 350, 60, "2 x 20 PL"); q.dim(-500, -110, -20, -110, -60, "5 000 lengths (typ.)"); q.dim(60, -85, 60, 335, 120, "420")
    q.weld(-20 - 6, 260, "8", "all round, both plates")
    q.leader(-30, 125, -300, 420, ["8 x M20 Gr 8.8/TB tensioned, at corners and", "mid-sides of 340 gauge; flange plates", "420x420x20 Gr 350, match-drilled in pairs"], anchor="end", cls="s")
    r = sh.view(1250, 800, 0.45)
    sh.heading(1020, 600, "SPLICE — END VIEW")
    r.rect(-210, -85, 420, 420, "l"); r.rect(-125, 0, 250, 250, "st"); r.rect(-116, 9, 232, 232, "l")
    for dx, dy in [(-170, -45), (0, -45), (170, -45), (-170, 125), (170, 125), (-170, 295), (0, 295), (170, 295)]: r.circle(dx, dy, 11, "l")
    r.dim(-170, -120, 170, -120, -60, "340"); r.dim(250, -45, 250, 295, 60, "340")
    r.leader(-170, 125, -250, 250, ["Bolt pattern gives equal capacity about both", "axes (bags load the beam vertically and sideways)"], anchor="end", cls="s")
    sh.titleblock(["Splices sit 0.5 m into the 6.0 m bay (moment 5.6 kNm ULS, utilisation below 5 %). Bolt after HDG; touch up damaged zinc with two coats of zinc-rich paint.",
                   "Erection: columns plumbed on levelling nuts, beam lengths landed and bolted, tensioned, alignment checked (beam level ±5 mm, columns plumb ≤ H/500), grout, anchor nuts after 3 days."])
    sh.save("DET-03-connections.svg")

if __name__ == "__main__":
    ga_sheet(); base_sheet(); hanger_sheet(); connection_sheet()
