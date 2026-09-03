# Boxing / Muay Thai bag gantry — 15 m, 7 hangers

Preliminary structural design package for a freestanding, hot-dip galvanised steel gantry that carries six or seven heavy bags being struck from any direction, designed for a 50-year life.

| File | What it is |
|---|---|
| `DESIGN-REPORT.md` | The design report: basis, loads, analysis, member and connection design, base plates, anchors, footings, concrete spec, fatigue, fabrication, erection, inspection, assumptions |
| `calcs/gantry_calcs.py` | Re-runnable calculation script (pure Python, no dependencies). 61 checks to AS/NZS 1170.0, AS 4100, AS 3600 and AS 5216 |
| `calcs/RESULTS.md` | Generated check table with every demand, capacity and utilisation, plus the full calculation log |
| `drawings/GA-01-general-arrangement.svg` | Elevation, plan and cross-section |
| `drawings/DET-01-base-plate-and-footing.svg` | Base plate, anchors, pad footing and reinforcement |
| `drawings/DET-02-hanger-lug.svg` | Hanger lug, shackle, swivel and load rating |
| `drawings/DET-03-connections.svg` | Beam-to-column connection and beam splice |
| `drawings/make_drawings.py` | Generates the SVG drawings |
| `gantry-design.html` | One-page summary with the drawings inline (built by `build_page.py`) |

## The design in one paragraph

Four 250 × 250 × 12.5 SHS columns at 0 / 4.5 / 10.5 / 15.0 m carry a continuous 250 × 250 × 9.0 SHS beam with its underside 3.0 m above the floor. Seven welded hanger lugs at 2.0 m centres each carry a 100 kg bag through a bolt-type 3.25 t shackle and a 2 t bearing swivel. Each column has a 550 × 550 × 32 base plate on 40 mm grout, held by four cast-in M24 Grade 8.8 anchors 450 mm deep in an 1 800 × 1 800 × 600 N32 pad footing reinforced with N16 @ 200 each way top and bottom. Steel mass about 2.8 t, concrete 7.8 m³.

## Status

Rev P1, preliminary design. Complete enough to price and to detail, but it must be reviewed and certified by a chartered structural engineer against the actual site (soil, existing slab, seismicity, bag equipment) before anything is fabricated or poured. Section 15 of the report lists what the certifier needs to confirm.

## Re-run

```
python3 calcs/gantry_calcs.py
python3 drawings/make_drawings.py
python3 build_page.py
```
