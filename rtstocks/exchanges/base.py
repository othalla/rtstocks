from abc import ABC, abstractmethod
from typing import Callable
import requests
from rtstocks.quote import Quote


class Exchange(ABC):
    @staticmethod
    @abstractmethod
    def quote(stock: str, http_get: Callable = requests.get) -> Quote:
        pass
