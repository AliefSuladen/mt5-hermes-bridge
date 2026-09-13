from . import schemas
from . import tools


def register(ctx):
    ctx.register_tool("mt5_account", "mt5", schemas.MT5_ACCOUNT, tools.mt5_account)
    ctx.register_tool("mt5_price", "mt5", schemas.MT5_PRICE, tools.mt5_price)
    ctx.register_tool("mt5_candles", "mt5", schemas.MT5_CANDLES, tools.mt5_candles)
    ctx.register_tool("mt5_positions", "mt5", schemas.MT5_POSITIONS, tools.mt5_positions)
    ctx.register_tool("mt5_risk", "mt5", schemas.MT5_RISK, tools.mt5_risk)
    ctx.register_tool("mt5_symbol_info", "mt5", schemas.MT5_SYMBOL_INFO, tools.mt5_symbol_info)
    ctx.register_tool("mt5_trade", "mt5", schemas.MT5_TRADE, tools.mt5_trade)
    ctx.register_tool("mt5_close_position", "mt5", schemas.MT5_CLOSE_POSITION, tools.mt5_close_position)
