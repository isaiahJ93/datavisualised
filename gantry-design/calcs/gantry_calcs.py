#!/usr/bin/env python3
"""
Boxing / Muay Thai bag gantry -- structural design calculations.

Freestanding 15 m hot-dip galvanised steel gantry, 4 fixed-base SHS columns,
continuous SHS spine beam, 7 welded hanger lugs, moment base plates on cast-in
anchors into reinforced concrete pad footings.

Design basis: AS/NZS 1170.0 (actions & combinations), AS 4100:2020 (steel),
AS/NZS 1554.1 (welding), AS 3600:2018 (concrete), AS 5216:2021 (anchors,
mirrors EN 1992-4), AS/NZS 4680 (galvanising). Units: kN, m for the global
model; N, mm, MPa for section/connection checks.

Pure Python (no third-party packages). Run:  python3 gantry_calcs.py
Writes RESULTS.md next to this file.
"""
from __future__ import annotations
import math, os, sys
from dataclasses import dataclass, field

OUT = []
def P(s=""):
    print(s); OUT.append(s)

CHECKS = []   # (group, description, demand, capacity, unit, ratio)
def check(group, desc, demand, capacity, unit="", note=""):
    ratio = demand / capacity if capacity else float("inf")
    CHECKS.append((group, desc, demand, capacity, unit, ratio, note))
    flag = "OK" if ratio <= 1.0 else "FAIL"
    P(f"  [{flag}] {desc}: {demand:.3g} / {capacity:.3g} {unit}  -> {ratio:.2f}" + (f"   ({note})" if note else ""))
    return ratio

# =============================================================================
# 1. DESIGN INPUTS
# =============================================================================
g = 9.81
E_STEEL = 200_000.0       # MPa  (AS 4100 200 GPa)
RHO_STEEL = 7850.0        # kg/m3
RHO_CONC = 2400.0         # kg/m3 (24 kN/m3)

# --- geometry (m) ---
L_FRAME = 15.0
X_COLS = [0.0, 4.5, 10.5, 15.0]                 # column centrelines
X_HANG = [1.5, 3.5, 5.5, 7.5, 9.5, 11.5, 13.5]  # hanger lugs (2.0 m centres)
X_SPLICE = [5.0, 10.0]                          # bolted flange-plate splices
BEAM_SOFFIT = 3.000       # underside of beam above finished floor level (FFL)
GROUT_T = 0.040           # non-shrink grout bed
BASEPL_T = 0.032          # base plate thickness
CAP_T = 0.020             # column cap plate
SHOE_T = 0.016            # beam shoe plate (welded under beam at each column)

# --- sections: AS 1163 C350L0 cold-formed SHS ---
FY_SHS = 350.0            # MPa
FU_SHS = 430.0
BEAM = dict(name="250x250x9.0 SHS", b=250.0, t=9.0)
COL  = dict(name="250x250x12.5 SHS", b=250.0, t=12.5)

# --- plates AS/NZS 3678 Grade 350 ---
def fy_plate(t):  # MPa by thickness (Grade 350)
    if t <= 12: return 360.0
    if t <= 20: return 350.0
    return 340.0
FU_PLATE = 450.0

# --- bolts AS/NZS 1252 Grade 8.8, HDG ---
FUF = 830.0
BOLT_AS = {12: 84.3, 16: 157.0, 20: 245.0, 24: 353.0}   # tensile stress area mm2
BOLT_AC = {12: 76.2, 16: 144.0, 20: 225.0, 24: 324.0}   # minor-diameter area mm2

# --- concrete AS 3600 ---
FC = 32.0                 # MPa, N32 pad footings
FC_GROUT = 50.0           # MPa, non-shrink cementitious grout
PAD_B = 1.8               # m square pad
PAD_D = 0.6               # m deep
SLAB_T = 0.15             # nominal adjoining slab (not relied on)

# --- anchors: 4 x M24 8.8 cast-in, 100x100x16 anchor plate ---
ANCH_D = 24
ANCH_G = 0.450            # gauge (m), both directions
ANCH_HEF = 0.450          # effective embedment to top of anchor plate (m)
BASEPL_B = 0.550          # square base plate side (m)

# --- bag actions ---
M_BAG = 100.0             # kg, rated (posted) max bag mass per hanger
W_BAG = M_BAG * g / 1000  # kN  static
DAF_V = 4.0               # vertical dynamic amplification on W (swing/snatch/jump abuse envelope)
Q_V = DAF_V * W_BAG       # kN per hanger, characteristic vertical
Q_H = 2.0                 # kN per hanger, characteristic horizontal, any direction
G_HARDWARE = 0.15         # kN per hanger (shackle, swivel, chains, lug plate)
DT = 20.0                 # K  temperature change from erection temperature (indoor)
ALPHA = 12e-6

# --- fatigue ---
DF_V = 1.0 * W_BAG        # kN vertical range per hit (typical hard strike)
DF_H = 1.0                # kN horizontal range per hit
CYCLES_HANGER = 2.0e8     # cycles per hanger, 50 yr busy gym (7 bags x 3 h/day x 60 hits/min)
PHI_FAT = 0.7             # AS 4100 11.1.5 non-redundant load path / uncertain history

# --- load factors AS/NZS 1170.0 ---
GAM_G, GAM_G_MIN, GAM_Q = 1.2, 0.9, 1.5

# =============================================================================
# 2. SECTION PROPERTIES  (SHS with rounded corners, r_o = 2.5t, r_i = 1.5t)
# =============================================================================
@dataclass
class SHS:
    name: str; b: float; t: float
    A: float = 0; I: float = 0; Zel: float = 0; Zpl: float = 0; r: float = 0
    J: float = 0; mass: float = 0; Aw: float = 0
    def __post_init__(self):
        b, t = self.b, self.t
        ro, ri = 2.5 * t, 1.5 * t
        bi = b - 2 * t
        Asp_o = (1 - math.pi / 4) * ro**2      # corner spandrel areas
        Asp_i = (1 - math.pi / 4) * ri**2
        c = 0.2234                                # spandrel centroid offset factor
        self.A = b * b - bi * bi - 4 * Asp_o + 4 * Asp_i
        I_rect = (b**4 - bi**4) / 12
        self.I = I_rect - 4 * Asp_o * (b / 2 - c * ro)**2 + 4 * Asp_i * (bi / 2 - c * ri)**2
        self.Zel = self.I / (b / 2)
        Zpl_rect = (b**3 - bi**3) / 4
        self.Zpl = Zpl_rect - 4 * Asp_o * (b / 2 - c * ro) + 4 * Asp_i * (bi / 2 - c * ri)
        self.r = math.sqrt(self.I / self.A)
        # Bredt torsion constant on mid-line
        rm = ro - t / 2; bm = b - t
        Am = bm * bm - (4 - math.pi) * rm**2
        pm = 4 * bm - (8 - 2 * math.pi) * rm
        self.J = 4 * Am**2 * t / pm
        self.mass = self.A * 1e-6 * RHO_STEEL
        self.Aw = 2 * (b - 2 * t) * t          # shear area (two webs) approx

