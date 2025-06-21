from src.Analysis.Analysis import Analysis
from src.Exception.InvalidArgumentException import InvalidArgumentException

class Initialize:

    args = None

    def __init__(self, args):
        Initialize.args = args

    def run(self):
        args = Initialize.args
        if len(args) == 1:
            raise InvalidArgumentException("No arguments given")

        if len(args) == 2:
            if args[1] == "help":
                print("This is a help message. Please provide valid arguments!")
            else:
                raise InvalidArgumentException("Invalid argument given")
            return

        if len(args) >= 3:
            if args[1] == "analysis":
                analysis = Analysis(args[2])
                analysis.analysis()
