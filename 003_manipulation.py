import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

from utils import data_inout as io

"""
Moving Averages.

The idea of a simple moving average is to take a window of time,
and calculate the average price in that window.
Then we shift that window over one period, and do it again.
In our case, we'll do a 100 day rolling moving average.
So this will take the current price, and the prices from the past 99 days,
add them up, divide by 100, and there's your current 100-day moving average.
Then we move the window over 1 day, and do the same thing again.
"""

df_tsla = io.read_data_from_csv('data/TSLA.csv')

# define 100ma as the rolling moving average with window=100 and min_periods=0
# to not have NaN values on the first 100 records
df_tsla['100ma'] = df_tsla['Adj Close'].rolling(window=100, min_periods=0).mean()
print(df_tsla.head())

# initialize a graph with 6 rows, 1 column divided in two graphs
# one that spans 5 rows and one that spans 1 row
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

# plot adj close and 100ma on the first graph and volume on the second one
ax1.plot(df_tsla.index, df_tsla['Adj Close'])
ax1.plot(df_tsla.index, df_tsla['100ma'])
ax2.bar(df_tsla.index, df_tsla['Volume'])

plt.show()
