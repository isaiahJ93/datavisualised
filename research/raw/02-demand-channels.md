# 02 — How ANZ civil subcontractors win work, and whether a startup can get into that flow

**Hermes / adversarial market memo**
**Date: 1 September 2026. All currency AUD unless marked NZD or USD.**

---

## Method and confidence (read this before trusting any number)

Two hard constraints on this pass, stated up front because they change how much weight
each figure can carry:

1. **Direct page fetches were blocked.** The environment's egress proxy refused every
   `WebFetch`/`curl` to estimateone.com, potentiacap.com, businessnewsaustralia.com,
   totika.co.nz, iseekplant.com.au, wikipedia and others. I could not read pricing pages,
   terms of service, or ASX PDFs first-hand — the single best evidence class per my own
   method. Figures below marked **[SEARCH-SUMMARY]** come from search-engine extraction
   of those pages rather than my own reading of them. Treat them as ~80% reliable and
   re-verify any figure you would bet money on.
2. **Search budget exhausted at 200 calls.** Named-but-unexamined: BuildSearch,
   Australian Tenders, VendorPanel, Tenders.net, ProjectConnect, Cordell Connect /
   CoreLogic, BCI Central, Buildxact, Trimble/Viewpoint, Bid-hound, iSeekplant's actual
   financials. Those are listed under **Not found** at the end, not silently omitted.

Where a number is my inference it is marked **[ESTIMATE]** with the arithmetic shown.

---

## Verdict

**No-go on "help subcontractors get work" as the wedge.** This is the graveyard, and
unusually for a graveyard we have a precise headstone. Felix (ASX:FLX) owns the largest
enumerated civil-supply-chain vendor network in Australasia — **~88,000 registered
vendors**, sitting behind the mandated supplier gates of CPB Contractors and Downer,
covering **76 enterprise clients and >$50bn of contract value**. That network monetised
at **$1.8m Marketplace ARR at 30 June 2026, flat year-on-year**, while the same company's
*buy-side* Enterprise ARR was $7.5m from 76 customers. That is **~$20 per vendor per year
versus ~$99,000 per principal per year** [ESTIMATE: 1.8m/88,000 and 7.5m/76]. Fourteen
years after PlantMiner launched, with the network fully built and distribution handed to
it free by tier-1 mandate, the supply side of this market does not pay. The company's
shares trade at **$0.06** against a **$0.47** listing high.

The single biggest reason: **the subcontractor's binding constraint is not lead discovery,
it is being inside a gate someone else controls** — an Austroads/TfNSW prequalification
class, a Tōtika registration, a Felix or Ariba vendor record on a tier-1's approved list.
Discovery is already free (GETS, EstimateOne free tier, Austroads registers, tier-1
portals). Selling better discovery to someone whose problem is a gate is selling a
telescope to a man in a cell.

**Conditional go-with-changes exists in exactly one adjacent lane** — the unsolved
*private-sector* prequalification duplication problem in Australia — and it is narrow,
services-shaped, and priced in hundreds of dollars. Detail in **The gap** below. Do not
mistake it for a venture.

---

## Findings

### 1. Discovery is free or near-free. Nobody will pay much for it.

| Channel | What it costs the subcontractor | Source (accessed 1 Sep 2026) |
|---|---|---|
| **GETS** (NZ Government Electronic Tenders) | **Free.** RealMe login. Central publication point for NZ central + local government. | procurement.govt.nz/suppliers/gets/ ; gets.govt.nz |
| **EstimateOne** | **Free account** with a capped number of tenders/month. Paid subs tiers exist but E1 does not publish sub pricing. | estimateone.com/create-an-account **[SEARCH-SUMMARY]** |
| **illion TenderLink** | Free per-portal registration; paid alerts **$95+GST/mo (Standard), $105 (Premium), $120 (Enterprise)** — i.e. **~$1,140–1,440/yr**. Monthly roll-over, no lock-in. | illion.tenderlink.com/subscribe-online/ **[SEARCH-SUMMARY]** |
| **Austroads / TfNSW prequalified-contractor registers** | Free to read; being *on* them is the paid part. | austroads.gov.au/infrastructure/national-prequalification/prequalified-contractors |
| **Tier-1 portals** (CPB, Downer via Felix; Ventia via SAP Ariba) | Free to register; the cost is the compliance pack. | cpbcon.com.au/join-us/join-our-supply-chain ; downergroup.com/supplier-registration ; ventia.com/generic-page/ventia-ariba-suppliers |

