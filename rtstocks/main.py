import sys
from rtstocks.render import stocks_datas, table


if __name__ == "__main__":
    stocks = sys.argv[1:]
    print(table(['Symbol', 'LatestSource', 'LatestPrice'],
                stocks_datas(stocks)))

