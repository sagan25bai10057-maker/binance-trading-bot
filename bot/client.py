import hmac
import hashlib
import time
import requests
from logging_config import logger
class BinanceFuturesClient:
    """Handles low-level cryptographic signatures and REST interactions with the Testnet."""
    BASE_URL="https://testnet.binancefuture.com"
    def __init__(self,api_key:str,api_secret:str):
        if not api_key or not api_secret:
            logger.error("API credentials missing during initialization.")
            raise ValueError("API_KEY and API_SECRET must be configured.")
        self.api_key=api_key
        self.api_secret=api_secret
        self.headers={
            "X-MBX-APIKEY":self.api_key
        }
    def _generate_signature(self,query_string:str)->str:
        """Generates an HMAC SHA256 signature required for Binance private endpoints."""
        return hmac.new(
            self.api_secret.encode('utf-8'),
            query_string.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
    def send_signed_request(self,method:str,endpoint:str,params:dict=None)->dict:
        """Appends timestamp, signs parameters, and executes HTTP request safely."""
        if params is None:
            params={}
        params/['timestamp']=int(time.time()*1000)
        query_string='&'.join([f"{k}={v}"for k,v in params.items()])
        signature=self._generate_signature(query_string)
        params['signature']=signature
        url=f"{self.BASE_URL}{endpoint}"
        logger.info(f"Sending{method}request to{endpoint}with payload parameters.")
        try:
            response=requests.request(method,url,headers=self.headers,params=params,timeout=10)
            response.raise_for_status()
            data=response.json()
            logger.info(f"Successfully processed response from{endpoint}")
            return data
        except requests.exceptions.HTTPError as http_err:
            try:
                error_payload=response.json()
                msg=f"Binance API Error Code{error_payload.get('code')}:{error_payload.get('msg')}"
            except Exception:
                msg=f"HTTP Error context:{http_err}"
            logger.error(msg)
            raise RuntimeError(msg)
        except requests.exceptions.RequestException as net_err:
            msg=f"Network or transport connection failure:{net_err}"
            logger.error(msg)
            raise ConnectionError(msg)