beam = SHS(**BEAM); col = SHS(**COL)

P("=" * 78)
P("BOXING / MUAY THAI BAG GANTRY -- STRUCTURAL CALCULATIONS (AS/NZS suite)")
P("=" * 78)
P("\n## 1. Section properties (computed, cold-formed corners r_o=2.5t)")
for s in (beam, col):
    P(f"  {s.name}: A={s.A:.0f} mm2  I={s.I/1e4:.0f} cm4  Zel={s.Zel/1e3:.0f} cm3  "
      f"Zpl={s.Zpl/1e3:.0f} cm3  r={s.r:.1f} mm  J={s.J/1e4:.0f} cm4  mass={s.mass:.1f} kg/m")

# compactness (AS 4100 Table 5.2, flat width b-2t... use clear flat (b-2r_o)/t vs 30*eps? use 40 for plastic limit CF)
for s in (beam, col):
    lam_e = (s.b - 2 * 2.5 * s.t) / s.t * math.sqrt(FY_SHS / 250)
    P(f"  {s.name}: flange slenderness lam_e={lam_e:.1f} (plastic limit 30, yield limit 40 for CF SHS) -> "
      + ("COMPACT" if lam_e <= 30 else "NON-COMPACT"))

# =============================================================================
# 3. CONTINUOUS BEAM FE MODEL (Euler-Bernoulli, cubic elements, spring supports)
# =============================================================================
def solve_dense(K, F):
    n = len(F); A = [row[:] + [F[i]] for i, row in enumerate(K)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(A[r][c])); A[c], A[p] = A[p], A[c]
        piv = A[c][c]
        for r in range(c + 1, n):
            f = A[r][c] / piv
            if f:
                for k in range(c, n + 1): A[r][k] -= f * A[c][k]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        x[r] = (A[r][n] - sum(A[r][k] * x[k] for k in range(r + 1, n))) / A[r][r]
    return x

def beam_fe(EI, L, supports, point_loads, w=0.0, dx=0.25):
    """EI [N m2], L [m], supports {x: k_spring [N/m] or 'rigid'}, point_loads {x: P [N] (+ = load direction)},
    w [N/m] UDL in load direction. Returns dict with x, v (m), M (N m, sagging +), V (N), R (N) per support."""
    xs = sorted(set([round(i * dx, 6) for i in range(int(round(L / dx)) + 1)] + list(supports) + list(point_loads)))
    n = len(xs); ndof = 2 * n
    K = [[0.0] * ndof for _ in range(ndof)]; F = [0.0] * ndof
    els = []
    for e in range(n - 1):
        Le = xs[e + 1] - xs[e]; k = EI / Le**3
        ke = [[12, 6 * Le, -12, 6 * Le], [6 * Le, 4 * Le**2, -6 * Le, 2 * Le**2],
              [-12, -6 * Le, 12, -6 * Le], [6 * Le, 2 * Le**2, -6 * Le, 4 * Le**2]]
        dofs = [2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]
        for i in range(4):
            for j in range(4): K[dofs[i]][dofs[j]] += k * ke[i][j]
        feq = [-w * Le / 2, -w * Le**2 / 12, -w * Le / 2, w * Le**2 / 12]   # loads act in -v (load direction = -v)
        for i in range(4): F[dofs[i]] += feq[i]
        els.append((e, Le, dofs, feq, k, ke))
    for x, Pl in point_loads.items(): F[2 * xs.index(x)] += -Pl
    for x, ks in supports.items():
        K[2 * xs.index(x)][2 * xs.index(x)] += (1e14 if ks == "rigid" else ks)
    u = solve_dense(K, F)
    M = [0.0] * n; V = [0.0] * n; Mleft = [None] * n
    for (e, Le, dofs, feq, k, ke) in els:
        ue = [u[d] for d in dofs]
        fe = [sum(k * ke[i][j] * ue[j] for j in range(4)) - feq[i] for i in range(4)]
        # internal actions: sagging moment = -M1 at left end, +M2 at right end
        M[e] = -fe[1] if M[e] == 0 else M[e]; M[e + 1] = fe[3]
        V[e] = fe[0] if V[e] == 0 else V[e]; V[e + 1] = -fe[2]
    R = {}
    for x, ks in supports.items():
        i = xs.index(x); R[x] = -(1e14 if ks == "rigid" else ks) * u[2 * i]   # reaction in load direction
    return dict(x=xs, v=[-u[2 * i] for i in range(n)], M=M, V=V, R=R)

EI_beam = E_STEEL * 1e6 * beam.I * 1e-12     # N m2
L_col = BEAM_SOFFIT + beam.b / 2000 - (GROUT_T + BASEPL_T)   # base-plate top to beam centroid (m)
L_col_pad = L_col + GROUT_T + BASEPL_T + PAD_D                # to underside of pad
EI_col = E_STEEL * 1e6 * col.I * 1e-12
k_col = 3 * EI_col / L_col**3                                 # N/m  cantilever tip stiffness
col_len = BEAM_SOFFIT - SHOE_T - CAP_T - (GROUT_T + BASEPL_T)  # fabricated column length (m)

P(f"\n## 2. Geometry")
P(f"  Columns at x = {X_COLS} m; hangers at x = {X_HANG} m; splices at {X_SPLICE} m")
P(f"  Beam soffit {BEAM_SOFFIT:.3f} m above FFL; column cantilever length to beam centroid L_c = {L_col:.3f} m")
P(f"  Fabricated column length = {col_len*1000:.0f} mm; column tip stiffness k = {k_col/1e6:.2f} MN/m each")

# --- permanent actions on beam ---
w_beam = beam.mass * g               # N/m
G_plates_col = (2 * 0.4 * 0.4 * (CAP_T + SHOE_T) / 2 * RHO_STEEL + 4 * 0.5) * g / 1  # N per column (cap+shoe+bolts)  ~ crude
G_splice = (2 * 0.4 * 0.4 * 0.020 * RHO_STEEL + 8 * 0.4) * g                      # N per splice
G_hanger = G_HARDWARE * 1000                                                        # N per hanger

