
import yfinance as yf

class Data:

    @staticmethod
    def getFromMarketPlace():
        data = yf.download("BTC-USD", start="2017-04-01")
        print(data.head())
