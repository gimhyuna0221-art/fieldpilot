# Market Research Capability Catalog — dynamic broker examples

Purpose: help FieldPilot decide **which capability to seek**, not hardcode a permanent winner.
Examples below are discovered current-market candidates and must be re-verified for active
features, coverage, price, access and terms at execution time.

| Capability class | Current examples to inspect | Typical use | Important limit |
|---|---|---|---|
| Survey build / logic / collectors | SurveyMonkey, Qualtrics, Typeform | questionnaire logic, branching, piping, randomization, collectors, exports | tool capability != valid research design |
| Panel / participant recruitment | SurveyMonkey Audience, Prolific, Pollfish | access to defined respondents/participants | panel composition/selection and target-population fit must be disclosed |
| Consumer / audience intelligence | GWI, SparkToro, Statista Consumer Insights | demographics, behaviors, media/attention, audience hypotheses | provider methodology, geography and denominator differ |
| Market/category databases | official statistics, trade bodies, Statista-style market databases, specialist research firms | market magnitude, forecasts, industry structure | estimates can conflict; preserve definitions/method |
| Digital competitive intelligence | Similarweb, Semrush | traffic/share-of-traffic, acquisition channels, keywords, digital competitors | modeled digital activity != total company revenue/demand |
| Social/consumer listening | Brandwatch and comparable services | public conversation, themes, trend/social signal | social participants != target population; sentiment model limits |
| Web/multi-channel retrieval | native search/connectors, Firecrawl, Agent Reach/upstream routes | fetch/search/extract multi-source evidence | access != truth; platform terms/login/privacy matter |
| Deep research/report synthesis | current capable host, GPT Researcher-style runtimes, STORM-style systems | question planning, broad retrieval, cited synthesis | breadth != market-research validity; keep evidence claim ceilings |
| Decision challenge/council | FieldPilot Decision Council, role-based board tools | expose trade-offs/blind spots | interpretation != independent market evidence |
| Synthetic scenario stress | FieldPilot Scenario Stress, simulation systems | second-order reaction hypotheses | synthetic != observed demand/forecast |
| Product analytics | Mixpanel, Google Analytics, Amplitude | event definitions, ordered funnels, paths, retention, cohorts | different units/windows/identity rules produce different answers; use PRODUCT_ANALYTICS_EXECUTION |
| Specialist statistical research | JMP, Quantilope, Qualtrics | designed experiments, conjoint, MaxDiff, segmentation, drivers | valid design and actual estimation required; use SPECIALIST_ANALYSIS_EXECUTION |
| Qualitative evidence grid | Insight7 and comparable tools | same questions across interviews with traceable quotes and negative cases | requires authorized source transcripts; automated coding is not verified prevalence |
| Predictive modeling | Pecan and task-fit statistical runtimes | target/horizon definition, held-out evaluation, baseline comparison | unavailable labels/runtime means design only, never a generated forecast sold as measured accuracy |
| Korean consumer research and recruitment | OpenSurvey, Pickply, verified local research providers | local instrument design, survey collection or participant recruitment | separate recruitment, completion and valid records; use LOCAL_AND_EXPERT_RESEARCH |
| Integrated fieldwork/research products | Ipsos Digital, Quantilope and task-fit research firms | question-design-collection-analysis handoff | proprietary indices and panels are not FieldPilot-owned methods or data |
| Search intent and relationships | ListeningMind, Semrush, task-fit search tools | intent clusters, temporal comparisons, query relations | query volume/relatedness is not people or purchase paths; use SEARCH_AND_COMMERCE_EVIDENCE |
| Competitive changes and battlecards | Crayon, authorized snapshots and CRM exports | source changes tied to affected comparisons and decisions | a scheduled update exists only with a configured authorized runtime |
| Seller and listing intelligence | SellingBooster, authorized store exports | comparable prices, listing history, reconciled seller metrics, CS patterns | no store connection, profit or causality inferred from marketing claims |
| Industry report discovery | Reportlinker, Statista, official/public specialist reports | comparable definitions, date/country/category filters, report selection | paywall metadata is not the report; do not average incompatible estimates |

These added classes route through the matching conditional modules in SKILL.md. The development
source register records inspection limits; at execution time recheck volatile capabilities.

## Selection contract

For the active job:
1. name the evidence/analysis capability actually needed;
2. discover current candidates;
3. inspect official scope and, where possible, actual output;
4. compare category/geography/period/method/access/cost/user effort;
5. reuse the strongest adequate authorized route;
6. preserve alternatives and gaps;
7. never call one platform globally best without comparable evidence.

## Build-vs-broker rule

FieldPilot should **not rebuild**:
- respondent panels;
- enterprise survey hosting/SSO;
- email/SMS delivery infrastructure;
- proprietary clickstream/consumer databases;
- large social-firehose archives;
- CRM/BI integrations already better provided elsewhere.

FieldPilot's product layer is research design + source/service brokerage + evidence QA + synthesis +
decision support + professional deliverable. Integrate or hand off to specialist infrastructure
when that is the stronger route.
