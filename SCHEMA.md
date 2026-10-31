# Schema

The library has two record types. `data/studies.json` is a JSON array of study records and `data/resources.json` is a JSON array of resource records. The CSV files are generated from the JSON by `build/build.py`; edit the JSON, not the CSV.

## What counts as a study

An empirical AI safety or alignment study that:

1. the field cites as load-bearing evidence, or that makes a strong training replication; and
2. publishes enough detail to attempt a replication (code, data, prompts, or a detailed method).

Failed, conditional and contested replications are included on purpose.

## Study record

| Field | Type | Rules |
|---|---|---|
| id | string | lowercase slug, short-name-year, e.g. `alignment-faking-2024`; unique |
| short_name | string | label for compact displays, e.g. "Alignment faking 2024"; generated from the id when empty |
| title | string | exact paper title |
| authors | string | "Surname et al." for 4 or more authors; all surnames for 1 to 3 |
| year | integer | year of first public version |
| organisation | string | main lab(s) or institution(s) |
| paper_url | string | canonical link (arXiv abstract page, official paper or blog page) |
| category | enum | one of the category values below |
| core_claim | string | what the study claims, including the conditions (models, setting, prompts) under which it was shown; 1 to 3 sentences |
| claim_types | array of enum | one or more of `existence`, `prevalence`, `magnitude`, `mechanism`, `ranking`, `method` |
| original_models | array of strings | models used in the original study |
| model_access | enum | `open-weight`, `API-only`, `mixed` |
| models_still_available | enum | `yes`, `partly`, `no`, `unknown` |
| code_url | string | official code repository, or empty |
| data_url | string | released dataset or prompts, or empty |
| tooling | string | e.g. Inspect, TransformerLens, custom PyTorch, lm-evaluation-harness, API scripts |
| compute_tier | enum | `T0`, `T1`, `T2`, `T3` (see below) |
| compute_note | string | basis for the tier; one sentence |
| difficulty | enum | `starter`, `intermediate`, `advanced` |
| replication_status | enum | see below |
| replications | array of objects | each `{title, url, by, year, outcome, summary}`; outcome is `replicated`, `partial`, `conditional`, `failed` or `extended` |
| replication_search_limited | boolean | `true` when the search for replications was cut short; `no public replication found` then means none turned up in a partial search |
| languages_tested | string | "English only", or the list of languages |
| multilingual_port | string | what re-running in another language would involve and where it could break; 1 to 2 sentences |
| why_it_matters | string | why the field leans on this result; one sentence |
| pitfalls | string | known replication problems; 1 to 2 sentences |
| replication_ideas | array of strings | 1 or 2 concrete, scoped replication or extension projects |
| tags | array of strings | lowercase keywords |

### Category values

- Model organisms and misalignment
- Oversight and weak-to-strong generalisation
- Evaluation and situational awareness
- Reasoning transparency, monitoring and control
- Interpretability and representations
- Fine-tuning, unlearning and tamper resistance
- Jailbreaks, robustness and multilingual safety
- Dangerous capabilities and agentic evaluation
- Evaluation science and measurement

### Claim types

- existence: X can occur under stated conditions
- prevalence: X occurs at some rate across a stated set of models or settings
- magnitude: a specific effect size
- mechanism: an internal or causal account of why X occurs
- ranking: comparisons across models or methods
- method: a technique (attack, defence, detector, protocol, metric) works as claimed

### Replication status

- `replicated`: at least one independent replication (different authors) reports that the main result holds
- `partially replicated`: some main claims hold and others do not, or effects are clearly weaker
- `conditional`: holds for some models or settings and not others
- `failed to replicate`: independent attempts did not find the main result
- `contested`: published disagreement without a clear resolution
- `no public replication found`: none located after searching

Follow-ups by the original authors are listed with outcome `extended` and do not by themselves make a study replicated.

### Compute tiers

For a faithful replication of the core result, not the whole paper.

- T0: API calls or a laptop only, under about $50
- T1: one GPU or modest API spend, about $50 to $500
- T2: several GPUs, fine-tuning mid-size models, or heavy API use, about $500 to $5,000
- T3: large-scale training or frontier-scale compute, over about $5,000

### Difficulty

- starter: prompting or inference only, with public code or a clear method; days of work for someone with basic Python
- intermediate: fine-tuning, activation-level work, or building a custom judge; weeks of work
- advanced: training runs, complex agent environments, or under-documented methods

## Resource record

| Field | Type | Rules |
|---|---|---|
| id | string | lowercase slug; unique |
| name | string | official name |
| type | enum | see below |
| url | string | official page |
| description | string | what it is; 1 to 2 sentences |
| use_for | string | how it helps someone replicating AI safety work; one sentence |
| access | enum | `free and open`, `free with sign-up`, `paid`, `restricted or by application` |
| maintainer | string | organisation or person |
| status | enum | `active`, `archived or discontinued`, `unknown` |
| multilingual_relevance | string | empty, or a short note on non-English use |
| tags | array of strings | lowercase keywords |

### Resource types

- Replication programme or collection
- Methodology guide or checklist
- Evaluation framework or harness
- Interpretability tooling
- Automated replication tool
- Benchmark or dataset
- Compute or model access
- Funding or fellowship
- Research group or lab
- Community or course
