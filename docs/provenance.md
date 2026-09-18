# Provenance and release decisions

The released data are a reduced shared subset. The inputs and frozen results described below refer to the original full sample.

## Bound analysis inputs

- Questionnaire: the 62-row processed scale-score dataset that reproduces current manuscript Table 5 (32 high-support, 30 low-support).
- IAT: the frozen N=62 participant selection and one locked multiverse specification: formal blocks, event-level units, event errors removed, 300–3000 ms retained RTs, legacy event-SD D formula, and the accuracy threshold recorded in the source analysis.
- ERP: the four final `stage2_v2/rank_01` endpoint cell tables on the verified T7 EEG data volume. These are the endpoint data underlying the current manuscript's final mixed-model fingerprints.

SHA-256 source and release hashes are stored in `MANIFEST.csv`. Local absolute paths and community names are intentionally omitted from the repository.

## De-identification

Only processed variables necessary for the reported analyses are included. Direct identifiers, demographics, source participant numbers, raw item patterns, raw task logs, raw EEG, photographs, and qualitative materials are excluded. Modality-specific identifiers prevent unintended cross-modal linkage.

## Known limitation

The questionnaire Welch confidence intervals are reproduced analytically and match the bound table. For the IAT table, the current bound source/script reproduces all displayed means, SDs, mean differences, t values, df, BH q values, and Hedges' g values. The manuscript's displayed IAT confidence intervals came from an earlier bootstrap output whose resampling artefact is not reproducibly bound; this repository therefore reports clearly labelled analytical Welch confidence intervals rather than claiming to reproduce that legacy bootstrap step.

ERP result CSVs are frozen outputs of the REML MMRM with an unstructured four-cell within-subject covariance matrix and denominator df=58. The release validates input completeness and output fingerprints; the full upstream EEG preprocessing/search environment remains in the controlled project archive rather than being duplicated here.
