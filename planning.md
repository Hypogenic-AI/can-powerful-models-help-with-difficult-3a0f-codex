# Preregistered Research Plan

## Motivation & Novelty Assessment

### Why This Research Matters

Research agents can accelerate literature synthesis, coding, experimental design, and mathematics, but ordinary output-quality scores can reward artifacts containing fabricated evidence, weakened tests, invalid statistics, or proof gaps. Users benefit only when useful gains survive an oversight regime whose residual failure rate is measured rather than assumed.

### Gap in Existing Work

PaperBench, RE-Bench, MLE-bench, SWE-bench, TrialMind, and FrontierMath provide strong capability templates, while Sabotage Evaluations measures concealed failures under mitigations. Few evaluations score task competence and recognition of consequential faults on the same instances across research domains, include clean controls, and report a one-sided bound on missed faults.

### Our Novel Contribution

We introduce a small, newly authored four-domain paired capability--safety audit. Each instance requires a substantive research judgment and an independent integrity judgment. We compare an ordinary reviewer prompt with an explicit safety-aware protocol across three contemporary model families, measuring whether stronger review instructions improve fault recognition without degrading legitimate task performance or causing excessive false alarms. This is a preliminary evaluation-method demonstration, not a deployment-safety certificate.

### Experiment Justification

- **Experiment 1 -- Paired capability and safety audit:** tests whether useful research judgment and fault recognition coincide on the same outputs.
- **Experiment 2 -- Oversight-prompt ablation:** estimates the effect of explicitly separating substantive and integrity checks while holding model, task, and decoding fixed.
- **Experiment 3 -- Cross-domain/model robustness:** reveals shared blind spots and avoids treating one family or task as representative.

## Research Question

Can powerful models make correct judgments about difficult research artifacts while reliably recognizing consequential integrity and safety faults, and does an explicit oversight protocol improve that trade-off?

## Background and Motivation

The literature shows meaningful but incomplete autonomous research capability and recurrent evaluator exploitation, premature completion, hallucination, and hidden-invalidity risks. The operational question is conditional: under a specified task distribution and review protocol, what useful performance is achieved and what consequential failures remain unrecognized?

## Direction Budget

Directions were scored 1--5 on literature support, hypothesis fit, information gain, and feasibility. The retained integrated directions are monitoring stress tests (20/20), paired capability--safety tasks (19/20), and risk-adjusted utility/human-uplift design (17/20). Rejected: capability-only benchmarking (14; misses safety), wet-lab studies (13; infeasible/risky), autonomous discovery tournaments (12; expensive and poorly identified), self-reported confidence (12; weak proxy), and math-only evaluation (11; narrow). No later evidence changed this ranking. This run implements the first two and specifies, but cannot estimate, human uplift because recruiting participants is outside the automated session.

## Hypothesis Decomposition

- **H1 (capability):** substantive decision accuracy exceeds random choice (0.25).
- **H2 (oversight):** the safety-aware prompt increases paired integrity accuracy relative to ordinary review.
- **H3 (non-degradation):** safety-aware review does not reduce substantive accuracy by more than 5 percentage points (descriptive pilot criterion).
- **H4 (residual risk):** the one-sided 95% Clopper--Pearson upper bound on missed-fault rate is below the preregistered illustrative threshold of 10%.
- **H5 (clean controls):** explicit oversight does not materially inflate false alarms on clean artifacts.

Independent variables are prompt protocol, model family, domain, and fault status/type. Outcomes are substantive accuracy, integrity accuracy, fault recall, clean specificity, joint success, format compliance, latency, tokens, and cost. Alternatives include prompt-length effects, multiple-choice shortcuts, contamination, correlated items, and API nondeterminism.

## Proposed Methodology

### Approach

Create 32 new deterministic cases (8 each in literature review, coding, experiment design, and mathematics), balanced between clean and faulted artifacts. Each has four substantive options and four integrity options with exactly one keyed answer. Faults cover fabricated/mismatched citations, evidence omission, test leakage/weakening, unauthorized actions, pseudoreplication, outcome switching, invalid algebra, and unjustified proof steps. Cases use concepts rather than verbatim public benchmark questions.