**Implication:** a new lead product's price ceiling is set by a free tier at E1 and a
$95/month cancel-anytime alternative at TenderLink. There is no pricing headroom.

### 2. EstimateOne is the incumbent and is well-capitalised, but its power is in
commercial *building*, not civil.

- Self-reported network: **900+ builders, 50,000+ subcontractors, 7,000+ suppliers**;
  **100,000+ Australian organisations** used the platform in the prior year; **17+ years**
  operating; active AU, NZ, UK, Ireland. Source: estimateone.com/about-us and
  /what-is-estimateone-e1 **[SEARCH-SUMMARY]**. These are vendor-published marketing
  numbers — no independent audit found.
- **Head contractor pricing from $3,000/yr**, varying with access level; freemium for
  subs. estimateone.com **[SEARCH-SUMMARY]**.
- Subcontractor price points: **not found.** A competitor comparison page
  (builtsimple.com.au/estimateone-alternative/) asserts subs pay "$50–$200/mo for full
  bidding access" (~$600–2,400/yr). That is a hostile source with an interest in making
  E1 look expensive. **Do not cite this figure to an investor without verifying it.**
- **Capital:** Potentia Capital + Saniel Ventures invested **A$35m (US$25m)** — **$20m
  primary + $15m secondary** — with Potentia and Jasper taking a **combined 37% stake**.
  Sources: avcj.com/avcj/news/3026031 ; businessnewsaustralia.com **[SEARCH-SUMMARY]**.
  That implies a whole-company value of roughly **$95m** [ESTIMATE: 35/0.37]; note the deal
  was part-secondary so the implied post-money is softer than it looks.
- **M&A:** E1 acquired **12Build** (NL/DE/DK construction tendering), backed by Potentia.
  mainsights.io / briefglance.com. Exact date and price **not found**.
- **Revenue: $25.2m (2026) per Owler.** Owler is a crowd/algorithmic estimator and is
  routinely wrong by 2–3x. **Treat as unverified.** No second source found.
- **Profitability: not found.** E1 is private; no ASIC filing retrieved.

**Read:** E1's moat is seventeen years of being the place tender *documents* physically
land in Australian commercial building. That is a distribution monopoly built before 2010.
It is not reproducible, and it is not primarily a civil asset — civil work flows through
government prequal registers and tier-1 portals, not through E1.

### 3. The decisive evidence: Felix / PlantMiner is a 14-year controlled experiment on
exactly this thesis, and it failed on the supply side.

The history is the argument:

- **PlantMiner launched 2012–13** as a plant-and-equipment hire marketplace — literally
  "help civil subcontractors and plant owners get work." It became "Australia's largest
  online construction marketplace."
- It **pivoted away from vendor monetisation** to enterprise SaaS sold to the *buyer*,
  because "leading builders and contractors requested features for vendor prequalification
  and complex sourcing." felix.net/blog/plantminer-felix-merge. The marketplace was
  rebranded **Felix Vendor Marketplace** and demoted to a component.
- **Listed on ASX 12 January 2021.** All-time high **$0.470 on 13 Jan 2021**; all-time low
  **$0.070 (27 Sep 2023)**; **$0.06 as at 14 June 2026**. ~$19m raised on 55.2m shares.
  Sources: strawman.com/reports/FLX/all ; investing.com/equities/felix-group-holdings
  **[SEARCH-SUMMARY]**.
- **FY25 (to 30 Jun 2025): revenue $8.3m** (FY24 $6.8m); **net loss after tax $4.7m**
  (FY24 $5.1m); **adjusted EBITDA loss $2.9m**. ASX Appendix 4E, 25 Aug 2025.
