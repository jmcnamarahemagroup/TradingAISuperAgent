"""Smoke tests for backtester."""
import pandas as pd
import numpy as np
from app.backtester import run_backtest


def test_backtest_deterministic():
    idx = pd.date_range("2024-01-01", periods=10, freq="D")
    df = pd.DataFrame({
        "close": np.linspace(100, 110, 10),
    }, index=idx)
    signals = pd.Series([0, 1, 1, 1, 0, 0, 1, 1, 0, 0], index=idx)
    res1 = run_backtest(df, signals)
    res2 = run_backtest(df, signals)
    assert res1["final_equity"] == res2["final_equity"]
    assert "results" in res1
