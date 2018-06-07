from unittest.mock import Mock
from rtstocks.quote import Quote
from rtstocks.exchanges.iex import IEX


class TestIEX:
    def test_quote_returns_stocks_quote_if_status_code_200(self):
        requests_get = Mock(name='requests.get')
        requests_get.return_value.status_code = 200
        requests_get.return_value.json.return_value = {
            "symbol": "NFLX",
            "latestSource": "IEX real time price",
            "latestPrice": 360,
        }
        stock_quote = IEX().quote('NFLX')
        assert isinstance(stock_quote, Quote)
        assert stock_quote.symbol == 'NFLX'
