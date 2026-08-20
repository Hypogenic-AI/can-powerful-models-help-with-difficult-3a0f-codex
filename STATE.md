# Research State

- Current phase: `None`
- Pipeline completed: `True`

## Previous phases

resource_finder (succeeded), experiment_runner (succeeded)

## Current phase context

- Phase: `experiment_runner`
- Status: `completed`
- Started: `2026-08-20T02:12:17.767725Z`
- Next steps:
  - Validate the report and experimental artifacts before finalizing.

## Workspace check

- Expected: `/workspaces/can-powerful-models-help-with-difficult-3a0f-codex`
- Actual: `/app`
- Directory usable: `True`
- Current process matches workspace: `False`

## Output validation

- Valid: `True`
- Expected: `REPORT.md`
- Missing: None
- Outside workspace: None

## Agent notes

<!-- NEURICO_AGENT_NOTES_START -->
### resource_finder
<!-- NEURICO_AGENT_NOTES_START:resource_finder -->
Phase `resource_finder` completed 2026-08-20. Verified workspace root despite stale generated `/app` check; created isolated `.venv` and local `pyproject.toml`. Artifacts: 9 validated PDFs (`papers/`), 3 official shallow clones (`code/`), 3 validated dataset/sample resources (`datasets/`), plus `literature_review.md`, `resources.md`, and `planning.md`. Deep-read all chunks of PaperBench, RE-Bench, and Sabotage Evaluations. Top directions retained: paired capability–safety tasks, monitoring stress tests, and human uplift with risk-adjusted utility; rejected directions are scored in `planning.md`. Key evidence paths: `papers/pages/`, `code/{mle-bench,re-bench,openai-preparedness}`, and dataset validation notes in `datasets/README.md`.

Next phase: `experiment_runner`. Implement a lightweight stratified task set; preregister capability and undetected-failure thresholds; run unaided/assisted/autonomous conditions with clean, planted-fault, and adversarial trials; use held-out tests, immutable logs, blinded grading, repeated seeds, and one-sided rare-event bounds. Uncertainty: paper-finder returned HTTP 500 (manual multi-source fallback used); MLE-bench Lite is ~158 GB and Kaggle-gated, and the raw metadata CSV is an LFS pointer; full benchmark executions require API credentials, containers/Vivaria, and often GPUs.
<!-- NEURICO_AGENT_NOTES_END:resource_finder -->

### experiment_runner
<!-- NEURICO_AGENT_NOTES_START:experiment_runner -->
Phases 1--6 complete. Reviewed gathered evidence and preregistered a 32-case, four-domain paired capability--safety audit (`planning.md`). Built/validated balanced data and modular harnesses (`datasets/research_agent_audit.json`, `src/`). OpenRouter was blocked by a hard 403 total-key limit and the direct OpenAI key was empty; documented deviation used real downloaded Qwen3-4B/8B/14B models on one RTX A6000. Completed all 192 trials with zero parse failures. Result: substantive accuracy 96.4%; safety-aware integrity accuracy 96.9% vs 93.8% ordinary (+3.1 pp, Holm p=.50); 3/48 safety-prompt faults missed, one-sided 95% upper bound 15.4%, failing preregistered 10% threshold; 0/48 clean false alarms. Conclusion: bounded usefulness demonstrated, low unrecognized residual risk not established. Artifacts: `results/`, `figures/`, `REPORT.md`, `README.md`. Validation: compilation passed; regenerated benchmark and analysis outputs were byte-identical. Remaining uncertainty: small artificial multiple-choice task set, one model family, no human participants, mathematical ceiling effect.
<!-- NEURICO_AGENT_NOTES_END:experiment_runner -->

<!-- NEURICO_AGENT_NOTES_END -->
