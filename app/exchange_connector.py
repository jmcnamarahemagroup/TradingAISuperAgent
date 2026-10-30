"""Binance testnet connector with dry-run support."""
import ccxt
import os
from typing import Dict, Any


class BinanceTestnetConnector:
    def __init__(self, dry_run: bool = True):
        self.dry_run = dry_run or os.getenv("DRY_RUN", "true").lower() == "true"
        self.exchange = ccxt.binance({
            "apiKey": os.getenv("BINANCE_API_KEY", ""),
            "secret": os.getenv("BINANCE_API_SECRET", ""),
            "enableRateLimit": True,
        })
        if hasattr(self.exchange, "set_sandbox_mode"):
            self.exchange.set_sandbox_mode(True)

    def place_order(self, symbol: str, side: str, amount: float, order_type: str = "market") -> Dict[str, Any]:
        if self.dry_run:
            return {
                "status": "dry_run",
                "symbol": symbol,
                "side": side,
                "amount": amount,
                "type": order_type,
                "message": "Order simulated (dry-run mode)",
            }
        try:
            order = self.exchange.create_order(symbol, order_type, side, amount)
            return {"status": "filled", "order": order}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def cancel_order(self, order_id: str, symbol: str) -> Dict[str, Any]:
        if self.dry_run:
            return {"status": "dry_run", "message": f"Cancel simulated for {order_id}"}
        try:
            result = self.exchange.cancel_order(order_id, symbol)
            return {"status": "cancelled", "result": result}
        except Exception as e:
            return {"status": "error", "message": str(e)}
