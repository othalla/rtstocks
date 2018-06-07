from typing import List
from tabulate import tabulate
from rtstocks.stock import Stock
from rtstocks.exchanges.iex import IEX
from rtstocks.exceptions import StockQuoteException


def stocks_datas(stocks: list, stock_provider=Stock) -> List[list]:
    result = []
    for stock in stocks:
        try:
            result.append(stock_provider(stock, IEX).quote())
        except StockQuoteException:
            result.append([stock, '---', '---'])
    return result


def print_table(headers: list, stocks_data: List[list],
                table_builder=tabulate) -> None:
    table = table_builder(stocks_data,
                          headers=headers,
                          tablefmt='grid')
    print(table)
