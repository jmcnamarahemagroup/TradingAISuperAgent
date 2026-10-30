# Installation Guide

## Requirements

- Python 3.10+
- pip

## Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# edit .env if using live/testnet keys
streamlit run app/app_streamlit.py
```

## Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
streamlit run app/app_streamlit.py
```

## Packaging

From the repo root:

```bash
bash scripts/package.sh 0.1.0
```

This produces a zip that can be unpacked and run on a fresh machine after `pip install -r requirements.txt`.

## Healthcheck

Open the app and visit the Healthcheck tab. It should report OK with version/env info.