# --- VERTICAL: permanent G ---
supp_rigid = {x: "rigid" for x in X_COLS}
pl_G = {x: G_hanger for x in X_HANG}; pl_G.update({x: G_splice for x in X_SPLICE})
resG = beam_fe(EI_beam, L_FRAME, supp_rigid, pl_G, w=w_beam)
# --- VERTICAL: imposed Q_v all hangers ---
resQv = beam_fe(EI_beam, L_FRAME, supp_rigid, {x: Q_V * 1000 for x in X_HANG})
# --- VERTICAL: single hanger (fatigue range & hanger reaction pattern) ---
# --- TRANSVERSE: Q_h all hangers same direction, beam on column springs ---
supp_spring = {x: k_col for x in X_COLS}
resQh = beam_fe(EI_beam, L_FRAME, supp_spring, {x: Q_H * 1000 for x in X_HANG})
resQh_single = {xh: beam_fe(EI_beam, L_FRAME, supp_spring, {xh: 1000.0}) for xh in X_HANG}  # 1 kN at one hanger

def at(res, x): return res["M"][res["x"].index(x)]

P(f"\n## 3. Beam analysis (continuous over 4 columns)")
P(f"  Self weight w = {w_beam:.0f} N/m; hanger char. actions Q_v = {Q_V:.2f} kN, Q_h = {Q_H:.2f} kN")
Mg_max = max(resG["M"]); Mg_min = min(resG["M"])
Mq_max = max(resQv["M"]); Mq_min = min(resQv["M"])
P(f"  G:   M_sag = {Mg_max/1e3:.2f} kNm, M_hog = {Mg_min/1e3:.2f} kNm")
P(f"  Q_v: M_sag = {Mq_max/1e3:.2f} kNm, M_hog = {Mq_min/1e3:.2f} kNm")
Mz_max = max(abs(m) for m in resQh["M"])
P(f"  Q_h (transverse, all 7 same direction, beam on column springs): |M_z| max = {Mz_max/1e3:.2f} kNm")
P("  Column reactions (kN):")
Rv_G = {x: resG["R"][x] / 1e3 for x in X_COLS}
Rv_Q = {x: resQv["R"][x] / 1e3 for x in X_COLS}
Rh_Q = {x: resQh["R"][x] / 1e3 for x in X_COLS}
for x in X_COLS:
    P(f"    x={x:5.1f}: R_G={Rv_G[x]:.2f}  R_Qv={Rv_Q[x]:.2f}  R_Qh,transv={Rh_Q[x]:.2f}")
P(f"  Sum check: G {sum(Rv_G.values()):.2f} vs applied {(w_beam*L_FRAME+sum(pl_G.values()))/1e3:.2f}; "
  f"Qv {sum(Rv_Q.values()):.2f} vs {Q_V*7:.2f}; Qh {sum(Rh_Q.values()):.2f} vs {Q_H*7:.2f}")

# ULS envelope for beam
M_uls_sag = GAM_G * Mg_max + GAM_Q * Mq_max
M_uls_hog = GAM_G * Mg_min + GAM_Q * Mq_min
M_uls_z = GAM_Q * Mz_max
V_uls = max(abs(GAM_G * a + GAM_Q * b) for a, b in zip(resG["V"], resQv["V"]))
M_splice_y = max(abs(GAM_G * at(resG, xs) + GAM_Q * at(resQv, xs)) for xs in X_SPLICE)
M_splice_z = max(abs(GAM_Q * at(resQh, xs)) for xs in X_SPLICE)
# torsion: H at pin lever below beam centroid
LEVER_PIN = beam.b / 2000 + 0.016 + 0.060       # centroid -> plate -> pin (m)
T_uls_beam = GAM_Q * Q_H * LEVER_PIN * 3         # up to 3 hangers' torsion accumulating to one column (6 m bay share)
P(f"  ULS beam: M_y sag={M_uls_sag/1e3:.1f} kNm, hog={M_uls_hog/1e3:.1f} kNm, M_z={M_uls_z/1e3:.1f} kNm, "
  f"V={V_uls/1e3:.1f} kN, T={T_uls_beam:.2f} kNm; at splices M_y={M_splice_y/1e3:.1f}, M_z={M_splice_z/1e3:.1f} kNm")

# =============================================================================
# 4. BEAM MEMBER CHECKS (AS 4100)
# =============================================================================
P(f"\n## 4. Beam checks -- {beam.name} C350L0")
phi = 0.9
Ms = FY_SHS * beam.Zpl * 1e-6                     # kNm (compact, Ze = Zpl <= 1.5 Zel)
Ms = min(Ms, FY_SHS * 1.5 * beam.Zel * 1e-6)
Vv = 0.6 * FY_SHS * beam.Aw * 1e-3                # kN
Mt_cap = 0.6 * FY_SHS * 2 * ((beam.b - beam.t)**2 - (4 - math.pi) * (2.5 * beam.t - beam.t / 2)**2) * beam.t * 1e-6  # Bredt: T = 2 Am t tau
check("beam", "Biaxial bending (M_y/phiM_s)^1.4+(M_z/phiM_s)^1.4 (AS4100 8.3.4)",
      (max(M_uls_sag, -M_uls_hog) / 1e3 / (phi * Ms))**1.4 + (M_uls_z / 1e3 / (phi * Ms))**1.4, 1.0, "",
      f"phiM_s={phi*Ms:.0f} kNm")
check("beam", "Shear V*/phiV_v", V_uls / 1e3, phi * Vv, "kN")
check("beam", "Torsion T*/phiT (Bredt, tau=0.6fy)", T_uls_beam, phi * Mt_cap, "kNm")
# deflection SLS: G + Q_v (short-term psi_s = 0.7 not applied -- full Q_v used, conservative)
v_max = max(a + b for a, b in zip(resG["v"], resQv["v"]))
L_bay = 6.0
check("beam", "Vertical deflection G+Q_v vs span/250 (6 m bay)", v_max * 1000, L_bay * 1000 / 250, "mm")
vz_max = max(abs(v) for v in resQh["v"])
check("beam", "Lateral deflection beam (all Q_h, on column springs) vs 15 mm", vz_max * 1000, 15.0, "mm")
# frequency: 6 m bay, simply supported lower bound, mass incl. 3 bags + hardware
m_lin = beam.mass + (3 * M_BAG + 3 * G_HARDWARE * 1000 / g) / L_bay
f_beam_v = (math.pi / 2) / L_bay**2 * math.sqrt(EI_beam / m_lin)
P(f"  Beam 6 m bay natural frequency (SS lower bound, bags lumped): f_v = f_lat = {f_beam_v:.1f} Hz (>= 8 Hz target)")
check("beam", "Beam bay frequency target 8 Hz / f", 8.0, f_beam_v, "Hz")