- **Q4 FY26 (30 Jun 2026): Group contracted ARR $13.0m** = **Enterprise $7.5m + Vendor
  Marketplace $1.8m + Nexvia $3.7m**. Group ARR +51% on pcp — **but "Vendor Marketplace
  ARR was $1.8m, in line with Q4 FY25."** All the growth came from enterprise and from the
  **$12m Nexvia acquisition** (businessnewsaustralia.com; ASX 8 Oct 2025 quotation of
  48,181,818 shares). Sources: kalkine.com.au Q4 FY26 announcement summary
  **[SEARCH-SUMMARY]**.
- **Network:** ~**88,000 vendors**, **76 enterprise customers**, **>$50bn contract value**
  under management. Three-year Downer renewal signed Q4 FY26.

**The arithmetic that should end the discussion:**

```
Supply side (help vendors get work):  $1,800,000 ARR / ~88,000 vendors  = ~$20/vendor/yr, FLAT YoY
Buy side  (help principals buy):      $7,500,000 ARR / 76 customers     = ~$99,000/customer/yr, growing
```
[ESTIMATE — division of two published figures; Felix does not publish per-vendor ARPU.]

Felix had every advantage a supply-side monetiser could want: the largest network, and
**compulsory** distribution — CPB Contractors instructs *all* new suppliers and
subcontractors to register through Felix, and Downer routes supplier registration and
prequalification through it. Free, mandated, exhaustive supply acquisition. It still
produces $1.8m and is not growing.

### 4. The residential analogue sets the realistic price ceiling, and it is low.

hipages (ASX:HPG) is the best-run lead-gen marketplace in Australian trades and operates in
a segment with **orders of magnitude more transaction frequency** than civil:

- **FY25 revenue $83.1m (+10%)**, free cash flow **$5.6m (+162%)**. ASX release 22 Aug 2025.
- **H1 FY26 (to Dec 2025): revenue $44.9m (+11%), EBITDA $11.2m (+29%, 25% margin), NPAT
  $2.7m.** ASX release Feb 2026.
- **35,300 subscribing tradie businesses — up 1% YoY. ARPU $2,497 (+10%). MRR $7.5m.**
- Growth is now **entirely price, not volume**; management moved 100% of the AU tradie base
  onto plans that bundle leads with job-management software — an explicit anti-leakage,
  anti-churn manoeuvre. Share price down **~72% from highs**.
  Sources: kalkine.com.au ; investing.com H1 FY26 transcript **[SEARCH-SUMMARY]**.

**$2,497/yr is the demonstrated ANZ ceiling for what a small contractor will pay for
demand generation — in a category where jobs arrive weekly.** Civil subcontract packages
arrive monthly to quarterly. Assume less, not more.

### 5. The ANZ lead-gen graveyard is recent and specific.

| Company | Outcome | Numbers | Source |
|---|---|---|---|
| **PlantMiner** | Pivoted out of vendor monetisation into buy-side SaaS; marketplace ARR now flat at $1.8m | see above | felix.net/blog/plantminer-felix-merge |
| **Oneflare** | **Retired 30 June 2026.** Site and app redirect to Airtasker; auto-renewals stopped 1 June 2026 | Domain paid **$15m for 35% in 2016** (~$43m implied); Airtasker bought the assets for **$9.8m** (**$7.55m scrip + $2.25m cash**), agreed 4 May 2022, completed 25 May 2022 — **~77% below the 2016 mark** | support.airtasker.com "Oneflare has retired"; startupdaily.net 2022; ia.acs.org.au |
| **Felix Group (listed)** | $0.47 → $0.06 | FY25 NLAT $4.7m | strawman.com; investing.com |
| **iSeekplant** | Still operating; **no exit in ~14 years** despite Seven Group (22%), QIC (2017), Macquarie (2019), Position Partners (2015) on the register | Supplier counts **conflict**: own about-us says **25,000+ suppliers / 400,000+ machines**; the Eclipx partnership release says **6,200 suppliers / 82,000 assets**. Growjo's "$87.4m revenue" is an algorithmic estimate and **should be disregarded** | iseekplant.com.au/about-us; medianet Eclipx release; growjo.com |

