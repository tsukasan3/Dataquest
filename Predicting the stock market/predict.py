import pandas as pd
from datetime import datetime
stock = pd.read_csv("sphist.csv")

stock["Date"] = pd.to_datetime(stock["Date"])

sorted_stock = stock.sort_values(by=["Date"])