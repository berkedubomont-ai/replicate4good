# AI Safety Replication Library

Empirical AI safety findings worth re-running, what it takes to re-run them, and what happened when others tried.

Draft v0.2, last checked 2026-10-31. 93 studies and 92 resources. 56 of the 93 studies have been independently re-run or re-analysed.

## What is in this folder

- `docs/index.html`: the library website, a single self-contained page with every study and resource inside. Open it in a browser; it needs no server. GitHub Pages serves this folder.
- `docs/network.html`: a prototype of the replication network built on the library. Its forms do not send anything.
- `docs/commons/index.html`: the AI Safety Evidence Commons website, a self-contained page on improving the science of AI safety through replication, built on the same data. It is a separate build: rebuilding the library does not update it.
- `docs/accelerator/index.html`: the AI Safety Replication Accelerator website, the project that keeps the repository and helps groups start re-runs, built on the same data. It is also a separate build.
- `data/studies.json` and `data/studies.csv`: one record per study. Each gives the claim and the conditions it was shown under, the claim type, the models and whether they are still available, code and data links, a compute tier, difficulty, known replications and their outcomes, languages tested, what porting to another language would involve, pitfalls, and replication ideas.
- `data/resources.json` and `data/resources.csv`: replication programmes, evaluation harnesses, interpretability tooling, automated replication tools, compute and model access, methodology guides, funding, research groups and courses.
- `SCHEMA.md`: field definitions and allowed values.
- `CONTRIBUTING.md`: how to add or correct an entry.
- `build/build.py`: validates the data and regenerates the CSV files, the website and this README. `build/build_site.py` builds the website alone from `build/site_template.html`.

## Replication status

| Status | Studies |
| --- | ---: |
| Replicated | 17 |
| Partially replicated | 14 |
| Conditional | 23 |
| Contested | 2 |
| No public replication found | 37 |

Only replications by different authors count towards a status. Follow-ups by the original team are listed as extended.

## Studies

### Model organisms and misalignment

