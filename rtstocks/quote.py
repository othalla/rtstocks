class Quote:
    def __init__(self, symbol: str, latest_source: str,
                 latest_price: float) -> None:
        self._symbol = symbol
        self._latest_source = latest_source
        self._latest_price = latest_price

    @property
    def symbol(self):
        return self._symbol

    @property
    def latest_source(self):
        return self._latest_source

    @property
    def latest_price(self):
        return self._latest_price
