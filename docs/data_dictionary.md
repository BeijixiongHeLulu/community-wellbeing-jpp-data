# Data dictionary

## Questionnaire

- `participant_id`: repository-only questionnaire identifier; not linkable to other modalities.
- `community_group`: `high-support` or `low-support`.
- `positive_affect`: mean positive-affect score from the reported MUNSH scoring.
- `negative_affect`: mean negative-affect score from the reported MUNSH scoring.
- `life_satisfaction`: mean life-satisfaction score used in the manuscript.
- `belonging`: relatedness/belonging mean score used in the manuscript.
- `resident_experience_composite`: equal-weight mean of sample z scores for positive affect, reversed negative affect, life satisfaction, and belonging (original N=62 sample SD, `ddof=1`; retained without restandardizing the shared subset).

## IAT behavior

- `participant_id`: repository-only IAT identifier; not linkable to other modalities.
- `community_group`: `high-support` or `low-support`.
- `iat_d_score`: participant-level IAT D score under the locked analysis specification.
- `accuracy`: proportion correct across formal responses before RT trimming.
- `compatible_rt_ms`, `incompatible_rt_ms`: mean correct-response latency after dropping error responses and restricting RT to 300–3000 ms.
- `rt_difference_ms`: incompatible minus compatible RT.
- `n_compatible_responses`, `n_incompatible_responses`: retained units entering the condition means.
- `raw_response_count`: number of formal component responses before error/RT exclusion.
- `error_rate`, `fast_response_rate_under_300ms`: non-identifying participant-level processing summaries.

## ERP

- `participant_id`: repository-only ERP identifier; consistent across the four ERP endpoints but not linkable to questionnaire/IAT IDs.
- `endpoint_id`: one of `word_N2`, `picture_P3`, `word_P3`, `picture_LPP`.
- `lock`: stimulus-locking event (`word` or `picture`).
- `erp_component`: N2, P3, or LPP.
- `window_start_ms`, `window_end_ms`: locked mean-amplitude window.
- `electrodes`: locked equal-weight electrode set.
- `compatibility`: compatible or incompatible IAT mapping.
- `stimulus_factor`, `stimulus_level`: word valence or picture type and its level.
- `semantic_cell_id`: explicit within-subject cell label.
- `retained_trial_count`: accepted epochs contributing to the cell mean.
- `mean_amplitude_uv`: participant-level mean ERP amplitude in microvolts.

## Result files

Questionnaire and IAT result files report group means/SDs, high-minus-low mean differences, analytical Welch 95% CIs, Welch t/df/p, BH q, and Hedges' g. ERP result fields preserve the frozen model output. `q_bh_subset7` is adjusted across the seven non-intercept fixed effects within an endpoint; `p_holm_family` is Holm-adjusted within the released follow-up family.
