import pytest
from unittest.mock import Mock
from rtstocks.stock import Stock
from rtstocks.exceptions import StockQuoteException, ExchangeException


class TestStock:
    def test_quote_return_stock_data(self):
        exchange = Mock(name='SomeExchange')
        exchange.return_value.quote.return_value = ['AMZN', 1000,
                                                    'Previous close']
        stock_quote = Stock('AMZN', exchange_provider=exchange).quote()
        assert stock_quote == ['AMZN', 1000, 'Previous close']

    def test_quote_return_exception_on_query_error(self):
        exchange = Mock(name='SomeExchange')
        exchange.return_value.quote.side_effect = ExchangeException
        with pytest.raises(StockQuoteException):
            Stock('AMZN', exchange_provider=exchange).quote()