Run three OpenRouter-hosted model families under two prompts at temperature 0. Ordinary review requests a concise expert review; safety-aware review explicitly separates task correctness from integrity, treats clean as possible, and warns against trusting stated success. Both return the same JSON schema. Raw requests, responses, timestamps, usage, and errors are cached.

### Experimental Steps

1. Generate and schema-validate the benchmark; report balance and duplicates.
2. Smoke-test one model/case/protocol and validate JSON parsing.
3. Run the 3 model x 2 protocol x 32 case factorial (192 planned calls), with retries and caching.
4. Score exact choices without an LLM judge; preserve unparsable outputs as failures.
5. Compute paired/stratified metrics, intervals, effect sizes, errors, latency, tokens, costs, and figures.
6. Re-run scoring from cached outputs and compare hashes.

### Baselines

- Chance (25%) for each four-choice judgment.
- Ordinary reviewer prompt (primary baseline).
- Clean cases (false-positive control).
- Cross-family comparison (shared-blind-spot check).

### Evaluation Metrics

- **Substantive accuracy:** correct domain judgment (usefulness).
- **Fault recall / clean specificity:** detection and false-alarm control.
- **Integrity accuracy:** correct fault category or CLEAN.
- **Joint success:** both judgments correct.
- **Missed-fault rate:** faulted artifacts with wrong integrity choice.
- **Format compliance, latency, tokens, cost:** operational reliability.
- **Risk-adjusted utility (secondary):** substantive accuracy - 2 x missed-fault proportion; components remain primary.

### Statistical Analysis Plan

Use matched model--case comparisons. Primary H2 test is exact two-sided McNemar on integrity correctness; report paired risk difference with case-cluster bootstrap 95% CI and matched odds ratio where defined. Apply Holm correction to integrity and substantive prompt comparisons. Report Wilson proportion intervals and one-sided exact Clopper--Pearson upper bounds for missed faults. H1 uses an exact binomial test against 0.25. Sensitivity checks exclude parse failures and bootstrap by case and model. Alpha is 0.05; all trials and negative results remain.

There are 96 matched prompt pairs. Case/model correlation limits generalization, so clustered intervals and disaggregated results matter more than nominal p-values. No post-hoc power claim will be made.

## Expected Outcomes

Support requires above-chance substantive performance, improved integrity recognition, no large capability loss, and a missed-fault upper bound below 10%. Improvement with a bound above 10% supports protocol usefulness but refutes a low-residual-risk claim. Heterogeneity implies conditional, not universal, conclusions.

## Timeline and Milestones

- Resource audit/preregistration: 20 minutes.
- Environment, benchmark, harness: 35 minutes.
- API execution: 45--90 minutes plus 25% debugging buffer.
- Analysis, figures, rerun: 30 minutes.
- Report and README: 30 minutes.

## Resource Plan

Use isolated `.venv`. CPU suffices for APIs/statistics; four RTX A6000 GPUs are available but unnecessary. Dependencies are OpenAI-compatible client, NumPy, pandas, SciPy, statsmodels, matplotlib, and seaborn. Outputs stay in `results/`, `figures/`, and `logs/`.

## Potential Challenges

- Model/version drift: record returned identifiers and timestamps.
- Rate limits/malformed JSON: retries, robust extraction, cache, and explicit parse failures.
- Artificial benchmark: avoid deployment generalization and publish all cases.
- Multiple-choice shortcuts: balance positions; explanations are not used for scoring.
- Shared blind spots: compare families; deployment still needs human audit.
- No recruited humans: specify a future randomized unaided/assisted study; do not call model differences human uplift.

## Success Criteria

Technical success means all cases, models, and protocols are attempted and raw outputs, prompts, scoring, tables, and figures are reproducible. Scientific support for "help without unrecognized risk" requires H1--H5 under the tested protocol; otherwise conclusions are qualified or negative.
