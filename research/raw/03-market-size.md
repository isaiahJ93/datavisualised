# 03 — Market size & buyer economics: SaaS for civil construction subcontractors, Australia & New Zealand

**Analyst:** Hermes
**Date of memo:** 1 September 2026
**Scope:** ANZSIC Division E Construction — Subdivision 31 (Heavy & Civil Engineering Construction) and the civil-relevant classes of Subdivision 32 (Construction Services), in Australia and New Zealand.
**Currency:** All figures AUD unless marked NZD or USD.

---

## RESEARCH INTEGRITY NOTE — read before using any number

This session's network egress policy **blocked direct access to every primary statistical source**:
`abs.gov.au`, `stats.govt.nz`, `asic.gov.au`, `asbfeo.gov.au`, `ibisworld.com`, `bdo.com.au`,
`figure.nz`, `estimateone.com`, `totika.co.nz` all returned 403 at the CONNECT tunnel
(verified: `curl -sS https://www.abs.gov.au/robots.txt` → `CONNECT tunnel failed, response 403`).
The web-search budget was then exhausted at 200/200 calls.

Consequence: figures below marked **[SEARCH-SUMMARY]** come from search-engine summaries of those
pages, not from the primary PDF/XLSX. They are directionally reliable but **must be re-pulled from
source before any figure appears in a deck, a data room, or an investment memo.**

**The single most important gap: I could not retrieve the ABS CABEE data cube giving business counts
by ANZSIC subdivision × employment size band.** The ABS publishes it (Counts of Australian
Businesses, Data Cubes 2–11, industry × employment size). It is the decisive input to this model and
it is a 20-minute job for anyone with unblocked access. Every subdivision-level count below is
therefore an **[ESTIMATE]** built by triangulation, and I have shown the reasoning so you can attack it.

---

## VERDICT

**No-go as a venture-scale bet. Go as a capital-efficient owner-operated business — and only if you
price to the 5+ employee band and sell on headcount displacement, not on seats.**

The single biggest reason: **the entire ANZ civil-subcontractor market is worth roughly A$34m of
annual recurring revenue if you win 100% of it at credible prices, and roughly A$22m if you exclude
the segments that cannot pay.** A$10m ARR requires ~69% of every civil contractor in Australia and
New Zealand with five or more employees, in a market where Australian engineering construction work
done is **down 5.1% year-on-year** and the transport pipeline is forecast to more than halve by 2029.
There is a real A$2–4m ARR business here. There is not a A$100m one.

The second reason, which is worse than the first: **HammerTech — the incumbent site-compliance
platform on ANZ civil and commercial projects — is free for subcontractors.** The head contractor
pays. Your buyer has already been trained that compliance software is something someone else buys
for them. That is a price anchor of zero on the exact job-to-be-done.

---

## 1. COUNTING THE UNITS

### 1.1 Australia — the whole construction division (citable)

| Figure | Value | As at | Source |
|---|---|---|---|
| Construction businesses trading | **462,939** | 30 Jun 2025 | ABS, *Counts of Australian Businesses (CABEE)*, Jul 2021–Jun 2025, rel. 26 Aug 2025 [SEARCH-SUMMARY] |
| Share with <20 employees | **98.6%** | 30 Jun 2025 | ABS, *The nuts and bolts of the Australian Construction industry* [SEARCH-SUMMARY] |
| → implied ≥20 employees (my arithmetic) | **6,478** | 30 Jun 2025 | derived: 462,939 × 1.4% |
| New construction businesses (entries) | **76,414** — highest of any industry | FY2024-25 | ABS CABEE [SEARCH-SUMMARY] |
| All Australian businesses | 2,729,648 (+2.5%, +66,650) | 30 Jun 2025 | ABS CABEE [SEARCH-SUMMARY] |
| All Australian business entries / exits | 437,150 / **370,500** | FY2024-25 | ABS CABEE [SEARCH-SUMMARY] |

**Derived, and it matters more than anything else in this section:** the all-industry annual exit rate
is 370,500 / 2,729,648 = **13.6%**. Construction is the worst-performing sector for failure (§3.2).
**Your logo churn floor from customer mortality alone is 14%+ per year, before a single customer
dislikes your product.**

Sources: https://www.abs.gov.au/statistics/economy/business-indicators/counts-australian-businesses-including-entries-and-exits/latest-release ; https://www.abs.gov.au/articles/nuts-and-bolts-australian-construction-industry

### 1.2 Australia — subdivision splits

ABS publishes subdivision **income** but I could not retrieve subdivision **counts**:

| Subdivision | Total income FY2023-24 | Share |
|---|---|---|
| 30 Building Construction | $235.2b | 37.1% |
| **31 Heavy & Civil Engineering Construction** | **$122.4b** | **19.3%** |
| 32 Construction Services ("tradies") | $276.1b | 43.6% |
| **Division E total** | **$633.6b** | 100% |

