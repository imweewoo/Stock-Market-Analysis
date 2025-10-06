#import libraries
import yfinance as yf
import pandas as pd

#import data for sp500
sp500 = yf.Ticker("^GSPC")
sp500 = sp500.history(period="max")

#remove unnecessary columns
del sp500["Dividends"]
del sp500["Stock Splits"]

print(sp500)