# =============================================================================
# 5. COLUMN ACTIONS: transverse, longitudinal, thermal, combinations
# =============================================================================
P(f"\n## 5. Column actions -- {col.name} C350L0, fixed base cantilevers, L_c = {L_col:.2f} m")
# longitudinal: 7 x Q_h shared equally by 4 equal columns (beam axially rigid)
Rh_long = 7 * Q_H / 4
# thermal: free expansion about stiffness centre (x=7.5), columns restrain
xc = sum(X_COLS) / 4
F_T = {x: k_col * ALPHA * DT * abs(x - xc) / 1e3 for x in X_COLS}       # kN per column (char)
N_beam_T = F_T[0.0] + F_T[4.5]                                          # kN axial in beam
P(f"  Longitudinal Q_h reaction per column (7 x {Q_H} kN / 4) = {Rh_long:.2f} kN")
P(f"  Thermal dT={DT:.0f} K: end-column restraint force {F_T[0.0]:.2f} kN (M = {F_T[0.0]*L_col:.1f} kNm), "
  f"mid {F_T[4.5]:.2f} kN; beam axial {N_beam_T:.1f} kN")

G_col_self = col.mass * col_len * g / 1e3 + 0.35   # kN column + cap/base plates
combos = []
for x in X_COLS:
    Ng = Rv_G[x] + G_col_self; Nq = Rv_Q[x]
    Mt = Rh_Q[x] * L_col; Ml = Rh_long * L_col; MT = F_T[x] * L_col
    Vt = Rh_Q[x]; Vl = Rh_long
    cases = {
        "U2 transverse": dict(N=GAM_G * Ng + GAM_Q * Nq, My=GAM_Q * Mt, Mz=0.0, V=GAM_Q * Vt),
        "U3 longitudinal+T": dict(N=GAM_G * Ng + GAM_Q * Nq, My=0.0, Mz=GAM_Q * Ml + MT, V=GAM_Q * Vl + F_T[x]),
        "U4 biaxial 45deg+T": dict(N=GAM_G * Ng + GAM_Q * Nq, My=GAM_Q * Mt * 0.7071, Mz=GAM_Q * Ml * 0.7071 + MT,
                                   V=math.hypot(GAM_Q * Vt * 0.7071, GAM_Q * Vl * 0.7071 + F_T[x])),
        "U5 min axial (anchors)": dict(N=GAM_G_MIN * Ng + 1.0 * (Nq / DAF_V), My=GAM_Q * Mt, Mz=0.0, V=GAM_Q * Vt),
        "U5b min axial long.": dict(N=GAM_G_MIN * Ng + 1.0 * (Nq / DAF_V), My=0.0, Mz=GAM_Q * Ml + MT, V=GAM_Q * Vl + F_T[x]),
    }
    for name, c in cases.items():
        c["M"] = math.hypot(c["My"], c["Mz"]); c["x"] = x; c["case"] = name; combos.append(c)
    P(f"  Column x={x:4.1f}: N_G={Ng:.1f} N_Q={Nq:.1f} | M_transv={Mt:.1f} M_long={Ml:.1f} M_therm={MT:.1f} kNm (char)")

worst = max(combos, key=lambda c: c["M"])
worstN = max(combos, key=lambda c: c["N"])
P(f"  Governing ULS: {worst['case']} at x={worst['x']}: N*={worst['N']:.1f} kN, M*_res={worst['M']:.1f} kNm "
  f"(My={worst['My']:.1f}, Mz={worst['Mz']:.1f}), V*={worst['V']:.1f} kN")

# --- column section & member capacity (AS 4100) ---
Ms_c = min(FY_SHS * col.Zpl, FY_SHS * 1.5 * col.Zel) * 1e-6
Ns_c = FY_SHS * col.A * 1e-3
# member compression: effective length 2.2 L (fixed-free) both axes
Le = 2.2 * L_col * 1000
lam_n = Le / col.r * math.sqrt(FY_SHS / 250)
alpha_b = -0.5  # cold-formed SHS stress relieved? use alpha_b = -0.5 for CF non-stress-relieved per AS4100 T6.3.3(1)... conservative use 0
alpha_b = 0.0
# AS 4100 6.3.3 alpha_c
aa = 2100 * (lam_n - 13.5) / (lam_n**2 - 15.3 * lam_n + 2050)
lam = lam_n + aa * alpha_b
eta = 0.00326 * (lam - 13.5); eta = max(eta, 0)
xi = ((lam / 90)**2 + 1 + eta) / (2 * (lam / 90)**2)
alpha_c = xi * (1 - math.sqrt(1 - (90 / (xi * lam))**2))
Nc_c = alpha_c * Ns_c
P(f"  Column: phiN_s={phi*Ns_c:.0f} kN, lam_n={lam_n:.0f}, alpha_c={alpha_c:.2f}, phiN_c={phi*Nc_c:.0f} kN, phiM_s={phi*Ms_c:.1f} kNm")
Mrx = Ms_c * (1 - worst["N"] / (phi * Ns_c))   # reduced section moment (conservative linear)
check("column", "Section: N*/phiN_s + M*_res/phiM_s (linear, conservative)",
      worst["N"] / (phi * Ns_c) + worst["M"] / (phi * Ms_c), 1.0)
check("column", "Member in-plane: N*/phiN_c + M*/phiM_s (cantilever, k=2.2)",
      worst["N"] / (phi * Nc_c) + worst["M"] / (phi * Ms_c), 1.0)
check("column", "Shear V*/phiV_v", worst["V"], phi * 0.6 * FY_SHS * col.Aw * 1e-3, "kN")
# SLS sway at beam level under characteristic transverse Q_h (all bags)
sway = max(Rh_Q.values()) * 1e3 / k_col * 1000
check("column", "Head sway under char. Q_h (all 7 same dir.) vs H/300", sway, L_col * 1000 / 300, "mm")