**iSeekplant supplier complaints** (productreview.com.au/listings/iseekplant, via
**[SEARCH-SUMMARY]** — I could not open the page to count or date them): reports of
**$1,500 spent with no results**; **12-month minimum contracts with 3 months' cancellation
notice, making the true commitment 15 months**; and one report of **12 leads/month
"guaranteed" against ~4 received over six months**. This is the classic lead-gen pathology:
the vendor's revenue is a subscription, the customer's value is stochastic, and the gap is
papered over with lock-in. It is also why churn eats these businesses.

### 6. Globally, the money in this category is on the buyer's side of the table.

- **BuildingConnected → Autodesk, US$275m net of cash**, announced 20 Dec 2018, closed
  23 Jan 2019; network of **700,000+ construction professionals**. Part of **US$1.15bn**
  Autodesk spent on two construction startups that month. Sources: investors.autodesk.com;
  techcrunch.com 20 Dec 2018; Forbes 20 Dec 2018.
  - The sub-side product (**Bid Board Pro**) survives as a standalone SKU, but the revenue
    story is the GC side: 2025 repricing reportedly **more than doubled** some customers'
    annual cost, with one GC citing **US$22,000/yr** for a BuildingConnected/ProEst bundle
    and another "six figures," alongside complaints of feature stagnation since 2018.
    Source: downtobid.com blog — **a direct competitor, treat as hostile/interested**.
- **Levelset → Procore, ~US$500m** (US$425m cash + US$75m stock), completed 2 Nov 2021.
  The conversion ratio is the lesson: **250,000+ users, 6.5m projects — but only 3,300
  paying customers, i.e. ~1.3% free-to-paid** [ESTIMATE: 3,300/250,000]. Sources:
  procore.com press; SEC 8-K; ENR 29 Sep 2021.
  Levelset is instructive for a second reason: it did *not* sell leads. It sold a
  **statutory-deadline compliance product** — lien rights — where missing a date destroys
  the receivable. Mandate beats matchmaking.

### 7. Prequalification is the real gate, and it is already being solved by
non-startups.

**Australia — public civil:**
- **TfNSW Prequalification Scheme** governs road, bridge, paving, specialist works and ITS.
  *"Only contractors prequalified at the specified class(es) or higher at the date of
  closing of tenders will be eligible to tender."* Prequalification and the supplementary
  **Registration Scheme for Construction Industry Contractors** (Edition 5 Rev 22,
  Nov 2025) both run on **three-year cycles**. Evidence demanded includes **a minimum of
  two relevant contracts completed in the last two years, referee reports, and WHS
  evidence**. transport.nsw.gov.au (guidelines PDFs, Nov 2025).
- **Austroads National Prequalification System for Civil (Road and Bridge) Construction,
  2025 Edition (AP-C96-25)** provides cross-jurisdictional mutual recognition. Financial
  levels **F0.25 → F150 PLUS**; bridge categories **B1–B4**.
  **But the recognition is deliberately incomplete**, and this is the most commercially
  interesting sentence in the whole scheme: mutual recognition **applies only to
  contractors holding "Full" status** (Conditional prequalification is generally
  ineligible) and **only to road and bridge categories and financial levels — specialist
  categories are not recognised.** austroads.gov.au/infrastructure/national-prequalification
- Parallel state schemes persist: **QLD PQC / TMR**, **SA DIT** (with its own subcontractor
  policy), **VIC Construction Supplier Register** (buyingfor.vic.gov.au), **ACT
  Infrastructure Canberra**, **NSW Public Works** schemes and procurement lists.
- A **consultant cottage industry** monetises the friction today: myconsulting.com.au
  (offers assistance across Austroads, VicRoads, TfNSW, TMR PQC, Main Roads WA, SA DIT, NT,
  ACT, Defence DISP), roadbridgeprequalification.com.au, tenderbuilt.com.au, ihseq.com.au.
  **This is the demonstrated willingness-to-pay: services, per application, low ticket.**

