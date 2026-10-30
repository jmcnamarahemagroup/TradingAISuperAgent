"""OHLCV charting with robust column handling."""
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd


def plot_ohlcv(df: pd.DataFrame, title: str = "OHLCV") -> go.Figure:
    """Create candlestick + volume chart. Handles various column name variants."""
    if df is None or df.empty:
        fig = go.Figure()
        fig.update_layout(title="No data to plot")
        return fig

    # Normalize columns
    col_map = {}
    for c in df.columns:
        cl = c.lower()
        if "open" in cl:
            col_map["open"] = c
        elif "high" in cl:
            col_map["high"] = c
        elif "low" in cl:
            col_map["low"] = c
        elif "close" in cl:
            col_map["close"] = c
        elif "volume" in cl or "vol" in cl:
            col_map["volume"] = c
        elif "time" in cl or "date" in cl or "timestamp" in cl:
            col_map["time"] = c

    required = ["open", "high", "low", "close"]
    if not all(k in col_map for k in required):
        fig = go.Figure()
        fig.update_layout(title=f"Missing required columns. Found: {list(df.columns)}")
        return fig

    time_col = col_map.get("time", df.index)
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03, row_heights=[0.7, 0.3])

    fig.add_trace(
        go.Candlestick(
            x=df[time_col] if isinstance(time_col, str) else df.index,
            open=df[col_map["open"]],
            high=df[col_map["high"]],
            low=df[col_map["low"]],
            close=df[col_map["close"]],
            name="OHLC",
        ),
        row=1, col=1,
    )

    if "volume" in col_map:
        fig.add_trace(
            go.Bar(x=df[time_col] if isinstance(time_col, str) else df.index, y=df[col_map["volume"]], name="Volume"),
            row=2, col=1,
        )

    fig.update_layout(title=title, xaxis_rangeslider_visible=False, height=600)
    return fig
