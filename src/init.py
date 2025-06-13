from src.Analysis.Analysis import Analysis
from src.Exception.InvalidInstanceException import InvalidInstanceException

class init:

    args = None

    def __init__(self, args):
        init.args = args

    def run(self):
        args = init.args
        if len(args) == 1:
            raise InvalidInstanceException("No arguments provided")

        if len(args) == 2:
            if args[1] == "help":
                print("This is a help message. Please provide valid arguments!")
            else:
                raise InvalidInstanceException("Invalid argument provided")
            return

        if len(args) >= 3:
            if args[1] == "analysis":
                analysis = Analysis(args[2])
                analysis.analysis()