Construction = 7.0% of GDP, ~1.3m employed, FY2023-24.
Source: ABS, *The nuts and bolts of the Australian Construction industry* [SEARCH-SUMMARY].

**IBISWorld cross-checks (2026 unless noted) [SEARCH-SUMMARY]:**
- Construction in Australia: **$641.1bn**, **431,000 businesses** — note IBISWorld counts 32k fewer
  businesses than ABS; use ABS. https://www.ibisworld.com/australia/industry/construction/306/
- Heavy Industry & Other Non-Building Construction: **$82.9bn**, **7,945 businesses** (7,997 in 2025,
  −0.4% y/y). https://www.ibisworld.com/australia/industry/heavy-industry-other-non-building-construction/314/
- Road & Bridge Construction: **$45.5bn (2025), −4.1% in 2025**, and **forecast to fall 18.0% over the
  two years through 2026-27** as the M6 Stage 1, Coffs Harbour Bypass, West Gate Tunnel and
  Rockhampton Ring Road complete. https://www.ibisworld.com/australia/industry/road-bridge-construction/313/

**[ESTIMATE] Subdivision 31 business count: 12,000–18,000, midpoint ~15,000.**
Reasoning: IBISWorld's "Heavy Industry & Other Non-Building" ($82.9bn, 7,945 firms) plus "Road &
Bridge" ($45.5bn) together sum to ~$128bn, closely bracketing ABS Sub-31 income of $122.4b — so the
two IBISWorld industries roughly span the subdivision. Road & Bridge is the more fragmented half at
the small end (council road maintenance, kerbing, line marking, drainage), so I assign it 4,000–10,000
firms. **Confidence: low. Re-pull ABS CABEE Data Cube 2.**

**[ESTIMATE] Civil-relevant Subdivision 32 classes: 15,000–40,000, midpoint ~25,000.**
This is where most small civil subcontractors actually sit: Class 3212 Site Preparation Services
(earthmoving, excavation), 3211 Land Development, 3292 Hire of Construction Machinery with Operator,
and the civil edge of 3291 Landscape Construction. **Not found in any accessible source.**

**→ Australia civil-relevant total: [ESTIMATE] ~40,000 businesses (range 27,000–58,000).**

### 1.3 New Zealand (citable)

| Figure | Value | As at | Source |
|---|---|---|---|
| Construction enterprises | **81,249** (13.2% of all NZ enterprises) | Feb 2025 | Stats NZ, *NZ Business Demography Statistics: At February 2025* [SEARCH-SUMMARY] |
| All NZ enterprises | 617,330 (+0.5% y/y) | Feb 2025 | as above |
| Construction employees | ~198,500 — **down 14,500 (−6.8%)** from the Feb 2024 peak of 213,000 | Feb 2025 | as above |
| Feb 2026 release | **not yet published — due October 2026** | — | Stats NZ |

Source: https://www.stats.govt.nz/information-releases/new-zealand-business-demography-statistics-at-february-2025/

**[ESTIMATE] NZ civil-relevant businesses: ~7,000 (range 5,000–10,000).**
Reasoning: NZ construction enterprise count is 17.5% of Australia's (81,249 / 462,939). Applying the
Australian civil share (40,000 / 462,939 = 8.6%) to the NZ base gives 6,988.

**→ ANZ civil-relevant total: [ESTIMATE] ~47,000 businesses.**

### 1.4 The size distribution — the decisive cut

I could not obtain the construction-specific size distribution. The all-industry Australian
distribution [SEARCH-SUMMARY, ASBFEO/ABS] is: **~64% non-employing, ~25% 1–4, ~9% 5–19, ~1.3% 20–199,
~0.06% 200+.** Construction skews **more** micro than this average — subcontracting *is* the industry's
operating model and construction is Australia's largest generator of non-employing sole traders
(76,414 entries in one year). **So the table below is generous to the founder.**

Applied to ~47,000 ANZ civil-relevant businesses:

| Employment band | ANZ civil firms [ESTIMATE] | Can they buy real SaaS? |
|---|---|---|
| Non-employing | **~30,000 (64%)** | **No.** Owner-operator, does paperwork in the ute at 9pm. Ceiling ~A$50/mo, and mostly A$0. |
| 1–4 | ~11,750 (25%) | Marginal. A$50–100/mo ceiling. Highest mortality band (§3.2). |
| **5–19** | **~4,230 (9%)** | **Yes — the real SMB target.** Has a bookkeeper or office admin. |
| **20–199** | **~610 (1.3%)** | **Yes — the best target.** Real budget line, real HSEQ role, still buys off-the-shelf. |
| 200+ | ~28 | Enterprise. You lose to Oracle / InEight / Assignar / Procore. |

**The serviceable buyer universe across all of Australia and New Zealand civil is ~4,868 firms
(5–19 plus 20–199 plus 200+). Call it 4,900. That is the number that governs this entire venture.**

