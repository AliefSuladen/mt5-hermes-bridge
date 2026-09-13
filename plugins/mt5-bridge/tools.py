import json
import os
import requests


def _request(method, path, **kwargs):
    base_url = os.getenv("MT5_BRIDGE_URL", "").rstrip("/")
    api_key = os.getenv("MT5_API_KEY", "")

    if not base_url:
        return json.dumps({"status": "error", "message": "MT5_BRIDGE_URL is not configured"})

    if not api_key:
        return json.dumps({"status": "error", "message": "MT5_API_KEY is not configured"})

    try:
        headers = kwargs.pop("headers", {})
        headers["X-API-Key"] = api_key

        r = requests.request(
            method,
            base_url + path,
            headers=headers,
            timeout=15,
            **kwargs
        )

        return r.text

    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": str(e)
        })


def mt5_account(args, **kwargs):
    return _request("GET", "/health")


def mt5_price(args, **kwargs):
    return _request(
        "GET",
        "/price",
        params={"symbol": args.get("symbol", "XAUUSD.vx")}
    )


def mt5_candles(args, **kwargs):
    count = int(args.get("count", 200))
    count = max(1, min(count, 1000))

    return _request(
        "GET",
        "/candles",
        params={
            "symbol": args.get("symbol", "XAUUSD.vx"),
            "timeframe": args.get("timeframe", "M5"),
            "count": count
        }
    )


def mt5_positions(args, **kwargs):
    return _request("GET", "/positions")


def mt5_risk(args, **kwargs):
    return _request("GET", "/risk-status")


def mt5_symbol_info(args, **kwargs):
    return _request(
        "GET",
        "/symbol-info",
        params={"symbol": args.get("symbol", "XAUUSD.vx")}
    )


def mt5_trade(args, **kwargs):
    payload = {
        "action": str(args["action"]).upper(),
        "symbol": args.get("symbol", "XAUUSD.vx"),
        "volume": float(args["volume"]),
        "sl": float(args["sl"]),
        "tp": float(args["tp"])
    }

    if args.get("idempotency_id"):
        payload["idempotency_id"] = str(args["idempotency_id"])

    return _request(
        "POST",
        "/trade",
        json=payload
    )


def mt5_close_position(args, **kwargs):
    payload = {
        "ticket": int(args["ticket"])
    }

    if args.get("volume") is not None:
        payload["volume"] = float(args["volume"])

    if args.get("idempotency_id"):
        payload["idempotency_id"] = str(args["idempotency_id"])

    return _request(
        "POST",
        "/close-position",
        json=payload
    )

def register_tools(ctx):
    from . import schemas

    ctx.register_tool("mt5_account", "mt5", schemas.MT5_ACCOUNT, mt5_account)
    ctx.register_tool("mt5_price", "mt5", schemas.MT5_PRICE, mt5_price)
    ctx.register_tool("mt5_candles", "mt5", schemas.MT5_CANDLES, mt5_candles)
    ctx.register_tool("mt5_positions", "mt5", schemas.MT5_POSITIONS, mt5_positions)
    ctx.register_tool("mt5_risk", "mt5", schemas.MT5_RISK, mt5_risk)
    ctx.register_tool("mt5_symbol_info", "mt5", schemas.MT5_SYMBOL_INFO, mt5_symbol_info)
    ctx.register_tool("mt5_trade", "mt5", schemas.MT5_TRADE, mt5_trade)
    ctx.register_tool("mt5_close_position", "mt5", schemas.MT5_CLOSE_POSITION, mt5_close_position)
