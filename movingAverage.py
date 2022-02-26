from dataImport import DataImport
import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'


# Prototype an average of some shit
# moving average of 20 days
# Create a pandas data frame and start averaging
# Built so the max average is 200 days across any time period
class MovingAverage:

    def __init__(self, stock_name, length_of_days):
        self.domain = length_of_days
        self.domain_full = length_of_days + 200

        self.stock = DataImport(stock_name, self.domain_full)
        self.master_data = self.stock.close_data()
        self.control_master_data = self.stock.close_data()
        self.working_data = self.stock.close_data()

    def control(self):
        upper_bounds = len(self.control_master_data)
        lower_bounds = upper_bounds - self.domain
        return self.control_master_data.iloc[lower_bounds:upper_bounds]

    # excludes current day
    def average(self, time_step):
        w_data = self.master_data
        upper_bounds = len(self.master_data) - 1
        lower_bounds = upper_bounds - self.domain
        # print(f"length {len(self.master_data)}")

        for i in range(upper_bounds, lower_bounds, -1):
            j = i - time_step
            w_data.iloc[i] = float(self.master_data.iloc[j + 1:i + 1].mean()) # This is where the fix is

        return w_data.iloc[lower_bounds + 1:upper_bounds + 1]


# stock = MovingAverage("msft", 200)
# test = stock.control()
# print("control")
# print(test)
# print("avg10")
# print(stock.average(10).head())
# print("avg50")
# print(stock.average(50).head())
#