**Independent triangulation — and it holds.** Civil Contractors Federation (Australia) has **~1,800
contractor and associate members employing 40,000+** (https://www.civilcontractors.com/about/, as at
Dec 2024 [SEARCH-SUMMARY]). Civil Contractors New Zealand represents **800+ businesses**
(https://civilcontractors.co.nz/about-ccnz/10898/ [SEARCH-SUMMARY]). Combined: **2,600 members.**
Firms with ≥5 employees are exactly the ones for whom peak-body membership and prequalification pay
for themselves — plausible penetration ~50% — implying **~5,200 firms of that size.** That lands
within 7% of my bottom-up 4,868. **Two independent methods, same answer. I have reasonable
confidence in ~5,000 real buyers.**

---

## 2. IS THE MARKET A TAILWIND OR A HEADWIND? — Headwind, clearly, in Australia

| Indicator | Reading | Source |
|---|---|---|
| Total construction work done, Jun qtr 2026 | **−2.1% q/q** to $82,515.9m (seas. adj.) | ABS, *Construction Work Done, Australia, Preliminary, June 2026* [SEARCH-SUMMARY] |
| **Engineering work done, Jun qtr 2026** | **−6.0% q/q and −5.1% year-on-year** | as above |
| Engineering work done, Mar qtr 2026 | $38,868.1m (+7.1% q/q). Private +15.9% to $22,928.1m; **public −3.5% to $15,940.0m** | ABS, *Engineering Construction Activity, Australia, March 2026* [SEARCH-SUMMARY] |
| Road & Bridge Construction AU | **−18.0% forecast over two years to 2026-27** | IBISWorld [SEARCH-SUMMARY] |
| ANZIP transport pipeline | Peaked Q1 2024 at **$11.4bn/quarter**; one more peak of $11.3bn, then **sustained decline to $5.2bn/quarter by end-2029** absent material new additions. Since 2022: 42 projects added vs 76 entering main works and 32 completed | Infrastructure Partnerships Australia, *The Pipeline Report*, Feb 2025 [SEARCH-SUMMARY] |
| NSW infrastructure budget | $86bn — **$470m lower nominal, $2.2bn lower in real terms** than prior year | IPA, *Australian Infrastructure Budget Monitor 2025-26* [SEARCH-SUMMARY] |

**Read the ANZIP number again: additions to the pipeline are running at roughly half the rate of
completions.** The 15-year Australian infrastructure boom is ending on a published schedule. A civil
SaaS launching in FY2027 is launching into a market that shrinks for three years.

**New Zealand is the better half, marginally.** The pipeline is **NZD 274bn**, of which **NZD 91.1bn
is entering or under construction, NZD 163.6bn is still in planning and NZD 12.5bn in procurement** —
i.e. **only 41% of initiatives are fully funded** (RLB/NZIER *Infrastructure Forecast Report 6*,
June 2026 [SEARCH-SUMMARY], https://www.rlb.com/wp-content/uploads/sites/1/2026/06/NZIER-Forecast-Infrastructure-Report-2026.pdf).
Civil construction cost inflation is forecast to peak ~5% late 2026, easing to ~1.6% late 2027.
But NZ construction employment has already fallen 6.8% from its Feb 2024 peak.

Sources: https://www.abs.gov.au/statistics/industry/building-and-construction/construction-work-done-australia-preliminary/latest-release ; https://infrastructure.org.au/tools-resources/articles/the-pipeline-report-february-2025-in-focus/

---

## 3. BUYER ECONOMICS

### 3.1 Net margins — thin, and thin margins cap price

| Figure | Value | Source |
|---|---|---|
| Average profit margin, all AU building & construction businesses | **~5%** | Master Builders Australia 2023 industry report, via The Access Group [SEARCH-SUMMARY, secondary] |
| General contractors, net | 2–4% | industry benchmark literature [SEARCH-SUMMARY, US-leaning — flag] |
| Specialty subcontractors, net | 5–10% | as above [US-leaning — flag] |
| Civil / excavation / concrete, A$1–5m revenue band, net | **~5.5%** | constructioncfo.net / civilcfo.com [SEARCH-SUMMARY, **US source — treat as indicative only**] |
| Construction leaders reporting margin increase in prior 12 months | 31%; 37% expected improvement | BDO Construction Survey 2025 [SEARCH-SUMMARY] |
| Respondents reporting financial loss from **subcontractor insolvency** in FY24 | **82%** | BDO Construction Survey 2024 [SEARCH-SUMMARY] |
| Small construction businesses **not** expecting a more profitable 2025/26 | **59%** | HIA 2026 Small Business Conditions Survey [SEARCH-SUMMARY] |

**Not found:** an ANZ-specific, statistically-sampled net margin series for *civil* subcontractors
specifically. The ATO Small Business Benchmarks (updated 2025, 100 industries, downloadable from
data.gov.au) contain exactly this for excavation/earthmoving and are the correct primary source.
`ato.gov.au` was not directly reachable this session. **Pull it.**

**What ~5% net does to willingness to pay.** A 20-person civil sub at a ~5% net margin has to sell
**A$20 of extra work to fund every A$1 of new annual software cost.** A A$12,000/yr subscription
requires A$240,000 of incremental revenue to be margin-neutral. This is why civil subs do not buy on
"efficiency" narratives — they buy on a line item they can point at and delete.

### 3.2 Insolvency — this is a churn finding, not colour

| Figure | Value | Source |
|---|---|---|
| All AU companies entering insolvency, FY2025-26 | **14,152** (down from 14,722 in FY2024-25) | ASIC insolvency statistics via Accountants Daily, https://www.accountantsdaily.com.au/business/22687-company-insolvencies-climb-to-14-152-for-fy-2025-26 [SEARCH-SUMMARY] |
| FY2024-25 | 14,722, **+33.2%** on FY2023-24 | ASIC [SEARCH-SUMMARY] |
| FY2023-24 | 11,053 (then a record) | ASIC [SEARCH-SUMMARY] |
| **Construction companies into external administration, FY2025-26** | **3,435** (3,472 incl. controller appointments), **−4.5%** — the **first annual fall in five years** | ASIC via The Good Builder [SEARCH-SUMMARY] |
| Construction share of all AU corporate failures | **~26–27%** — worst sector, every year | ASIC; Building 4.0 CRC #80 [SEARCH-SUMMARY] |
| Construction insolvency growth, three years to FY24 | **+118%** | Building 4.0 CRC Project #80, final report, Oct 2025 [SEARCH-SUMMARY] |
| **Size of failing construction firms, FY24** | **>75% had fewer than 19 FTEs; the vast majority had fewer than 5 FTEs** | Building 4.0 CRC #80 [SEARCH-SUMMARY] |

Sources: https://building4pointzero.org/wp-content/uploads/2025/10/CRC80_Project-Report_Final-Version-for-publication.pdf ; https://eprints.qut.edu.au/260918/ ; https://www.asic.gov.au/about-asic/corporate-publications/statistics/insolvency-statistics

**The arithmetic you must not skip:**
- Formal construction insolvencies alone: 3,435 / 462,939 = **0.74%/yr.** That is companies only.
- But total Australian business *exits* run at **13.6%/yr** (370,500 / 2,729,648, ABS FY2024-25), and
  construction is the worst sector on every failure measure.
- **[ESTIMATE] Annual logo churn floor from customer death in the 1–4 employee civil band: 14–18%.**

**Conclusion: the segment with the most acute pain (micro subs) has a churn rate that makes positive
unit economics structurally impossible at any CAC above roughly one month's revenue.** If your
payback is 9 months and 16% of your customers cease to exist each year, you are running a treadmill.
This alone eliminates the 42,000 firms in the non-employing and 1–4 bands from any serious plan.

### 3.3 Administrative burden — real, quantified, and already absorbed into headcount

**HIA 2026 Small Business Conditions Survey** [SEARCH-SUMMARY]
(https://hia.com.au/our-industry/housing/in-focus/2026/04/small-builders-big-contribution):

| Finding | Value |
|---|---|
| Small builders spending **≥5 hours/week** on regulatory tasks | **>50%** |
| Spending **>10 hours/week** | **~33%** |
| Have **hired new staff or redeployed existing staff** to manage admin/regulatory tasks | **56%** |
| Have **considered scaling back or closing** because of red tape | **68%** |
| Do not expect to hire more staff in the year ahead | 73% |
| Said NCC 2025 changes had a moderate or major business impact | 63% |

**Productivity Commission, *Housing construction productivity: Can we fix it?*, released 16 Feb 2025**
(https://www.pc.gov.au/inquiries-and-research/housing-construction/) [SEARCH-SUMMARY]:
- **Physical productivity in housing construction has fallen 53% over 30 years.**
- Labour productivity down 12% over the same period, while whole-economy labour productivity rose 49%.
- Construction costs +40% in five years; build times up to +80% over 15 years.
- A subsequent PC report estimates regulation adds **up to $320,000 to a new house and $175,000 to a
  new apartment**, ~**$47.5bn/yr** nationally.
- Master Builders Australia is calling for a **$12bn red-tape reduction** in its 2026-27 budget submission.

**Dollarising the burden [ESTIMATE]:** 5 hrs/wk × 46 working weeks × A$80/hr loaded admin cost =
**A$18,400/yr**; at 10 hrs/wk, **A$36,800/yr**. So the theoretical value of halving it is
A$9,000–18,000/yr per firm. That looks like a great WTP story.

**It isn't, and here is why — the most important buyer-economics finding in this memo.**
**56% of these businesses have already hired or redeployed a person to absorb the burden.** The pain
has been converted into a **salary line, not a software line.** There is no "compliance software"
budget waiting to be captured; there is a part-time admin on A$45–70k. To win that money you must
credibly displace or prevent that hire. That is a slower, more consultative, more evidence-hungry
sale than a A$250/month product motion can support — but it is also the *only* place a five-figure
ACV can come from.

**Not found:** a credible study isolating hours or dollars spent specifically on *prequalification,
insurance certificate renewal, SWMS preparation and tender submission* for civil subcontractors in
ANZ. The HIA figure is all regulatory tasks and skews residential. This is a genuine white space and
a reason to run your own survey (§7).

### 3.4 What they already pay for software

All price points below are **published vendor or aggregator pricing, as at Sep 2026**:

| Vendor | Price | Note |
|---|---|---|
| **Xero (AU, from Jul 2026, AUD/mo incl GST)** | Ignite **$37**, Grow **$78**, Comprehensive **$107**, Ultimate 10 **$143**, Ultimate 20 **$180**, Ultimate 50 **$250**, Ultimate 100 **$300** | Payroll included but capped by tier; upgrades driven by headcount. https://www.xero.com/au/pricing-plans/ |
| **MYOB (AU, Jul 2026, GST-excl)** | SOLO ~**A$11**, Business Lite **A$35**, AccountRight Plus **A$165**, Premier **A$210** /mo; payroll +~A$3/employee/mo on lower tiers | [SEARCH-SUMMARY] |
| **SafetyCulture** | Premium **$24/seat/mo** annual ($29 monthly); free tier is widely used; Enterprise custom | Currency shown as $ on G2/Capterra, **likely USD — verify**. https://www.g2.com/products/safetyculturehq/pricing |
| **Assignar** | listed from **$99/user/mo** | Vendor does not publish; aggregator listing. ANZ-founded, explicitly targets self-performing contractors and subs. https://www.capterra.com/p/143935/Assignar/ |
| **HammerTech** | aggregator lists ~$89/user/mo, but vendor states pricing is by annual construction volume and active job sites — **and HammerTech is free for subcontractors** | https://www.hammertech.com/en-us/pricing |
| **Payapps (Autodesk)** | Tiered by contracts/claims per period: Pay-as-you-go → Basic → Plus → Standard → Premium → Ultimate. **Subcontractors get the first claim free every month on self-manage** | https://www.payapps.com/pricing-subcontractors/ |
| Construction estimating software, generally | $50–200/user/mo typical; $275–950/user/mo high end | [SEARCH-SUMMARY] |
| Fleet / telematics (EROAD, Teletrac, Verizon Connect) | **Not found** — no citable current ANZ price | — |
| Prequalification portals (Avetta, Cm3, Rapid Global, Sitepass, Totika NZ) | **Not found** — `estimateone.com` and `totika.co.nz` were egress-blocked | — |

**[ESTIMATE] Total annual software spend, 20-person ANZ civil sub:**

| Line | Annual |
|---|---|
| Xero Ultimate 20 (A$180/mo) | A$2,160 |
| SafetyCulture Premium, 8 seats @ ~A$36 | A$3,456 *(many run the free tier: A$0)* |
| Field/workforce management (Assignar-class), 5 seats @ ~A$150/mo | A$9,000 |
| Payapps or equivalent progress claims | A$3,000 |
| Civil estimating/takeoff, 2 seats @ ~A$150/mo | A$3,600 |
| HammerTech | **A$0 — head contractor pays** |
| **Subtotal, software only** | **~A$21,200** |
| Fleet/telematics, 15 assets @ ~A$45/mo *(unverified)* | A$8,100 |
| **Total incl. telematics** | **~A$29,300** |

**→ [ESTIMATE] A$20,000–30,000/yr, or roughly A$1,000–1,500 per employee per year.**

Two things follow. First, **only the accounting/payroll line is genuinely non-negotiable** — everything
else has a free or bundled substitute (SafetyCulture free tier, HammerTech free for subs, Payapps
first claim free, spreadsheets). Second, a new entrant asking A$3,000–12,000/yr is asking for
**10–40% of the entire existing software budget**. At that share you are not an addition. You are a
replacement, and you must name what you replace.

---

## 4. BOTTOM-UP TAM / SAM / SOM

**Price points used [ESTIMATE], and the reasoning:** the reference price these buyers have internalised
for "the software that runs my business" is Xero at A$107–180/month. A new tool that prices *above*
the accounting system triggers a conversation with the owner; one that prices below gets approved by
the office manager. Hence A$250/mo as the realistic 5–19 band ACV and A$1,250/mo for 20–199 where a
dedicated HSEQ or contracts role exists to champion it.

### TAM — every civil-relevant business in Australia and New Zealand

| Band | ANZ civil firms [EST] | Realistic ACV [EST] | Band value |
|---|---|---|---|
| Non-employing | 30,000 | **A$0** — will not buy | **A$0** |
| 1–4 | 11,750 | A$900/yr (A$75/mo) | A$10.6m |
| 5–19 | 4,230 | A$3,000/yr (A$250/mo) | A$12.7m |
| 20–199 | 610 | A$15,000/yr | A$9.2m |
| 200+ | 28 | A$60,000/yr | A$1.7m |
| **TAM** | **46,618** | | **A$34.1m/yr** |

`(11,750×900) + (4,230×3,000) + (610×15,000) + (28×60,000) = 10,575,000 + 12,690,000 + 9,150,000 + 1,680,000 = A$34,095,000`

**A$34m is the whole prize — 100% share of every civil contractor in two countries.**

### SAM — the segments that can actually transact

Remove non-employing (no budget), 1–4 (14–18% mortality churn, §3.2), and 200+ (enterprise
procurement you lose to Oracle/InEight/Assignar):

`(4,230 × A$3,000) + (610 × A$15,000) = A$12.69m + A$9.15m = **A$21.8m/yr**`

### SOM — 5 years, realistically

Well-run vertical SaaS reaching 10–15% of a defined SMB vertical in five years is a good outcome;
20%+ is top-decile — and top-decile is harder in a contracting market.

| Share of SAM | ARR | Customers |
|---|---|---|
| 10% | **A$2.2m** | ~487 |
| 15% | A$3.3m | ~730 |
| 20% (top-decile) | **A$4.4m** | ~974 |

*(Customer counts use the SAM blended ACV of A$4,486 = A$21.84m / 4,868 firms.)*

**SOM base case: A$2–4m ARR by year five.** [ESTIMATE]

---

## 5. SENSITIVITY — what it takes to hit A$1m and A$10m ARR

Denominator: **4,868 ANZ civil firms with ≥5 employees**; of which **610** are in the 20–199 band.

### To reach A$1m ARR

| Price | Customers needed | = % of the 4,868 ≥5-employee universe | Verdict |
|---|---|---|---|
| A$100/mo (A$1,200/yr) | **833** | 17.1% | Hard. Forces you into the 1–4 band. |
| A$250/mo (A$3,000/yr) | **333** | 6.8% | **Achievable.** |
| A$500/mo (A$6,000/yr) | **167** | 3.4% | **Comfortably achievable if the product earns it.** |
| A$1,250/mo (A$15,000/yr) | **67** | 11.0% *of the 610-firm 20–199 band* | **Achievable, and by far the cheapest to sell.** |

**A$1m ARR is real.** 67 mid-size civil subs at A$15k, or 333 small ones at A$3k. Both are reachable
with a named-account list — CCF and CCNZ membership rosters plus state prequalification registers
give you essentially the entire target universe by name.

### To reach A$10m ARR

| Price | Customers needed | = % of universe | Verdict |
|---|---|---|---|
| A$100/mo | 8,333 | **171%** of ≥5-employee firms | **Impossible.** |
| A$250/mo | 3,333 | **68.5%** of every civil firm ≥5 employees in AU **and** NZ | **Not credible.** |
| A$500/mo | 1,667 | **34.2%** | Top of what vertical SaaS ever achieves — **and it requires a growing market. The market is shrinking (§2).** |
| A$1,250/mo | 667 | **109%** of the 20–199 band | **Impossible.** |
| A$2,500/mo | 333 | **55%** of the 20–199 band, at 2× the estimated band ceiling | **Not credible.** |

**A$10m ARR is not reachable from ANZ civil subcontractors alone at any credible price × attach
combination.** To get there you must do at least one of:

1. **Widen to all of Subdivision 32** (43.6% of construction income, hundreds of thousands of firms) —
   but you then compete with Simpro, Tradify, ServiceM8, Fergus, AroFlo and Buildxact, and you lose
   the civil-specific positioning that was your only wedge.
2. **Go geographic** (UK, Canada, US) — but if the moat is ANZ regulation (SWMS, WHS Acts,
   Security of Payment, state prequalification schemes), that moat does not travel and you rebuild
   the product per jurisdiction.
3. **Move up to head contractors and asset owners** at A$50–250k — a different product, a different
   sale, and Procore, InEight, Oracle and Assignar own it.
4. **Take a cut of flow, not seats** — payments, retention/trust accounts, insurance placement,
   labour hire, plant hire. **This is the only route where A$10m comes from ~500 customers**, because
   revenue scales with their project value rather than their headcount. Payapps sits on exactly this
   flow. It is also the only route where the shrinking pipeline hurts you proportionally rather than
   catastrophically.

---

## 6. IS THIS A "GET RICH" OUTCOME? — No. It is a very good lifestyle business.

- Venture-scale exit (A$100m+) needs A$12–17m ARR at 6–8× revenue. **Section 5 shows that is
  arithmetically unavailable in ANZ civil.**
- The achievable outcome — **A$2–4m ARR at ~80% gross margin with a 3–6 person team** — throws off
  roughly **A$1.5–3m/yr** and would trade to Assignar, SafetyCulture, Autodesk/Payapps or a private
  buyer at maybe **A$8–20m**. [ESTIMATE]
- That is an excellent outcome for a founder who wants to own 100% of it. **It is a poor outcome for
  anyone who takes institutional venture money, because the fund needs the A$100m case and this
  market cannot produce it.** Raising a seed round against this TAM sets up a forced march into
  adjacent markets you did not want to enter.

**Be honest with yourself about which business you are building before you take the first cheque.**

---

## 7. KILL SHOTS — ranked by probability

1. **The market is A$22m of serviceable ARR and it is shrinking (~85% likely to bind).** Engineering
   work done is −5.1% y/y; road & bridge −18% over two years; the ANZIP transport pipeline halves by
   2029. You are building a fixed-cost software business into a three-year contraction in your only
   vertical. Every sales forecast in your model needs a shrinking-base assumption.

2. **Compliance software for subcontractors has been price-anchored at zero (~70%).** HammerTech is
   free for subs; SafetyCulture has a large free tier; Payapps gives subs a free claim monthly. In
   every case the *head contractor* or the *platform* pays and the sub consumes for free. Your buyer
   has been trained for a decade that this category costs them nothing. Overcoming that is a
   positioning problem, not a feature problem, and features will not solve it.

3. **The pain lives in a salary line, not a software line (~65%).** 56% of small construction
   businesses have already hired or redeployed someone to absorb the admin burden (HIA 2026). You are
   not capturing an unspent budget; you are asking an owner to bet that your software lets them not
   replace their office manager. That sale is 3–6 months long and needs proof you will not have on
   day one.

4. **Customer mortality caps your unit economics (~60%).** Construction is 26–27% of all Australian
   corporate insolvencies; >75% of failing construction firms have <19 FTEs and most have <5. Total
   business exits run at 13.6%/yr economy-wide and construction is the worst sector. Any plan that
   sells below 5 employees dies on churn regardless of product quality.

5. **Assignar is already here, ANZ-founded, and aimed at exactly this buyer (~45%).** It targets
   self-performing contractors and subcontractors in civil, prices from ~$99/user/month, and has years
   of head start. Whatever the gap is, you must be able to say in one sentence why Assignar has not
   closed it — and "they're focused upmarket" is a nine-month reprieve, not a moat.

---

## 8. CHEAPEST NEXT TEST — 30 days, under A$5,000

**The biggest unknown is not market size. It is whether a firm in the 20–199 band will pay a five-figure
annual price for a compliance/admin product when HammerTech is free.** Resolve that first; everything
else is downstream.

**Run three things in parallel:**

1. **Pull the two data cubes I could not reach (half a day, A$0).**
   (a) ABS *Counts of Australian Businesses* Data Cubes 2–11: Division E by **subdivision × employment
   size band**, June 2026 release. This replaces the largest [ESTIMATE] in this memo.
   (b) ATO *Small Business Benchmarks* (data.gov.au): net profit ratio for excavation/earthmoving and
   civil trades. This replaces the US-sourced margin proxies in §3.1.
   If the real Subdivision 31+civil-32 ≥5-employee count comes back materially **below 4,000**, stop.

2. **Twenty structured calls with civil subs in the 20–199 band (A$2,000 in incentives).**
   Source from the CCF state branch rosters and CCNZ member list — that is your named universe, and it
   is public. Two questions that matter, asked exactly this way:
   - *"Walk me through the last time you lost a job or a day because a prequal, SWMS or certificate of
     currency wasn't ready. What did it cost?"* — you need a dollar figure in their words, not a
     complaint.
   - *"Who does that work today, what do you pay them, and what would have to be true for you to not
     replace them when they leave?"* — this tests the headcount-displacement thesis directly.

3. **A price test before you build (A$1,000).**
   Put a one-page offer in front of 30 of those firms at **A$1,250/month** with an explicit
   "replaces X hours of admin" claim. Ask for a A$500 deposit against a pilot.

**Stop conditions — take these seriously:**
- **Fewer than 3 of 30 will put down a deposit at A$1,250/mo.** The five-figure ACV is not there, which
  means the 20–199 band cannot carry the business, which means A$1m ARR requires 333+ small customers
  in a shrinking market with 14%+ mortality churn. **Stop, or pivot to the transactional model (§5.4).**
- **More than half say "HammerTech/SafetyCulture already does that and it's free."** Your wedge is not
  differentiated. **Stop and re-scope.**
- **Nobody can name a dollar figure for the pain.** Acute pain with no quantified cost is a complaint,
  not a budget. **Stop.**

**Green light:** 5+ of 30 pay a deposit at A$1,250/mo *and* three or more independently describe the
alternative as "hiring another admin". That combination says the headcount-displacement sale is real,
and it puts A$1m ARR within reach of 67 customers you can name today.

---

## 9. WHAT TO RE-VERIFY BEFORE THIS MEMO LEAVES YOUR DESK

| # | Item | Why it matters | Where |
|---|---|---|---|
| 1 | **ABS CABEE business counts, Division E by subdivision × employment size, Jun 2026** | Replaces the single largest estimate in the model (~15,000 Sub-31 and ~25,000 civil Sub-32 firms) | abs.gov.au, Data Cubes 2–11 |
| 2 | **Construction-specific size distribution** | I used the all-industry split (64/25/9/1.3/0.06). Construction is more micro, so the real ≥5-employee universe is probably **smaller** than 4,868 | same cube |
| 3 | **Stats NZ business demography, Feb 2026** | Due **October 2026**; will tell you if NZ construction enterprise counts followed the −6.8% employment fall | stats.govt.nz |
| 4 | **ATO Small Business Benchmarks — excavation/earthmoving net profit ratio** | Replaces US-sourced margin proxies | data.gov.au |
| 5 | **Assignar, HammerTech, Payapps actual ANZ quotes** | All three are quote-based; aggregator prices are unreliable | request quotes as a 25-person civil sub |
| 6 | **Prequalification portal fees (Avetta, Cm3, Rapid Global, Sitepass, Totika NZ)** | This is the closest existing product to the likely wedge, and it is a proven paid line item for subs. **Not found — both target sites were egress-blocked** | vendor pricing pages |
| 7 | **ANZ fleet/telematics per-asset pricing** | Needed to complete the software-budget estimate | EROAD, Teletrac Navman |

---

## SOURCE LIST

**Business counts**
- ABS, *Counts of Australian Businesses, including Entries and Exits* — https://www.abs.gov.au/statistics/economy/business-indicators/counts-australian-businesses-including-entries-and-exits/latest-release (Jul 2021–Jun 2025 rel. 26 Aug 2025; Jul 2022–Jun 2026 now current)
- ABS, *The nuts and bolts of the Australian Construction industry* — https://www.abs.gov.au/articles/nuts-and-bolts-australian-construction-industry
- Stats NZ, *NZ Business Demography Statistics: At February 2025* — https://www.stats.govt.nz/information-releases/new-zealand-business-demography-statistics-at-february-2025/
- Civil Contractors Federation (AU) — https://www.civilcontractors.com/about/
- Civil Contractors New Zealand — https://civilcontractors.co.nz/about-ccnz/10898/

**Industry value & trend**
- ABS, *Construction Work Done, Australia, Preliminary, June 2026* — https://www.abs.gov.au/statistics/industry/building-and-construction/construction-work-done-australia-preliminary/latest-release
- ABS, *Engineering Construction Activity, Australia, March 2026* — https://www.abs.gov.au/statistics/industry/building-and-construction/engineering-construction-activity-australia/latest-release
- Infrastructure Partnerships Australia, *The Pipeline Report*, Feb 2025 — https://infrastructure.org.au/tools-resources/articles/the-pipeline-report-february-2025-in-focus/
- Infrastructure Partnerships Australia, *Australian Infrastructure Budget Monitor 2025-26* — https://infrastructure.org.au/policy-research/major-reports/australian-infrastructure-budget-monitor-2025-26/
- RLB / NZIER, *Infrastructure Forecast Report 6*, June 2026 — https://www.rlb.com/wp-content/uploads/sites/1/2026/06/NZIER-Forecast-Infrastructure-Report-2026.pdf
- IBISWorld AU: Construction (306), Heavy Industry & Other Non-Building Construction (314), Road & Bridge Construction (313) — https://www.ibisworld.com/australia/industry/construction/306/

**Buyer economics**
- ASIC, *Insolvency statistics* — https://www.asic.gov.au/about-asic/corporate-publications/statistics/insolvency-statistics
- Accountants Daily, *Company insolvencies climb to 14,152 for FY2025–26* — https://www.accountantsdaily.com.au/business/22687-company-insolvencies-climb-to-14-152-for-fy-2025-26
- Building 4.0 CRC, *Project #80: Why are insolvencies so high in the construction industry*, final report Oct 2025 — https://building4pointzero.org/wp-content/uploads/2025/10/CRC80_Project-Report_Final-Version-for-publication.pdf ; https://eprints.qut.edu.au/260918/
- Productivity Commission, *Housing construction productivity: Can we fix it?*, 16 Feb 2025 — https://www.pc.gov.au/inquiries-and-research/housing-construction/
- HIA, *2026 Small Business Conditions Survey* — https://hia.com.au/our-industry/housing/in-focus/2026/04/small-builders-big-contribution
- BDO, *Construction Survey* (2024, 2026) — https://www.bdo.com.au/en-au/insights/real-estate-construction/bdo-construction-survey

**Software pricing**
- Xero AU — https://www.xero.com/au/pricing-plans/
- MYOB AU pricing (via StackPick/Rounded, Jul 2026)
- SafetyCulture — https://www.g2.com/products/safetyculturehq/pricing
- Assignar — https://www.capterra.com/p/143935/Assignar/
- HammerTech — https://www.hammertech.com/en-us/pricing
- Payapps (subcontractor plans) — https://www.payapps.com/pricing-subcontractors/