# =============================================================================
# 6. FRAME SWAY FREQUENCY (transverse = longitudinal, 4 columns in parallel)
# =============================================================================
P(f"\n## 6. Frame sway frequency")
m_beam_total = beam.mass * L_FRAME
m_plates = 8 * 0.42**2 * 0.018 * RHO_STEEL + 4 * 0.42**2 * 0.02 * RHO_STEEL
m_bags = 7 * (M_BAG + G_HARDWARE * 1000 / g)
m_cols_eff = 4 * 0.24 * col.mass * col_len
m_sway = m_beam_total + m_plates + m_bags + m_cols_eff
k_sway_rigid = 4 * k_col
f_rigid = math.sqrt(k_sway_rigid / m_sway) / (2 * math.pi)
# base connection rotational stiffness: two anchors on tension side, stretch length ~ 12d + plate + grout
Lb = 12 * ANCH_D / 1000 + BASEPL_T + GROUT_T
k_anchor = E_STEEL * 1e6 * BOLT_AS[ANCH_D] * 1e-6 / Lb            # N/m
k_theta_base = 2 * k_anchor * (ANCH_G / 2 + BASEPL_B / 2 * 0.8)**2  # N m/rad, lever to compression edge
# footing rocking on soil: G_soil conservative 15 MPa, nu 0.3, square pad equivalent radius
G_soil = 15e6; nu = 0.3
r_eq = (PAD_B**4 / (3 * math.pi))**0.25
k_theta_soil = 8 * G_soil * r_eq**3 / (3 * (1 - nu))
k_col_flex = 1 / (1 / k_col + L_col**2 / k_theta_base + L_col**2 / k_theta_soil)
f_flex = math.sqrt(4 * k_col_flex / m_sway) / (2 * math.pi)
f_nobags = math.sqrt(k_sway_rigid / (m_sway - m_bags)) / (2 * math.pi)
P(f"  Participating mass = {m_sway:.0f} kg (beam {m_beam_total:.0f}, bags+hardware {m_bags:.0f}, plates {m_plates:.0f}, columns {m_cols_eff:.0f})")
P(f"  Rigid bases: f = {f_rigid:.1f} Hz (bags excluded: {f_nobags:.1f} Hz)")
P(f"  Base connection k_theta = {k_theta_base/1e6:.0f} MNm/rad; pad-on-soil (G={G_soil/1e6:.0f} MPa) k_theta = {k_theta_soil/1e6:.0f} MNm/rad")
P(f"  With base-plate + soil flexibility: f = {f_flex:.1f} Hz")
check("dynamics", "Sway frequency target 8 Hz / f (rigid base)", 8.0, f_rigid, "Hz")
check("dynamics", "Sway frequency target 6 Hz / f (flexible base, soft soil)", 6.0, f_flex, "Hz")
# resonance amplification at 4.5 Hz punch cadence
r = 4.5 / f_flex; damp = 0.02
DAF_res = 1 / math.sqrt((1 - r**2)**2 + (2 * damp * r)**2)
P(f"  Dynamic amplification of a 4.5 Hz punch cadence at f={f_flex:.1f} Hz, 2% damping: {DAF_res:.2f}")

# =============================================================================
# 7. BASE PLATE (moment base, large eccentricity)  -- AS 4100 / AISC DG1 method
# =============================================================================
P(f"\n## 7. Base plate {BASEPL_B*1000:.0f}x{BASEPL_B*1000:.0f}x{BASEPL_T*1000:.0f} Gr350, 4 x M{ANCH_D} at {ANCH_G*1000:.0f} gauge")
Bp = BASEPL_B * 1000; f_dist = ANCH_G * 1000 / 2; a_col = col.b
m_cant = f_dist - a_col / 2                        # bolt line to column face (mm)
# bearing stress limit AS 3600 12.6: phi 0.9 f'c sqrt(A2/A1) <= phi 1.8 f'c, phi=0.6 ; capped by grout
fp_max = min(0.6 * 1.8 * FC, 0.6 * 0.9 * FC_GROUT)
def base_plate(N, M, V):
    """N compression (kN, +), M (kNm), V (kN). Returns dict."""
    N_, M_ = N * 1e3, M * 1e6
    e = M_ / N_ if N_ > 0 else 1e9
    if e <= Bp / 6:   # no uplift: elastic bearing
        fp = N_ / Bp**2 + 6 * M_ / Bp**3
        return dict(mode="no-uplift", fp=fp, T=0.0, Y=Bp, C=N_ / 1e3)
    # bearing block at edge, tension in far anchors, moments about anchor line
    A_ = Bp / 2 + f_dist; q = fp_max * Bp
    disc = A_**2 - 2 * (M_ + N_ * f_dist) / q
    Y = A_ - math.sqrt(disc) if disc > 0 else None
    C = q * Y; T = C - N_
    return dict(mode="uplift", fp=fp_max, T=T / 1e3, Y=Y, C=C / 1e3)

bp_results = {}
for c in combos:
    if "min" in c["case"] or c["case"].startswith("U2") or c["case"].startswith("U3") or c["case"].startswith("U4"):
        rr = base_plate(c["N"], c["M"], c["V"]); rr.update(case=c["case"], x=c["x"], N=c["N"], M=c["M"], V=c["V"])
        bp_results[(c["x"], c["case"])] = rr
worst_bp = max(bp_results.values(), key=lambda r: r["T"])
P(f"  Governing for anchors: {worst_bp['case']} x={worst_bp['x']}: N*={worst_bp['N']:.1f} kN M*={worst_bp['M']:.1f} kNm -> "
  f"bearing block Y={worst_bp['Y']:.0f} mm at {worst_bp['fp']:.1f} MPa, C={worst_bp['C']:.0f} kN, "
  f"anchor pair tension T={worst_bp['T']:.1f} kN ({worst_bp['T']/2:.1f} kN/bolt)")
T_bolt = worst_bp["T"] / 2
# plate bending -- tension side: cantilever m from column face, effective width 2m per corner bolt (45 deg spread, conservative)
b_eff = 2 * m_cant
fyp = fy_plate(BASEPL_T * 1000); tp = BASEPL_T * 1000
M_pl_cap = phi * fyp * tp**2 / 4 * b_eff          # N mm
check("base plate", "Plate bending, tension side (T_bolt x m vs phi fy t^2/4 b_eff)", T_bolt * 1e3 * m_cant, M_pl_cap, "Nmm",
      f"t_req={math.sqrt(4*T_bolt*1e3*m_cant/(phi*fyp*b_eff)):.1f} mm")
# compression side: bearing block Y at fp over cantilever m (Y < m -> block near edge)
Y = worst_bp["Y"]; fp = worst_bp["fp"]
m_edge = Bp / 2 - a_col / 2                       # plate edge to column face (mm)
Mc = fp * Bp * min(Y, m_edge) * (m_edge - min(Y, m_edge) / 2)   # N mm about the column face
check("base plate", "Plate bending, compression side", Mc, phi * fyp * tp**2 / 4 * Bp, "Nmm")
# prying: thick plate -> negligible; require t >= sqrt(4 T m / (phi fy b_eff)) x 1.25 for prying-free
# shear transfer: friction on compression block (mu=0.4) + anchors in bearing as backup
V_star = max(c["V"] for c in combos)
check("base plate", "Base shear via friction 0.4 C (grout/steel)", V_star, 0.4 * worst_bp["C"], "kN",
      "anchors in shear as backup")
# column-to-base weld: 10 mm fillet all round (SP, E48XX). Line properties of square perimeter
a_w = col.b; Lw = 4 * a_w - (8 - 2 * math.pi) * 2.5 * col.t
Zw = 4 * a_w**2 / 3                                          # mm2 per unit throat (square perimeter line)
tw = 10.0; vw = 0.8 * 0.6 * 490 * 0.707 * tw                 # N/mm  (phi=0.8 SP, fuw 490)
f_w = math.hypot(worst["M"] * 1e6 / Zw + worst["N"] * 1e3 / Lw, worst["V"] * 1e3 / Lw)
check("base plate", f"Column-base fillet weld {tw:.0f} mm, resultant force per mm", f_w, vw, "N/mm")

