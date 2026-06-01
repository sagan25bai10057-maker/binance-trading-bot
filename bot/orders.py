from bot.client 
import BinanceFuturesClient
from bot.logging_config import logger
class OrderManager:
    """Abstraction layer converting structured trading intents into signed execution targets."""
    def __init__(self, client: BinanceFuturesClient):
        self.client=client
    def place_futures_order(self,symbol:str,side:str,order_type:str,quantity:float,price:float=None)->dict:
        """Constructs specific parameters payload for the /fapi/v1/order endpoint."""
        endpoint="/fapi/v1/order"
        params={
            "symbol":symbol,
            "side":side,
            "type":order_type,
            "quantity":str(quantity),
            "timeInForce": "GTC"
        }
        if order_type=="LIMIT":
            params["price"]=str(price)
        elif order_type=="MARKET":
            params.pop("timeInForce",None)
        logger.info(f"Staging execution layout:{side}{quantity}{symbol}via{order_type}")
        return self.client.send_signed_request("POST",endpoint,params)