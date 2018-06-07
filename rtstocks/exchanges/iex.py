from typing import Callable
import requests
from rtstocks.quote import Quote
from rtstocks.exchanges.base import Exchange
from rtstocks.exceptions import UnknowStockException, IEXExchangeException


IEX_API_URL = "https://api.iextrading.com/1.0"


class IEX(Exchange):
    @staticmethod
    def quote(stock: str, http_get: Callable = requests.get) -> Quote:
        response = http_get(f"{IEX_API_URL}/stock/{stock}/quote")
        if response.status_code == 200:
            data = response.json()
            return Quote(data['symbol'], data['latestSource'],
                         data['latestPrice'])
        elif response.status_code == 404:
            raise UnknowStockException
        else:
            raise IEXExchangeException
