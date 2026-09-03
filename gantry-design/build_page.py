#!/usr/bin/env python3
"""Builds gantry-design.html: a one-page summary of the design with the four drawings inlined
and the governing checks pulled live from calcs/gantry_calcs.py. Run: python3 build_page.py"""
import contextlib, io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "calcs"))
with contextlib.redirect_stdout(io.StringIO()):
    import gantry_calcs as gc  # runs all checks on import

def svg(name):
    s = open(os.path.join(HERE, "drawings", name)).read()
    return re.sub(r'\swidth="\d+"\sheight="\d+"', "", s, count=1)  # let CSS size it

GROUP_LABEL = {"beam": "Spine beam", "column": "Columns", "dynamics": "Sway frequency", "base plate": "Base plates",
               "anchors": "Anchors", "footing": "Pad footings", "beam-column": "Beam-to-column", "splice": "Splices",
               "hanger": "Hanger lugs and gear", "fatigue": "Fatigue (all details)"}
worst = {}
for grp, desc, d, c, u, r, note in gc.CHECKS:
    if grp not in worst or r > worst[grp][2]: worst[grp] = (desc, f"{d:.3g} / {c:.3g} {u}".strip(), r)
order = ["footing", "dynamics", "fatigue", "base plate", "hanger", "anchors", "column", "beam-column", "beam", "splice"]
rows = "\n".join(
    f'<li><div class="chk-head"><span class="chk-grp">{GROUP_LABEL[g]}</span><span class="chk-val">{worst[g][2]:.2f}</span></div>'
    f'<div class="bar"><span style="width:{min(worst[g][2],1)*100:.0f}%"></span></div>'
    f'<div class="chk-desc">{worst[g][0]} <span class="chk-num">{worst[g][1]}</span></div></li>'
    for g in order)
n_checks = len(gc.CHECKS); max_util = max(c[5] for c in gc.CHECKS)