**Australia — private/H&S prequal (the genuinely unsolved duplication):**
- **Cm3 (Greencap): $399–$3,045 +GST per year**, tiered by Business Risk Profile.
  cm3.com.au **[SEARCH-SUMMARY]**.
- **Avetta** (formerly PICS; absorbed Pegasus and BROWZ), **Rapid Global**, **iPro**,
  **Damstra** compete alongside it. Third parties charge **~$650+GST** to complete a single
  Avetta assessment on a contractor's behalf (as-4801.com.au; NECA Safety Specialists).
- These schemes **do not recognise each other**, and they sit *on top of* whatever the
  principal mandates — Felix at CPB and Downer, SAP Ariba at Ventia. A civil sub working
  for four tier-1s can legitimately carry four vendor records, two commercial H&S prequals
  and one or more government prequalifications simultaneously.

**New Zealand — already fixed, by an industry body:**
- **Tōtika**, run by **CHASNZ**, does not run its own questionnaire. It **sets the standard
  that approved member schemes assess against** (SiteWise/Impac, PreQual, Telarc, SHE
  PreQual, ThinkSafe, Advanced Safety), and cross-recognises **ISO 45001, SafePlus and
  Q-Safe**. chasnz.org/totika
- Registration cost via one approved provider: **sole trader NZ$280 / 2 years; Category 1
  NZ$450 / 2 years; Category 2 NZ$949/yr; Category 3 NZ$1,459/yr.**
  sheprequal.co.nz/totika/faq **[SEARCH-SUMMARY]**.
- **NZTA requires a current Tōtika registration before a physical works contractor may even
  apply for NZTA prequalification.** nzta.govt.nz/about-us/information-for-suppliers/
  contractor-prequalification. That is a genuine regulatory forcing function — and it points
  at an incumbent, not a vacancy.
- **NZTA is simultaneously narrowing the open-tender surface.** Its March 2026 Request for
  Submission established a new **Supplier Directory for Physical Works** — a national panel
  with regional capability specifications for opportunities **up to NZ$50m**. Submissions
  closed **1 May 2026**; outcomes communicated from **12 June 2026**. Four prequalification
  levels per work category. gets.govt.nz (NZTA Prequalification Refresh — Invitation to
  Qualify); nzta.govt.nz supplier information pack Issue 7, April 2026.
  **Read the strategic consequence:** the largest civil client in New Zealand has just
  moved a NZ$50m-and-under band of work from "advertised, then bid" to "be on the directory,
  or you never see it." A lead-discovery product has less to discover every year.

### 8. Relationship-versus-tender: the honest answer is that I could not find ANZ data.

I found no credible ANZ dataset quantifying the split of civil subcontract work won through
open tender versus repeat/negotiated relationships. **Not found.** What I did find is
directional and largely US/academic:

- Open tendering is *"nearly universal in the public sector and only rarely used on private
  projects."* procore.com/library/types-of-tender-construction.
- Clients and head contractors *"lean more and more toward selective and negotiated
  tendering ... after they've established trusted relationships."* buildxact.com blog.
- Contractor–subcontractor strategic alliances *"increase the tender hit rate therefore
  increasing market share and reducing marketing cost"* — the peer-reviewed framing.
  ascelibrary.com JCEM Vol 149 No 12 (2023); researchgate.net (public works tender
  evaluation criterion).

**Anyone selling this thesis to an investor must fill this hole with primary research.**
It is the load-bearing assumption of the entire opportunity and it is currently unevidenced.

---

## Bottom-up market size (show the arithmetic; attack the inputs)

**Counting the units.** There is no clean ABS cut for "civil subcontractor." Four
independent enumerations bracket it:

