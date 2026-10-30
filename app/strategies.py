"""RSI-DCA strategy (configurable)."""
import pandas as pd
import numpy as np


def compute_rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain = delta.where(delta > 0, 0).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


def rsi_dca_signals(
    df: pd.DataFrame,
    rsi_period: int = 14,
    rsi_buy: float = 30.0,
    rsi_sell: float = 70.0,
    dca_steps: int = 3,
    cooldown_bars: int = 5,
) -> pd.Series:
    """Generate position signals for RSI-DCA. Config-driven."""
    close = df["close"] if "close" in df.columns else df.iloc[:, 3]
    rsi = compute_rsi(close, rsi_period)

    signals = pd.Series(0.0, index=df.index)
    position = 0.0
    last_trade = -cooldown_bars

    for i in range(len(df)):
        if i - last_trade < cooldown_bars:
            signals.iloc[i] = position
            continue

        r = rsi.iloc[i]
        if pd.isna(r):
            signals.iloc[i] = position
            continue

        if r <= rsi_buy and position < dca_steps:
            position += 1.0 / dca_steps
            last_trade = i
        elif r >= rsi_sell and position > 0:
            position = 0.0
            last_trade = i

        signals.iloc[i] = position

    return signals
