from unittest.mock import Mock
from rtstocks.render import table


def test_show_table_from_data():
    table_builder = Mock(name='tabulate')
    table([['symbol', 'latestPrice', 'latestSource'],
        ['AAPL', 158.73, 'Previous close']], table_builder=table_builder)
    table_builder.assert_called_once()
