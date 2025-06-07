from src.Analysis.Data.Data import Data
from src.Exception.InvalidArgumentException import InvalidArgumentException


class Analysis:

    def __init__(self, task):
        if task == "get":
            Data.getFromMarketPlace()
        else:
            raise InvalidArgumentException("Invalid task provided")