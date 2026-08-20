# Paper outline

## Title and abstract
- Lead with the central result: useful judgments did not establish low residual risk.
- Summarize 32 cases, three Qwen3 sizes, two paired protocols, and 192 trials.
- Evidence: 96.4% substantive accuracy; +3.1 pp prompt differences; 3/48 misses; 15.4% upper bound.

## 1. Introduction
- Motivate the distinction between useful output and recognized integrity faults.
- Identify the gap between capability benchmarks and sabotage/oversight evaluations.
- Introduce the paired capability--integrity audit and point to the pipeline figure.
- Preview quantitative results and state four contributions.
- Citations: PaperBench, RE-Bench, MLE-bench, SWE-bench, TrialMind, FrontierMath, Sabotage Evaluations.

## 2. Related work
- Research and engineering capability benchmarks.
- Literature synthesis and mathematical verification.
- Integrity, evaluator exploitation, and sabotage evaluations.
- Position this work as a same-instance, clean-controlled, rare-event-bounded audit.

## 3. Methodology
- Formalize substantive and integrity choices, correctness, joint success, fault recall, and specificity.
- Describe 32 newly authored balanced cases across four domains and the fault taxonomy.
- Describe ordinary versus safety-aware prompts, exact grading, models, decoding, and compute.
- State chance and ordinary-prompt baselines, hypotheses, paired tests, clustering, and confidence bounds.
- Note the OpenRouter-to-local-Qwen preregistration deviation.

## 4. Results
- Main paired outcomes table: substantive, integrity, and joint accuracy.
- Model/protocol table: accuracy, recall, specificity, misses, and exact upper bounds.
- Figures: model/protocol performance and integrity by domain.
- Error analysis: duplicate-population misses and fabricated-metric misclassification.
- Interpret the prompt comparison as an ablation; distinguish descriptive gains from inference.

## 5. Discussion
- Interpret H1--H5 separately.
- Explain why no observed event is not a safety certificate.
- Cover construct validity, difficulty, family diversity, sample size, no humans/propensity estimate, deterministic decoding, category strictness, and cost measurement.
- Discuss bounded responsible use and risks of overgeneralizing recognition results to deployment.

## 6. Conclusion
- Restate contribution and conditional negative answer.
- Recommend larger, harder, open-ended, multi-family, human-controlled follow-up studies.

## Tables and figures
- `tables/main_results.tex`: paired aggregate outcomes.
- `tables/model_results.tex`: disaggregated safety outcomes.
- `figures/audit_pipeline.tex`: benchmark-to-inference-to-analysis pipeline.
- Existing `performance.png` and `integrity_by_domain.png`, copied from experiment outputs.

## Appendix
- Reproducibility commands and acceptance-rule details.
