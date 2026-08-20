# Resources Catalog

## Summary

The workspace contains nine validated papers, three locally available benchmark/sample datasets, and three shallow-cloned official evaluation repositories. The selection emphasizes joint measurement of research usefulness and failures that escape oversight.

## Papers

| Title | Year | File | Key use |
|---|---:|---|---|
| MLE-bench | 2025 | `papers/2410.07095_mle_bench.pdf` | ML engineering and medal-based human reference |
| PaperBench | 2025 | `papers/2504.01848_paperbench.pdf` | Author-backed hierarchical replication rubrics |
| RE-Bench | 2024 | `papers/2411.15114_re_bench.pdf` | AI R&D tasks, human time budgets, exploit analysis |
| FrontierMath | 2024 | `papers/2411.04872_frontiermath.pdf` | Difficult, novel mathematical reasoning |
| TrialMind | 2024 | `papers/2406.17755_trialmind.pdf` | Literature search/screen/extraction and human uplift |
| MLAgentBench | 2023 | `papers/2310.03302_mlagentbench.pdf` | Iterative ML experimentation traces |
| The AI Scientist | 2024 | `papers/2408.06292_ai_scientist.pdf` | End-to-end autonomous research baseline |
| SWE-bench | 2024 | `papers/2310.06770_swe_bench.pdf` | Repository-scale coding with tests |
| Sabotage Evaluations | 2024 | `papers/anthropic_2024_sabotage_evaluations.pdf` | Concealed attack and mitigation-aware safety metrics |

See `papers/README.md` for authors and annotations.

## Datasets

| Name | Source | Local material | Task | Notes |
|---|---|---|---|---|
| SWE-bench Lite | Hugging Face | 16 validated rows | Coding | Full download instructions provided |
| MLE-bench metadata | OpenAI/Kaggle | LFS pointer plus cloned configs | ML engineering | Full Lite data is ~158 GB and needs credentials |
| RE-Bench asset | METR repository | 1,000 JSONL records | Research engineering | Full task assets live in cloned repo |

See `datasets/README.md` for schemas, licenses, and reproducible download/build instructions.

## Code repositories

| Name | URL | Location | Purpose |
|---|---|---|---|
| MLE-bench | https://github.com/openai/mle-bench | `code/mle-bench/` | Preparation, agents, grading, splits |
| RE-Bench | https://github.com/METR/RE-Bench | `code/re-bench/` | Seven METR-standard AI R&D environments |
| Frontier Evals | https://github.com/openai/preparedness | `code/openai-preparedness/` | PaperBench and other frontier evals |

## Search and selection notes

The primary paper-finder was attempted first and failed twice (missing `httpx`, then server HTTP 500); `httpx` was installed locally and the service failure was preserved in `paper_search_results/`. Manual search used arXiv, Semantic Scholar-indexed records, official project pages, and citation chasing. Papers were retained when they offered realistic tasks, objective/expert grading, human comparisons, or operational hidden-risk measures. Nine PDFs were downloaded and parsed successfully; three central papers received complete chunk-by-chunk processing.

No explicit resources or staged local assets were supplied in the topic specification. Full MLE-bench data was not downloaded because even the Lite split is approximately 158 GB and requires Kaggle credentials; a small SWE-bench API sample and RE-Bench asset provide immediate schema-level experiment inputs. The MLE CSV fetched from raw GitHub is a Git-LFS pointer, documented transparently rather than treated as usable data.

## Recommendations for experiment design

1. **Primary tasks:** start with a small PaperBench rubric subset, one lightweight RE-Bench or MLE-bench task, SWE-bench Lite instances, TrialMind-style extraction records, and expert-verifiable math items.
2. **Baselines:** unaided human, human+agent, single-call model, standard agent scaffold, and deliberately faulted/adversarial agent.
3. **Metrics:** rubric/test score, time, cost, uplift, undetected consequential error, planted-fault recall and false positives, unauthorized actions, calibration, and attack success under a fixed review budget.
4. **Code reuse:** PaperBench for rubrics/judge calibration; RE-Bench for time-budgeted environments and trajectory analysis; MLE-bench for deterministic grading and repeated-seed conventions.
5. **Safety rule:** preregister a maximum acceptable one-sided confidence bound on undetected consequential failures. Do not infer safety from a capability score or an absence of observed incidents alone.

The ranked directions, rejected alternatives, and concrete minimum experiment appear in `planning.md`.

## Experiment-runner additions (2026-08-20)

- Authored `datasets/research_agent_audit.json`: 32 unique, balanced cases across literature review, coding, experiment design, and mathematics; 16 clean and 16 planted-fault artifacts.
- Implemented deterministic construction (`src/build_benchmark.py`), OpenRouter/direct API harness (`src/run_experiment.py`), local real-model GPU harness (`src/run_local_models.py`), and preregistered scoring/statistics (`src/analyze.py`).
- OpenRouter returned HTTP 403 because the supplied key's total limit was exceeded; `OPENAI_API_KEY` was empty. The executed fallback used downloaded Qwen3-4B/8B/14B weights, not simulated agents.
- Completed 192 trials. Primary outputs: `results/raw_outputs_{small,14b}.json`, `results/scored_trials.csv`, `results/statistical_results.json`, `results/error_cases.csv`, and `figures/`.
- Exact environment and reproducibility hashes are in `results/environment.json` and `results/hashes.json`. Full interpretation is in `REPORT.md`.
