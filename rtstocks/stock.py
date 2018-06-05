from rtstocks.exceptions import StockQuoteException, ExchangeException


class Stock:
    def __init__(self, stock: str, exchange_provider) -> None:
        self._stock = stock
        self._exchange_provider = exchange_provider

    def quote(self) -> list:
        try:
            data = self._exchange_provider(self._stock).quote()
        except ExchangeException:
            raise StockQuoteException
        return data
