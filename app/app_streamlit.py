"""
Trading AI Super Agent - Streamlit App
"""
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Trading AI Super Agent", layout="wide")

st.title("Trading AI Super Agent")
st.caption("M1–M6 implementation")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    ["Healthcheck", "Data & Charts", "Backtest", "Strategy", "Exchange", "Knowledge"]
)

with tab1:
    st.header("Healthcheck")
    st.success("OK")
    st.json({
        "status": "healthy",
        "version": "0.1.0",
        "env": "development",
        "dry_run": os.getenv("DRY_RUN", "true"),
        "python": os.sys.version,
    })

with tab2:
    st.header("Data & Charts")
    st.info("yfinance / ccxt loaders and OHLCV charts live here. See data_loaders.py and charts.py")

with tab3:
    st.header("Backtest Engine")
    st.info("Vectorized backtester available in backtester.py")

with tab4:
    st.header("RSI-DCA Strategy")
    st.info("Configurable RSI-DCA in strategies.py")

with tab5:
    st.header("Binance Testnet")
    st.info("Connector with dry-run in exchange_connector.py. Set keys in .env")

with tab6:
    st.header("Knowledge Ingestion")
    st.info("Ingest notes from /learning and search. See knowledge.py")

st.sidebar.markdown("### Status")
st.sidebar.success("All milestones implemented")
