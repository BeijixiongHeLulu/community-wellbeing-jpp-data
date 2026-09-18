# Community well-being JPP analysis data

This is the independent data repository for the current *Journal of Positive Psychology* manuscript. It is not the repository for the Chinese journal (xuebao) paper.

The data files are a reduced shared subset; `results/` retains the original full-sample outputs.

The repository contains only de-identified, processed data that directly enter the reported questionnaire, IAT behavioral, and ERP analyses. Raw EEG recordings, raw task logs, questionnaire item responses, demographics, qualitative materials, photographs, and any identity key are excluded.

## Contents

- `data/questionnaire/questionnaire_analysis_ready.csv`: 57 participants (29 high-support, 28 low-support), four scale scores and the resident well-being composite used in manuscript Table 5.
- `data/behavior/iat_subject_analysis_ready.csv`: 57 participants (27 high-support, 30 low-support), the five subject-level IAT outcomes used in manuscript Table 6, plus non-identifying response-count/QC summaries.
- `data/erp/erp_subject_cell_analysis_ready.csv`: 55 participants (25 high-support, 30 low-support), four locked ERP endpoints × four within-subject conditions = 880 rows, used in the final 2 × 2 × 2 mixed models.
- `results/`: original full-sample questionnaire/IAT group comparisons and frozen ERP fixed-effect, gate-released follow-up, and model-metric outputs supporting manuscript Table 7 and Supplementary Table S2.
- `config/erp_endpoints.csv`: locked time windows, electrode sets, and factor definitions.
- `docs/data_dictionary.md`: variable-level definitions.
- `docs/provenance.md`: source binding, privacy decisions, and known limitations.

## Reproduce and validate

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python code/reproduce_tables.py
```

The validation script recomputes all questionnaire and IAT means, standard deviations, Welch tests, degrees of freedom, Benjamini-Hochberg q values, and Hedges' g values. It also verifies the released ERP sample, four-cell completeness, and result-table row counts.

## Privacy and scope

Identifiers are modality-specific (`Q...`, `IAT...`, `ERP...`). They deliberately cannot be joined across questionnaire, behavior, and ERP files. The shared subset does not fully reproduce the original full-sample results. No re-identification key is included.

The repository is public. No explicit data or code licence has been assigned; see `DATA_USE.md` for the current use status.
