import sys
from rtstocks.render import stocks_datas, print_table


if __name__ == "__main__":
    stocks = sys.argv[1:]
    print_table(['Symbol', 'LatestSource', 'LatestPrice'],
                stocks_datas(stocks))

