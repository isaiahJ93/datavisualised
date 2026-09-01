# Vaultry — market research

Research workspace for **Vaultry**: a product for civil-construction subcontractors in
Australia and New Zealand covering (a) winning work and (b) managing documents and
compliance.

## Layout

| Path | What it is |
| --- | --- |
| `.claude/agents/hermes.md` | **Hermes** — the adversarial market-research analyst profile. Falsifies before it validates, sizes bottom-up, cites everything. |
| `research/raw/` | Raw research memos, one per front (incumbents, demand channels, market size, business model, regulation). |
| `research/vaultry-market-assessment.md` | The synthesised verdict. |

## Scope of this round

- **Market:** Australia / New Zealand
- **Segment:** civil construction (roads, rail, water, utilities, earthworks) — not residential
- **Stage assumed:** prototype / MVP, pre-revenue
- **Question:** is the gap real, who pays, and what is the honest ceiling?

## Running Hermes again

```
Use the Agent tool with .claude/agents/hermes.md as the operating profile,
one agent per research front, and have each write its memo to research/raw/.
```
