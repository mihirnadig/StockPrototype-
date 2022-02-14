import pandas as pd
import yfinance as yf

class DataImport:

    def __init__(self, ticker, days):
        # Stock Attributes and Data
        self.ticker_symbol = str(ticker.upper())
        self.stock = yf.Ticker(self.ticker_symbol)

        #Returns data for number of days
        self.working_data = pd.DataFrame
        self.days = str(days) + "d"
        self.working_data = yf.download(self.ticker_symbol, period=self.days)

        # Column Switches
        self.open_col = True
        self.high_col = True
        self.low_col = True
        self.close_col = True
        self.adj_close_col = True
        self.vol_col = True

    # Get all Historical Data
    # def historical_data(self):
    #     return self.stock.history(period="max")

    def open_data(self):
        return self.working_data.iloc[:, [True, False, False, False, False, False]]

    def high_data(self):
        return self.working_data.iloc[:, [False, True, False, False, False, False]]

    def low_data(self):
        return self.working_data.iloc[:, [False, False, True, False, False, False]]

    def close_data(self):
        return self.working_data.iloc[:, [False, False, False, True, False, False]]

    def adj_close_data(self):
        return self.working_data.iloc[:, [False, False, False, False, True, False]]

    def vol_data(self):
        return self.working_data.iloc[:, [False, False, False, False, False, True]]


# blah = DataImport("msft",10)
# print(blah.working_data)

# test = DataImport("msft")
# print(test.past_period(10))
# print("working data ")
# print(test.high_data())
# print(data.head(5))
# print(data.shape)


 # Returns data for past number of days
    # def past_period(self, days):
    #     time_period = str(days) + "d"
    #     self.working_data = yf.download(self.ticker_symbol, period=time_period)
    #     return self.working_data.iloc[:,
    #         [self.open_col, self.high_col, self.low_col, self.close_col, self.adj_close_col, self.vol_col]]
