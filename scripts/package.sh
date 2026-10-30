#!/usr/bin/env bash
# Package script - creates a distributable zip from clean checkout
set -e
VERSION=${1:-0.1.0}
OUT="TradingAISuperAgent-${VERSION}.zip"

echo "Creating package ${OUT}..."
zip -r "${OUT}" \
  app/ \
  .github/ \
  docs/ \
  learning/ \
  scripts/ \
  tests/ \
  requirements.txt \
  README.md \
  .env.example \
  .gitignore \
  --exclude "*.pyc" --exclude "__pycache__/*" --exclude ".venv/*"

echo "Done: ${OUT}"
echo "To install on a fresh machine:"
echo "  unzip ${OUT} && cd TradingAISuperAgent && pip install -r requirements.txt && streamlit run app/app_streamlit.py"
