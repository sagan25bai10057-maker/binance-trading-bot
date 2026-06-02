# ⚡ Binance Futures Testnet Simplified Trading Bot

A production-grade, dependency-light Python CLI tool engineered to securely package, sign, and execute algorithmic orders directly onto the Binance Futures Testnet (USDT-M) engine. Zero heavy wrappers. Pure cryptographic execution.

---

## 🎯 Features
- **Clean Architecture**: Fully decoupled layers separating CLI parser routing, business rules logic, and raw API communications.
- **Hardened Security**: Uses native `hmac-sha256` signing signatures over lightweight `requests` primitives—preventing SDK version locks.
- **Dual-Stream Logging**: Execution paths, validation checks, and wire footprints are streamed concurrently to stdout and persistent `logs/bot.log` files.
- **Fail-Fast Boundaries**: Rigid pre-flight input inspection catches runtime anomalies before touching network layers.

---

## 🛠️ Quickstart Guide

### 1. Build the Workspace Environment
```
# Clone the repository and navigate to workspace
git clone <your-repository-url-here>
cd trading_bot

# Spin up isolated virtual environment

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install minimalist manifest footprint
```
```
pip install -r requirements.txt
```
### 2. Configure Local Secrets
```
Populate a secret registry file named .env in your root project directory:
BINANCE_API_KEY="your_binance_testnet_api_key_here"
BINANCE_API_SECRET="your_binance_testnet_api_secret_here"
```

💻 Live Production Runs
```
The engine runs directly out of your terminal using explicit option flags.

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.005
```
🟢 Instant Market Entry
```
  python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.005
```
🔴 Strategic Limit Placement
```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 65250.00
```

🎛️ System Design & Assumptions

Symbol Invariance: System expects strict USD-Margined trading syntax convention (e.g., BTCUSDT, ETHUSDT). Lowercase strings are normalized dynamically in the validation interceptor.

Execution Policy: Limit tracking structures assume structural GTC (Good 'Till Cancelled) properties to enforce placement durability.

Precision Delegation: Floating-point rounding boundaries are safely offloaded directly to the Testnet exchange handler engines, keeping internal calculation arrays perfectly predictable.

Stream Tracking: Application processes naturally capture both full round-trip API network wire traces and intercept exceptions smoothly without crashing runtime processes.
