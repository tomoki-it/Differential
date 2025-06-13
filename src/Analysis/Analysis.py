from src.Analysis.Data.Data import Data
from src.Exception.InvalidArgumentException import InvalidArgumentException


class Analysis:

    task = None

    def __init__(self, task):
        self.task = task

    def analysis(self):
        if self.task == "get":
            Data.getFromMarketPlace()
        elif self.task == "output":
            Data.outputToJson()
        else:
            raise InvalidArgumentException("Invalid task provided")