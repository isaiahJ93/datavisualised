# 09 — AI opportunities for a solo, Indigenous-owned, construction-domain operator

**Hermes market memo · as at 2 September 2026 · AUD unless marked**
Client: Supply Nation **registered** business, civil/construction domain, <A$50,000 capital,
solo, no engineering team, wants cash inside 12 months and a path to a large outcome.

> **Sourcing constraint (read this first).** This session's egress policy blocked **every**
> direct page fetch — `WebFetch` and `curl` both returned 403 CONNECT for every domain
> attempted, including `abs.gov.au`, `niaa.gov.au`, `iba.gov.au`, `business.gov.au`,
> `industry.gov.au`, `supplynation.org.au`, `en.wikipedia.org` and all vendor pricing pages.
> Web *search* worked until the session budget (200 calls) was exhausted. **Every figure below
> is search-result synthesis, not a read of the primary document.** This is the same
> constraint recorded in `research/METHODOLOGY.md` for the previous round. It was reported,
> not worked around. Confidence tags are used throughout; §8 lists what must be re-verified.

---

## VERDICT

**Go — but as a services business with an AI-leveraged delivery model, not as an AI startup.**

The honest answer to the assignment's closing question is the uncomfortable one: for this
operator, AI is **leverage inside a service**, not a product to sell. The evidence is not
ambiguous. The Australian-founded company that built exactly the software this client's domain
suggests — **Bidhive, Brisbane, bid & proposal management** — reached roughly **US$210k revenue
in 2023, *down* from US$233k in 2021**, six years after founding, and was **acquired by
Responsive (US) in May 2025** ([getlatka](https://getlatka.com/companies/bidhive),
[SmartCompany](https://www.smartcompany.com.au/startupsmart/bidhive-responsive-acquisition-bid-proposal-management-startup/),
both **[SEARCH-SUMMARY, LOW CONFIDENCE on revenue]**). That is the empirical ceiling of an
Australian bid-tech SaaS built by a competent, funded, non-solo team. Meanwhile the *service*
it was trying to automate still bills **A$4,000–8,000 + GST per tender** and up to **A$40,000 +
GST for major project bids** ([The Tender Team](https://thetenderteam.com.au/fees-tender-writing-rates/),
[TenderWise](https://www.tenderwise.com.au/blog/2023/4/28/how-much-does-a-tender-writer-charge),
[SEARCH-SUMMARY]).

The single biggest reason for the verdict: **this client owns one asset that no competitor can
copy and no foundation model can absorb — verified Indigenous ownership under a procurement
regime with a legislated, rising, dated mandate.** Every other candidate on the list (AI
consulting, automation agency, fractional AI officer, data labelling, construction AI SaaS) is
something a thousand better-capitalised people can also do. Indigenous Procurement Policy
eligibility is a registry status, not a skill. Anthropic cannot ship it in a model release and
AutogenAI cannot buy it.

**The condition on the "go": there is a gating question that must be answered in week one.**
From **1 July 2026** the IPP requires **51%+ Indigenous owned *and controlled*** (or ORIC
registration), up from 50% ([MinterEllison](https://www.minterellison.com/articles/changes-to-the-commonwealths-indigenous-procurement-policy);
[NIAA IPP Guidelines, 12 May 2026](https://www.niaa.gov.au/sites/default/files/documents/2026-05/IPP-Guidelines-12-May-2026.pdf)
[SEARCH-SUMMARY]). Supply Nation **"Registered"** is the 50% tier; **"Certified"** is the 51%+
owned/managed/controlled tier ([supplynation.org.au FAQ](https://supplynation.org.au/resources/faqs/faqs-indigenous-business/)
[SEARCH-SUMMARY]). The client is described as *registered*. **If the entity sits at exactly 50%,
or Indigenous control is not demonstrable, the entire distribution advantage in this memo expires
on a known date and the recommendation collapses to "generic bid writer with no edge."** Resolve
this before spending a dollar.

**And the part the client will not want to hear:** the realistic ceiling of the recommended
business is roughly **A$500k–1m/year of owner-operated revenue with an exit at 1–3x revenue to a
bid-consultancy or proposal-software roll-up.** That is a very good outcome for someone starting
with <A$50k. It is not a large outcome in the venture sense, and nothing in the 2026 AI landscape
changes that for an unfunded solo operator. Anyone promising otherwise is selling a course.

---

## 1. THE SERVICES-AS-SOFTWARE THESIS — half true, and the popular evidence for it is a category error

### 1.1 The headline numbers everyone quotes are not services companies

The thesis circulating in 2025–26 is that AI lets you deliver a *service* at *software* margins,
evidenced by extreme revenue-per-head figures. The figures are real. The inference is wrong.

| Company cited | Revenue / head | What it actually is |
|---|---|---|
| Lovable | ~US$2.7m ARR/employee (US$400m ARR, 146 FTE, early 2026) | **Self-serve software product.** No service delivery at all. |
| Midjourney | ~US$18m/employee (~US$200m rev, ~11 staff) | **Consumer subscription product.** No service delivery at all. |
| Private SaaS median | **US$141,125/employee (2026)**, up from US$129,724 | The actual benchmark ([SaaS Capital](https://www.saas-capital.com/blog-posts/revenue-per-employee-benchmarks-for-private-saas-companies/)) |

Sources: [RiffOn](https://riffon.com/insight/ins_bko640vxb1j3),
[Forbes / Paul Baier, 31 Mar 2026](https://www.forbes.com/sites/paulbaier/2026/03/31/ai-native-firms-lead-in-revenue-per-employee/)
[SEARCH-SUMMARY]. **Citing Lovable and Midjourney as proof that AI services scale is survivorship
bias stacked on a category error.** They are not services businesses. They prove nothing about
whether an agency can bill software-like margins.

### 1.2 What the services data actually says

The one genuinely useful finding: **agencies that *reduced* their service lines posted the
fastest growth in 2025 and averaged 30% net margins; agencies that *expanded* services averaged
10%** ([Promethean Research, Digital Agency Industry Report](https://prometheanresearch.com/digital-agency-industry-report/)
[SEARCH-SUMMARY]). That is an argument for **narrowness**, not for AI. It happens to be the single
most actionable sentence in this section for a solo operator: pick one deliverable, refuse the rest.

### 1.3 The mechanism, stated honestly

AI compresses **drafting labour** on document-heavy work by perhaps 30–60% `[ESTIMATE — no
independent measurement found for bid writing specifically; the one vendor-published figure,
"80% reduction in RFP response time, 71% of answers auto-filled," is a customer testimonial on a
vendor's own blog and should be discounted heavily]`. It does **not** compress:

- **Selling.** Still one founder, still one calendar.
- **Discovery.** You cannot LLM your way through the two-hour interview where the site foreman
  tells you what actually happened on the last job. That content is what wins bids.
- **Accountability.** The client is buying someone to blame. That is not automatable and it is
  the thing they are actually paying for.
- **Utilisation.** A solo operator's binding constraint is 220 working days, not tokens.

**Read: services-as-software is real, but the effect is gross-margin expansion per delivered
hour, not software economics.** Revenue stays linear in founder-days. Anyone telling a solo
operator otherwise is describing a product company.

---

## 2. BID AND TENDER RESPONSE — the software is unwinnable, the service is immediately monetisable

### 2.1 The software side: do not enter. Here is the whole board.

| Player | Capital | Scale | Price | Status |
|---|---|---|---|---|
| **AutogenAI** (UK/US) | **US$65.3m total** (US$39.5m Series B, Salesforce Ventures + Spark) | ~194 staff (2026); **~US$36.1m ARR (2025)** [LOW CONF — getlatka] | **No public price.** Third-party estimate **~US$30k+/yr, 5-seat minimum**, rising to mid-five/six figures | Founded 2022, scaling |
| **Responsive** (ex-RFPIO) | Venture-backed | Global | Sales-gated, est. **US$20k+/yr**; ~US$299/user/mo + platform fee | **Bought Bidhive, May 2025** |
| **Loopio** (CA) | Venture-backed | Global | Published **US$20,000/yr for 10 seats**; **median buyer US$22,786/yr**, range US$11,682–55,704 (Vendr) | Established |
| **Bidhive** (Brisbane) | 2 institutional investors, amount not found | **~US$210k revenue 2023, down from US$233k 2021** [LOW CONF] | n/d | **Acquired May 2025** |

Sources: [thebaehq](https://www.thebaehq.com/news/autogenai-secures-39-5m-series-b-funding-to-revolutionise-bid-writing-with-generative-ai),
[getlatka AutogenAI](https://getlatka.com/companies/autogenai.com),
[inventive.ai pricing teardown](https://www.inventive.ai/blog-posts/autogen-ai-pricing),
[Vendr / Loopio](https://www.vendr.com/marketplace/loopio),
[AutoRFP.ai Loopio pricing](https://autorfp.ai/blog/loopio-pricing),
[getlatka Bidhive](https://getlatka.com/companies/bidhive),
[SmartCompany](https://www.smartcompany.com.au/startupsmart/bidhive-responsive-acquisition-bid-proposal-management-startup/).
All **[SEARCH-SUMMARY]**.

**Three things this table settles:**

1. **The category is enterprise, sales-gated, US$20–30k ACV.** That is a 6–12 month sales cycle
   requiring a salesperson. A solo founder with <A$50k cannot fund one cycle, let alone a pipeline.
2. **Bidhive is the control experiment and it failed the way Vaultry would fail.** An Australian
   founder, a genuinely good product, real named logos (UK healthcare staffing, US waste
   management, global engineering), Open Contracting Partnership coverage in 2022 — and revenue
   that *went backwards* between 2021 and 2023 before an acquisition. **An ANZ-only bid-software
   market does not support a venture outcome.** This is the same A$22m-SAM wall the previous round
   hit on compliance (`research/raw/03-market-size.md`), from a completely different direction.
3. **The category has already consolidated.** Responsive bought Bidhive. There is no independent
   ANZ slot left to occupy.

### 2.2 The service side: real prices, paid today, in this client's domain

| What | Price (AUD, ex GST unless noted) | Source |
|---|---|---|
| Bid/tender writing consultant, hourly | **A$165 + GST** (published guide); market band **A$150–350/hr** | [The Tender Team](https://thetenderteam.com.au/writing-services/frequently-asked-questions/) |
| **Average tender, complete response** | **A$4,000–8,000 + GST** | [The Tender Team](https://thetenderteam.com.au/how-much-does-it-cost-for-a-professional-tender-writer-to-help-us-write-our-tenders/) |
| Small / simple tender | A$2,000–5,000 (one source: from **A$2,200**) | [TenderWise](https://www.tenderwise.com.au/blog/2023/4/28/how-much-does-a-tender-writer-charge) |
| Medium complexity | A$5,000–15,000 | ibid. |
| Large / major project bid | **A$15,000–30,000+**, up to **A$40,000 + GST** | ibid. |
| Prequalification completed by consultant (existing ANZ civil benchmark) | **~A$650 + GST per assessment** | `research/raw/02-demand-channels.md` (prior round) |

All **[SEARCH-SUMMARY]** — the pricing pages themselves were egress-blocked.

**The critical structural fact:** the buyer of bid writing has *already decided* to pursue a
specific contract worth **10–100x the writing fee**. Price sensitivity is therefore low relative
to the decision already made. This is the exact opposite of Vaultry's compliance buyer, who was
being asked to pay for an obligation with no upside. **Follow the money: the bid-writing fee comes
out of a bid/no-bid budget that already exists and is already being spent — on internal staff time
if not on a consultant.** That is a budget line, not a hope.

### 2.3 Has AI commoditised bid writing? Not yet. Here is the honest window.

I could not find a single non-vendor source measuring price movement in Australian bid-writing
fees. **Not found.** Every "AI hasn't replaced bid writers" article located was published by a bid
consultancy with an obvious interest ([Thornton & Lowe](https://thorntonandlowe.com/ai-in-bid-writing-using-chatgpt/),
[tenderconsultants.co.uk](https://www.tenderconsultants.co.uk/ai-bid-writing/)) or by an AI bid
tool ([AutoRFP.ai](https://autorfp.ai/blog/ai-tender), [mytender.io](https://mytender.io/blog/ai-bid-writing-tips-2026-win-more-tenders)).
**Discount both directions.**

What is verifiable and matters more:

- **Procurement is starting to regulate AI use in responses.** Suppliers on the whole-of-government
  **Management Advisory Services and People panels must declare planned AI use when responding to
  RFQs**; the DTA updated its *Policy for the Responsible Use of AI in Government* in **December
  2025** and published **AI Model Clauses v2.0**
  ([Australian Tenders guide](https://info.australiantenders.com.au/guide-to-procurement-and-ai-use-in-tendering);
  [Digital Watch](https://dig.watch/updates/australia-finance-generative-ai-guidance)) **[SEARCH-SUMMARY]**.
- **Privacy Act 2024 automated-decision-making disclosure obligations commence 10 December 2026**
  ([anitech.ai](https://anitech.ai/ai-governance-government-contractors-australia/) — secondary
  source, **verify against the Act**).

**Read: AI in bids is becoming a *disclosure and governance* question, not just a drafting
question.** That is good news for a human accountable service and bad news for an undisclosed
AI-generated one. It also creates a small, real, sellable artefact: an **AI-use declaration and
tender AI policy** for firms that now have to answer that question in submissions.

**The window on the fee, stated plainly:** the A$5,000 fee is currently justified by hours. When
the client's own estimator can draft competently with an LLM — 2 to 4 years `[ESTIMATE]` — the
drafting component compresses toward A$1,500–2,500. The defensible residue is win strategy,
evaluator insight, accountability, and **Indigenous participation credibility**. Only the last one
does not compress.

---

## 3. THE DISTRIBUTION EDGE — this is the actual finding

The IPP is a legislated, dated, rising mandate that this client is on the inside of.

| Fact | Value | As at | Source |
|---|---|---|---|
| Commonwealth Indigenous procurement **value target** | **3%** (up from 2.5%), rising **+0.25%/yr to 4% by 2030** | from 1 Jul 2025 | [NIAA](https://www.niaa.gov.au/our-work/employment-and-economic-development/indigenous-procurement-policy-ipp), [Sparke Helmore](https://www.sparke.com.au/insights/enhancing-the-indigenous-procurement-policy/) |
| **Mandatory Set-Aside** | **all remote-area** procurements; **all non-remote A$80,000–200,000 (GST inc.)** | 2026 | [NIAA IPP Guidelines 12 May 2026](https://www.niaa.gov.au/sites/default/files/documents/2026-05/IPP-Guidelines-12-May-2026.pdf) |
| IPP delivery 2024–25 | **1,200+ Indigenous businesses**, **13,000+ contracts**, **A$1.6bn** (avg **~A$123k/contract**) | FY2024-25 | ibid. |
| **Eligibility tightens** | **51%+ Indigenous owned *and controlled***, or ORIC-registered; **transition from 1 Jul 2026**; explicit anti-"black cladding" enforcement intent | 1 Jul 2026 | [MinterEllison](https://www.minterellison.com/articles/changes-to-the-commonwealths-indigenous-procurement-policy), [Ministers' media centre](https://ministers.pmc.gov.au/mccarthy/strengthening-indigenous-procurement-policy) |
| Commonwealth contracts published on AusTender | **86,926 contracts, A$104.90bn**; 93.8% by volume to Australian-address businesses | FY2024-25 | [Dept of Finance](https://www.finance.gov.au/government/procurement/statistics-australian-government-procurement-contracts-) |

All **[SEARCH-SUMMARY]**.

**Two buyers fall out of this, and only one of them has money.**

**Buyer A — Indigenous businesses bidding for set-aside and IPP work.** 1,200+ of them won
Commonwealth work last year. Acute need, low internal bid capability. **But the average contract
is ~A$123k.** A firm winning two of those a year cannot pay a A$48k retainer. **If the client
sells only to this segment, this is Vaultry again in different clothing: real pain, no budget.**
Only the top decile by revenue can sustain a retainer.

**Buyer B — non-Indigenous head contractors and primes.** These firms must evidence Indigenous
participation to win major public infrastructure work, and must *write that section of the
submission*. They have real bid budgets — the previous round counted **~610 ANZ civil firms in the
20–199 employee band** and **~4,868 with ≥5 employees** (`research/raw/03-market-size.md`), and
established that this band has genuine budget lines. **Buyer B signs the cheque out of an existing
bid cost line, and Buyer B cannot become Indigenous-owned to avoid needing you.**

**This is the only structurally defensible position in this entire memo.** Not the AI. The registry
status plus the domain plus the fact that the buyer's alternative is worse for them.

**The hard limit on it — say it out loud:** the government has stated it will work with regulators
on **"disingenuous conduct, or 'black cladding', designed to gain access to the IPP"**
([MinterEllison](https://www.minterellison.com/articles/changes-to-the-commonwealths-indigenous-procurement-policy)).
If this business scales by fronting non-Indigenous delivery labour, it *becomes* the enforcement
case study. **That caps headcount scaling, which caps the outcome.** The honest business is one
where the Indigenous owner genuinely does or genuinely supervises the work.

---

## 4. AI IN CONSTRUCTION 2026 — what is bought, what is bundled, and why a solo founder must not enter

### 4.1 The funded field, with the numbers

| Company | Capital | Traction | 2026 status |
|---|---|---|---|
| **Trunk Tools** | **US$70m total**; US$40m Series B (Insight Partners, 24 Jul 2025); **US$325m valuation** | **~US$8.5m ARR (2025)**; Suffolk enterprise agreement, 1,500+ field users | Scaling. **~38x ARR valuation — capital-intensive per revenue dollar.** |
| **Document Crunch** | **US$32.5m** (US$9m A, Feb 2024 + US$21.5m B) | **400+ customers** (Balfour Beatty, DPR, Swinerton, Webcor); **~US$12.6m revenue**, 60 staff; US$350bn construction volume processed | **ACQUIRED — Trimble, announced 2 Apr 2026, close expected Q2 2026** |
| **ALICE Technologies** | Venture-backed since 2015 | McKinsey commercial alliance; hiring in 2026 | Alive, no distress found |
| **nPlan** | Round led by CapHorn, **Dec 2025**, with Chevron Tech Ventures + Suffolk Technologies | Anglian Water AMP8 (2025–30); highways partnership Feb 2026 | Alive. **No shutdown found** — the assignment's premise was wrong |
| **Buildots / OpenSpace / Dusty Robotics / Versatile** | — | **Not verified this session** (search budget exhausted before reaching them) | **NOT FOUND** |

Sources: [SiliconANGLE](https://siliconangle.com/2025/07/24/trunk-tools-raises-40m-revolutionize-construction-teams-interact-project-data/),
[getlatka Trunk Tools](https://getlatka.com/companies/trunktools.com),
[Trimble newsroom, 2 Apr 2026](https://news.trimble.com/2026-04-02-Trimble-to-Acquire-Document-Crunch-to-Add-AI-Powered-Risk-Management-and-Document-Compliance-to-Trimble-Construction-One-Project-Delivery-Ecosystem),
[Document Crunch Series A](https://www.documentcrunch.com/news/series-a),
[nPlan press](https://www.nplan.io/news-and-press), [ALICE newsroom](https://www.alicetechnologies.com/all-news).
All **[SEARCH-SUMMARY]**.

### 4.2 The bundling event that closes the door

On **23 July 2026 Procore announced Digital Coworker packages**
([Procore press release](https://www.procore.com/press/procore-introduces-digital-coworker-packages-expands-ai-agent-library-and-previews-skills-to-help-construction-teams-put-ai-to-work),
[StockTitan/PCOR](https://www.stocktitan.net/news/PCOR/procore-introduces-digital-coworker-packages-expands-ai-agent-flfcexk3nvkt.html)):

- **Starter:** 5 bundled agents — **Deep Search, Submittal Review, RFI, Daily Log, Contract Review**
- **Pro:** **20 agents**, spanning "project planning and **bidding**, safety, quality and risk management"
- **Enterprise:** **Agent Studio** for building custom agents
- **Skills** (teach Procore your own standards) rolling out across all tiers from **August 2026**
- Procore R&D budget reported at **~US$300m** ([constructionindustry.ai](https://www.constructionindustry.ai/product/procore-ai-copilot-agents-review/) [SEARCH-SUMMARY])

**Read the sequence.** Document Crunch built construction contract-review AI, raised US$32.5m,
reached 400 customers and ~US$12.6m revenue — and in **April 2026 was bought by Trimble**. Three
months later, in **July 2026, Procore shipped "Contract Review" as one of five agents in its
*entry-level* bundle.** The category leader's entire product became a line item in a competitor's
starter tier inside a single quarter.

**What an unfunded solo founder therefore cannot do in construction AI:**

- **Data moat:** you have none. The corpus that matters (drawings, specs, RFIs, submittals across
  thousands of projects) sits inside Procore, Autodesk, Trimble and the GCs. You cannot acquire it.
- **Integration burden:** the product must live inside Procore/Autodesk/Bentley to be used. You are
  building on a platform whose owner is shipping your feature.
- **Sales cycle:** enterprise construction is 9–18 months. Government AI procurement is worse — one
  Australian practitioner notes government AI tenders take **ten months while the product changes
  every three** ([True Source Consulting, 2 Jun 2026](https://truesourceconsulting.com.au/2026/06/02/government-ai-tender-procurement-product-velocity-gap/) [SEARCH-SUMMARY]).
  <A$50k does not survive one cycle.
- **Safety-critical liability:** an AI answer wrong on a structural spec or an SWMS is not a support
  ticket. Professional indemnity for an unproven solo vendor asserting engineering-adjacent outputs
  is either unobtainable or ruinous.
- **The wedge is already taken locally:** **Framework AI's "Form Fill"** — automating construction
  prequalifications and bid/tender submissions from a company knowledge base — **launched September
  2026** (`research/raw/04-business-model.md`, [frameworkai.ca/form-fill](https://frameworkai.ca/form-fill)).

**Verdict on §3 of the assignment: closed. Not "hard" — closed.**

---

## 5. DEFENSIBILITY — ranked by durability, not excitement

The right question is not "is this a good idea" but **"what class of moat is it, and can a solo
operator hold that class?"**

| Moat class | Holds against a model release? | Holds against an incumbent? | Available to a solo operator with <A$50k? |
|---|---|---|---|
| **(a) Model capability / prompting** | **No.** Absorbed on the next release. | No | Yes — worthless |
| **(b) Proprietary data** | Yes | Partly | **No** — you don't have it in construction |
| **(c) Workflow lock-in / integrations** | Yes | Partly | **No** — requires engineering you don't have |
| **(d) Legal / registry status** | **Yes — structurally** | **Yes** | **YES. This is the one.** |
| **(e) Accountability / liability transfer** | **Yes** | Yes | **YES — this is what a service sells** |

**Evidence that (a) gets you killed:**

- **Chegg.** Q1 2026 revenue **US$63.3m, down 48% YoY**; Academic Services **down 57% to US$45.7m**;
  **45% of workforce cut, 27 Oct 2025**, after a 22% cut in May 2025; stock **down ~99%** from a
  US$14bn peak — with the company itself attributing it to "the new realities of AI" and Google AI
  Overviews ([CNBC 27 Oct 2025](https://www.cnbc.com/2025/10/27/chegg-slashes-45percent-of-workforce-blames-new-realities-of-ai.html),
  [Chegg 10-Q via StockTitan](https://www.stocktitan.net/sec-filings/CHGG/10-q-chegg-inc-quarterly-earnings-report-a76e084cb71a.html),
  [Forbes 29 Oct 2025](https://www.forbes.com/sites/petercohan/2025/10/29/chegg-stock-down-99-learn-whether-ai-45-layoffs-make-chgg-a-buy/)).
  This is the canonical case with SEC-filed numbers, not blog commentary.
- **Document Crunch → Trimble (Apr 2026)** and **Procore bundling contract review (Jul 2026)** — the
  incumbent-absorption case, in this client's exact adjacency, twice in one year.
- **Bidhive → Responsive (May 2025)** — the same, in the exact category the client is drawn to.

I deliberately discarded the widely-circulating "**2,000 AI agencies in 2024 → 12,000 in 2026**"
and "**99% of AI startups dead by 2026**" claims. Both trace to marketing blogs with no
methodology ([ciela.ai](https://ciela.ai/blogs/is-ai-agency-market-saturated-reddit),
[skooloflife on Medium](https://skooloflife.medium.com/99-of-ai-startups-will-be-dead-by-2026-heres-why-bfc974edd968)).
**Directionally suggestive of saturation; not citable as fact.**

**Ranked opportunity durability for THIS operator:**

| # | Opportunity | Moat class | Durability | Verdict |
|---|---|---|---|---|
| **1** | **Indigenous-owned bid/tender + IPP participation-plan service, AI-leveraged** | **(d) + (e)** | **High** | **DO THIS** |
| 2 | Won-bid content corpus built *while* delivering #1, later productised | (b), earned slowly | Medium | Do as a by-product, never as the plan |
| 3 | AI-use policy / declaration artefacts for tenderers (Dec 2026 forcing function) | (e), small | Medium-low | Small upsell, real |
| 4 | Agentic workflow automation for the same clients | (c), weak | Low | Upsell only, never the business |
| 5 | Generic AI implementation consulting for SMEs | (a) | **Low** | Filler income at best |
| 6 | Fractional AI officer | reputation | Low now | Not for 12–24 months — no track record |
| 7 | Construction AI SaaS | (b)/(c) — unavailable | **Zero** | **Do not enter** |
| 8 | Data labelling / dataset creation | none | **Zero** | No. Offshore price floor, lab procurement cycles |

---

## 6. THE NUMBERS — bottom-up, attack the inputs

### 6.1 What a solo AI-leveraged bid writer actually earns (per-tender model)

| Input | Value | Basis |
|---|---|---|
| Working days/yr | 220 | standard |
| Delivery utilisation (solo must also sell) | **50–55% → ~115 delivery days** | `[ESTIMATE]` |
| Days per tender **with AI leverage** | **~2.5 avg** (1.5 small / 3 medium / 6 major) | `[ESTIMATE]` — derived: A$4–8k ÷ A$165/hr ≈ 24–48 billable hrs = 3–6 days pre-AI; AI compresses drafting, not interviews or review |
| Tenders/yr at steady state | **~46 theoretical → 35–45 realistic** | allowance for abandoned/lost pursuits |
| Average fee | **A$5,000** | midpoint of A$4–8k band, discounted for smaller Indigenous-SME clients |
| **Year 1 (ramping from zero clients)** | **18–25 tenders → A$90k–125k** | |
| **Year 2 (steady state, solo)** | **35–45 tenders → A$175k–225k** | |
| Direct costs | **~A$10k/yr** (AI tooling A$200–500/mo; PI insurance A$1.5–3k; portals/subs A$1.5–3k) | `[ESTIMATE]` |

**Answer to "cash in 12 months": yes — roughly A$90–125k gross in year one, from a standing start,
with near-zero cash CAC.** That is the single strongest argument for this path over anything else
in the assignment.

### 6.2 The model that actually creates enterprise value (retainer)

Per-tender is a sales treadmill: you re-sell every engagement. Convert to **"bid function as a
service"**: **A$3,000–6,000/month** covering opportunity screening (AusTender + state portals),
bid/no-bid triage, content-library maintenance, and 1–2 submissions/month.

- **8 retainers × A$4,000/mo = A$384k/yr** — above the per-tender solo ceiling, because it kills the
  per-engagement sales cost.
- **The pitch:** an in-house bid coordinator costs roughly **A$90–130k + on-costs** `[ESTIMATE —
  NOT VERIFIED this session]`. A A$48k/yr retainer is under half, with no leave and no recruitment.
- **A retainer book is saleable. A per-tender pipeline is not.**

### 6.3 Serviceable market for the retainer model

| Step | Count | Reasoning |
|---|---|---|
| Indigenous businesses winning Commonwealth contracts | **1,200+** | NIAA, FY2024-25 |
| — of which can sustain A$48k/yr (top decile by revenue) | **~120** | `[ESTIMATE]` — avg contract A$123k means most cannot |
| + state/local Indigenous procurement uplift (~+50%) | **~180** | `[ESTIMATE]` |
| ANZ civil firms with ≥5 employees | **4,868** | prior round, two independent methods |
| — subset bidding public work above participation thresholds (~10%) | **~490** | `[ESTIMATE]` |
| **Total addressable** | **~670 firms** | |
| Realistic 5-yr attach for a 3–5 person consultancy | **2–4% → 13–27 clients** | `[ESTIMATE]` |
| **Ceiling: 20 retainers × A$48k** | **≈ A$960k/yr** | |

**That is the honest ceiling: ~A$1m/yr services revenue with 3–5 people.** Attack the inputs: the
top-decile assumption (120) and the 10% prime-contractor subset (490) are the two soft numbers.
If the top decile is really the top 5%, the ceiling halves.

### 6.4 And the productisation ceiling, so nobody is surprised later

670 addressable firms × 25% penetration × A$6,000/yr = **~A$1.0m ARR.** Same wall Vaultry hit
(A$22m SAM, `research/raw/03-market-size.md`), same wall **Bidhive actually hit in reality**.
**An Australia-only vertical bid-tech SaaS caps at roughly A$1–5m ARR.** A large outcome requires
either export (the UK Social Value Model and Canada's 5% Indigenous procurement target are the
structurally analogous regimes — **not researched this session**) or a trade sale to
Responsive / EstimateOne / Felix at a services multiple. **Probability of a venture-scale outcome:
low single digits. Say this to the client's face.**

---

## 7. DISTRIBUTION — how the first 20 customers are reached, and what it costs

Not 100 customers. **20.** That is the whole business.

| # | Channel | Cost | Why it works |
|---|---|---|---|
| **1** | **AusTender contract notices** — every Indigenous business that won a Commonwealth contract in the last 12 months is a **named, public, free lead with a proven bidding habit and a proven budget** | **A$0** | [tenders.gov.au/cn/search](https://www.tenders.gov.au/cn/search). This is the best free lead list in the country for this offer. |
| **2** | **Supply Nation Indigenous Business Direct + Connect trade show** — corporate and government buyers come looking **for you** | Membership/exhibition **not verified** | [connect.supplynation.org.au](https://connect.supplynation.org.au/supplier-diversity-awards-2026/) |
| **3** | **State prequalification registers** (NSW Public Works schemes, QLD PQC, VicRoads) — named civil contractors with public-work habits | A$0 | prior round, `02-demand-channels.md` |
| **4** | **Direct to bid managers at mid-tier civil primes** (Fulton Hogan, BMD, Seymour Whyte, Georgiou, Shamrock) for the **Indigenous Participation Plan module** | A$0 + time | This is Buyer B — the one with budget |
| **5** | Referral from accountants/lawyers servicing Indigenous businesses | A$0 | |

**CAC:** at ~20% meeting rate and ~15% close, **~35 conversations per client, ~10 founder-hours,
≈A$0 cash** `[ESTIMATE]`. **Near-zero cash CAC is the entire reason this fits <A$50k of capital and
Vaultry did not.**

---

## 8. GRANTS AND NON-DILUTIVE FUNDING — mostly a trap, and here is what I could and could not verify

### 8.1 Verified this session

| Programme | Status as at Sep 2026 | Detail | Source |
|---|---|---|---|
| **R&D Tax Incentive** | **Live** | Aggregated turnover **<A$20m → refundable offset = company tax rate + 18.5% premium** (≈**43.5%** for a 25% base-rate entity). **Minimum A$20,000** notional R&D deductions. **Registration deadline: 10 months after income year end — absolute, no discretion to extend.** Software claims are an explicit ATO/AusIndustry focus requiring contemporaneous technical documentation. | [ATO](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/incentives-and-concessions/research-and-development-tax-incentive/r-d-tax-incentive-rates-and-entitlements/rates-of-r-d-tax-incentive-offset), [business.gov.au](https://business.gov.au/grants-and-programs/research-and-development-tax-incentive/apply-to-register-with-the-randd-tax-incentive) |
| **Entrepreneurs' Programme** | **CLOSED** | Replaced by the Industry Growth Program | [industry.gov.au](https://www.industry.gov.au/science-technology-and-innovation/industry-innovation/industry-growth-program) |
| **Industry Growth Program** | **ON HOLD for new applicants and pipeline applicants** following the **2026–27 Federal Budget**; funding **cut by A$102m**; not confirmed whether it will restart, be replaced or be cancelled | Eligibility (when open): turnover <A$20m for each of 3 prior FYs, ABN, NRF priority sectors | [fundfindrs](https://fundfindrs.com.au/industry-growth-program-igp-whats-changed-what-matters-and-who-should-apply/) **[SEARCH-SUMMARY — verify]** |

**The honest read on the R&D Tax Incentive: it is not funding, it is a reimbursement.** It refunds
43.5% of money **already spent**, arriving **9–18 months later**, and **unpaid founder labour is not
claimable** — you must actually pay salaries or contractors. For an operator with <A$50k it is a
year-two mechanism, not runway. It also requires a **company** structure and A$20k+ of genuinely
eligible experimental activity. Writing bids with an LLM is **not** eligible R&D.

### 8.2 NOT VERIFIED — do not plan around these until checked

Search budget was exhausted and every government domain was egress-blocked. I will not fill these
with plausible numbers.

| Programme | What must be established | Where to check |
|---|---|---|
| **IBA business finance** (Indigenous Business Australia) | Current loan minimums/maximums, concessional rate, equity/deposit requirement, whether a solo services startup qualifies | iba.gov.au — **call them; a 20-minute phone call beats a week of desk research** |
| **Indigenous Entrepreneurs Fund** | **Whether it still exists in 2026** and whether services businesses (vs capital equipment) are in scope | niaa.gov.au |
| **Export Market Development Grants (EMDG)** | Round status for 2026–27, tier amounts, whether services exports qualify, application window | austrade.gov.au / business.gov.au |
| **State innovation grants** (NSW MVP Ventures, QLD Ignite Ideas, Vic, SA/WA equivalents) | Open/closed status, amounts, whether a services business qualifies at all | each state's business portal |
| **Supply Nation** membership/certification fees and Connect exhibition cost | Cash cost of the distribution channel in §7 | supplynation.org.au |

### 8.3 The grant advice the client will not get elsewhere

**Grant-chasing is negative expected value for this operator.** A A$30,000 grant application costs
~40 founder-hours at perhaps a 20% hit rate = **EV ≈ A$150/hour**. Forty hours spent selling bid
services at a 15% close rate on a A$5,000 fee across ~4 prospects returns **EV ≈ A$75–190/hour**
*and* produces a client, a reference, a case study and a content library asset that compounds
`[ESTIMATE — attack these conversion assumptions]`. **The grant produces cash once and a
relationship never.** The only exception worth the time: **IBA finance**, because it is Indigenous-
specific, relationship-based, and the client is unusually well-positioned in a small applicant pool.

---

## 9. KILL SHOTS — ranked by probability

1. **The client's own IPP eligibility fails (probability: unknown, impact: total, deadline: passed
   1 Jul 2026 with transition).** Supply Nation **"Registered"** is the 50% tier. The IPP now
   requires **51%+ owned *and controlled***. If the entity is a 50/50 structure, or Indigenous
   control cannot be evidenced, **every argument in this memo evaporates.** Resolve in week one.
   Nothing else matters until this is answered in writing.
2. **No budget in the Indigenous-SME segment (~high).** Average IPP contract A$123k. A firm winning
   two a year cannot pay A$48k/yr. **If the client sells only to Buyer A, this is Vaultry with a new
   coat of paint: acute pain, no budget line.** The business only works if Buyer B — the primes with
   real bid budgets — is at least half the book.
3. **Solo utilisation collapse (~medium-high, chronic).** Tender deadlines are non-negotiable and
   clustered. One person cannot sell and deliver in the same fortnight. The first big win eats the
   pipeline; the pipeline dies; three months later revenue is zero. **This kills more solo
   consultancies than competition does.** The retainer model in §6.2 is the specific structural
   defence — it smooths delivery and pre-sells capacity.
4. **Fee compression as clients adopt AI themselves (~medium, 2–4 years).** The A$5,000 fee is
   priced on hours. Defence: migrate value to win-strategy, evaluator insight, accountability and
   Indigenous-participation credibility. Only the last one is genuinely uncompressible.
5. **Black-cladding enforcement (~medium, rising).** Government has stated intent to act on
   "disingenuous conduct." Scaling by fronting non-Indigenous delivery labour makes this business
   the test case. **This is a hard cap on headcount scaling and therefore on the exit.**
6. **Incumbent/model absorption (~low for the service, ~certain for any software).** Chegg −48%
   revenue, −45% headcount. Document Crunch absorbed by Trimble. Procore bundling contract review
   and bidding agents. Bidhive absorbed by Responsive. **Cheaper models make the *service* more
   profitable and make the *software* worthless. Choose accordingly.**

---

## 10. CHEAPEST NEXT TEST — 30 days, under A$2,000

**Test 1 — the eligibility gate. A$0, 3 days. Run this before anything else.**
Get written confirmation from Supply Nation and NIAA that the entity meets the post-1-July-2026
**51%-owned-and-controlled** test, and upgrade Registered → **Certified** if the structure allows.
**Stop condition:** if it does not and cannot be restructured, **discard this memo's core thesis**
and re-scope to generic bid writing, where the client has domain knowledge but no edge — a
materially worse business.

**Test 2 — the budget test. A$0–500, 3 weeks. Twelve conversations.**
Six with Indigenous civil/facilities businesses that have won Commonwealth contracts — **pull the
names free from [AusTender contract notices](https://www.tenders.gov.au/cn/search)**. Six with bid
managers at mid-tier civil primes.
- To Buyer A: *"What did your last tender cost you in hours and cash, and who actually wrote it?"*
- To Buyer B: *"Who writes your Indigenous Participation Plan section, and what line does it come
  out of?"*
**Stop condition:** **if fewer than 3 of 12 can name a dollar figure they already spend, there is no
budget line and this is Vaultry again.** Walk.

**Test 3 — the revenue test. A$300–1,000, 2 weeks. This is the one that matters.**
Do not run a landing-page test. **Win one paid engagement.** Offer a live tender response at
**A$2,000 fixed + A$3,000 on award**, plus a **A$1,500 Indigenous Participation Plan module**, to
the same list. The success-weighted structure de-risks the client's first purchase and prices your
inexperience honestly.
**Stop condition:** **zero paid engagements from 20 qualified conversations in 30 days = the buyer,
the price or the offer is wrong.** One signed engagement = revenue, a case study, a reference, and
the first entries in the content corpus that becomes the only real asset here.

**What NOT to do in the next 30 days:** do not write a line of product code, do not apply for a
grant, do not build a landing page, do not register a domain for a SaaS. Every one of those is a
way of avoiding Test 3.

---

## 11. WHAT I COULD NOT ESTABLISH

Recorded so nobody mistakes silence for absence of risk.

- **Any non-vendor measurement of Australian bid-writing fee movement 2023→2026.** The single most
  important number for kill-shot #4. **Not found — and it may not exist publicly.** Measure it by
  asking five bid consultancies for a quote on an identical scope.
- **Bidhive acquisition price, total funding raised, and revenue verified from a primary source.**
  Revenue figures are getlatka estimates. **Low confidence.** SmartCompany was egress-blocked.
- **Buildots, OpenSpace, Dusty Robotics, Versatile** — assignment items not reached before the
  search budget ran out. **Not found.**
- **IBA finance terms, Indigenous Entrepreneurs Fund status, EMDG 2026 round status, state grant
  status, Supply Nation fees.** All egress-blocked. §8.2 lists the check.
- **Australian in-house bid coordinator salary**, which anchors the retainer pitch in §6.2.
  **Estimated, not verified.**
- **UK Social Value Model and Canada's 5% Indigenous procurement target** as export analogues — the
  only credible route to a large outcome. **Not researched.** Worth one hour before any investor
  conversation.
- **Whether the ~120 top-decile figure in §6.3 is right.** It is the load-bearing estimate in the
  market size. AusTender supplier-level data could settle it in an afternoon.

