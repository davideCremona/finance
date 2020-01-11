import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

from utils import data_inout
df = data_inout.read_data_from_csv('data/TSLA.csv')

# importing finance plotting utility and date data type for matplotlib
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

# takes the "Adj Close" column and resample it with ohcl format.
# (every N days collect open, high, low, close values)
# we can also do mean(), avg() and other aggregation functions with others time periods.
df_ohlc = df['Adj Close'].resample('10D').ohlc()

# takes the "Volume" column and resample it with sum function every 10 days
df_volume = df['Volume'].resample('10D').sum()

df_ohlc = df_ohlc.reset_index()
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)


# setup plot to have 6 rows and 1 column.
# also tell that ax1 x-axis is showing date as type.
fig = plt.figure()
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)
ax1.xaxis_date()

# candlestick plot on ax1 graph
candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')

# volume traded in the same ohcl period
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

plt.show()
