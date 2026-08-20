# Cloned Repositories

## OpenAI MLE-bench

- URL: https://github.com/openai/mle-bench
- Location: `code/mle-bench/`
- Provides: 75 Kaggle competition configurations, preparation/grading logic, agent adapters, splits, and leaderboard aggregation.
- Key entry points: `mlebench`, `experiments/splits/`, `experiments/aggregate_grading_reports.py`.
- Requirements: Kaggle credentials, Git LFS, Docker, and substantial storage/compute. The recommended full setting is too expensive for a smoke test; use one lightweight competition or the 22-task Lite split.
- Research use: capability tasks and deterministic held-out grading. Add immutable action logs and planted safety faults rather than using medal rate alone.

## METR RE-Bench

- URL: https://github.com/METR/RE-Bench
- Location: `code/re-bench/`
- Provides: seven open-ended AI R&D environments in the METR Task Standard, including scaling-law prediction, kernel optimization, model repair, and restricted model design.
- Key entry points: `suite_manifest.yaml`, per-task `manifest.yaml`, and `setup/`.
- Requirements: Vivaria/task-standard infrastructure; several tasks require GPUs. Protected reference solutions must remain hidden.
- Research use: time-budgeted human/agent comparison and realistic opportunities for reward hacking; suitable for the paired capability–safety design.

## OpenAI Preparedness / Frontier Evals

- URL: https://github.com/openai/preparedness
- Location: `code/openai-preparedness/`
- Provides: PaperBench, SWE-Lancer, and EVMbench evaluation code.
- Key entry point: `project/paperbench/`; each project has its own `pyproject.toml` and `uv.lock`.
- Requirements: project-specific `uv sync`, containers, model API access, and substantial experiment compute.
- Research use: PaperBench's hierarchical rubrics, author-backed grading criteria, and judge calibration are the primary template for research-output scoring.

## Validation

All repositories were shallow-cloned successfully and their top-level documentation and relevant entry points were inspected. Full executions were not attempted because they require model API credentials, Docker/Vivaria, Kaggle credentials, and/or GPUs; these are documented blockers rather than installation failures.
