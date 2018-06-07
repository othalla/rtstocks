from unittest.mock import Mock
import pytest
from rtstocks.quote import Quote
from rtstocks.exchanges.iex import IEX
from rtstocks.exceptions import UnknowStockException, IEXExchangeException


class TestIEX:
    def test_quote_returns_stocks_quote_if_status_code_200(self):
        requests_get = Mock(name='requests.get')
        requests_get.return_value.status_code = 200
        requests_get.return_value.json.return_value = {
            "symbol": "NFLX",
            "latestSource": "IEX real time price",
            "latestPrice": 360,
        }
        stock_quote = IEX().quote('NFLX', http_get=requests_get)
        assert isinstance(stock_quote, Quote)
        assert stock_quote.symbol == 'NFLX'

    def test_quote_raises_unknown_stock_exception_with_status_code_404(self):
        requests_get = Mock(name='requests.get')
        requests_get.return_value.status_code = 404
        with pytest.raises(UnknowStockException):
            IEX().quote('NFLX', http_get=requests_get)

    def test_quote_raises_iex_exception_with_bad_status_code(self):
        requests_get = Mock(name='requests.get')
        requests_get.return_value.status_code = 500
        with pytest.raises(IEXExchangeException):
            IEX().quote('NFLX', http_get=requests_get)
