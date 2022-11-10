import pandas as pd

from Data.data import collect_data

ticker = "aapl"

data = collect_data(ticker)
print(data)