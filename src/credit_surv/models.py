"""
생존분석 모형 5종 통합 인터페이스
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Literal, Optional, Any

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)

ModelType = Literal["KM", "Cox", "AFT", "RSF", "DeepSurv"]


# ======================================================================
# 결과 컨테이너
# ======================================================================
@dataclass
class SurvivalResult:
    """생존모형 추정 결과 표준 컨테이너."""

    model_type: ModelType
    coefficients: Optional[pd.Series] = None  # Cox/AFT
    hazard_ratios: Optional[pd.Series] = None  # exp(coef)
    p_values: Optional[pd.Series] = None
    concordance_index: float = 0.0           # C-index (랭킹 지표)
    log_likelihood: Optional[float] = None
    aic: Optional[float] = None
    bic: Optional[float] = None
    feature_importance: Optional[pd.Series] = None  # RSF/DeepSurv
    n_obs: int = 0
    n_events: int = 0
    raw_model: Any = None

    def summary(self) -> str:
        raise NotImplementedError("TODO: pretty print")


# ======================================================================
# Kaplan-Meier (비모수)
# ======================================================================
class KaplanMeier:
    """비모수 생존함수 추정."""

    def fit(self, durations, events, label: str = "all") -> "KaplanMeier":
        raise NotImplementedError(
            "TODO: from lifelines import KaplanMeierFitter; "
            "self.kmf = KaplanMeierFitter().fit(durations, events, label=label)"
        )

    def survival_function(self) -> pd.DataFrame:
        raise NotImplementedError("TODO: self.kmf.survival_function_")

    def median_survival_time(self) -> float:
        raise NotImplementedError("TODO: self.kmf.median_survival_time_")


# ======================================================================
# Cox PH (준모수)
# ======================================================================
class CoxModel:
    """
    Cox Proportional Hazards Model.

    h(t|x) = h₀(t) × exp(x'β)

    Example:
        >>> cox = CoxModel(duration_col="duration", event_col="event")
        >>> cox.fit(df, covariates=["roa", "debt_ratio", "size"])
        >>> result = cox.summary()
    """

    def __init__(
        self,
        duration_col: str = "duration",
        event_col: str = "event",
        penalizer: float = 0.0,
    ):
        self.duration_col = duration_col
        self.event_col = event_col
        self.penalizer = penalizer
        self.fitted_ = None

    def fit(self, df: pd.DataFrame, covariates: list[str]) -> SurvivalResult:
        raise NotImplementedError(
            "TODO: from lifelines import CoxPHFitter; "
            "cph = CoxPHFitter(penalizer=self.penalizer); "
            "cph.fit(df[[duration_col, event_col] + covariates], "
            "duration_col=self.duration_col, event_col=self.event_col); "
            "SurvivalResult 채우기"
        )

    def predict_survival(self, X: pd.DataFrame, times: list[float]) -> pd.DataFrame:
        """주어진 시점들의 생존확률 예측."""
        raise NotImplementedError("TODO: self.fitted_.predict_survival_function(X, times)")

    def check_proportional_hazards(self) -> pd.DataFrame:
        """비례위험 가정 검정 (Schoenfeld residuals)."""
        raise NotImplementedError("TODO: self.fitted_.check_assumptions(df)")


# ======================================================================
# AFT (모수)
# ======================================================================
class AFTModel:
    """Accelerated Failure Time (Weibull, Log-Normal)."""

    def __init__(self, distribution: str = "weibull"):
        self.distribution = distribution

    def fit(self, df, covariates) -> SurvivalResult:
        raise NotImplementedError(
            "TODO: from lifelines import WeibullAFTFitter or LogNormalAFTFitter"
        )


# ======================================================================
# Random Survival Forest (ML)
# ======================================================================
class RSFModel:
    """
    Random Survival Forest (Ishwaran et al. 2008).

    비선형·상호작용 자동 탐색. SHAP으로 해석 가능.
    """

    def __init__(
        self,
        n_estimators: int = 100,
        max_depth: int = 5,
        random_state: int = 42,
    ):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.random_state = random_state

    def fit(self, X: pd.DataFrame, y) -> SurvivalResult:
        raise NotImplementedError(
            "TODO: from sksurv.ensemble import RandomSurvivalForest; "
            "from sksurv.util import Surv; "
            "y_struct = Surv.from_arrays(event=df.event, time=df.duration); "
            "rsf = RandomSurvivalForest(n_estimators, max_depth, random_state).fit(X, y_struct)"
        )

    def feature_importance(self) -> pd.Series:
        raise NotImplementedError(
            "TODO: from sklearn.inspection import permutation_importance"
        )

    def explain(self, X: pd.DataFrame) -> np.ndarray:
        """SHAP 값 계산."""
        raise NotImplementedError("TODO: shap.TreeExplainer(self.rsf).shap_values(X)")


# ======================================================================
# 모형 비교
# ======================================================================
def compare_survival_models(
    results: list[SurvivalResult],
) -> pd.DataFrame:
    """C-index, AIC, BIC 한 테이블 비교."""
    raise NotImplementedError(
        "TODO: pd.DataFrame([{'model': r.model_type, 'c_index': ...} for r in results])"
    )
