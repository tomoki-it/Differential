import os

import yfinance as yf
import json
import pandas as pd
from datetime import datetime

from src.Exception.DataFetchException import DataFetchException


class Data:

    @staticmethod
    def getFromMarketPlace():
        data = yf.download(
            tickers="BTC-USD",
            interval="1h",
            period="7d",
            start="2023-07-01"
        )

        if not isinstance(data, pd.DataFrame) | data.empty:
            raise DataFetchException("No data fetched from the market place")

        return data

    @staticmethod
    def outputToJson():
        try:
            data = Data.getFromMarketPlace()
            result = {}
            for timestamp, row in data.iterrows():
                key = pd.to_datetime(timestamp).strftime("%Y-%m-%d %H:%M:%S")
                result[key] = {
                    "Open": float(row["Open"].iloc[0]),
                    "Close": float(row["Close"].iloc[0])
                }

            output_dir = "output"
            os.makedirs(output_dir, exist_ok=True)
            output_file = os.path.join(output_dir, "btc_open_close.json")

            with open(output_file, "w") as f:
                json.dump(result, f, indent=2)

        except DataFetchException as e:
            print(f"Error fetching data: {e}")
            return None
