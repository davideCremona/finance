import os
import pandas as pd
import datetime as dt
from utils import data_inout as io

sp500tickers_filename = 'sp500tickers.pickle'
sp500tickers_path = os.path.join('data', sp500tickers_filename)
# start date and end date
start_date = dt.datetime(2015, 1, 1)
end_date = dt.datetime.now()


def get_data_from_yahoo(tickers_path, start, end):
    
    tickers = io.read_tickers(tickers_path)
    for ticker in tickers:
        ticker_csv_path = os.path.join('data', ticker)
        
        if not os.path.exists(ticker_csv_path):
            ticker_df = io.read_data_from_web(ticker, 'yahoo', start, end)
            if ticker_df is not None:
                io.save_data_to_csv(ticker_df, ticker_csv_path)
                print("{} data saved".format(ticker))
            else:
                print("{} data cannot be downloaded".format(ticker))
        else:
            print("{} data already saved".format(ticker))
    

get_data_from_yahoo(sp500tickers_path, start_date, end_date)
