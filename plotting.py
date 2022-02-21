import matplotlib as mlt
import pandas as pd

from movingAverage import MovingAverage
pd.options.mode.chained_assignment = None  # default='warn'

stock = MovingAverage("msft",100)
print(type(stock))
