from rtstocks.quote import Quote
from rtstocks.exchanges.base import Exchange
from rtstocks.exchanges.iex import IEX
from rtstocks.exceptions import StockQuoteException, ExchangeException


class Stock:
    @staticmethod
    def quote(stock: str, exchange_provider: Exchange = IEX) -> Quote:
        try:
            quote = exchange_provider.quote(stock)
        except ExchangeException:
            raise StockQuoteException
        return quote
