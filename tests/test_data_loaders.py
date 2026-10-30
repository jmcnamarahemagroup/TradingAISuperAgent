"""Basic loader tests (mocked / smoke)."""
def test_import_loaders():
    from app.data_loaders import get_ohlcv_yf, load_ohlcv_ccxt
    assert callable(get_ohlcv_yf)
    assert callable(load_ohlcv_ccxt)