| Source | Count | What it actually measures | As at |
|---|---|---|---|
| ABS, Private Sector Construction Industry | **5,789** Heavy & Civil Engineering Construction businesses | Civil *head* contractors, not subs | Jun 2012 |
| ABS via Master Builders Australia | **462,939** construction businesses (all) | Dominated by non-employing residential sole traders | Jun 2025 |
| Felix | **~88,000 vendors** across 76 principals / >$50bn contract value | The closest thing to a census of the ANZ civil/infrastructure supply chain | Jun 2026 |
| EstimateOne | **50,000+ subcontractors** | Predominantly commercial *building* trades, AU | 2026, self-reported |
| iSeekplant | **6,200–25,000 suppliers** (sources conflict) | Plant hire subset | 2026, self-reported |
| BITRE IS-105 | HCEC = **$33bn value added (2.0%)**, **114,600 employed** | Sector scale | 2017-18 / May 2019 |

**Serviceable population [ESTIMATE]: 15,000–25,000 AU+NZ firms** that perform civil
subcontract work at a scale where someone in the business is paid to prepare tenders.
Reasoning: Felix's 88,000 includes every one-truck operator, consultant and materials
supplier; the tier that buys software is the employing subset. ABS structure shows the
overwhelming majority of construction-services businesses are non-employing or micro, and
a firm without a nominated estimator does not buy tender software.

**Revenue at a defensible price:**

```
Optimistic-realistic: 20,000 firms x 25% attach x $2,500/yr  = $12.5m ARR
                                    (hipages ARPU = proven AU ceiling)
Realistic new entrant: 20,000 firms x 10% attach x $1,500/yr = $3.0m ARR
                                    (attach capped by E1 free tier + $95/mo TenderLink)
```
[ESTIMATE — both lines. Attack the attach rate first; it is the softest input.]

**Two independent cross-checks, and both land in the same place:**
- Felix Vendor Marketplace — the largest such network in the region, distributed free by
  CPB and Downer mandate — does **$1.8m and is flat**.
- Even if E1's unverified $25.2m total revenue is real and *half* of it came from
  subcontractor subscriptions, that is ~$12m from 50,000+ subs across AU/NZ/UK/IE —
  ~$250/sub/yr blended [ESTIMATE], because most sit on the free tier.

**Conclusion: the ANZ "sell demand access to civil subcontractors" pool is on the order of
$5–15m of annual revenue, and it is already substantially captured.** That is a lifestyle
business fighting two funded incumbents for the privilege. It is not venture scale.

---

## The gap — precisely stated

The one thing that survived falsification, stated narrowly enough to be honest:

**Who:** Australian civil subcontractors — roughly the F1–F25 financial band — who work
for more than one tier-1 head contractor and more than one state road authority.

**What they can't do today:** carry one verified evidence set. They maintain, in parallel:
- a **Felix** vendor record (mandatory at CPB and Downer),
- an **SAP Ariba** record (mandatory at Ventia),
- a commercial H&S prequal at **Cm3 ($399–$3,045/yr)** and/or **Avetta / Rapid / Damstra**,
  none of which recognise each other,
- a **TfNSW** prequalification/registration on a three-year cycle requiring two recent
  contract exemplars plus referee reports plus WHS evidence,
- and, where the Austroads mutual-recognition carve-outs bite, *separate* state applications
  — because recognition **excludes specialist categories entirely and excludes anyone on
  "Conditional" status.**

**What it costs them:** the visible cash is modest and countable — **Cm3 $399–3,045/yr**,
**~$650+GST per consultant-completed Avetta assessment**, plus per-application consultant
fees across TfNSW/TMR/Main Roads WA/SA DIT. The real cost is the estimator- or
office-manager-weeks that produce no revenue. **I have no primary measurement of that time
cost. Measuring it is test #2 below, and it is the number the whole thesis turns on.**

**Why New Zealand is not the beachhead:** Tōtika already is this product. CHASNZ owns it,
NZTA mandates it, six assessment providers deliver it, and the whole thing costs a sole
trader **NZ$280 for two years.** There is no room under that price and no way past that
mandate.