# =============================================================================
# 8. ANCHORS (AS 5216 / EN 1992-4) -- cast-in M24 8.8, 100x100x16 plate
# =============================================================================
P(f"\n## 8. Anchors: 4 x M{ANCH_D} 8.8 cast-in, h_ef = {ANCH_HEF*1000:.0f} mm, pad {PAD_B} x {PAD_B} x {PAD_D} m N{FC:.0f}")
hef = ANCH_HEF * 1000; s_anch = ANCH_G * 1000
c_edge = (PAD_B * 1000 - s_anch) / 2
N_Rk_s = BOLT_AS[ANCH_D] * 800 / 1e3                         # kN (fuk 800 for 8.8)
N_Rd_s = N_Rk_s / 1.5                                          # gamma_Ms = 1.2 fuk/fyk >= 1.4 -> 1.5
check("anchors", "Steel tension per anchor N*/N_Rd,s", T_bolt, N_Rd_s, "kN")
k1 = 8.9                                                       # cracked concrete, headed
N0_Rk_c = k1 * math.sqrt(FC) * hef**1.5 / 1e3                 # kN
scr = 3 * hef; ccr = 1.5 * hef
A0 = scr**2
# tension group = 2 anchors along one edge line: extent along s: s + scr (s < scr); across: scr limited by edges
Ac = (min(s_anch, scr) + scr) * scr
psi_s = min(1.0, 0.7 + 0.3 * c_edge / ccr)
psi_re = 1.0 if hef >= 100 else 0.5 + hef / 200
N_Rk_c = N0_Rk_c * Ac / A0 * psi_s * psi_re
N_Rd_c = N_Rk_c / 1.5
check("anchors", "Concrete cone, 2-anchor tension group N*/N_Rd,c", worst_bp["T"], N_Rd_c, "kN",
      f"N0={N0_Rk_c:.0f} kN, Ac/A0={Ac/A0:.2f}, psi_s={psi_s:.2f}, c={c_edge:.0f} mm vs c_cr={ccr:.0f}")
A_h = 100 * 100 - math.pi * (ANCH_D / 2)**2
N_Rk_p = 7.5 * A_h * FC / 1e3
check("anchors", "Pull-out (head bearing) N*/N_Rd,p", T_bolt, N_Rk_p / 1.5, "kN")
# shear: concrete pry-out and steel (backup path only)
V_Rk_s = 0.5 * BOLT_AS[ANCH_D] * 800 / 1e3 ; V_Rd_s = V_Rk_s / 1.25
check("anchors", "Anchor steel shear, friction ignored, V*/4 per anchor / V_Rd,s", V_star / 4, V_Rd_s, "kN")
V_Rk_cp = 2.0 * N_Rk_c * 2 / 1.0   # k8=2 for hef>=60, on full 4-anchor group approx (2x the 2-anchor cone)
check("anchors", "Concrete pry-out of anchor group V*/V_Rd,cp", V_star, V_Rk_cp / 1.5, "kN")

# detailing sanity: pad depth vs embedment + plate + cover; edge distance vs c_cr
check("anchors", "Embedment fits: h_ef + anchor plate + bottom cover (mm) / pad depth", hef + 16 + 75, PAD_D * 1000, "mm")
P(f"  Edge distance c = {c_edge:.0f} mm >= c_cr,N = {ccr:.0f} mm -> full cone develops, psi_s = {psi_s:.2f}")
# fatigue of anchor (bolt in tension, category 50) - stress range with prying-free thick plate and pretension share 0.25
dM_base = (2 * DF_H) * L_col   # two adjacent bags striking together toward one column (kNm range)
dT_pair = dM_base * 1e3 / ((ANCH_G / 2 + BASEPL_B / 2 * 0.8) * 1e3) * 1e3 / 1e3   # kN
dsig_anchor = 0.25 * (dT_pair / 2) * 1e3 / BOLT_AS[ANCH_D]
f3_50 = 0.737 * 50
check("fatigue", "Anchor bolt stress range (cat 50, pretensioned) vs phi f3", dsig_anchor, PHI_FAT * f3_50, "MPa")

# =============================================================================
# 9. PAD FOOTING (AS 3600 / AS/NZS 1170.0 stability)
# =============================================================================
P(f"\n## 9. Pad footing {PAD_B} x {PAD_B} x {PAD_D} m, N{FC:.0f}, N16@200 EW T&B")
W_pad = PAD_B**2 * PAD_D * RHO_CONC * g / 1e3
for x in X_COLS:
    Ng = Rv_G[x] + G_col_self
    # transverse: destabilising 1.5 x Q_h reaction at pad base level; stabilising 0.9 (pad + steel G)
    M_dst_t = GAM_Q * Rh_Q[x] * L_col_pad
    M_dst_l = GAM_Q * Rh_long * L_col_pad          # thermal excluded: strain-controlled, relaxes on rotation
    M_stb = GAM_G_MIN * (W_pad + Ng) * PAD_B / 2
    check("footing", f"Overturning x={x}: transverse E_dst/E_stb", M_dst_t, M_stb, "kNm")
    check("footing", f"Overturning x={x}: longitudinal E_dst/E_stb", M_dst_l, M_stb, "kNm")
    # bearing (SLS char) with eccentricity
    Nsls = W_pad + Ng + Rv_Q[x] / DAF_V           # static bag weight only for bearing
    Msls = max(Rh_Q[x], Rh_long) * L_col_pad
    e = Msls / Nsls
    if e <= PAD_B / 6: qmax = Nsls / PAD_B**2 * (1 + 6 * e / PAD_B)
    else: qmax = 2 * Nsls / (3 * PAD_B * (PAD_B / 2 - e))
    check("footing", f"Bearing x={x}: q_max (e={e:.2f} m) vs 100 kPa allowable (assumed, verify on site)", qmax, 100.0, "kPa")
# pad bending: ULS cantilever from column face under max bearing (conservative uniform q_uls over cantilever)
c_cant = (PAD_B - BASEPL_B) / 2
N_uls = max(c["N"] for c in combos) + 1.2 * W_pad; M_uls_pad = max(c["M"] for c in combos) + max(c["V"] for c in combos) * PAD_D
e = M_uls_pad / N_uls
q_uls = (2 * N_uls / (3 * PAD_B * (PAD_B / 2 - e)) if e > PAD_B / 6 else N_uls / PAD_B**2 * (1 + 6 * e / PAD_B))
M_pad = q_uls * c_cant**2 / 2 * PAD_B                          # kNm across full width
d_eff = PAD_D * 1000 - 75 - 16 - 8
Ast = 1005.0 * PAD_B                                           # N16@200 -> 1005 mm2/m
phiMu = 0.85 * Ast * 500 * (d_eff - Ast * 500 / (2 * 0.85 * FC * PAD_B * 1000)) * 1e-6
check("footing", "Pad bending M*/phiM_u (N16@200 bottom, both ways)", M_pad, phiMu, "kNm")
Ast_min = 0.20 * (PAD_D * 1000 / d_eff)**2 * 0.6 * math.sqrt(FC) / 500 * 1000 * d_eff
check("footing", "Minimum flexural reinforcement A_st,min (AS3600 8.1.6.1, alpha_b=0.20) / N16@200 provided", Ast_min, 1005.0, "mm2/m")
# one-way shear at d from column face (no shear reinf.)
V_pad = q_uls * (c_cant - d_eff / 1000) * PAD_B
phiVuc = 0.7 * 0.15 * math.sqrt(FC) * PAD_B * 1000 * d_eff * 1e-3   # simplified kv floor (AS3600 8.2.4.3 kv=0.15 conservative)
check("footing", "One-way shear V*/phiV_uc (kv=0.15)", max(V_pad, 0), phiVuc, "kN")

