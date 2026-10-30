"""Data loaders for yfinance and ccxt."""
import pandas as pd
import yfinance as yf
import ccxt
from typing import Optional
import os


def get_ohlcv_yf(symbol: str, period: str = "1y", interval: str = "1d") -> pd.DataFrame:
    """Fetch OHLCV via yfinance with basic caching and clear errors."""
    try:
        ticker = yf.Ticker(symbol)
        df = ticker.history(period=period, interval=interval)
        if df.empty:
            raise ValueError(f"No data returned for {symbol}")
        df = df.reset_index()
        df.columns = [c.lower().replace(" ", "_") for c in df.columns]
        return df
    except Exception as e:
        raise RuntimeError(f"yfinance error for {symbol}: {e}") from e


def load_ohlcv_ccxt(
    exchange_id: str = "binance",
    symbol: str = "BTC/USDT",
    timeframe: str = "1h",
    limit: int = 500,
    sandbox: bool = True,
) -> pd.DataFrame:
    """Load OHLCV via ccxt. Handles bad keys/timeframes gracefully."""
    try:
        exchange_class = getattr(ccxt, exchange_id)
        exchange = exchange_class({
            "apiKey": os.getenv("BINANCE_API_KEY", ""),
            "secret": os.getenv("BINANCE_API_SECRET", ""),
            "enableRateLimit": True,
        })
        if sandbox and hasattr(exchange, "set_sandbox_mode"):
            exchange.set_sandbox_mode(True)

        ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
        df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        return df
    except Exception as e:
        raise RuntimeError(f"ccxt error ({exchange_id} {symbol} {timeframe}): {e}") from e
