
from src.Exception.InvalidInstanceException import InvalidInstanceException

class init:


    instance = None


    def __init__(self):
        init.instance = self


    @staticmethod
    def getInstance():
        if init.instance is not None:
            return init.instance
        else:
            raise InvalidInstanceException("Invalid Instance Variable Type")

