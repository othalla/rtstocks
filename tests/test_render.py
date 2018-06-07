from unittest.mock import Mock
from rtstocks.quote import Quote
from rtstocks.render import print_table, stocks_datas
from rtstocks.exceptions import StockQuoteException


def test_show_table_from_data():
    table = Mock(name='tabulate')
    print_table(['symbol', 'latestPrice', 'latestSource'],
                [['AAPL', 158.73, 'Previous close'],
                 ['AMZN', 1158.73, 'Previous close']],
                table_builder=table)
    table.assert_called_once_with(
        [['AAPL', 158.73, 'Previous close'],
         ['AMZN', 1158.73, 'Previous close']],
        headers=['symbol', 'latestPrice', 'latestSource'],
        tablefmt='grid')
    table.assert_called_once()


def test_return_stocks_data_from_stocks():
    stock = Mock(name='Stock')
    stock.quote.side_effect = [
        Quote('AAPL', 'Previous close', 150),
        Quote('AMZN', 'Previous close', 100)]
    datas = stocks_datas(['AMZN', 'AAPL'], stock_provider=stock)
    assert stock.quote.call_count == 2
    assert datas == [['AAPL', 'Previous close', 150],
                     ['AMZN', 'Previous close', 100]]


def test_return_blank_data_with_stock_quote_exception():
    stock = Mock(name='Stock')
    stock.quote.side_effect = StockQuoteException
    datas = stocks_datas(['AMZN'], stock_provider=stock)
    assert stock.quote.call_count == 1
    assert datas == [['AMZN', '---', '---']]
