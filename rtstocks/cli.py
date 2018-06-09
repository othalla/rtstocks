import argparse
from rtstocks.render import stocks_datas, table


def stocks():
    parser = argparse.ArgumentParser()
    parser.add_argument('--stocks', nargs='*', required=True)
    cli_params = parser.parse_args()
    print(table(['Symbol', 'LatestSource', 'LatestPrice'],
                stocks_datas(cli_params.stocks)))