# =============================================================================
# 10. CONNECTIONS
# =============================================================================
P(f"\n## 10. Connections (bolts Gr 8.8 HDG, phi=0.8; welds SP E48XX phi=0.8)")
def phiVf(d): return 0.8 * 0.62 * FUF * BOLT_AC[d] / 1e3     # kN threads in shear plane
def phiNtf(d): return 0.8 * FUF * BOLT_AS[d] / 1e3           # kN
# 10a beam-to-column: shoe plate 420x420x16 on cap plate 420x420x20, 4 x M20 8.8/TB at 340 gauge
Rv_max = max(GAM_G * Rv_G[x] + GAM_Q * Rv_Q[x] for x in X_COLS)
Hcol_max = max(max(GAM_Q * Rh_Q[x], GAM_Q * Rh_long + F_T[x]) for x in X_COLS)
Tcol = GAM_Q * Q_H * LEVER_PIN * 3
M_nom = 10.0                                                    # kNm nominal joint moment for robustness
n_b = 4; g_b = 340.0                                           # bolt gauge; plates 420x420
Vb = math.hypot(Hcol_max / n_b, Tcol * 1e3 / (4 * (g_b / 2 * math.sqrt(2))))       # kN per bolt shear
Tb = M_nom * 1e3 / (2 * g_b) if M_nom > 0 else 0                                  # kN per bolt (2 bolts/side)
check("beam-column", "M20 bolt combined (V/phiVf)^2+(N/phiNtf)^2", (Vb / phiVf(20))**2 + (Tb / phiNtf(20))**2, 1.0, "",
      f"V={Vb:.1f} kN, N={Tb:.1f} kN per bolt")
m_shoe = (g_b - col.b) / 2
check("beam-column", "Shoe/cap plate bending (16 mm) T x m vs phi fy t^2/4 b_eff", Tb * 1e3 * m_shoe,
      phi * fy_plate(16) * 16**2 / 4 * (2 * m_shoe + 60), "Nmm")
check("beam-column", "Cap plate weld 8 mm fillet (perimeter) under M_nom+V", math.hypot(M_nom * 1e6 / Zw, Rv_max * 1e3 / Lw),
      0.8 * 0.6 * 490 * 0.707 * 8, "N/mm")
check("beam-column", "Beam web bearing at column R*/phiR_by (AS4100 5.13.3)", Rv_max,
      phi * 1.25 * (col.b + 2 * 2.5 * beam.t) * beam.t * FY_SHS * 2 / 1e3, "kN")
# 10b splice: flange plates 420x420x20, 8 x M20 8.8/TB (corners + mid-sides at 340 gauge)
M_sp = math.hypot(M_splice_y, M_splice_z) / 1e3 + 0            # kNm resultant
V_sp = max(abs(GAM_G * resG["V"][resG["x"].index(xs)] + GAM_Q * resQv["V"][resQv["x"].index(xs)]) for xs in X_SPLICE) / 1e3
Tb_sp = M_sp * 1e3 / (3 * g_b * 0.9) + N_beam_T / 8            # 3 bolts on tension side, lever ~0.9 g
Vb_sp = math.hypot(V_sp / 8, Tcol * 1e3 / (8 * g_b / 2 * 1.2))
check("splice", "M20 bolt combined (V/phiVf)^2+(N/phiNtf)^2", (Vb_sp / phiVf(20))**2 + (Tb_sp / phiNtf(20))**2, 1.0, "",
      f"M*={M_sp:.1f} kNm, V*={V_sp:.1f} kN -> N={Tb_sp:.1f} kN/bolt")
m_sp = (g_b - beam.b) / 2
check("splice", "Flange plate bending (20 mm) T x m vs phi fy t^2/4 b_eff", Tb_sp * 1e3 * m_sp,
      phi * fy_plate(20) * 20**2 / 4 * (2 * m_sp + 60), "Nmm")
check("splice", "Beam-to-flange-plate 8 mm fillet under M*+V*", math.hypot(M_sp * 1e6 / Zw, V_sp * 1e3 / Lw),
      0.8 * 0.6 * 490 * 0.707 * 8, "N/mm")
# 10c hanger lug: 20 mm lug, 100 wide, hole 22, pin 60 mm below plate; plate 200x300x16 welded 8 mm all round
F_v = GAM_Q * Q_V + 1.2 * G_HARDWARE; F_h = GAM_Q * Q_H
lug_t, lug_w, hole, e_pin = 20.0, 100.0, 22.0, 60.0
fy_l = fy_plate(lug_t)
check("hanger", "Lug net tension F_v/(phi fy (w-hole) t)", F_v * 1e3, phi * fy_l * (lug_w - hole) * lug_t, "N")
check("hanger", "Lug out-of-plane bending F_h e / (phi fy w t^2/4)", F_h * 1e3 * e_pin, phi * fy_l * lug_w * lug_t**2 / 4, "Nmm")
check("hanger", "Lug in-plane bending F_h e / (phi fy t w^2/6)", F_h * 1e3 * e_pin, phi * fy_l * lug_t * lug_w**2 / 6, "Nmm")
check("hanger", "Pin bearing on lug, 19 mm shackle pin, vs phi 1.5 f_u (conservative ply bearing)", F_v * 1e3 / (19 * lug_t), 0.9 * 1.5 * FU_PLATE, "MPa")
check("hanger", "Lug shear tear-out beyond hole (2 planes)", F_v * 1e3, phi * 0.6 * fy_l * 2 * (60 - hole / 2) * lug_t, "N")
Lw_lug = 2 * lug_w
check("hanger", "Lug-to-plate 8 mm fillet both sides (F_v + F_h + couple from F_h e)", math.hypot(F_v * 1e3 / Lw_lug, F_h * 1e3 * e_pin / (lug_w * (lug_t + 8)) + F_h * 1e3 / Lw_lug),
      0.8 * 0.6 * 490 * 0.707 * 8, "N/mm")
