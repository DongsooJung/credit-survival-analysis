"""생존모형 테스트 스켈레톤."""
import pytest
import numpy as np
import pandas as pd


@pytest.fixture
def synthetic_panel():
    pytest.skip("load_synthetic_credit_panel 미구현")


class TestCoxModel:
    def test_recovers_known_hazard_ratio(self, synthetic_panel):
        """진짜 HR=exp(0.5)=1.65 ± 0.1 추정 가능해야 함."""
        pytest.skip("CoxModel 미구현")

    def test_concordance_above_chance(self, synthetic_panel):
        """C-index ≥ 0.6"""
        pytest.skip("미구현")


class TestRSF:
    def test_higher_c_index_than_cox_in_nonlinear(self):
        """비선형 데이터에서는 RSF C-index > Cox."""
        pytest.skip("미구현")


class TestKM:
    def test_monotone_decreasing(self, synthetic_panel):
        """Kaplan-Meier 곡선은 단조감소해야 함."""
        pytest.skip("미구현")
