"""
신용 생존데이터 로더

생존분석 표준 형식:
    columns:
        - firm_id: str
        - duration: float (관측 시작부터 사건/검열까지 기간, 일)
        - event: 0/1 (1=부도, 0=관측 종료까지 생존)
        - covariates: 재무비율, 산업, 거시 변수 등
"""
from __future__ import annotations

import logging
from typing import Literal, Optional

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)

EventType = Literal["default", "downgrade", "delisting"]


def load_credit_panel(
    event_type: EventType = "default",
    data_dir: str = "data/processed",
    industries: Optional[list[str]] = None,
    year_range: Optional[tuple[int, int]] = None,
) -> pd.DataFrame:
    """
    신용 생존데이터 로드.

    Args:
        event_type: 'default' | 'downgrade' | 'delisting'
        data_dir: parquet 파일 경로
        industries: KSIC 코드 필터 (예: ['C', 'F'] = 제조·건설)
        year_range: 관측 시작 연도 범위

    Returns:
        long-format 또는 단일행 형식 DataFrame
        Standard columns:
            - firm_id, duration, event,
            - 재무: roa, debt_ratio, current_ratio, ocf_ratio
            - 산업: industry_ksic
            - 거시: kospi_return, gdp_growth
    """
    raise NotImplementedError(
        "TODO: pd.read_parquet(f'{data_dir}/credit_{event_type}.parquet'); "
        "industries/year_range 필터링"
    )


def load_synthetic_credit_panel(
    n_firms: int = 1000,
    max_duration: int = 365 * 5,
    censoring_rate: float = 0.6,
    seed: int = 42,
) -> pd.DataFrame:
    """
    Cox 모형 검증용 합성 생존 데이터 생성.

    True hazard:
        h(t|x) = h₀(t) × exp(0.5·debt_ratio - 0.3·roa)

    Returns:
        ['firm_id', 'duration', 'event', 'roa', 'debt_ratio', 'industry'] 컬럼
    """
    raise NotImplementedError(
        "TODO: from lifelines.datasets 또는 직접 시뮬레이션 — "
        "Weibull baseline + 공변량 의존 hazard"
    )


def to_survival_format(
    transactions: pd.DataFrame,
    firm_id_col: str = "firm_id",
    start_col: str = "obs_start",
    event_col: str = "default_date",
    censor_date: Optional[pd.Timestamp] = None,
) -> pd.DataFrame:
    """
    Long-format → 생존 표준 (duration, event) 형식 변환.

    Args:
        transactions: 기업별 시계열 (재무비율 등)
        censor_date: 검열 기준일 (None이면 max(date))
    """
    raise NotImplementedError(
        "TODO: groupby(firm_id) → "
        "duration = (event_date or censor_date) - start_date; "
        "event = (event_date is not null).astype(int)"
    )