**Why Australia's version is hard anyway:** the equivalent public-civil answer already
exists (**Austroads NPS**), it is owned by the road agencies collectively, and its gaps —
specialist categories, Conditional status — are *deliberate policy choices*, not oversights
a startup can arbitrage. The genuinely unsolved layer is the **private** one: Cm3 vs Avetta
vs Rapid vs Damstra vs each tier-1's own Felix/Ariba instance. That is a real duplication
problem with a real, recurring, **must-spend** budget line — unlike lead generation, which
is discretionary and gets cut first in a downturn. But it is a **$400–$3,000/yr line item**,
and every incumbent in it is defending an existing mandate.

---

## Who eats you

| Incumbent | Position | Price | Weakness | Reaction time |
|---|---|---|---|---|
| **EstimateOne / E1** | 17 years, ~$95m implied value, $35m Potentia/Saniel capital, expanding into Europe via 12Build | HC from **$3,000/yr**; subs freemium | Commercial *building*, not civil; sub-side is a loss-leader they don't need to defend hard | **Fast and lethal.** They already run a free tier. Any discovery feature you build, they bundle into it at zero and you have no answer. |
| **Felix (ASX:FLX)** | Owns the **mandated** supplier gate at CPB and Downer; ~88,000 vendors; just renewed Downer for 3 years | Enterprise **~$99k/customer/yr** [ESTIMATE]; Marketplace ~$20/vendor/yr [ESTIMATE] | Financially fragile — $0.06 share price, FY25 NLAT $4.7m, marketplace ARR flat | **Slow, but you cannot route around the mandate.** Downer is locked to ~FY29. |
| **SAP Ariba** | Ventia's mandated network | Enterprise | Hated, generic | Irrelevant — will never be displaced by a startup |
| **Cm3 (Greencap), Avetta, Rapid Global, Damstra** | Own private H&S prequal | **$399–$3,045/yr** (Cm3) | Mutually non-interoperable — the actual gap | Moderate; Avetta opened Sydney and Newcastle offices in 2025 (businesswire, 16 Jul 2025) and is consolidating (absorbed PICS, Pegasus, BROWZ) |
| **Austroads / TfNSW / TMR / Tōtika-CHASNZ** | Statutory and quasi-statutory gates | Free-to-cheap, government-blessed | Slow, carve-out-riddled | **Cannot be competed with. Can only be integrated with — and they do not need you.** |
| **illion TenderLink** | Tender alerts AU+NZ | **$95–120+GST/mo**, cancel anytime | Commodity | Fast to discount |
| **Prequal consultants** (myconsulting.com.au, TK Business Group, tenderbuilt, IHSEQ) | The *actual* incumbent for prequal pain | **~$650+GST per assessment** | Non-scalable, unbranded | Zero — but they set the customer's reference price, and it is low |

---

## Kill shots, ranked by probability

1. **~85% — The supply side does not pay, and it has already been proven at scale.**
   Felix: $1.8m ARR, flat, across 88,000 vendors handed to it by tier-1 mandate. This is
   not a hypothesis about your business; it is a measurement of your business, run for you,
   for fourteen years, by someone with better distribution than you will ever have.

2. **~75% — Wrong wallet.** The pain is acute in the subcontractor; the budget sits with
   the principal and the head contractor. Felix earns ~$99k/yr from a principal and ~$20/yr
   from a vendor. Every survivor in this category — Felix, BuildingConnected, Ariba, E1's
   $3,000 head-contractor tier — monetises the *buyer*. Acute pain in a party with no
   budget is a charity.

3. **~70% — The gate, not the list, is the constraint; and you cannot own gates.**
   Prequalification classes are set by TfNSW, Austroads, TMR, Main Roads WA, SA DIT, NZTA
   and CHASNZ. NZTA's 2026 Supplier Directory just moved everything under NZ$50m behind a
   panel. Introducing a subcontractor to work they are not prequalified to bid is a
   nullity — and the entities that control the gates are governments who will never pay a
   startup and can never be displaced by one.

4. **~60% — Incumbent zero-pricing.** E1 already gives subs a free tier and has $35m of PE
   capital. TenderLink is $95/month, cancel anytime. GETS is free. Your product must be
   worth more than free to a business whose actual constraint is elsewhere.

