import pytest
from unittest.mock import Mock
from rtstocks.stock import Stock
from rtstocks.quote import Quote
from rtstocks.exceptions import StockQuoteException, ExchangeException


class TestStock:
    def test_quote_return_stock_data(self):
        exchange = Mock(name='SomeExchange')
        exchange.quote.return_value = Quote('AMZN', 'source', 10)
        stock_quote = Stock.quote('AMZN', exchange)
        assert isinstance(stock_quote, Quote)
        assert stock_quote.symbol == 'AMZN'

    def test_quote_return_exception_on_query_error(self):
        exchange = Mock(name='SomeExchange')
        exchange.quote.side_effect = ExchangeException
        with pytest.raises(StockQuoteException):
            Stock.quote('AMZN', exchange)
