from unittest.mock import Mock
from rtstocks.render import print_table


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