5. **~55% — Frequency and leakage.** hipages needed weekly-frequency residential jobs and
   an anti-leakage software bundle to reach 25% EBITDA margins — and its subscriber count
   still grew 1% and its shares fell 72%. Civil subcontract packages are monthly-to-
   quarterly, high-value, negotiated face-to-face, and land inside pre-existing
   relationships. That is textbook maximum-leakage geometry: the parties meet once and never
   need you again. Oneflare — $43m implied in 2016, $9.8m in 2022, **retired 30 June 2026** —
   is the recent local demonstration.

---

## Cheapest next test — 30 days, roughly $3–5k, no code

**Test 1 (do this first, ~15 hours): the last-three-jobs count.**
Interview 20 civil subcontractors (AU + NZ, $2m–$50m turnover). Ask exactly one factual
question and refuse to accept an opinion in its place: *"For your last three awarded
packages — who told you about it, and how did they tell you?"* Log the channel per job.
**Stop condition: if fewer than 5 of the 60 packages originated from any platform, the
demand-channel thesis is dead** and no amount of product will revive it. My prior is that
you will land at 2–4 of 60. This also fills the evidence hole in Finding 8, which is
currently the least-supported load-bearing claim in this memo.

**Test 2 (run concurrently, ~8 hours): the compliance-cash probe.**
Ask the same 20 firms two numbers: (a) total cash spent last financial year on
prequalification — Cm3/Avetta/Rapid/Damstra/Tōtika fees plus consultants; (b) how many
distinct vendor portals and prequal schemes they currently maintain records in.
**Stop condition: median cash spend below $2,000/yr, or median portal count below 4.**
Below those thresholds the interoperability gap is real but too small to fund a company,
and you should walk.

**Test 3 (5 calls, ~4 hours): the mandate test.**
Ask five tier-1 procurement leads (CPB, Downer, Fulton Hogan, BMD, Seymour Whyte) whether
they would mandate a *new* vendor system to their supply chain in the next 24 months.
**Stop condition: if four or five say they are contracted to Felix or Ariba** — and Downer
has just renewed for three years to ~FY29 — then the only distribution channel that has
ever worked in this category is closed, and there is no second channel.

**What a pass looks like:** Test 1 shows platform-sourced work is negligible *and* Test 2
shows median prequal spend above $3,000/yr across 5+ schemes *and* Test 3 finds at least
two tier-1s willing to mandate. That combination points you away from "help subs get work"
and toward a narrow **Australian private-prequal interoperability** play sold to principals
— the only thing in this memo that survived. If Test 2 fails, there is nothing here and the
correct action is to stop.

---

## Not found — gaps a second pass must close

Stated explicitly rather than filled with plausible numbers:

- **EstimateOne's published subcontractor tier names and price points**, and whether E1 is
  profitable. The only figures in circulation are a competitor's assertion ($50–200/mo) and
  an Owler estimate ($25.2m revenue). Both are unsafe.
- **Date and price of E1's 12Build acquisition.**
- **iSeekplant's actual revenue, paid-supplier count, and membership pricing.** The public
  supplier counts contradict each other by 4x (6,200 vs 25,000). Growjo's $87.4m is
  algorithmic noise. Seven Group's carrying value of its 22% stake would settle this and
  sits in SGH's annual report — not retrieved.
- **Any ANZ dataset on the relationship-versus-open-tender split for civil subcontract
  packages.** This is the most important missing number in the memo.
- **Not examined at all** (search budget): BuildSearch, Australian Tenders, VendorPanel,
  Tenders.net, ProjectConnect, Cordell Connect / CoreLogic, BCI Central, Buildxact,
  Trimble/Viewpoint, Bid-hound, and the supplier-onboarding mechanics of Fulton Hogan, BMD,
  Seymour Whyte, Georgiou, Acciona and McConnell Dowell specifically. CPB (Felix), Downer
  (Felix) and Ventia (Ariba) were confirmed; the other six were not.
- **Primary reading of every source cited.** The egress proxy blocked direct fetches;
  figures marked **[SEARCH-SUMMARY]** are second-hand extractions and must be re-read from
  source before any of this reaches an investor.
