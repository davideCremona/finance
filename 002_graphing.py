import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

# start date and end date
start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()

def read_data_from_web(company_id, service, start_date, end_date):
    # download company data from service API
    df = web.DataReader(company_id, service, start, end)

    # set new index of the dataframe to 'Date' column only
    df.reset_index(inplace=True)
    df.set_index('Date', inplace=True)

    return df

# df_tsla = read_data_from_web('TSLA', 'yahoo', start, end)
# df_tsla.to_csv('data/TSLA.csv')

def read_data_from_csv(file_path):
    df = pd.read_csv(file_path, parse_dates=True, index_col=0)

    # set new index of the dataframe to 'Date' column only
    df.reset_index(inplace=True)
    df.set_index('Date', inplace=True)

    return df


df_tsla = read_data_from_csv('data/TSLA.csv')

# explore Tesla data
# print(df_tsla.head())

# plot entire dataframe
# df_tsla.plot()
# plt.show()

# plot only adjusted close
# df_tsla['Adj Close'].plot()
# plt.show()

def plot_df_columns(df, columns):
    df[columns].plot()
    plt.show()

plot_df_columns(df_tsla, ['High', 'Low'])
