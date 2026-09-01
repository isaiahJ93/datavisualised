# Methodology and limitations

## How this research was produced

Five Hermes agents ran in parallel, one per research front (incumbents, demand
channels, market size, business model, regulation). Each was instructed to falsify
before validating, to size bottom-up from counted units, and to attach a source and
date to every material claim.

## Hard constraint: no primary sources were opened

This session's network egress policy blocked **all** direct page fetches. Confirmed
against the proxy status endpoint, which logged 403 CONNECT denials for, among others:

- `www.abs.gov.au` and `api.data.abs.gov.au` (the primary business-count source)
- `estimateone.com`, `iseekplant.com.au`, `www.totika.co.nz`
- `www.afr.com`, `en.wikipedia.org`
- vendor pricing pages (`cm3.com.au`, `linksafe.com.au`, `avetta.com`)

Web *search* worked; web *fetch* did not. Every figure in these memos therefore comes
from search-engine result synthesis, not from reading the source document. This was not
worked around — the policy denial was reported rather than bypassed.

## What that means for confidence

| Claim type | Confidence | Why |
| --- | --- | --- |
| Vendor exists, positioning, who it sells to | **High** | Consistently described across many independent results |
| Ownership, acquisitions, funding events | **High** | Widely reported news events, cross-referenced |
| Published list prices | **Medium** | Read from result snippets, not the live pricing page; may be stale or tier-dependent |
| ABS/Stats NZ unit counts | **Medium-Low** | Primary source unreachable; figures are second-hand |
| Anything about how many platforms a typical sub pays for | **Low — unverified** | No survey, submission or inquiry evidence found to exist |

## The one number that decides the venture

No source was found quantifying how many separate compliance platforms a typical ANZ
civil subcontractor pays for, or what that costs per year. The working estimate of 3-5
platforms is **inference, not measurement**. The entire "aggregate the compliance tax"
thesis rests on it.

This is not a gap to be closed with more desk research — the data does not appear to
exist publicly. It has to be measured by calling subcontractors. That is why the
recommended next step in every memo is primary interviews, not further reading.
