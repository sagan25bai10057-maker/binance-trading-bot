import argparse
import os
import sys
from dotenv import load_dotenv
load_dotenv()
from bot.logging_config import logger
from bot.validators import validate_inputs
from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
def main():
    parser=argparse.ArgumentParser(
        description="Simplified Binance Futures Testnet Execution Bot",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--symbol", type=str, required=True, help="Trading pair code, e.g., BTCUSDT")
    parser.add_argument("--side", type=str, required=True, choices=["BUY", "SELL"], help="Direction of execution path")
    parser.add_argument("--type", type=str, required=True, choices=["MARKET", "LIMIT"], help="Order execution type")
    parser.add_argument("--quantity", type=float, required=True, help="Target asset count to execute")
    parser.add_argument("--price", type=float, default=None, help="Trigger target price evaluation (Required for LIMIT)")
    args=parser.parse_args()
    print("\n"+"="*50)
    print("         ORDER REQUEST STAGING SUMMARY         ")
    print("="*50)
    print(f" Target Instrument :{args.symbol.upper()}")
    print(f" Execution Path    :{args.side.upper()}")
    print(f" Order Type        :{args.type.upper()}")
    print(f" Target Volume     :{args.quantity}")
    if args.price:
        print(f" Limit Strike Price:{args.price}")
    print("="*50 +"\n")
    try:
        symbol, side, order_type = validate_inputs(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )
    except ValueError as val_err:
        print(f"Input Validation Refusal:\n{val_err}\n")
        sys.exit(1)
    api_key=os.getenv("BINANCE_API_KEY")
    api_secret=os.getenv("BINANCE_API_SECRET")
    if not api_key or not api_secret:
        print("Configuration Missing: Please declare BINANCE_API_KEY and BINANCE_API_SECRET inside a local .env file.")
        logger.error("Execution failed due to unpopulated API environment variables.")
        sys.exit(1)
    try:
        client=BinanceFuturesClient(api_key=api_key,api_secret=api_secret)
        manager=OrderManager(client)
        print("⏳ Dispatching signed instructions packet to Binance Testnet Engine...")
        response=manager.place_futures_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=args.quantity,
            price=args.price
        )
        print("Throttled Order Response Framework:")
        print(f"  Status        : {response.get('status')}")
        print(f"  Order ID      : {response.get('orderId')}")
        print(f"  Executed Qty  : {response.get('executedQty')}")
        print(f"  Avg Execution : {response.get('avgPrice', 'N/A')} USDT")
        print(f"  Order processed and executed successfully on the testnet ledger.")
    except (ConnectionError,RuntimeError) as api_err:
        print(f" Execution Exception Encountered:{api_err}")
        sys.exit(1)
if __name__ == "__main__":
    main()