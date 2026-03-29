from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        self.client = Client(
            self.api_key,
            self.api_secret
        )


        self.client.FUTURES_URL = "https://demo-fapi.binance.com/fapi"

    def place_order(self, **params):
        return self.client.futures_create_order(**params)