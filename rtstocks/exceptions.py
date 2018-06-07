class StockQuoteException(Exception):
    pass


class ExchangeException(Exception):
    pass


class UnknowStockException(ExchangeException):
    pass


class IEXExchangeException(ExchangeException):
    pass
