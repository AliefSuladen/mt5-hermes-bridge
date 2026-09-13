# Hermes Agent × MetaTrader 5

An experimental **Agentic AI integration** that connects Hermes Agent with MetaTrader 5 through an HTTP-based trading bridge.

This project explores how an AI agent can interact with market data, account information, risk status, open positions, and controlled trade execution through dedicated tools.

> **Status:** Experimental / Research

## Architecture

```text
┌─────────────────────┐
│    Hermes Agent     │
│      AI Agent       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  MT5 Bridge Plugin  │
│      AI Tools       │
└──────────┬──────────┘
           │
           │ HTTP API
           ▼
┌─────────────────────┐
│   MT5 Trading       │
│      Bridge         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    MetaTrader 5     │
└─────────────────────┘
Features
Retrieve MT5 account status
Retrieve live bid/ask prices
Retrieve OHLCV candles
Retrieve open positions
Retrieve risk status
Retrieve symbol trading constraints
Execute market BUY/SELL orders
Close positions by exact ticket
Support idempotency identifiers
Read-only position monitoring
Environment-based API credentials
Available Tools
Tool	Description
mt5_account	Get MT5 account status
mt5_price	Get current bid/ask price
mt5_candles	Get recent market candles
mt5_positions	Get currently open positions
mt5_risk	Get risk and trading permission status
mt5_symbol_info	Get broker symbol constraints
mt5_trade	Execute a market BUY/SELL order
mt5_close_position	Close an existing position by ticket
How It Works

Hermes Agent can use the MT5 tools to retrieve market and account information through the bridge.

For operations that require trade execution, the agent sends a structured request to the MT5 bridge. The bridge is responsible for authentication, broker constraints, risk controls, idempotency, and trade verification.

The architecture separates the AI agent from the trading terminal rather than giving the agent direct access to the MetaTrader 5 process.

Security

Credentials are not hardcoded into the source code.

The MT5 bridge URL and API key are loaded from environment variables:

MT5_BRIDGE_URL=https://your-mt5-bridge.example.com
MT5_API_KEY=your_api_key_here

Never commit real:

API keys
passwords
access tokens
private keys
production credentials

The repository includes a .gitignore configured to exclude .env files and local configuration.

Configuration

Create a local .env file based on .env.example:

MT5_BRIDGE_URL=https://your-mt5-bridge.example.com
MT5_API_KEY=your_api_key_here

Replace the placeholder values with your actual configuration.

Do not commit the .env file.

Installation

Clone the repository:

git clone git@github.com:AliefSuladen/mt5-hermes-bridge.git
cd mt5-hermes-bridge

Install the Python dependencies:

pip install -r requirements.txt

The MT5 bridge plugin is intended to run within a compatible Hermes Agent environment and communicate with an MT5 trading bridge.

Monitoring

The repository includes a read-only MT5 position monitoring script:

python scripts/mt5_position_update.py

The monitor retrieves:

Current bid/ask price
Open positions
Position volume
Entry price
Profit/Loss
Stop Loss
Take Profit
Account equity
Daily loss percentage
Trading permission

The monitoring script is read-only and does not execute trades.

Example Workflow

A typical workflow can be represented as:

1. Hermes Agent receives a task
          │
          ▼
2. Agent requests market/account data
          │
          ▼
3. MT5 Bridge validates the request
          │
          ▼
4. MetaTrader 5 provides the requested data
          │
          ▼
5. Hermes analyzes the available information
          │
          ▼
6. Trade operation is requested when appropriate
          │
          ▼
7. MT5 Bridge applies risk and broker constraints
          │
          ▼
8. Trade execution is verified
Project Structure
mt5-hermes-bridge/
├── .env.example
├── .gitignore
│
├── mt5/
│   └── mt5.py
│
├── plugins/
│   └── mt5-bridge/
│       ├── __init__.py
│       ├── plugin.yaml
│       ├── schemas.py
│       └── tools.py
│
└── scripts/
    └── mt5_position_update.py
Design Principles

This project follows several principles:

Separation of concerns

The AI agent is separated from the MetaTrader 5 execution environment through an API bridge.

Environment-based secrets

Sensitive credentials are supplied through environment variables instead of being embedded in source code.

Controlled execution

Trade requests are structured and passed through the bridge, where authentication, risk controls, broker constraints, idempotency, and verification can be applied.

Read-only monitoring

Monitoring functionality is separated from trade execution functionality.

Project Status

This project is currently an experimental Agentic AI research project.

The primary goal is to explore the technical integration between an AI agent and MetaTrader 5 rather than provide a production-ready autonomous trading system.

Future Improvements

Potential future improvements include:

Automated integration tests
More robust error handling
Expanded market analysis tools
More granular risk controls
Improved trade verification
Structured logging and observability
Better failure recovery
Containerized deployment examples
Additional broker compatibility
More comprehensive documentation
Trading Risk Disclaimer

This project is provided for educational and research purposes only.

It is not financial advice, investment advice, or a recommendation to trade any financial instrument.

Automated trading involves substantial risk and can result in financial loss. Always test the system using a demo account before considering any real-money deployment.

Users are responsible for configuring appropriate authentication, risk controls, broker constraints, and monitoring before enabling trade execution.

License

This project is intended for educational and research purposes.
