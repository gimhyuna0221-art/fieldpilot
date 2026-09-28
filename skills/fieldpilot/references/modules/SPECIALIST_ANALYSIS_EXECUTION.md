# Specialist analysis execution

Load only when the active question warrants specialist statistics, qualitative synthesis or forecasting. Reuse the matching method card and `RESEARCH_ANALYSIS_COMPILER.md`; the provider does not select the method.

## Choose, execute and check

For each analysis, preserve: question, estimand/construct, unit, design, data dictionary, missingness, assumptions, tool/algorithm/version, parameters, reproducible steps, output and limitations. Separate a designed analysis from a computed result. If execution is unavailable, deliver an executable specification and a bounded descriptive answer, never invented coefficients or tests.

| Job | Input and execution requirements | Acceptable output and hard limit |
|---|---|---|
| Conjoint or choice modeling | designed attributes/levels and shown profiles/tasks with respondent/task IDs; choice models need actual shown alternatives and choices, while other conjoint variants need their corresponding profile ratings or rankings; inspect design identifiability and burden | utilities/relative importance with model and uncertainty only after estimation; an ordinary liking question without a designed conjoint task is not conjoint data or market share |
| MaxDiff | actual shown sets, best/worst selections, respondent/task IDs and exposure counts; evaluate coverage, balance and identifiability rather than presuming them | method-specific score and uncertainty; do not compute from a plain rating question as if equivalent |
| Segmentation or latent classes | task-relevant features, missingness/scaling, size, stability and interpretable differences; compare simpler alternatives | labeled candidate segments and validation; arbitrary clusters are not proven buyer groups |
| Experiment/causal estimate | assignment mechanism, eligible/exposed units, unit of randomization, outcome window, interference, missing outcomes, analysis plan | effect, uncertainty and practical decision; before/after alone is not randomized impact |
| Predictive forecast | timestamped target with horizon, features available at prediction time, time-based holdout, leakage audit, naive baseline, drift/retraining plan | holdout performance and calibration where applicable; no performance claim from in-sample fit or future information |
| Qualitative synthesis | original transcript/response IDs, question context, speaker anonymization and quote locators, codebook and discrepant cases | traceable themes, evidence excerpts, negative cases and recommendations; AI sentiment is a hypothesis to audit, not a representative prevalence estimate |

Use the existing survey, pricing, sizing, qualitative and experiment cards for design specifics. JMP, Qualtrics Stats iQ/Text iQ, Quantilope, Insight7 or Pecan are replaceable provider candidates when their verified current scope fits. A marketing page only establishes advertised capability; inspect a relevant output or authorized test before claiming task performance. Never suggest upload of confidential transcripts or event data without permission.

For prediction, record prediction time, feature window, outcome window, collection delay and
data cutoff separately. A target whose outcome window or reporting delay has not ended is not
automatically a negative label. Ordinary holdout scores use finalized outcomes; any censoring-aware
alternative needs its own stated method and assumptions. Report total, evaluable and immature
excluded counts. Time-based splitting alone does not settle outcome maturity.

When choosing among the advanced methods listed in the supplied references, load
`references/modules/ADVANCED_METHOD_HANDOFF_MATRIX.md` for the specific method's input,
diagnostics and execution boundary. Do not load every advanced method for ordinary summaries.

## Method details that often get lost in a generic report

- For designed experiments, record controllable factors and levels, forbidden combinations, hard-to-change factors, blocks, randomization unit, replication and resource constraints. Compare feasible candidate designs for identifiable effects and aliasing/power where actually computable. Do not manufacture design diagnostics when the required engine is absent.
- For cross-interview analysis, use interviews as rows and common research questions as columns; bind each cell to the original speaker/record and excerpt position. Preserve contradictory and ambiguous cases, with AI-coded and human-reviewed states separate.
- Distinguish reach, recall, attitude, stated preference, reaction time and actual purchase when selecting concept, ad or implicit tests. TURF needs measured item-level reach/choice and a defined optimization objective; an implicit association task needs a controlled timing design. Do not substitute an ordinary survey for either or reproduce a proprietary score without its definition and rights.
- For time series: mark seasonality, structural breaks, autocorrelation and observation frequency. Backtest with past-to-future splits; do not shuffle observations then advertise future forecasting quality.
- For narrative analysis: retain chronology and how the speaker constructs meaning, rather than turning every interview into keyword counts.
- For mystery shopping or observation: predefine scenario, observable checklist, place/time and observer consistency. Do not impersonate customers deceptively, fabricate a field visit or make purchases without authority. Report observed service behavior, not private motives.
- For a requested specialist estimate outside available runtime capability, find an appropriate service and produce the exact input/output acceptance brief. Do not spend money or install an unreviewed analysis package merely to avoid admitting a limitation.

Deliver the useful result or a precise evidence gap, not a list of every possible statistical technique. Supplying a provider name is not execution. A successful calculation is not external customer validation.
