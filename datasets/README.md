# Downloaded Datasets

Data files are excluded from Git. The local samples verify schemas and permit smoke tests; full benchmark payloads require the upstream credentials or compute described below.

## SWE-bench Lite sample

- Source: `princeton-nlp/SWE-bench_Lite` on Hugging Face
- Local: `swe_bench_lite/samples/first_rows.json`
- Validated: 16 rows; fields include repository, base commit, problem statement, patch, test patch, and pass/fail tests.
- Task: resolve real Python repository issues under executable tests.
- License: follows source repositories and dataset terms; inspect upstream before redistribution.
- Full download:

```python
from datasets import load_dataset
ds = load_dataset("princeton-nlp/SWE-bench_Lite", split="test")
ds.save_to_disk("datasets/swe_bench_lite/full")
```

## MLE-bench metadata

- Source: OpenAI MLE-bench repository/Kaggle
- Local: `mle_bench_metadata/competition_categories.csv`
- Status: the upstream raw GitHub object is a Git-LFS pointer (129 bytes), correctly identified during validation; benchmark code and per-competition configurations are available in `code/mle-bench`.
- Scale: 75 competitions; Lite is 22 competitions and approximately 158 GB, versus about 3.3 TB for the full set.
- Full download requires Kaggle credentials:

```bash
cd code/mle-bench
mlebench prepare --lite
cd -
```

Use a single small competition first (for example `detecting-insults-in-social-commentary`) to control cost.

## RE-Bench asset sample

- Source: METR RE-Bench, `ai_rd_optimize_llm_foundry/assets/train_data.jsonl`
- Local: `re_bench_assets/samples/train_data_sample.jsonl`
- Validated: 1,000 JSONL prompt/response records.
- Task: fixed-data input for the LLM Foundry optimization environment.
- License: MIT repository license.
- Full benchmark: already present in `code/re-bench`; task assets are built through its METR Task Standard manifests. Some protected solutions intentionally require the password documented upstream and must not be exposed to evaluated agents.

## Quick EDA result

All JSON/JSONL samples parse successfully. SWE-bench has nested lists and patch text; RE-Bench has two string fields (`prompt`, `response`). No schema corruption was observed. The MLE metadata download is deliberately recorded as an LFS pointer rather than falsely treated as CSV data.