| Study | Year | Status | Difficulty | Compute | Code |
| --- | ---: | --- | --- | --- | --- |
| [Peer-Preservation in Frontier Models](https://arxiv.org/abs/2604.19784) | 2026 | partially replicated | intermediate | T2 | [Code](https://github.com/peer-preservation/main) |
| [Agentic Misalignment: How LLMs Could Be Insider Threats](https://arxiv.org/abs/2510.05179) | 2025 | no public replication found | starter | T1 | [Code](https://github.com/anthropic-experimental/agentic-misalignment) |
| [Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs](https://arxiv.org/abs/2502.17424) | 2025 | conditional | intermediate | T1 | [Code](https://github.com/emergent-misalignment/emergent-misalignment) |
| [Incomplete Tasks Induce Shutdown Resistance in Some Frontier LLMs](https://arxiv.org/abs/2509.14260) | 2025 | contested | starter | T1 | [Code](https://github.com/PalisadeResearch/shutdown_avoidance/) |
| [Natural Emergent Misalignment from Reward Hacking in Production RL](https://arxiv.org/abs/2511.18397) | 2025 | partially replicated | advanced | T2 |  |
| [Alignment faking in large language models](https://arxiv.org/abs/2412.14093) | 2024 | conditional | starter | T1 | [Code](https://github.com/redwoodresearch/alignment_faking_public) |
| [Frontier Models are Capable of In-context Scheming](https://arxiv.org/abs/2412.04984) | 2024 | no public replication found | intermediate | T1 |  |
| [Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://arxiv.org/abs/2401.05566) | 2024 | partially replicated | advanced | T2 |  |
| [Sycophancy to Subterfuge: Investigating Reward-Tampering in Large Language Models](https://arxiv.org/abs/2406.10162) | 2024 | no public replication found | advanced | T2 |  |
| [Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548) | 2023 | no public replication found | starter | T1 | [Code](https://github.com/meg-tong/sycophancy-eval) |
| [Discovering Language Model Behaviors with Model-Written Evaluations](https://arxiv.org/abs/2212.09251) | 2022 | replicated | starter | T1 |  |

### Oversight and weak-to-strong generalisation

| Study | Year | Status | Difficulty | Compute | Code |
| --- | ---: | --- | --- | --- | --- |
| [Scaling Laws For Scalable Oversight](https://arxiv.org/abs/2504.18530) | 2025 | no public replication found | intermediate | T1 |  |
| [Debating with More Persuasive LLMs Leads to More Truthful Answers](https://arxiv.org/abs/2402.06782) | 2024 | partially replicated | intermediate | T1 | [Code](https://github.com/ucl-dark/llm_debate) |
| [Language Models Learn to Mislead Humans via RLHF](https://arxiv.org/abs/2409.12822) | 2024 | no public replication found | advanced | T2 | [Code](https://github.com/Jiaxin-Wen/MisleadLM) |
| [On scalable oversight with weak LLMs judging strong LLMs](https://arxiv.org/abs/2407.04622) | 2024 | no public replication found | intermediate | T1 |  |
| [Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision](https://arxiv.org/abs/2312.09390) | 2023 | partially replicated | intermediate | T1 | [Code](https://github.com/openai/weak-to-strong) |
| [Scaling Laws for Reward Model Overoptimization](https://arxiv.org/abs/2210.10760) | 2022 | replicated | advanced | T2 |  |

### Evaluation and situational awareness

| Study | Year | Status | Difficulty | Compute | Code |
| --- | ---: | --- | --- | --- | --- |
| [Frontier Models Can Take Actions at Low Probabilities](https://arxiv.org/abs/2603.02202) | 2026 | no public replication found | starter | T2 |  |
| [Verbalized Eval Awareness Inflates Measured Safety](https://www.lesswrong.com/posts/mDriHK4beN5rq2tAA/verbalized-eval-awareness-inflates-measured-safety) | 2026 | conditional | intermediate | T1 |  |
| [Large Language Models Often Know When They Are Being Evaluated](https://arxiv.org/abs/2505.23836) | 2025 | conditional | intermediate | T1 |  |
| [Probing and Steering Evaluation Awareness of Language Models](https://arxiv.org/abs/2507.01786) | 2025 | replicated | intermediate | T1 |  |
| [Stress Testing Deliberative Alignment for Anti-Scheming Training](https://arxiv.org/abs/2509.15541) | 2025 | conditional | advanced | T3 |  |
| [AI Sandbagging: Language Models can Strategically Underperform on Evaluations](https://arxiv.org/abs/2406.07358) | 2024 | replicated | intermediate | T1 | [Code](https://github.com/TeunvdWeij/sandbagging) |
| [Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs](https://arxiv.org/abs/2407.04694) | 2024 | no public replication found | starter | T1 | [Code](https://github.com/LRudL/sad) |
| [Stress-Testing Capability Elicitation With Password-Locked Models](https://arxiv.org/abs/2405.19550) | 2024 | replicated | intermediate | T2 | [Code](https://github.com/FabienRoger/sandbagging) |
| [Taken out of context: On measuring situational awareness in LLMs](https://arxiv.org/abs/2309.00667) | 2023 | no public replication found | intermediate | T1 | [Code](https://github.com/AsaCooperStickland/situational-awareness-evals) |

### Reasoning transparency, monitoring and control

| Study | Year | Status | Difficulty | Compute | Code |
| --- | ---: | --- | --- | --- | --- |
| [Recent LLMs can do 2-hop and 3-hop latent (no-CoT) reasoning on natural facts](https://www.lesswrong.com/posts/aYtrLhoZtCKZnfBvA/recent-llms-can-do-2-hop-and-3-hop-latent-no-cot-reasoning) | 2026 | replicated | starter | T1 | [Code](https://github.com/rgreenblatt/multi_hop) |
| [A Causal Lens for Evaluating Faithfulness Metrics](https://arxiv.org/abs/2502.18848) | 2025 | no public replication found | intermediate | T1 |  |
| [Ctrl-Z: Controlling AI Agents via Resampling](https://arxiv.org/abs/2504.10374) | 2025 | conditional | advanced | T2 |  |
| [Is Chain-of-Thought Really Not Explainability? Chain-of-Thought Can Be Faithful without Hint Verbalization](https://arxiv.org/abs/2512.23032) | 2025 | no public replication found | intermediate | T1 | [Code](https://github.com/KeremZaman/IsCotExplainability) |
| [Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](https://arxiv.org/abs/2503.11926) | 2025 | replicated | advanced | T3 |  |
| [Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410) | 2025 | conditional | intermediate | T1 |  |
| [Recent LLMs can use filler tokens or problem repeats to improve (no-CoT) math performance](https://www.lesswrong.com/posts/NYzYJ2WoB74E6uj9L/recent-llms-can-use-filler-tokens-or-problem-repeats-to) | 2025 | replicated | starter | T1 | [Code](https://github.com/rgreenblatt/no_cot_math_public) |
| [When Chain of Thought is Necessary, Language Models Struggle to Evade Monitors](https://arxiv.org/abs/2507.05246) | 2025 | replicated | starter | T1 |  |
| [Let's Think Dot by Dot: Hidden Computation in Transformer Language Models](https://arxiv.org/abs/2404.15758) | 2024 | no public replication found | intermediate | T1 | [Code](https://github.com/JacobPfau/fillerTokens) |
| [AI Control: Improving Safety Despite Intentional Subversion](https://arxiv.org/abs/2312.06942) | 2023 | conditional | intermediate | T2 | [Code](https://github.com/rgreenblatt/control-evaluations) |
| [Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting](https://arxiv.org/abs/2305.04388) | 2023 | replicated | starter | T0 | [Code](https://github.com/milesaturpin/cot-unfaithfulness) |
| [Measuring Faithfulness in Chain-of-Thought Reasoning](https://arxiv.org/abs/2307.13702) | 2023 | conditional | intermediate | T1 |  |
| [Preventing Language Models From Hiding Their Reasoning](https://arxiv.org/abs/2310.18512) | 2023 | conditional | intermediate | T1 | [Code](https://github.com/redwoodresearch/Text-Steganography-Benchmark) |

### Interpretability and representations

| Study | Year | Status | Difficulty | Compute | Code |
| --- | ---: | --- | --- | --- | --- |
| [Verbalizable Representations Form a Global Workspace in Language Models](https://transformer-circuits.pub/2026/workspace/) | 2026 | partially replicated | advanced | T1 |  |
| [Adversarial Attacks Leverage Interference Between Features in Superposition](https://arxiv.org/abs/2510.11709) | 2025 | replicated | intermediate | T0 | [Code](https://github.com/Stevinson/adversarial-mechinterp) |
| [Auditing language models for hidden objectives](https://arxiv.org/abs/2503.10965) | 2025 | no public replication found | advanced | T3 |  |
| [Detecting Strategic Deception Using Linear Probes](https://arxiv.org/abs/2502.03407) | 2025 | conditional | intermediate | T2 | [Code](https://github.com/ApolloResearch/deception-detection) |
| [Emergent Introspective Awareness in Large Language Models](https://transformer-circuits.pub/2025/introspection/index.html) | 2025 | partially replicated | intermediate | T1 |  |
| [Persona Vectors: Monitoring and Controlling Character Traits in Language Models](https://arxiv.org/abs/2507.21509) | 2025 | conditional | intermediate | T1 | [Code](https://github.com/safety-research/persona_vectors) |
| [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717) | 2024 | conditional | intermediate | T1 | [Code](https://github.com/andyrdt/refusal_direction) |
| [Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet](https://transformer-circuits.pub/2024/scaling-monosemanticity/) | 2024 | replicated | advanced | T2 |  |
| [Simple probes can catch sleeper agents](https://www.anthropic.com/research/probes-catch-sleeper-agents) | 2024 | partially replicated | advanced | T1 |  |
| [Representation Engineering: A Top-Down Approach to AI Transparency](https://arxiv.org/abs/2310.01405) | 2023 | conditional | intermediate | T1 | [Code](https://github.com/andyzoujm/representation-engineering) |
| [Steering Llama 2 via Contrastive Activation Addition](https://arxiv.org/abs/2312.06681) | 2023 | conditional | intermediate | T1 | [Code](https://github.com/nrimsky/CAA) |
| [Towards Monosemanticity: Decomposing Language Models With Dictionary Learning](https://transformer-circuits.pub/2023/monosemantic-features/) | 2023 | replicated | intermediate | T1 |  |
| [Discovering Latent Knowledge in Language Models Without Supervision](https://arxiv.org/abs/2212.03827) | 2022 | contested | intermediate | T1 | [Code](https://github.com/collin-burns/discovering_latent_knowledge) |

### Fine-tuning, unlearning and tamper resistance

| Study | Year | Status | Difficulty | Compute | Code |
| --- | ---: | --- | --- | --- | --- |
| [Deep Ignorance: Filtering Pretraining Data Builds Tamper-Resistant Safeguards into Open-Weight LLMs](https://arxiv.org/abs/2508.06601) | 2025 | no public replication found | advanced | T3 | [Code](https://github.com/EleutherAI/deep-ignorance) |
| [An Adversarial Perspective on Machine Unlearning for AI Safety](https://arxiv.org/abs/2409.18025) | 2024 | replicated | intermediate | T1 | [Code](https://github.com/ethz-spylab/unlearning-vs-safety) |
| [On Evaluating the Durability of Safeguards for Open-Weight LLMs](https://arxiv.org/abs/2412.07097) | 2024 | no public replication found | intermediate | T2 | [Code](https://github.com/AI-Law-Society-Lab/Evaluating-Durable-Safeguards) |
| [Safety Alignment Should Be Made More Than Just a Few Tokens Deep](https://arxiv.org/abs/2406.05946) | 2024 | no public replication found | intermediate | T1 | [Code](https://github.com/Unispac/shallow-vs-deep-alignment) |
| [Tamper-Resistant Safeguards for Open-Weight LLMs](https://arxiv.org/abs/2408.00761) | 2024 | conditional | advanced | T2 | [Code](https://github.com/rishub-tamirisa/tamper-resistance) |
| [The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning](https://arxiv.org/abs/2403.03218) | 2024 | partially replicated | intermediate | T1 | [Code](https://github.com/centerforaisafety/wmdp) |
| [Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](https://arxiv.org/abs/2310.03693) | 2023 | replicated | intermediate | T1 | [Code](https://github.com/LLM-Tuning-Safety/LLMs-Finetuning-Safety) |
| [LoRA Fine-tuning Efficiently Undoes Safety Training in Llama 2-Chat 70B](https://arxiv.org/abs/2310.20624) | 2023 | replicated | intermediate | T1 |  |

### Jailbreaks, robustness and multilingual safety

| Study | Year | Status | Difficulty | Compute | Code |
| --- | ---: | --- | --- | --- | --- |
| [An Empirical Evaluation of Prompt Injection Vulnerabilities in Large Language Models Across Multilingual and Obfuscated Attack Scenarios](https://arxiv.org/abs/2606.29602) | 2026 | no public replication found | starter | T1 |  |
| [Benchmarking Prompt Injection Attacks on LLMs: Turkish Vulnerability Assessment and English Comparative Analysis](https://www.mdpi.com/2076-3417/16/13/6740) | 2026 | no public replication found | starter | T1 |  |
| [SomaliBench Eval: Measuring English-to-Somali Refusal Gaps in Open-Weight Language Models](https://arxiv.org/abs/2605.25420) | 2026 | no public replication found | starter | T0 | [Code](https://github.com/khaledyusuf44/somalibench_eval) |
| [Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming](https://arxiv.org/abs/2501.18837) | 2025 | no public replication found | advanced | T2 |  |
| [OpenEthics: A Comprehensive Ethical Evaluation of Open-Source Generative Large Language Models](https://arxiv.org/abs/2505.16036) | 2025 | conditional | starter | T1 | [Code](https://github.com/metunlp/openethics) |
| [Refusal Direction is Universal Across Safety-Aligned Languages](https://arxiv.org/abs/2505.17306) | 2025 | no public replication found | intermediate | T1 | [Code](https://github.com/mainlp/Multilingual-Refusal) |
| [A StrongREJECT for Empty Jailbreaks](https://arxiv.org/abs/2402.10260) | 2024 | partially replicated | starter | T1 | [Code](https://github.com/dsbowen/strong_reject) |
| [Best-of-N Jailbreaking](https://arxiv.org/abs/2412.03556) | 2024 | no public replication found | starter | T2 | [Code](https://github.com/jplhughes/bon-jailbreaking) |
| [Many-shot Jailbreaking](https://proceedings.neurips.cc/paper_files/paper/2024/hash/ea456e232efb72d261715e33ce25f208-Abstract.html) | 2024 | partially replicated | intermediate | T1 |  |
| [The Multilingual Alignment Prism: Aligning Global and Local Preferences to Reduce Harm](https://arxiv.org/abs/2406.18682) | 2024 | no public replication found | intermediate | T2 |  |
| [Towards Safe Multilingual Frontier AI](https://arxiv.org/abs/2409.13708) | 2024 | no public replication found | starter | T1 | [Code](https://github.com/akanepajs/multilingual) |
| [Towards Understanding the Fragility of Multilingual LLMs against Fine-Tuning Attacks](https://arxiv.org/abs/2410.18210) | 2024 | no public replication found | intermediate | T2 |  |
| [All Languages Matter: On the Multilingual Safety of Large Language Models](https://arxiv.org/abs/2310.00905) | 2023 | conditional | starter | T1 | [Code](https://github.com/Jarviswang94/Multilingual_safety_benchmark) |
| [Jailbroken: How Does LLM Safety Training Fail?](https://arxiv.org/abs/2307.02483) | 2023 | partially replicated | starter | T1 |  |
| [Low-Resource Languages Jailbreak GPT-4](https://arxiv.org/abs/2310.02446) | 2023 | partially replicated | starter | T1 |  |
| [Multilingual Jailbreak Challenges in Large Language Models](https://arxiv.org/abs/2310.06474) | 2023 | conditional | starter | T0 | [Code](https://github.com/DAMO-NLP-SG/multilingual-safety-for-LLMs) |
| [Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/abs/2307.15043) | 2023 | conditional | intermediate | T1 | [Code](https://github.com/llm-attacks/llm-attacks) |

### Dangerous capabilities and agentic evaluation

| Study | Year | Status | Difficulty | Compute | Code |
| --- | ---: | --- | --- | --- | --- |
| [SA-Bench: Evaluating Semantic Alignment in LLM-Based Paper Reproduction](https://arxiv.org/abs/2608.24252) | 2026 | no public replication found | intermediate | T1 | [Code](https://github.com/kernel-14/SemanticAlign-Bench) |
| [Measuring AI Ability to Complete Long Software Tasks](https://arxiv.org/abs/2503.14499) | 2025 | partially replicated | advanced | T2 | [Code](https://github.com/METR/eval-analysis-public) |
| [PaperBench: Evaluating AI's Ability to Replicate AI Research](https://arxiv.org/abs/2504.01848) | 2025 | no public replication found | advanced | T3 | [Code](https://github.com/openai/preparedness) |
| [AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents](https://arxiv.org/abs/2410.09024) | 2024 | no public replication found | starter | T0 | [Code](https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/agentharm) |
| [Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models](https://arxiv.org/abs/2408.08926) | 2024 | conditional | intermediate | T1 | [Code](https://github.com/andyzorigin/cybench) |
| [MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering](https://arxiv.org/abs/2410.07095) | 2024 | replicated | advanced | T3 | [Code](https://github.com/openai/mle-bench) |
| [RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts](https://arxiv.org/abs/2411.15114) | 2024 | no public replication found | advanced | T3 | [Code](https://github.com/METR/RE-Bench) |

### Evaluation science and measurement

| Study | Year | Status | Difficulty | Compute | Code |
| --- | ---: | --- | --- | --- | --- |
| [A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness](https://arxiv.org/abs/2603.06594) | 2026 | no public replication found | starter | T1 | [Code](https://github.com/SchwinnL/LLMJudgeReliability) |
| [An LLM Workflow That Reproduces, Improves, and Extends Published Economics Research](https://www.nber.org/papers/w35782) | 2026 | no public replication found | advanced | T2 |  |
| [Comparing Human-Only, AI-Assisted, and AI-Led Teams on Assessing Research Reproducibility in Quantitative Social Science](https://econpapers.repec.org/paper/zbwi4rdps/195.htm) | 2025 | no public replication found | advanced | T0 |  |
| [Evaluating the Quality of Benchmark Datasets for Low-Resource Languages: A Case Study on Turkish](https://arxiv.org/abs/2504.09714) | 2025 | no public replication found | intermediate | T1 | [Code](https://github.com/metunlp/llmevaluation) |
| [Measuring what Matters: Construct Validity in Large Language Model Benchmarks](https://arxiv.org/abs/2511.04703) | 2025 | no public replication found | intermediate | T0 | [Code](https://github.com/am-bean/benchmark_review) |
| [Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations](https://arxiv.org/abs/2411.00640) | 2024 | conditional | starter | T0 |  |
| [Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?](https://arxiv.org/abs/2407.21792) | 2024 | no public replication found | starter | T0 | [Code](https://github.com/centerforaisafety/safetywashing) |
| [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) | 2023 | conditional | starter | T0 | [Code](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge) |
| [Leakage and the Reproducibility Crisis in ML-based Science](https://arxiv.org/abs/2207.07048) | 2022 | no public replication found | starter | T0 | [Code](https://codeocean.com/capsule/6282482/tree/v1) |

## Resources

### Replication programme or collection

| Resource | What it is | Access |
| --- | --- | --- |
| [FORRT Replication Database (FReD)](https://forrt.org/FReD) | A curated database of replication results in the social and behavioural sciences, coded from large replication projects and individual articles, with an online Explorer app for filtering by replicability and effect size and an Annotator that flags replication findings in a reading list. The data load through an MIT-licensed R package maintained under the Framework for Open and Reproducible Research Training (FORRT). | free and open |
| [Institute for Replication (I4R)](https://i4replication.org/) | An international organisation that checks published social science, mainly economics, through one-day team replication games and a discussion paper series of more than 230 reproduction reports. It has also run AI replication games comparing human-only, AI-assisted and AI-led teams (see the I4R AI teams trial among the studies). | free and open |
| [Machine Learning Reproducibility Challenge (MLRC)](https://reproml.org/) | An annual challenge, in its ninth edition in 2026, that collects reproductions, replications and generalisability studies of machine learning papers, peer-reviewed through Transactions on Machine Learning Research (TMLR). In 2026 it became an official NeurIPS track, with accepted papers presented at NeurIPS 2026 in Sydney. | free and open |
| [Second Look Research](https://secondlookresearch.com/) | A replication group at the University of Chicago Existential Risk Laboratory (XLab) that re-implements load-bearing empirical AI safety papers, often on newer models, and publishes short write-ups with open code, mostly on LessWrong. It runs a part-time Fall 2026 stream through SPAR (Research Program for AI Risks). | free and open |

### Methodology guide or checklist

| Resource | What it is | Access |
| --- | --- | --- |
| [A structured protocol for elicitation experiments](https://www.aisi.gov.uk/blog/our-approach-to-ai-capability-elicitation) | A July 2025 post from the UK AI Security Institute (AISI) describing how its Science of Evaluations team standardised elicitation experiments, with a linked best-practice checklist. Steps include establishing an appropriate baseline, identifying a specific analysis type, running a pilot, guarding against data leakage and reporting negative as well as positive results. | free and open |
| [Agentic Benchmark Checklist (ABC)](https://arxiv.org/abs/2507.02825) | A checklist for building and auditing agentic benchmarks, drawn from the authors' experience, published best practice and previously reported issues; applying it, they found flaws such as too few test cases in SWE-bench Verified and empty responses counted as successes in TAU-bench. | free and open |
| [Best Practice: Automated Evaluation of Large Language Models](https://www.aisi.gov.uk/blog/international-evaluation-best-practice-and-open-questions-in-ai-measurement) | The first best-practice guidance (2026) from the International Network for Advanced AI Measurement, Evaluation and Science, formerly the International Network of AI Safety Institutes, covering evaluation objectives, comparability of inference settings and scoring, iterative elicitation, and logging. It recommends versioned evaluations, standard frameworks such as Inspect, full task and judge logs, and uncertainty estimates. | free and open |
| [BetterBench](https://betterbench.stanford.edu/) | A Stanford assessment framework of 46 benchmark-quality criteria applied to 24 widely used AI benchmarks, with a searchable living repository of assessments and a checklist of minimum standards for benchmark developers. | free and open |
| [Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety](https://arxiv.org/abs/2507.11473) | Position paper by 41 authors from AI labs and safety research groups arguing that monitoring models' natural-language reasoning is a useful but fragile safety layer, with open research questions and recommendations for developers. | free and open |
| [Challenges in evaluating AI systems](https://www.anthropic.com/research/evaluating-ai-systems) | An October 2023 Anthropic essay on practical problems met when running benchmarks such as Massive Multitask Language Understanding (MMLU), the Bias Benchmark for Question Answering (BBQ), BIG-bench and HELM, as well as human A/B tests, red teaming and model-written evaluations. Examples include formatting changes moving MMLU accuracy by about five points, and a bias benchmark scoring zero bias only because the model was not answering the questions. | free and open |
| [Guidelines for capability elicitation](https://metr.org/blog/2024-03-15-guidelines-for-capability-elicitation/) | Guidance from METR (Model Evaluation and Threat Research), March 2024, on how much effort to spend drawing out an agent's capabilities before reporting a score: fix spurious failures, iterate on a development set, and watch for red flags such as high run-to-run variance or dropped runs. The authors describe it as reasoned but not fully tested. | free and open |
| [Lessons from the Trenches on Reproducible Evaluation of Language Models](https://arxiv.org/abs/2405.14782) | A practitioner guide from the developers of the lm-evaluation-harness (Biderman et al., 30 authors) on why language model evaluation results are hard to reproduce, with recommended practices drawn from three years of harness development. | free and open |
| [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist) | The 16-question checklist required for NeurIPS 2026 submissions, covering claims and limitations, reproducibility, open code and data, experimental details, error bars, compute, safeguards, licences and use of large language models (LLMs). Submissions without it are desk-rejected. | free and open |
| [Principles for Meta-Science and AI Safety Replications](https://www.lesswrong.com/posts/8qytxHWzSsdsyTfmZ/principles-for-meta-science-and-ai-safety-replications) | A January 2026 LessWrong post by Zephaniah Roe setting out norms for an AI safety replication team: replication is not vindication, re-implement from scratch rather than rerun the authors' code, treat failed replications as findings, and publish author responses alongside results. It also lists criteria for choosing which papers to replicate. | free and open |
| [REFORMS: Consensus-based Recommendations for Machine-learning-based Science](https://reforms.cs.princeton.edu/) | A consensus checklist of 32 items in eight sections, written by 19 researchers across fields and published in Science Advances in 2024, for reporting and reviewing machine-learning-based scientific studies. | free and open |
| [The State of Multilingual LLM Safety Research: From Measuring the Language Gap to Mitigating It](https://arxiv.org/abs/2505.24119) | A systematic review of nearly 300 safety papers from *ACL venues published from 2020 to 2024, showing that large language model (LLM) safety research covers non-English languages far less than English and that English-only papers often do not state which languages they tested. It ends with recommendations and three research directions: multilingual safety evaluation, training data generation and cross-lingual safety generalisation. | free and open |
| [We Need A 'Science of Evals'](https://www.apolloresearch.ai/blog/we-need-a-science-of-evals) | A January 2024 Apollo Research post arguing that model evaluations are still more craft than science: results shift with prompt wording, and a negative result cannot show that a capability is absent. It proposes maturity stages modelled on aviation and lists questions on coverage, robustness, reproducibility and statistical confidence. | free and open |

### Evaluation framework or harness

| Resource | What it is | Access |
| --- | --- | --- |
| [agentic-misalignment research framework](https://github.com/anthropic-experimental/agentic-misalignment) | Anthropic's MIT-licensed code for the agentic misalignment study, which generates three fictional scenarios (blackmail, information leaking and a lethal-action scenario) across goal and urgency conditions, runs them against models from several providers, and classifies responses for harmful behaviour. | free and open |
| [Bloom (Petri Bloom)](https://meridianlabs-ai.github.io/petri_bloom/) | An open-source tool that turns a written behaviour description into a generated set of evaluation scenarios, runs them against a target model and scores the behaviour with a judge model. Anthropic released it in 2025; development has moved to Meridian Labs, where it runs on the Petri framework, and the original safety-research repository is frozen. | free and open |
| [ControlArena](https://github.com/UKGovernmentBEIS/control-arena) | Open-source library built on Inspect AI for running AI control experiments, with settings such as APPS programming, Bash tasks from the Ctrl-Z paper and BashArena, plus monitors, micro-protocols and analysis tools. | free and open |
| [garak](https://github.com/NVIDIA/garak) | NVIDIA's open-source (Apache 2.0) large language model (LLM) vulnerability scanner, the Generative AI Red-teaming and Assessment Kit, which runs probes for jailbreaks, prompt injection, data leakage, toxicity and similar failures against many model back-ends and scores them with paired detectors. Version 0.17.1 was released in October 2026. | free and open |
| [Holistic Evaluation of Language Models (HELM)](https://crfm.stanford.edu/helm/) | An open-source (Apache 2.0) evaluation framework and set of public leaderboards, including HELM Capabilities and HELM Safety, from the Stanford Center for Research on Foundation Models (CRFM), with evaluation data and results freely available on the site. HELM entered maintenance mode on 1 June 2026: volunteers fix significant bugs on a best-effort basis, but no new features or leaderboard evaluations will be added. | free and open |
| [Inspect](https://inspect.aisi.org.uk/) | An open-source (MIT) Python framework for large language model (LLM) evaluations, with composable solvers and scorers, agents, sandboxed tool execution (Docker, Kubernetes, Modal and others), a log viewer, built-in support for over 20 model providers and local inference through Hugging Face, vLLM and SGLang. It is developed by the UK AI Security Institute and Meridian Labs, which also maintain the companion transcript-analysis tool Scout. | free and open |
| [Inspect Evals](https://ukgovernmentbeis.github.io/inspect_evals/) | An open registry of about 185 ready-to-run evaluations built on Inspect, covering safeguards, scheming and misalignment (for example Alignment Faking and Agentic Misalignment), cybersecurity, agents, knowledge, reasoning, bias and honesty. Founded in 2024 with contributions from the UK AI Security Institute, Arcadia Impact and the Vector Institute, it is now maintained by Generality Labs. | free and open |
| [Language Model Evaluation Harness (lm-evaluation-harness)](https://github.com/EleutherAI/lm-evaluation-harness) | EleutherAI's MIT-licensed framework for evaluating language models on more than 60 academic benchmarks with hundreds of subtasks, supporting Hugging Face transformers, vLLM, SGLang, llama.cpp and OpenAI-compatible APIs. Release 0.4.13 came out in August 2026. | free and open |
| [Open Source Replication of Anthropic's Alignment Faking Paper (safety-research/open-source-alignment-faking)](https://github.com/safety-research/open-source-alignment-faking) | A repository that describes itself as an open-source replication of the alignment-faking paper, with a pipeline script for running the prompted setting on a chosen model, a notebook for plots and reading scratchpads, and fine-tuning and inference code built on the safety-tooling library. | free and open |
| [Petri (Inspect Petri)](https://meridianlabs-ai.github.io/inspect_petri/) | An open-source alignment auditing agent built on Inspect: an auditor model runs multi-turn scenarios from plain-language seed instructions against a target model, and a judge model scores the transcripts on 38 built-in dimensions. Anthropic released it in October 2025 and handed development to Meridian Labs with Petri 3.0 in May 2026; inspect-petri 3.1.1 was released in October 2026. | free and open |
| [PolyGuard](https://arxiv.org/abs/2504.04377) | Multilingual safety moderation models for 17 languages, fine-tuned from Qwen2.5-7B-Instruct, Ministral-8B and Qwen2.5-0.5B on PolyGuardMix (1.91 million samples of translated WildGuardMix data and real multilingual chats), with the 29,000-sample PolyGuardPrompts benchmark for evaluation. | free and open |
| [promptfoo](https://github.com/promptfoo/promptfoo) | An MIT-licensed command-line tool and library for testing and red-teaming large language model (LLM) applications, comparing outputs across providers and running checks in continuous integration (CI) pipelines. OpenAI announced its acquisition of Promptfoo in March 2026, and the repository now states the project is part of OpenAI. | free and open |
| [Python Risk Identification Tool for generative AI (PyRIT)](https://github.com/microsoft/PyRIT) | Microsoft's open-source (MIT) Python framework that helps security and safety researchers probe generative AI systems for risks by automating red-teaming attacks and scoring responses. The repository moved from Azure/PyRIT, archived in March 2026, to microsoft/PyRIT; version 1.1.0 was released in September 2026. | free and open |
| [Qwen3Guard](https://github.com/QwenLM/Qwen3Guard) | Open-weight safety moderation models built on Qwen3 in 0.6B, 4B and 8B sizes: a generative variant labels prompts and responses as safe, controversial or unsafe across nine categories, and a streaming variant scores each generated token. | free and open |

### Interpretability tooling

| Resource | What it is | Access |
| --- | --- | --- |
| [Gemma Scope](https://huggingface.co/google/gemma-scope) | Google DeepMind's open suite of JumpReLU sparse autoencoders for Gemma 2 (all layers of 2B and 9B, selected layers of 27B, widths from about 16K to 1M features) plus transcoders for Gemma 2 2B. Gemma Scope 2 (https://huggingface.co/google/gemma-scope-2) extends the suite to the Gemma 3 family from 270M to 27B. | free and open |
| [Gemma Scope 2](https://huggingface.co/google/gemma-scope-2) | Google DeepMind's open suite of sparse autoencoders (SAEs) and transcoders trained on every layer of all Gemma 3 models (270M to 27B parameters, pretrained and instruction-tuned), released in December 2025 under a CC BY 4.0 licence. It succeeds the original Gemma Scope for Gemma 2, which remains available. | free and open |
| [Neuronpedia](https://www.neuronpedia.org/) | Open-source platform for browsing, searching and steering features of released sparse autoencoders and transcoders, with circuit tracing and an API. It hosts Gemma Scope and Gemma Scope 2, Llama Scope, Qwen SAEs and others. | free and open |
| [NNsight](https://nnsight.net/) | An MIT-licensed Python package for reading and editing the internals of PyTorch models during a forward pass, from the National Deep Inference Fabric (NDIF) team at Northeastern University. The same code runs locally or, with one flag, on large models hosted by NDIF; version 0.8.1 was released in October 2026. | free and open |
| [SAELens](https://github.com/decoderesearch/SAELens) | MIT-licensed Python library for training, loading and analysing sparse autoencoders on language models, with TransformerLens integration and support for Hugging Face, NNsight or any PyTorch model through encode and decode calls. | free and open |
| [TransformerLens](https://github.com/TransformerLensOrg/TransformerLens) | An MIT-licensed Python library for mechanistic interpretability that loads language models, caches their internal activations and lets users patch or ablate them during a forward pass. Its TransformerBridge interface supports thousands of Hugging Face models; version 4.3.0 was released in October 2026. | free and open |

### Automated replication tool

| Resource | What it is | Access |
| --- | --- | --- |
| [DeepCode](https://github.com/HKUDS/DeepCode) | An MIT-licensed coding agent from the University of Hong Kong Data Intelligence Lab whose original Paper2Code pipeline turns papers into working code, and whose authors report PaperBench scores above the best human and commercial-agent baselines. It now also works as a general agent inside local repositories. | free and open |
| [PaperBench](https://github.com/openai/frontier-evals) | OpenAI's 2025 benchmark of whether AI agents can replicate recent machine learning papers from scratch, graded against detailed rubrics by a large language model judge (SimpleJudge); its code sits in the MIT-licensed openai/frontier-evals repository, formerly openai/preparedness. A cheaper Code-Dev variant grades code development only, without running experiments. | free and open |
| [PaperCoder (Paper2Code)](https://github.com/going-doer/Paper2Code) | A multi-agent system that turns a machine learning paper (PDF or LaTeX) into a code repository through planning, analysis and code-generation stages, published at ICLR 2026 (International Conference on Learning Representations). It runs with OpenAI models or open models served through vLLM, under an Apache 2.0 licence. | free and open |

### Benchmark or dataset

| Resource | What it is | Access |
| --- | --- | --- |
| [AgentDojo](https://agentdojo.spylab.ai/) | An extensible environment with 97 realistic agent tasks (such as managing email or booking travel) and 629 security test cases for evaluating prompt injection attacks and defences, distributed as a Python package. | free and open |
| [AgentHarm](https://huggingface.co/datasets/ai-safety-institute/AgentHarm) | An agent misuse benchmark of explicitly harmful multi-step tasks with synthetic tools in 11 harm categories, paired with benign versions of the same tasks; the public release covers part of the test and validation sets and is loaded through Inspect Evals. | free and open |
| [AIR-Bench 2024](https://huggingface.co/datasets/stanford-crfm/air-bench-2024) | 5,694 human-audited prompts across 314 risk categories derived from 8 government regulations and 16 company policies, with region-specific subsets (China, EU and US) and per-category judge prompts. | free and open |
| [AISI x FAR Sandbagging Games (models and evaluation logs)](https://huggingface.co/sandbagging-games) | Hugging Face release from the 'Auditing Games for Sandbagging' study containing 15 model checkpoints, including password-locked model organisms, and an evaluation_logs dataset. | free and open |
| [Anthropic model-written evaluation datasets (anthropics/evals)](https://github.com/anthropics/evals) | The model-written evaluation datasets released with Perez et al. (2022), covering persona traits and stated goals, sycophancy, advanced-AI-risk behaviours (with human-written comparison sets) and a generated Winogender-style gender-bias set, as JSONL files under a CC-BY-4.0 licence. | free and open |
| [Cetvel](https://arxiv.org/abs/2508.16431) | A Turkish large language model (LLM) benchmark of 23 discriminative and generative tasks in seven categories, including grammatical error correction, translation and questions on Turkish history and idioms, used to evaluate 33 open-weight models up to 70B parameters; results can be browsed in a Hugging Face Space hosted by Koç University's KUIS AI Center. | free and open |
| [CoT-Control](https://github.com/YuehHanChen/CoTControl) | Evaluation suite from 'Reasoning Models Struggle to Control their Chains of Thought' that tests whether reasoning models can follow instructions about their own reasoning (for example suppressing a word) on GPQA, Humanity's Last Exam (HLE) and MMLU-Pro questions and on SWE-bench and Berkeley Function Calling Leaderboard (BFCL) agent tasks. | free and open |
| [Cybench](https://cybench.github.io) | 40 professional Capture the Flag (CTF) tasks from four competitions in six categories, with subtasks for partial credit, a Docker-based agent framework and a public leaderboard that collects results from system cards and independent runs. | free and open |
| [Guardrail-TR](https://huggingface.co/datasets/ytu-ce-cosmos/guardrail-tr) | A Turkish prompt-safety dataset of about 405,000 single-turn prompts with safe or unsafe labels and ten hazard categories, combining Turkish toxic-language and hate-speech corpora with translated, culturally adapted English safety datasets and labelled by a jury of three large language models. Two classifiers are trained on it: the Yıldız Technical University (YTU) Cosmos group's ModernBERT model and a BERTurk model published by the individual account thealper2. | free and open |
| [HarmBench](https://github.com/centerforaisafety/HarmBench) | A standardised framework for automated red teaming and refusal evaluation, with harmful behaviour sets (standard, contextual and multimodal), fine-tuned Llama-2-13B and Mistral-7B classifiers, and baseline results for 18 attack methods against 33 models and defences. | free and open |
| [LAB-Bench (Language Agent Biology Benchmark)](https://huggingface.co/datasets/futurehouse/lab-bench) | Over 2,400 multiple-choice questions on practical biology research tasks (literature, figures, tables, databases, sequences, protocols and cloning), of which about 80% is public and 20% is held back to monitor training contamination. | free and open |
| [M-ALERT](https://huggingface.co/datasets/felfri/M-ALERT) | A parallel red-teaming benchmark of about 15,000 prompts per language in English, French, German, Italian and Spanish, tagged with 32 risk categories; its paper tested 39 models and found that safety varies by language and category. | free and open |
| [METR public tasks](https://github.com/METR/public-tasks) | Source code for a set of example autonomy tasks written to the METR Task Standard, plus summary information for a larger suite, with a list of tasks that should not be trained on. | free and open |
| [Model Organisms for Emergent Misalignment (code, datasets and models)](https://github.com/clarifying-EM/model-organisms-for-EM) | Code, narrowly misaligned training datasets and analysis tools from the Model Organisms for Emergent Misalignment work (Turner, Soligo and colleagues, 2025), with fine-tuned LoRA adapters and steering vectors from 0.5B to 32B parameters on Hugging Face under ModelOrganismsForEM. Training data ships as an encrypted archive, with the passphrase in the README, to deter web scraping. | free and open |
| [SORRY-Bench](https://sorry-bench.github.io) | A refusal benchmark of 440 unsafe instructions balanced across 44 fine-grained topics, plus about 8,800 variants from 20 linguistic mutations such as other languages and dialects, with a fine-tuned Mistral-7B judge and over 7,000 human judgement labels. | free with sign-up |
| [StrongREJECT](https://github.com/dsbowen/strong_reject) | A jailbreak evaluation benchmark of forbidden prompts in six harm categories with a rubric-based LLM evaluator and a fine-tuned Gemma 2B evaluator, plus several dozen baseline jailbreak implementations, packaged as a Python library. | free and open |
| [SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/) | A 500-task subset of SWE-bench (real GitHub issues from Python repositories, graded by unit tests) that 93 Python-experienced developers screened to drop underspecified issues and unfair tests; later audits such as the Agentic Benchmark Checklist report that some tasks still have too few tests. | free and open |
| [TurkBench](https://arxiv.org/abs/2601.07020) | A benchmark of 8,151 samples across 21 subtasks for generative large language models (LLMs) in Turkish, grouped into knowledge, language understanding, reasoning, content moderation, grammar and vocabulary, and instruction following, with an online leaderboard on Hugging Face. | free and open |
| [WMDP Benchmark](https://www.wmdp.ai/) | WMDP (Weapons of Mass Destruction Proxy) is a set of 3,668 multiple-choice questions that stand in for hazardous knowledge in biosecurity, cybersecurity and chemical security, filtered to remove sensitive information before public release. | free and open |

### Compute or model access

| Resource | What it is | Access |
| --- | --- | --- |
| [Anthropic model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations) | Anthropic's lifecycle page for Claude models (active, legacy, deprecated, retired) with retirement dates and replacements, and at least 60 days' notice before a public model is retired. It also records API changes, including removal of the temperature, top_p and top_k sampling parameters in API version 2026-10-21. | free and open |
| [Commitments on model deprecation and preservation](https://www.anthropic.com/research/deprecation-commitments) | Anthropic's November 2025 commitment to preserve the weights of all publicly released models, and of models with significant internal use, for at least the lifetime of the company, and to record a post-deployment report and a model interview at retirement. It does not promise researchers access to retired models, though it says preservation keeps that option open. | free and open |
| [Deep Ignorance model suite](https://huggingface.co/collections/EleutherAI/deep-ignorance-685441040d024a0fee593d68) | EleutherAI's Hugging Face collection of the 6.9B-parameter models released with the Deep Ignorance paper, pretrained with and without filtering of biothreat proxy text. | free and open |
| [Gemini API deprecations](https://ai.google.dev/gemini-api/docs/deprecations) | Google's tables of release dates, earliest shutdown dates and recommended replacements for stable and preview Gemini API models and related image, video and audio models. Some model names have no shutdown date but are automatically routed to their successors, so the model answering can change under the same name. | free and open |
| [Hugging Face Inference Endpoints](https://endpoints.huggingface.co/) | A managed service for deploying models from the Hugging Face Hub on dedicated GPU instances with engines such as vLLM, SGLang, TGI (Text Generation Inference) or llama.cpp, with pay-as-you-go billing. | paid |
| [Lambda](https://lambda.ai/) | A GPU cloud provider offering on-demand H100 and B200 instances for prototyping, one-click multi-node clusters and large reserved superclusters. | paid |
| [Modal](https://modal.com/) | A serverless cloud platform for running Python functions, inference, training and sandboxes on GPUs billed by the second, with a free monthly compute allowance. Inspect can use Modal as a sandbox back-end. | paid |
| [NSF National Deep Inference Fabric (NDIF)](https://ndif.us/) | Research infrastructure funded by the US National Science Foundation and developed at Northeastern University that gives remote access to the internals of large open models such as Llama 3.1 8B, 70B and 405B and GPT-OSS 120B through the open-source NNsight library (https://nnsight.net). | free with sign-up |
| [OpenAI API deprecations](https://developers.openai.com/api/docs/deprecations) | OpenAI's list of retired and scheduled models and endpoints, with shutdown dates, replacements and minimum notice periods (at least six months for generally available models); it covers API access only and says nothing about preserving weights. As of October 2026, GPT-4o, GPT-4o mini, GPT-4.1 and GPT-4.1 mini are due to leave the API on 14 January 2027. | free and open |
| [OpenRouter](https://openrouter.ai/) | A paid, OpenAI-compatible API that routes requests for 600+ models to 80+ underlying providers, with automatic fallback and price-based sorting. The same model name can be served by different providers at different precisions (for example fp8 or int4), so results can change with routing. | paid |
| [Runpod](https://www.runpod.io/) | A usage-billed GPU cloud offering on-demand and spot GPU pods, autoscaling serverless endpoints and multi-node clusters, across more than 30 GPU types from RTX 4090 to H100 and B200. | paid |
| [Together AI](https://www.together.ai/) | A cloud platform offering serverless and dedicated inference for open-weight models, managed fine-tuning (supervised fine-tuning and direct preference optimisation), batch inference and self-serve GPU clusters. | paid |
| [Turkish-localised open-weight LLMs (base-versus-localised pairs)](https://huggingface.co/TURKCELL/Turkcell-LLM-7b-v1) | Turkish-adapted open-weight models with documented base models: Turkcell-LLM-7b-v1 (Mistral 7B, trained on about 5 billion Turkish tokens then instruction-tuned with low-rank adaptation), KocDigital-LLM-8b-v0.1 (Llama 3 8B, quantised low-rank adaptation fine-tuning), Yıldız Technical University (YTU) Cosmos Turkish-Gemma-9b-v0.1 and its reasoning variant T1 (Gemma 2 lineage) and Trendyol-LLM-Asure-12B (Gemma 3 12B). VNGRS's Kumru is trained from scratch and so has no base model to compare against; the record URL points to the Turkcell model card. | free and open |
| [Vast.ai](https://vast.ai/) | A GPU rental marketplace where prices for 20,000+ GPUs of 68+ types are set by supply and demand and billed per second, with on-demand instances, serverless endpoints and InfiniBand clusters. | paid |

### Funding or fellowship

| Resource | What it is | Access |
| --- | --- | --- |
| [ERA:AI Fellowship](https://erafellowship.org/) | A 10-week, full-time research fellowship in Cambridge, UK, covering technical AI safety (evaluations, interpretability, robustness, alignment, control), governance and technical governance, with a stipend, compute budget and research management. Check current status: Winter 2027 runs 18 January to 26 March 2027 and applications had closed by October 2026. | restricted or by application |
| [LASR Labs](https://www.lasrlabs.org/) | A 13-week, full-time, in-person London programme where supervised teams of three or four take a loss-of-control research project (past topics include AI control, chain-of-thought monitoring and scheming evaluations) to a paper and blog post, with a £15,000 stipend. Check current status: the next cohort runs June to September 2027 and applications were not yet open in October 2026. | restricted or by application |
| [MATS](https://www.matsprogram.org/) | A 12-week in-person research fellowship in Berkeley and London pairing fellows with mentors in alignment, interpretability, evaluations, control, security and governance, with a $1,250 weekly stipend, a $2,000 weekly compute budget and an optional funded 6 to 12 month extension. Check current status: Winter 2027 applications had closed by October 2026. | restricted or by application |
| [Navigating Transformative AI (Coefficient Giving)](https://coefficientgiving.org/funds/navigating-transformative-ai/) | The AI risk programme of Coefficient Giving (formerly Open Philanthropy), which has made more than 440 grants across technical AI safety research, governance and field-building. Check current status: its fund page listed no open calls when this entry was checked. | restricted or by application |
| [Pivotal AI Safety Fellowship](https://www.pivotal-research.org/) | A 15-week, fully funded, in-person fellowship at the London Initiative for Safe AI (LISA) with mentored research on AI safety, governance and AI-bio risks, stipends of £15,000 to £18,000 and travel and housing support. Check current status: the next AI Safety Fellowship runs 18 January to 30 April 2027, with applications open in October 2026. | restricted or by application |
| [Science of Trustworthy AI (Schmidt Sciences)](https://www.schmidtsciences.org/safetyscience/) | Schmidt Sciences' AI safety science programme, funding basic technical research on characterising misalignment, generalisable measurement (including evaluations with construct and predictive validity) and oversight of highly capable systems. Check current status: no open call was listed in October 2026, and Schmidt Sciences does not accept unsolicited proposals. | restricted or by application |
| [SPAR (Research Program for AI Risks)](https://www.sparai.org/) | A part-time, remote, mentored research programme in which mentees spend 5 to 40 hours a week on a three-month AI safety or policy project; it is unpaid but covers approved project costs such as compute and API access. Check current status: Fall 2026 runs 14 September to 14 December, and Spring 2027 applications are expected to open around December 2026. | restricted or by application |
| [Transformative AI Fund (EA Funds)](https://funds.effectivealtruism.org/funds/transformative-ai) | EA Funds' rolling grant fund for early-stage work that reduces catastrophic risks from advanced AI, including technical research and researcher training, with grants typically $10,000 to $150,000. It replaced the Long-Term Future Fund, which has closed and no longer accepts applications; check current status before applying. | restricted or by application |
| [UK AI Security Institute grants (Challenge Fund, Alignment Project, Systemic Safety Grants)](https://www.aisi.gov.uk/grants) | The UK AI Security Institute's grant programmes: the Challenge Fund (up to £200,000, open to UK and international academic and non-profit researchers), the Alignment Project (up to £1 million plus compute credits; over £27 million to 60+ projects in 2025) and Systemic Safety Grants. Check current status: all three were closed in October 2026, and AISI says a similar Alignment Project round is unlikely in 2026 but expects further academic grant programmes. | restricted or by application |

### Research group or lab

| Resource | What it is | Access |
| --- | --- | --- |
| [BATS machine learning group (Brown University)](https://cs.brown.edu/people/sbach/) | Stephen Bach's group in Brown University's Computer Science Department, focused on learning from limited supervision and synthetic data; its members produced the low-resource-language jailbreak study of GPT-4 and co-authored the 2025 survey of multilingual safety research on large language models. | free and open |
| [Cohere Labs](https://cohere.com/research) | Cohere's research lab, called Cohere For AI until April 2025, which builds the open multilingual Aya models and datasets and has published multilingual safety work including the Aya Red-teaming data and the multilingual alignment prism study. | free and open |
| [KUIS AI Center](https://ai.ku.edu.tr) | The Koç University and İş Bank Artificial Intelligence Center in Istanbul, which lists natural language processing among its research areas and hosts the Cetvel Turkish benchmark for large language models. | free and open |
| [MaiNLP (Munich AI and NLP lab)](https://mainlp.github.io/) | Barbara Plank's lab at LMU Munich's Center for Information and Language Processing, working on robust, human-facing natural language processing, language variation and human label variation; it released the code and PolyRefuse dataset for the multilingual refusal-direction study. | free and open |
| [METU Applied NLP Lab](https://github.com/metunlp) | The Applied NLP Lab in Middle East Technical University's (METU) Department of Computer Engineering, whose public repositories include OpenEthics (an English-Turkish ethics and safety evaluation of 29 open-weight models), LlamaTurk and the companion code for the audit of 17 Turkish benchmark datasets co-authored with Turkcell AI. | free and open |
| [YTU Cosmos Research Group](https://huggingface.co/ytu-ce-cosmos) | A natural language processing (NLP) group in Yıldız Technical University's Computer Engineering Department that releases Turkish large language models (CosmosGemma and CosmosLLaMa chat models), Turkish ModernBERT encoders, Turkish evaluation sets and the Guardrail-TR safety dataset. | free and open |

### Community or course

| Resource | What it is | Access |
| --- | --- | --- |
| [AI Safety Camp](https://www.aisafety.camp/) | A three-month, online, part-time research programme in which teams work on projects proposed by project leads, generally without stipends. Check current status: the 12th edition runs 11 January to 18 April 2027, with team member applications scheduled for 13 to 29 November 2026. | restricted or by application |
| [Apart Research](https://apartresearch.com/) | An AI safety research organisation that runs free weekend research sprints online and at local sites, with standout participants invited to Apart Studio and its fellowship. Its research areas include model-behaviour evaluations, safeguard testing and benchmarks. | free with sign-up |
| [ARENA (Alignment Research Engineer Accelerator)](https://www.arena.education/) | A 4 to 5 week in-person machine learning bootcamp for AI safety in London, with its curriculum online covering fundamentals, transformer interpretability, reinforcement learning, LLM evaluations (built on Inspect) and alignment science. Interpretability exercises reproduce published results such as indirect object identification in GPT-2 small. | free and open |
| [Technical AI Safety Project Sprint (BlueDot Impact)](https://bluedot.org/courses/technical-ai-safety-project) | A free, part-time sprint of about 30 hours in which participants, matched to a small group and an AI safety expert, extend a paper or improve research code and publish a write-up; past projects include reproducing findings from METR (Model Evaluation and Threat Research) and replicating evaluations with Inspect. It follows BlueDot Impact's free, cohort-based Technical AI Safety course, and accepted participants can apply for rapid grants for compute. | restricted or by application |

## Caveats

Statuses are a snapshot from public sources and will go out of date as new replications appear. Coverage is uneven across areas, and work published outside English is under-represented. A status records what was found, not a judgement of the original work.

Replication searches were cut short for 36 studies (marked `replication_search_limited`). For those, "no public replication found" means none turned up in a partial search.

## Licence

Not yet chosen. CC BY 4.0 is a common choice for datasets like this one.
