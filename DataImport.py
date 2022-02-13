import pandas as pd
import yfinance as yf


# Function that returns data for set period of time.
# Inputs: Ticker Symbol, Time period
def get_data(ticker_symb, days):
    ticker_symb = str(ticker_symb.upper())
    stock = ticker_symb
    time_period = str(days) + "d"
    data = yf.download(stock, period=time_period)
    return data


# print(get_data("aapl", 10))

# #print(data.head(10))
# print(data.shape)
#
# print(data.iloc[:,[True, False, False, False, False, False]])
#
