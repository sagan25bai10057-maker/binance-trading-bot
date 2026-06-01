import sys
from logging_config import logger
def validate_inputs(symbol:str,side:str,order_type:str,quantity:float,price:float=None):
    """Validates CLI parameters before making network requests.Raises ValueError for invalid configurations."""
    errors=[]
    symbol=symbol.upper().strip()
    side=side.upper().strip()
    order_type=order_type.upper().strip()
    if not symbol.endswith("USDT"):
        errors.append(f"Invalid symbol'{symbol}'.Must be a USDT pair (e.g., BTCUSDT).")
    if side not in ["BUY","SELL"]:
        errors.append(f"Invalid side'{side}'.Must be BUY or SELL.")
    if order_type not in ["MARKET","LIMIT"]:
        errors.append(f"Invalid order type'{order_type}'.Must be MARKET or LIMIT.")
    if quantity<=0:
        errors.append(f"Quantity must be greater than 0. Provided:{quantity}")
    if order_type=="LIMIT":
        if price is None or price<=0:
            errors.append("Price is strictly required and must be greater than 0 for LIMIT orders.")
    if errors:
        for err in errors:
            logger.error(f"Validation Failure:{err}")
        raise ValueError("|".join(errors))
    return symbol,side,order_type