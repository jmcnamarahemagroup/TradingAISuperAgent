# Trading AI Super Agent

A Streamlit-based trading research and execution platform supporting data loading, charting, backtesting, strategy development (RSI-DCA), exchange connectivity (Binance testnet), and knowledge ingestion.

## Features

- **Data**: yfinance + ccxt loaders with caching and error handling
- **Charts**: Robust OHLCV candlestick + volume plots
- **Backtesting**: Vectorized single-asset engine with fees, slippage, position sizing
- **Strategy**: Configurable RSI-DCA
- **Execution**: Binance testnet connector with dry-run mode
- **Knowledge**: Ingest and search notes/transcripts
- **Packaging**: Cross-platform install and packaging scripts

## Quick Start

```bash
# Clone
git clone https://github.com/jmcnamarahemagroup/TradingAISuperAgent.git
cd TradingAISuperAgent

# Install
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt

# Copy env
cp .env.example .env
# Edit .env with your API keys if needed

# Run
streamlit run app/app_streamlit.py
```

See [docs/INSTALL.md](docs/INSTALL.md) for full installation instructions.

## Project Status

This repository implements the full M1–M6 roadmap defined in the original issues.

## License

MIT
