from yfinance.scrapers.analysis import Analysis

from src.Exception.InvalidInstanceException import InvalidInstanceException

class init:


    instance = None


    def __init__(self, args):
        init.instance = self

        if len(args) == 0:
            raise InvalidInstanceException("No arguments provided")

        if len(args) == 1:
            if args[1] == "help":
                print("This is a help message. Please provide valid arguments!")
            else:
                raise InvalidInstanceException("Invalid argument provided")

        if args[0] == "analysis":
            Analysis(args[1])


    @staticmethod
    def getInstance():
        if init.instance is not None:
            return init.instance
        else:
            raise InvalidInstanceException("Invalid Instance Variable Type")