page = f"""<title>15 m Bag Gantry</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=Source+Sans+3:ital,wght@0,400;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root{{
  --paper:#F6F7F5; --paper-2:#ECEEEA; --ink:#1B2430; --ink-2:#4B5563; --rule:#C8CED3; --rule-2:#DFE3E6;
  --steel:#2F5D8A; --steel-2:#DCE7F2; --orange:#C9561F; --orange-2:#F7E3D8;
  --display:"Barlow Condensed","Arial Narrow","Helvetica Neue",Arial,sans-serif;
  --body:"Source Sans 3","Source Sans Pro","Segoe UI",Helvetica,Arial,sans-serif;
  --mono:"IBM Plex Mono","SFMono-Regular",Menlo,Consolas,monospace;
}}
@media (prefers-color-scheme: dark){{ :root:not([data-theme="light"]){{
  --paper:#15191E; --paper-2:#1E242B; --ink:#E7EBEF; --ink-2:#A6B0BA; --rule:#3A434D; --rule-2:#2A323A;
  --steel:#7FB0E0; --steel-2:#22364B; --orange:#F08A50; --orange-2:#3E2418; }} }}
:root[data-theme="dark"]{{
  --paper:#15191E; --paper-2:#1E242B; --ink:#E7EBEF; --ink-2:#A6B0BA; --rule:#3A434D; --rule-2:#2A323A;
  --steel:#7FB0E0; --steel-2:#22364B; --orange:#F08A50; --orange-2:#3E2418; }}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--paper);color:var(--ink);font-family:var(--body);font-size:17px;line-height:1.5;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:1180px;margin:0 auto;padding:32px 24px 64px}}
h1,h2,h3{{font-family:var(--display);font-weight:600;line-height:1.05;margin:0;text-wrap:balance;letter-spacing:.005em}}
h1{{font-size:clamp(40px,6vw,64px);text-transform:uppercase}}
h2{{font-size:30px;text-transform:uppercase;letter-spacing:.02em;margin-bottom:14px}}
h3{{font-size:21px;margin-bottom:6px}}
p{{margin:0 0 12px;max-width:68ch}}
.eyebrow{{font-family:var(--mono);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-2)}}
.tb{{border:1.5px solid var(--ink);display:grid;grid-template-columns:1fr auto;gap:0;margin-bottom:36px}}
.tb-main{{padding:22px 26px 20px;border-right:1.5px solid var(--ink)}}
.tb-side{{display:grid;grid-template-rows:auto auto auto;min-width:260px}}
.tb-side > div{{padding:12px 18px;border-bottom:1px solid var(--rule)}}
.tb-side > div:last-child{{border-bottom:0}}
.tb-side .lab{{font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-2);display:block;margin-bottom:2px}}
.tb-side .val{{font-family:var(--display);font-size:22px;font-weight:600;line-height:1.1}}
.lede{{font-size:19px;max-width:70ch;margin-top:12px}}
.status{{display:inline-block;margin-top:10px;padding:5px 10px;border:1.5px solid var(--orange);color:var(--orange);font-family:var(--mono);font-size:12px;letter-spacing:.1em;text-transform:uppercase;background:var(--orange-2)}}
section{{margin:0 0 44px}}
.spec{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:0 36px;border-top:1.5px solid var(--ink)}}
.spec div{{display:grid;grid-template-columns:150px 1fr;gap:12px;padding:10px 0;border-bottom:1px solid var(--rule-2);align-items:baseline}}
.spec dt{{font-family:var(--mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-2);margin:0}}
.spec dd{{margin:0;font-size:16px}}
.spec dd b{{font-weight:600}}
.checks{{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:14px 36px}}
.checks li{{padding:8px 0 6px;border-bottom:1px solid var(--rule-2)}}
.chk-head{{display:flex;justify-content:space-between;align-items:baseline;gap:12px}}
.chk-grp{{font-family:var(--display);font-size:20px;font-weight:600}}
.chk-val{{font-family:var(--mono);font-size:16px;font-variant-numeric:tabular-nums}}
.bar{{height:7px;background:var(--paper-2);border:1px solid var(--rule);margin:6px 0 6px;position:relative}}
.bar span{{display:block;height:100%;background:var(--steel)}}
.chk-desc{{font-size:14px;color:var(--ink-2);line-height:1.35}}
.chk-num{{font-family:var(--mono);font-size:12.5px;white-space:nowrap}}
.checks-note{{font-size:15px;color:var(--ink-2);margin-top:14px;max-width:80ch}}
figure{{margin:0 0 28px;border:1px solid var(--rule);background:var(--paper);overflow:hidden}}
figure .fig-head{{display:flex;justify-content:space-between;align-items:baseline;padding:10px 16px;border-bottom:1px solid var(--rule);background:var(--paper-2);gap:12px;flex-wrap:wrap}}
figure .fig-no{{font-family:var(--display);font-size:20px;font-weight:600}}
figure .fig-title{{font-family:var(--mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2)}}
figure .fig-body{{overflow-x:auto;padding:8px}}
figure svg{{display:block;width:100%;min-width:900px;height:auto;color:var(--ink)}}
.loads{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px 28px}}
.loads h3{{font-family:var(--display);text-transform:uppercase;letter-spacing:.02em;font-size:18px;color:var(--steel)}}
.loads p{{font-size:15.5px;margin-bottom:6px}}
.num{{font-family:var(--mono);font-size:14px;white-space:nowrap}}
ol.confirm{{padding-left:22px;max-width:80ch;margin:0}}
ol.confirm li{{margin-bottom:8px;padding-left:4px}}
.files{{font-family:var(--mono);font-size:13.5px;line-height:1.8;color:var(--ink-2)}}
.files b{{color:var(--ink);font-weight:500}}
a{{color:var(--steel)}}
@media (max-width:760px){{ .tb{{grid-template-columns:1fr}} .tb-main{{border-right:0;border-bottom:1.5px solid var(--ink)}} .tb-side{{grid-template-rows:none;grid-template-columns:1fr 1fr 1fr}} .tb-side > div{{border-bottom:0;border-right:1px solid var(--rule)}} .spec div{{grid-template-columns:120px 1fr}} }}
@media (prefers-reduced-motion:no-preference){{ .bar span{{transition:width .6s ease}} }}
</style>

<div class="wrap">
<header class="tb">
  <div class="tb-main">
    <span class="eyebrow">Structural design package · Rev P1</span>
    <h1>15 m Bag Gantry</h1>
    <p class="lede">A freestanding galvanised steel frame for seven boxing and Muay Thai bags struck from any direction: four fixed-base SHS columns, a continuous SHS spine beam, welded hanger lugs with rated shackles and swivels, moment base plates on cast-in anchors, and reinforced concrete pad footings. Designed for a 50-year life to the Australian Standards suite.</p>
    <span class="status">Preliminary · certification by a chartered structural engineer required before construction</span>
  </div>
  <div class="tb-side">
    <div><span class="lab">Frame</span><span class="val">15.0 m · 7 hangers · 3.0 m soffit</span></div>
    <div><span class="lab">Rated load</span><span class="val">100 kg per hanger</span></div>
    <div><span class="lab">Checks</span><span class="val">{n_checks} pass · max {max_util:.2f}</span></div>
  </div>
</header>

<section>
  <h2>Design summary</h2>
  <dl class="spec">
    <div><dt>Spine beam</dt><dd><b>250 × 250 × 9.0 SHS</b> AS 1163 C350L0, continuous over four columns; three 5.0 m lengths, flange-plate splices at 5.0 and 10.0 m</dd></div>
    <div><dt>Columns</dt><dd><b>4 × 250 × 250 × 12.5 SHS</b> C350L0 at 0 / 4.5 / 10.5 / 15.0 m; fabricated length 2 892 mm; fixed base</dd></div>
    <div><dt>Hangers</dt><dd><b>7 at 2.0 m centres</b>: 200 × 300 × 16 plate + 20 mm lug, shop welded; 3.25 t bolt-type bow shackle and 2 t bearing swivel each</dd></div>
    <div><dt>Base plates</dt><dd><b>550 × 550 × 32</b> Grade 350, 10 mm fillet weld all round, on 40 mm non-shrink grout (≥ 50 MPa)</dd></div>
    <div><dt>Anchors</dt><dd><b>4 × M24 Grade 8.8</b> cast-in per column, 450 mm embedment, 100 × 100 × 16 anchor plate, 450 × 450 gauge</dd></div>
    <div><dt>Footings</dt><dd><b>4 × 1 800 × 1 800 × 600</b> pads, concrete <b>N32</b> (f′c = 32 MPa), N16 @ 200 each way top and bottom, hairpins at anchors, N12 dowels into the slab</dd></div>
    <div><dt>Connections</dt><dd>Beam-to-column: 420 × 420 cap and shoe plates, 4 × M20 8.8/TB. Splices: 420 × 420 × 20 flange plates, 8 × M20 8.8/TB</dd></div>
    <div><dt>Protection</dt><dd>Hot-dip galvanised to AS/NZS 4680, all steel and bolts; 25 mm closed-cell column padding to 2.0 m</dd></div>
    <div><dt>Quantities</dt><dd>≈ 2.8 t steel · 7.8 m³ N32 concrete · ≈ 420 kg reinforcement</dd></div>
    <div><dt>Dynamics</dt><dd>Frame sway 9.8 Hz on rigid bases, 7.7 Hz with base and soil flexibility; beam bays 15.7 Hz. Bags swing at 0.5-1 Hz; punches up to ~5 Hz</dd></div>
    <div><dt>Bag heights</dt><dd>Beam soffit 3.0 m: a 1.8 m Muay Thai bag hangs with its base 0.3 m off the floor on a 0.7 m shackle, swivel and chain set; boxing bags on 0.6-0.9 m sets. Roof clearance 3.6 m minimum</dd></div>
    <div><dt>Standards</dt><dd>AS/NZS 1170.0 actions, AS 4100 steel, AS/NZS 1554.1 welding, AS 3600 concrete, AS 5216 anchors (mirrors EN 1992-4), AS/NZS 4680 galvanising</dd></div>
  </dl>
</section>

<section>
  <h2>Governing checks</h2>
  <ul class="checks">
{rows}
  </ul>
  <p class="checks-note">Utilisation is demand divided by design capacity and must stay at or below 1.00. The frame is governed by footing stability and stiffness, not by steel strength: every member and connection sits below 0.25. Full table of {n_checks} checks in <span class="num">calcs/RESULTS.md</span>.</p>
</section>

<section>
  <h2>Load basis</h2>
  <div class="loads">
    <div><h3>Bag actions per hanger</h3>
      <p>Rated bag <span class="num">100 kg (W = 0.98 kN)</span>. Vertical dynamic <span class="num">3.92 kN = 4 W</span>, an envelope for snatch loads when a bag is lifted and dropped or jumped on; a hard kick alone gives about 1.2 W. Horizontal <span class="num">2.0 kN</span> in any direction from impulse transfer and swing.</p></div>
    <div><h3>Simultaneity</h3>
      <p>All seven hangers loaded with the vertical and horizontal actions in the same direction at once. Conservative for the frame and footings, and what keeps a freestanding frame from ever rocking.</p></div>
    <div><h3>Temperature</h3>
      <p><span class="num">±20 K</span> from erection temperature. The beam forces the columns to follow its expansion: end columns pick up <span class="num">3.9 kN (12.0 kN·m)</span> at the base. Included in strength design, excluded from stability because it relaxes on rotation.</p></div>
    <div><h3>Fatigue</h3>
      <p><span class="num">1.0 kN</span> vertical and horizontal ranges per strike, <span class="num">2 × 10⁸</span> cycles per hanger over 50 years. Every welded and bolted detail is below the constant-amplitude fatigue limit with φ = 0.7, so life is not cycle-limited.</p></div>
    <div><h3>Combinations</h3>
      <p>AS/NZS 1170.0: 1.2 G + 1.5 Q for strength; 0.9 G + 1.0 W<sub>static</sub> + 1.5 Q<sub>h</sub> for anchor tension; 0.9 G stabilising against 1.5 Q<sub>h</sub> for pad overturning.</p></div>
    <div><h3>Frequency targets</h3>
      <p>Frame sway ≥ 8 Hz on rigid bases and ≥ 6 Hz with base-plate rotation and pad rocking on soft soil (G = 15 MPa), so a 4.5 Hz punch cadence amplifies by no more than 1.5.</p></div>
  </div>
</section>

<section>
  <h2>Drawings</h2>
  <figure><div class="fig-head"><span class="fig-no">GA-01</span><span class="fig-title">General arrangement — elevation, plan, section A-A</span></div><div class="fig-body">{svg("GA-01-general-arrangement.svg")}</div></figure>
  <figure><div class="fig-head"><span class="fig-no">DET-01</span><span class="fig-title">Column base plate, anchors and pad footing</span></div><div class="fig-body">{svg("DET-01-base-plate-and-footing.svg")}</div></figure>
  <figure><div class="fig-head"><span class="fig-no">DET-02</span><span class="fig-title">Hanger lug and bag hardware</span></div><div class="fig-body">{svg("DET-02-hanger-lug.svg")}</div></figure>
  <figure><div class="fig-head"><span class="fig-no">DET-03</span><span class="fig-title">Beam-to-column connection and beam splice</span></div><div class="fig-body">{svg("DET-03-connections.svg")}</div></figure>
</section>

<section>
  <h2>What the certifying engineer must confirm</h2>
  <ol class="confirm">
    <li>Bag mass stays at or below 100 kg per hanger and nothing else (rings, ropes, pull-up bars) is hung from the frame without added lugs and a local re-check.</li>
    <li>Interior, unconditioned building; ±20 K temperature range; site seismicity low enough that the bag loads govern.</li>
    <li>Ground under the pads: allowable bearing ≥ 100 kPa and shear modulus ≥ 15 MPa, by inspection or test pit. Softer ground needs larger pads or a ground beam.</li>
    <li>Existing slab thickness, grade, services and any post-tensioning at the four pad locations before saw-cutting.</li>
    <li>Shop drawings, weld procedures and the galvaniser's vent-hole layout. The dynamic load model is a first-principles envelope, not a measurement; the frame has margin either way and the footings keep a 1.4 margin on the factored overturning check.</li>
  </ol>
</section>

<section>
  <h2>Package files</h2>
  <div class="files">
    <b>DESIGN-REPORT.md</b> — basis, loads, analysis, members, connections, base plates, anchors, footings, fatigue, fabrication, erection, inspection, assumptions<br>
    <b>calcs/gantry_calcs.py</b> — pure-Python calculation script, {n_checks} checks; <b>calcs/RESULTS.md</b> — generated check table and log<br>
    <b>drawings/*.svg</b> — the four sheets above, generated by <b>drawings/make_drawings.py</b><br>
    <b>build_page.py</b> — builds this page from the calculations and drawings
  </div>
</section>
</div>
"""
out = os.path.join(HERE, "gantry-design.html")
with open(out, "w") as f: f.write(page)
print("wrote", out, f"({len(page)/1024:.0f} kB)")
