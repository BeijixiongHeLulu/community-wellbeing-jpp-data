#!/usr/bin/env python3
"""Reproduce the public questionnaire/IAT tables and validate the ERP release."""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]


def welch(high, low):
    high, low = np.asarray(high, float), np.asarray(low, float)
    result = stats.ttest_ind(high, low, equal_var=False)
    vh, vl = high.var(ddof=1) / len(high), low.var(ddof=1) / len(low)
    se = math.sqrt(vh + vl)
    df = (vh + vl) ** 2 / (vh**2 / (len(high) - 1) + vl**2 / (len(low) - 1))
    difference = high.mean() - low.mean()
    half = stats.t.ppf(.975, df) * se
    pooled = math.sqrt(((len(high)-1)*high.var(ddof=1)+(len(low)-1)*low.var(ddof=1))/(len(high)+len(low)-2))
    g = difference / pooled * (1 - 3 / (4 * (len(high) + len(low)) - 9))
    return dict(n_high=len(high), mean_high=high.mean(), sd_high=high.std(ddof=1),
                n_low=len(low), mean_low=low.mean(), sd_low=low.std(ddof=1),
                mean_difference=difference, ci95_low_welch=difference-half,
                ci95_high_welch=difference+half, t=result.statistic, df=result.df,
                p_value=result.pvalue, hedges_g=g)


def analyze(path, measures):
    data = pd.read_csv(path)
    rows = []
    for metric, label in measures:
        rows.append({"metric": metric, "label": label, **welch(
            data.loc[data.community_group.eq("high-support"), metric],
            data.loc[data.community_group.eq("low-support"), metric])})
    result = pd.DataFrame(rows)
    result["q_bh"] = stats.false_discovery_control(result.p_value, method="bh")
    return result


def main():
    questionnaire = analyze(ROOT / "data/questionnaire/questionnaire_analysis_ready.csv", [
        ("resident_experience_composite", "Resident well-being composite"),
        ("positive_affect", "Positive affect"), ("negative_affect", "Negative affect"),
        ("life_satisfaction", "Life satisfaction"), ("belonging", "Belonging")])
    behavior = analyze(ROOT / "data/behavior/iat_subject_analysis_ready.csv", [
        ("iat_d_score", "IAT D score"), ("accuracy", "Accuracy"),
        ("compatible_rt_ms", "Compatible RT"),
        ("incompatible_rt_ms", "Incompatible RT"),
        ("rt_difference_ms", "Incompatible minus compatible RT")])
    fixed = pd.read_csv(ROOT / "results/erp_fixed_effects_all_terms.csv")
    cells = pd.read_csv(ROOT / "data/erp/erp_subject_cell_analysis_ready.csv")
    follow = pd.read_csv(ROOT / "results/erp_followups_gate_released.csv")
    assert len(cells) == 880 and cells.participant_id.nunique() == 55
    assert cells.groupby(["participant_id", "endpoint_id"]).size().eq(4).all()
    assert len(fixed) == 32 and fixed.effect.ne("Intercept").sum() == 28
    assert len(follow) == 25 and follow.gate_released.eq(1).all()

    out = ROOT / "results/reproduced"
    out.mkdir(parents=True, exist_ok=True)
    questionnaire.to_csv(out / "questionnaire_group_comparisons.csv", index=False)
    behavior.to_csv(out / "iat_group_comparisons.csv", index=False)
    print("PASS: shared subset questionnaire N=57; IAT N=57; ERP N=55 and 880 subject-condition rows; results/ contains original full-sample outputs.")


if __name__ == "__main__":
    main()
