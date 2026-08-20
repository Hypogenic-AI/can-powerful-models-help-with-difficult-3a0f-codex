# Paired Capability--Safety Evaluation for Research Agents

This project tests real instruction models on substantive and integrity judgments spanning literature review, coding, experiment design, and mathematics. It pairs useful-task scoring with planted-fault recognition so high capability cannot conceal residual safety risk.

## Key findings

- Qwen3 4B/8B/14B achieved 96.4% substantive accuracy across 192 real GPU inference trials.
- Safety-aware review improved substantive and integrity accuracy by 3.1 percentage points, but paired effects were not significant after Holm correction (adjusted *p*=.50).
- Safety-aware review missed 3/48 planted faults (6.25%); the one-sided 95% upper bound was 15.4%, failing the preregistered 10% criterion.
- It produced 0/48 false alarms on clean artifacts; ordinary review produced two.
- The pilot demonstrates usefulness, but does not establish usefulness without unrecognized safety risk.

See [REPORT.md](REPORT.md) for the complete methods, results, figures, limitations, and references.

## Reproduce

```bash
uv venv
source .venv/bin/activate
uv sync
python src/build_benchmark.py

# Requires an NVIDIA GPU; downloads real Qwen3 weights.
export CC="$PWD/scripts/zigcc"
python src/run_local_models.py --models Qwen/Qwen3-4B Qwen/Qwen3-8B --output results/raw_outputs_small.json
HF_HOME="$PWD/.hf_cache" python src/run_local_models.py --models Qwen/Qwen3-14B --batch-size 12 --output results/raw_outputs_14b.json

python src/analyze.py
```

To reproduce only the scoring and figures from cached raw outputs, run `python src/analyze.py`. Python 3.12.8 and exact dependencies in `uv.lock` were used. The local run used one 49 GB RTX A6000.

## Structure

- `planning.md` — preregistered hypotheses, thresholds, and statistical plan
- `literature_review.md`, `resources.md`, `papers/` — evidence synthesis and gathered sources
- `datasets/research_agent_audit.json` — 32 balanced audit cases
- `src/` — benchmark builder, API/local inference harnesses, and analysis
- `results/` — raw outputs, scored trials, statistics, errors, hashes, environment
- `figures/` — publication-ready result plots
- `REPORT.md` — primary research report