Lw_pl = 2 * 300 + 2 * 200
check("hanger", "Hanger plate-to-beam 8 mm fillet all round (F_v + F_h lever)", F_v * 1e3 / Lw_pl + F_h * 1e3 * (e_pin + 16) / (200 * 300),
      0.8 * 0.6 * 490 * 0.707 * 8, "N/mm")
# local bending of beam bottom wall between webs: plate 200 wide vs 232 clear -> lever <= 16 mm
check("hanger", "Beam bottom wall local bending (lever 16 mm, b_eff 300)", F_v * 1e3 * 16, phi * FY_SHS * beam.t**2 / 4 * 300, "Nmm")
# rated hardware
SHACKLE_WLL = 3.25 * g; SWIVEL_WLL = 2.0 * g   # kN (3.25 t bow shackle bolt-type; 2 t bearing swivel)
F_res = math.hypot(F_v, F_h)
check("hanger", "Shackle 3.25 t bolt-type: ULS resultant / WLL (rated gear, min 6:1 to MBL)", F_res, SHACKLE_WLL, "kN")
check("hanger", "Swivel 2 t bearing type: ULS resultant / WLL", F_res, SWIVEL_WLL, "kN")

# =============================================================================
# 11. FATIGUE (AS 4100 Section 11, infinite-life check vs phi f3 (5e6 CAFL))
# =============================================================================
P(f"\n## 11. Fatigue -- {CYCLES_HANGER:.0e} cycles per hanger; infinite-life check, phi = {PHI_FAT}")
def f3(cat): return 0.737 * cat
# beam bottom face at hanger plate (longitudinal attachment L>100: cat 50): global stress range from 1 bag hit
dM_beam = max(abs(m) for m in beam_fe(EI_beam, L_FRAME, supp_rigid, {7.5: DF_V * 1000})["M"])
check("fatigue", "Beam wall at hanger plate weld toe (cat 50) global range", dM_beam / beam.Zel, PHI_FAT * f3(50), "MPa")
# hanger plate weld throat, load-carrying fillet (cat 36 on throat)
check("fatigue", "Hanger plate fillet throat, load range (cat 36)", DF_V * 1e3 / (Lw_pl * 0.707 * 8), PHI_FAT * f3(36), "MPa")
# lug at hole: pin-loaded plate, cat 50 with Kt implicit? use net section x Kt 2.5 vs cat 90 plain material
check("fatigue", "Lug net section x Kt 2.5 at pin hole (cat 71 taken)", 2.5 * DF_V * 1e3 / ((lug_w - hole) * lug_t), PHI_FAT * f3(71), "MPa")
# column base weld toe: cat 36 (tube-to-plate fillet, t>8)
dsig_base = dM_base * 1e6 / col.Zel
check("fatigue", "Column base tube wall at weld toe (cat 36), 2-bag range", dsig_base, PHI_FAT * f3(36), "MPa")
# cap plate weld similar with joint moment range small
# splice bolts in tension (cat 50), pretensioned share 0.25
dM_sp = max(abs(at(beam_fe(EI_beam, L_FRAME, supp_rigid, {7.5: DF_V * 1000}), xs)) for xs in X_SPLICE)
check("fatigue", "Splice bolt tension range (cat 50, pretensioned 8.8/TB)", 0.25 * dM_sp / (3 * g_b * 0.9) / BOLT_AS[20], PHI_FAT * f3(50), "MPa")
# beam at splice end-plate weld (transverse fillet to plate, cat 36)
check("fatigue", "Beam-to-splice plate weld toe (cat 36)", dM_sp / beam.Zel, PHI_FAT * f3(36), "MPa")

# =============================================================================
# 12. BILL OF MATERIALS
# =============================================================================
P(f"\n## 12. Materials summary")
steel = {
    f"Beam {beam.name}, 3 x 5.0 m": beam.mass * L_FRAME,
    f"Columns {col.name}, 4 x {col_len*1000:.0f} mm": col.mass * col_len * 4,
    "Base plates 550x550x32": 4 * 0.55**2 * 0.032 * RHO_STEEL,
    "Cap plates 420x420x20 + shoe plates 420x420x16": 4 * 0.42**2 * (0.020 + 0.016) * RHO_STEEL,
    "Splice flange plates 420x420x20 (4)": 4 * 0.42**2 * 0.020 * RHO_STEEL,
    "Hanger plates 200x300x16 + lugs 100x160x20 (7)": 7 * (0.2 * 0.3 * 0.016 + 0.1 * 0.16 * 0.02) * RHO_STEEL,
    "Anchor rods M24 x 650 + plates (16)": 16 * (math.pi * 0.012**2 * 0.65 * RHO_STEEL + 0.1 * 0.1 * 0.016 * RHO_STEEL),
    "Bolts M20/M16 8.8 HDG, washers, nuts": 40.0,
}
for k, v in steel.items(): P(f"  {k}: {v:.0f} kg")
P(f"  TOTAL steel (before HDG ~+4%): {sum(steel.values()):.0f} kg")
P(f"  Concrete N{FC:.0f}: 4 pads x {PAD_B**2*PAD_D:.2f} m3 = {4*PAD_B**2*PAD_D:.1f} m3 (+ blinding); grout 4 x {BASEPL_B**2*GROUT_T*1000:.1f} L")
P(f"  Reinforcement D500N: approx {4*(2*2*9*1.7*1.58 + 4*1.2*1.58):.0f} kg")

# =============================================================================
# 13. SUMMARY TABLE
# =============================================================================
P("\n## 13. Check summary")
worst_ratio = max(c[5] for c in CHECKS)
P(f"  {len(CHECKS)} checks; maximum utilisation = {worst_ratio:.2f}; all OK = {all(c[5] <= 1 for c in CHECKS)}")

def write_results():
    here = os.path.dirname(os.path.abspath(__file__))
    lines = ["# Calculation results (generated by gantry_calcs.py)", "",
             "Run `python3 gantry_calcs.py` to regenerate. Utilisation = demand / capacity; must be <= 1.00.", "",
             "| Group | Check | Demand | Capacity | Unit | Util. | Note |", "|---|---|---:|---:|---|---:|---|"]
    for grp, desc, d, c, u, r, note in CHECKS:
        lines.append(f"| {grp} | {desc} | {d:.3g} | {c:.3g} | {u} | **{r:.2f}** | {note} |")
    lines += ["", "## Full log", "", "```"] + OUT + ["```", ""]
    with open(os.path.join(here, "RESULTS.md"), "w") as f: f.write("\n".join(lines))
    print(f"\nWrote {os.path.join(here, 'RESULTS.md')}")

if __name__ == "__main__":
    write_results()
    sys.exit(0 if worst_ratio <= 1 else 1)
