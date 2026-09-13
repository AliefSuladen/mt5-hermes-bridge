MT5_ACCOUNT = {
    "name": "mt5_account",
    "description": (
        "Get current MetaTrader 5 account status, including server, "
        "balance, equity, login, and account mode."
    ),
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

MT5_PRICE = {
    "name": "mt5_price",
    "description": "Get current live bid and ask price for an exact MT5 symbol.",
    "parameters": {
        "type": "object",
        "properties": {
            "symbol": {"type": "string"}
        },
        "required": ["symbol"]
    }
}

MT5_CANDLES = {
    "name": "mt5_candles",
    "description": "Get recent OHLCV candles for market analysis.",
    "parameters": {
        "type": "object",
        "properties": {
            "symbol": {"type": "string"},
            "timeframe": {"type": "string"},
            "count": {"type": "integer"}
        },
        "required": ["symbol"]
    }
}

MT5_POSITIONS = {
    "name": "mt5_positions",
    "description": "Get all currently open MT5 positions.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

MT5_RISK = {
    "name": "mt5_risk",
    "description": "Get current MT5 bridge risk status and trading permission.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

MT5_SYMBOL_INFO = {
    "name": "mt5_symbol_info",
    "description": "Get broker trading constraints for an MT5 symbol.",
    "parameters": {
        "type": "object",
        "properties": {
            "symbol": {"type": "string"}
        },
        "required": ["symbol"]
    }
}

MT5_TRADE = {
    "name": "mt5_trade",
    "description": (
        "Execute a market BUY or SELL order. Hermes may use this tool "
        "autonomously when its analysis determines a trade is appropriate. "
        "Every opening trade MUST include both SL and TP. The bridge "
        "enforces risk controls, broker constraints, idempotency and verification."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "action": {
                "type": "string",
                "enum": ["BUY", "SELL"]
            },
            "symbol": {"type": "string"},
            "volume": {"type": "number"},
            "sl": {"type": "number"},
            "tp": {"type": "number"},
            "idempotency_id": {"type": "string"}
        },
        "required": ["action", "symbol", "volume", "sl", "tp"]
    }
}

MT5_CLOSE_POSITION = {
    "name": "mt5_close_position",
    "description": "Close an existing MT5 position by exact ticket.",
    "parameters": {
        "type": "object",
        "properties": {
            "ticket": {"type": "integer"},
            "volume": {"type": "number"},
            "idempotency_id": {"type": "string"}
        },
        "required": ["ticket"]
    }
}
