# Product analytics execution

Load for event data, funnel/cohort/retention analysis or a measurement gap that changes a product decision. Reuse BEHAVIORAL_ANALYTICS in `references/methods/concept-usability-behavior.md` and `RESEARCH_ANALYSIS_COMPILER.md`. Do not force this module onto an idea without usage data.

## 1. Establish what the events actually measure

Before computing, record the unit (person, account, session or event), identifier mapping, timezone, observation cutoff, eligibility, internal/test traffic, bot filters, consent limits and event definitions. Inspect supplied schema and rows first. A missing event can mean missing instrumentation, not missing behavior.

Define a compact measurement contract:

```text
business question -> eligible unit -> exposure/entry event -> ordered outcome events
-> conversion window -> observation cutoff -> exclusions -> decision implication
```

Keep an event dictionary: name, trigger, required properties, source system, timestamp semantics, unique event key and known gaps. Reconcile duplicates by stable event ID; identical IDs with conflicting payloads are a data error, not an arbitrary row to discard. Do not join anonymous and logged-in IDs without a supplied or verified identity mapping. Never infer people from pageviews.

## 2. Compute with auditable denominators

- For a closed ordered funnel, a later stage qualifies only after its preceding stage for the same eligible unit within the specified window. For an open funnel, explicitly define allowed entry stages, entry assignment and denominators; enforce sequence only after that unit's allowed entry, not before it. A payment before signup does not count as a post-signup conversion. Explain whether simultaneous timestamps can be ordered by an actual sequence key.
- Freeze first-entry versus repeated-attempt counting, closed versus open funnel, intervening events and any property held constant (for example, the same product). An open funnel or path exploration answers a different question from a closed signup cohort. Never silently change the count mode to improve conversion.
- Separate entry-cohort size, fully observable size, reached-stage counts and each conversion denominator. A cohort that has not had the full conversion window is right-censored; do not call it a failed conversion.
- Retention requires a stated return event and interval: exact day/week, rolling return or unbounded return are different metrics. Separately fix calendar-date versus elapsed-24-hour boundaries, timezone, Day 0 convention and inclusive/exclusive endpoints. Keep first-use cohort and returning activity separate. Compare cohorts at the same maturity under the chosen return definition.
- Distinguish unique buyers, orders, gross revenue, discounts, refunds and net revenue. Currency, tax, accounting recognition and contribution margin need their own definitions. Do not call gross sales profit.
- Report raw counts and uncertainty with percentages. Tiny samples can show where to inspect, not establish a dominant cause. Acquisition attribution is not incremental causal impact.
- Use local scripts or authorized analytics exports for reproducible calculations. Save transformation, exclusions and a reconciliation table. No guessed statistical significance.

## 3. Specialist platform bridge

For authorized, already eligibility-filtered CSV data matching the limited local contract,
`tools/product_event_analysis.py` computes a closed, first-entry, strictly ordered funnel and
exact elapsed-24-hour-day retention. Read its help before use. Input columns are exactly
`event_id,unit_id,event,timestamp`; config fields are `steps,window_hours,cutoff,retention_event,retention_day`.
Duplicate IDs with conflicting payloads fail instead of guessing. It emits counts, denominators,
per-unit reconciliation and censored records. It does not compute open funnels, session metrics,
calendar-day retention, identity stitching, product-property constraints or revenue.

```text
python tools/product_event_analysis.py --events events.csv --config config.json --out result.json
```

The included `tests/competitor_coverage` example is synthetic, not a customer result. If the
requested definition differs, use a suitable authorized platform or separately verified
calculation; never silently replace the requested definition with this helper's mode.

For Mixpanel, Amplitude, Google Analytics or another current provider, inspect the specific event, funnel, identity, retention and export capability needed. Record export limits, sampling/thresholding where applicable and whether the supplied data matches the UI metric definition. A platform screenshot without the metric definition is insufficient for a precise comparison.

If no connected authorized account exists, analyze provided exports or create a ready-to-implement measurement specification. Do not claim the SDK was installed, a dashboard was created or instrumentation was repaired. Any app implementation is a handoff to the builder, with events and acceptance checks, not an unauthorized edit to the user's app.

## 4. Deliver only what changes the decision

Provide the observed bottleneck with counts, measurement limitations, competing explanations and one next action. For a file request deliver the funnel/cohort table, event-definition sheet and calculation notes. Missing critical data gets an explicit gap and the smallest retrieval/instrumentation handoff; continue the bounded diagnosis.

Do not read customer exports into external services without authority. This module does not grant access to competitors' private events or implement a new analytics SaaS.
