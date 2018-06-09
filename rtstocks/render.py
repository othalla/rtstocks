from typing import List
from tabulate import tabulate
from rtstocks.stock import Stock
from rtstocks.exchanges.iex import IEX
from rtstocks.exceptions import StockQuoteException


def stocks_datas(stocks: list, stock_provider=Stock) -> List[list]:
    result = []
    for stock in stocks:
        try:
            quote = stock_provider.quote(stock)
            result.append([quote.symbol, quote.latest_source,
                           quote.latest_price])
        except StockQuoteException:
            result.append([stock, '---', '---'])
    return result


def table(headers: list, stocks_data: List[list],
          table_builder=tabulate) -> None:
    return table_builder(stocks_data, headers=headers, tablefmt='grid')
