"""Vectorized single-asset backtester."""
import pandas as pd
import numpy as np
from typing import Dict, Any


def run_backtest(
    df: pd.DataFrame,
    signals: pd.Series,
    initial_capital: float = 10000.0,
    fee_rate: float = 0.001,
    slippage: float = 0.0005,
    position_size: float = 1.0,
) -> Dict[str, Any]:
    """
    Deterministic vectorized backtest.
    signals: 1 = long, -1 = short, 0 = flat (or series of position targets)
    """
    if df.empty or signals.empty:
        return {"error": "Empty data or signals"}

    close = df["close"].values if "close" in df.columns else df.iloc[:, 3].values
    signals = signals.reindex(df.index).fillna(0).values

    positions = np.zeros(len(close))
    cash = np.zeros(len(close))
    equity = np.zeros(len(close))

    cash[0] = initial_capital
    equity[0] = initial_capital

    for i in range(1, len(close)):
        prev_pos = positions[i - 1]
        target = signals[i] * position_size

        trade_qty = target - prev_pos
        if abs(trade_qty) > 1e-8:
            price = close[i] * (1 + np.sign(trade_qty) * slippage)
            cost = trade_qty * price
            fee = abs(cost) * fee_rate
            cash[i] = cash[i - 1] - cost - fee
            positions[i] = target
        else:
            cash[i] = cash[i - 1]
            positions[i] = prev_pos

        equity[i] = cash[i] + positions[i] * close[i]

    results = pd.DataFrame({
        "close": close,
        "position": positions,
        "cash": cash,
        "equity": equity,
    }, index=df.index)

    total_return = (equity[-1] / initial_capital) - 1
    return {
        "results": results,
        "final_equity": equity[-1],
        "total_return": total_return,
        "max_drawdown": (equity / np.maximum.accumulate(equity) - 1).min(),
    }
