from typing import List
from tabulate import tabulate


def print_table(headers: list, stocks_data: List[list],
                table_builder=tabulate) -> None:
    table = table_builder(stocks_data,
                          headers=headers,
                          tablefmt='grid')
    print(table)
