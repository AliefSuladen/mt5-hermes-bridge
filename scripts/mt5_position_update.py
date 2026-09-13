import json
import os
import urllib.parse
import urllib.request

base = os.environ.get("MT5_BRIDGE_URL", "").rstrip("/")
key = os.environ.get("MT5_API_KEY", "")
if not base:
    print("MT5 bridge belum terkonfigurasi.")
    raise SystemExit(0)


def get(path, params=None):
    url = base + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"X-API-Key": key})
    with urllib.request.urlopen(req, timeout=10) as response:
        return json.load(response)

try:
    positions = get("/positions").get("positions", [])
    price = get("/price", {"symbol": "XAUUSD.vx"})
    risk = get("/risk-status")
except Exception as exc:
    print(f"⚠️ Monitor MT5 gagal membaca bridge: {exc}")
    raise SystemExit(0)

print("📊 Update MT5 XAUUSD.vx")
print(f"Bid: {price.get('bid')} | Ask: {price.get('ask')}")
print(f"Posisi terbuka: {len(positions)}")
for position in positions:
    side = "BUY" if position.get("type") == 0 else "SELL"
    print(
        f"- Ticket {position.get('ticket')}: {side} {position.get('volume')} "
        f"@ {position.get('price_open')} | P/L {position.get('profit')} | "
        f"SL {position.get('sl')} | TP {position.get('tp')}"
    )
print(
    f"Equity: {risk.get('current_equity')} | "
    f"Daily loss: {risk.get('daily_loss_percent')}% | "
    f"Trading allowed: {risk.get('trading_allowed')}"
)
print("Read-only monitor; tidak melakukan trade.")
