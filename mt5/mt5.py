import os
import requests
from dotenv import load_dotenv

load_dotenv(os.path.expanduser("~/mt5/.env"))

BASE_URL = os.getenv("MT5_BRIDGE_URL")
API_KEY = os.getenv("MT5_API_KEY")

HEADERS = {
    "X-API-Key": API_KEY
}


def health():
    r = requests.get(
        f"{BASE_URL}/health",
        timeout=10
    )
    print(r.json())


def price(symbol):
    r = requests.get(
        f"{BASE_URL}/price",
        params={"symbol": symbol},
        headers=HEADERS,
        timeout=10
    )
    print(r.json())


def positions():
    r = requests.get(
        f"{BASE_URL}/positions",
        headers=HEADERS,
        timeout=10
    )
    print(r.json())


if __name__ == "__main__":
    print("=== MT5 CONNECTION ===")
    health()

    print("\n=== XAUUSD PRICE ===")
    price("XAUUSD")

    print("\n=== POSITIONS ===")
    positions()
