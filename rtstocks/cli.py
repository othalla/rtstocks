import argparse
from rtstocks.render import stocks_datas, table


def stocks():
    parser = argparse.ArgumentParser()
    parser.add_argument('--stocks', nargs='*', required=True)
    parser.add_argument('--refresh', action='store_true')
    _cli_behavior(parser.parse_args())


def _cli_behavior(namespace: argparse.Namespace):
    if namespace.refresh:
        raise NotImplementedError
    else:
        print(table(['Symbol', 'LatestSource', 'LatestPrice'],
                    stocks_datas(namespace.stocks)))
