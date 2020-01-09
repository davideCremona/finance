import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()

df_tsla = web.DataReader('TSLA', 'yahoo', start, end)
df_tsla.reset_index(inplace=True)
df_tsla.set_index('Date', inplace=True)
# df_tsla = df_tsla.drop('Symbol', axis=1)

print(df_tsla.head())
