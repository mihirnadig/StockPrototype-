import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# from pandas import DataFrame


from movingAverage import MovingAverage

pd.options.mode.chained_assignment = None  # default='warn'

stock = MovingAverage("msft", 200)
var1 = stock.control().head()
print(var1.head())
var2 = stock.average(10).head()
print(var2.head())
print(stock.average(50).head())

# control_data = stock.control()
# working_data = stock.average(20)
# working_data_2 = stock.average(50)


# control_data.plot()
# #working_data.plot()
# plt.plot(control_data)
# plt.plot(working_data)
# plt.plot(working_data_2)
# plt.show()


# plt.show()
# plt.figure(num=1)
#
# working_data.plot()
# plt.show()
# plt.figure(num=2)
#
