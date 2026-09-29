# General Deep Research vs FieldPilot — development comparison (2026-09-29)

## Purpose

Record the product-development signal from a same-topic comparison so the resulting runtime change has durable provenance.

Topic used in the comparison: remote PC power-on programs/services.

This is **not** a controlled model benchmark. The two outputs differed in workflow, context, prompt history, tools, time and source volume. Treat it as design evidence only.

## What the general deep-research output did better

The general report was substantially stronger at broad industry orientation:

- market boundary: remote power-on was placed inside larger remote-desktop and KVM-over-IP markets rather than treated as a clean standalone market;
- market magnitude/growth: multiple market-research estimates were compared, including disagreement/ranges;
- vendor landscape: free WOL, remote-control SaaS, dedicated power hardware, IP-KVM and enterprise management layers were mapped;
- enterprise alternatives: Intel vPro/AMT, BMC, SCCM/Intune and VPN/WOL relay approaches were included;
- company/industry context: major vendor results, market-position evidence and product-line economics were investigated;
- security/technology context: IP-KVM vulnerabilities and cloud/platform shifts were surfaced;
- the output retained more industry facts useful for an analyst who wanted a broad landscape.
## What FieldPilot did better

The FieldPilot output was stronger at turning research into a user decision:

- it reframed competitors as every way the user can solve the job, including free/bundled/cloud/no-build alternatives;
- it connected the answer to the user's likely setup and immediate use case;
- it distinguished an interesting problem from evidence that customers will pay;
- it treated platform-side cloud execution as a substitute that could shrink the need to wake a PC;
- it used a stronger HOLD discipline rather than manufacturing an entry recommendation from category breadth;
- it converted the residual uncertainty into a low-cost real test instead of ending with more research;
- it exposed what was unverified instead of treating searched-not-found as whitespace.

## Product implication

Do not replace FieldPilot's decision-first architecture with a generic deep-research report.

Instead add an **industry-depth backstop** so broad category/commercial questions cannot finalize before checking whether general deep research would reveal a material missing layer.

Target combination:

```text
FieldPilot signature
reference-first
+ job/substitute map
+ claim ceilings
+ build/change/hold
+ one next action

PLUS

general deep-research strength
market boundary/structure
+ supportable magnitude/growth
+ vendor/price ladder
+ enterprise/infrastructure alternatives
+ security/regulation/technology shifts
+ local/global context
```
## Design rule

The breadth layer must be conditional.

A narrow price/feature/source question must stay narrow.

A broad category/viability/commercialization question receives at least a compact industry backstop when industry structure can change the decision.

Escalate to deeper industry research only when the compact sweep finds a contradiction or structural factor capable of reversing the recommendation.

This avoids two failures:

1. **FieldPilot-too-narrow:** excellent HOLD/next-action advice while missing an important industry layer a strong general researcher would have found.
2. **FieldPilot-too-bloated:** every simple builder question becoming a 50-page industry report.

## Claim ceiling

This comparison does not prove:

- FieldPilot is generally better at decisions;
- general deep research is generally better at market coverage;
- either workflow produces higher commercial outcomes;
- more sources cause better decisions;
- the new backstop improves customer willingness to pay.

Those require clean-session evaluation across multiple tasks.

## Implementation

Runtime module:
- `references/modules/INDUSTRY_DEPTH_BACKSTOP.md`

Contract test:
- `tests/test_industry_depth_backstop_contract.py`

The module reuses existing sizing, secondary/competitor, market-prior, local/expert, trend and regulatory methods. It does not create a second research methodology.
