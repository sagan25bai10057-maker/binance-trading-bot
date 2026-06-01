# Binance Futures Testnet Simplified Trading Bot

A lightweight, robust Python CLI tool built to interact securely with the Binance Futures Testnet (USDT-M) API. Designed with a clear separation of concerns, strict cryptographic request signing, and graceful input/error handling.

## 🚀 Features
- **Structural Cleanliness**: Fully segregated Client API layer, Business/Order layer, and Command CLI interface layer.
- **Robust Security**: Built using native cryptographic signature pipelines (`hmac-sha256`) over raw `requests`. Avoids heavy third-party SDK dependencies.
- **Dual Destination Logging**: Direct validation streams and API payloads track concurrently to both standard shell output and structured logfiles under `logs/bot.log`.

---

## 🛠️ Setup & Installation

### 1. Clone the Repository
git clone <your-repository-url-here>
cd trading_bot
2. Configure Environment Isolation
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Required Dependencies
pip install -r requirements.txt
4. Set Up API Credentials
Create a .env file in the root directory of the project to securely house your credentials:
Code snippet
BINANCE_API_KEY="your_binance_testnet_api_key"
BINANCE_API_SECRET="your_binance_testnet_api_secret"
💻 Usage Examples
The tool evaluates inputs natively using an explicit command-line interface framework.
1. Place a Market Order
Instantly execute a market entry position:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.005
2. Place a Limit Order
Stage a priced limit tracking target on the order book:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 65250.00
📝 Key Architectural Assumptions
Symbol Syntax:Pair entries must explicitly follow the Binance standard USD-Margined tracking layout (e.g.,BTCUSDT,ETHUSDT).
Time In Force:Limit orders assume a default policy execution mapping of GTC (Good'Till Cancelled).
Precision Validation:The system passes volume truncation boundaries directly to the API handler to protect calculations against floating-point drift error conditions.
