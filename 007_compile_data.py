import os
import pickle

import pandas as pd

from utils import data_inout as io

sp500tickers_filename = 'sp500tickers.pickle'
sp500tickers_path = os.path.join('data', sp500tickers_filename)


def compile_data(tickers):

    with open(tickers, 'rb') as tickers_file:
        tickers_list = pickle.load(tickers_file)

    main_df = pd.DataFrame()

    # taking every company data and dropping all but Adj Close column
    for i, ticker in enumerate(tickers_list):

        company_data_path = os.path.join('data', ticker)
        try:
            ticker_df = pd.read_csv(company_data_path)
            ticker_df.set_index('Date', inplace=True)

            # some useful columns that will not be covered for now
            # ticker_df['{}_HL_pct_diff'.format(ticker)] = (ticker_df['High'] - ticker_df['Low']) / ticker_df['Low']
            # ticker_df['{}_daily_pct_chng'.format(ticker)] = (ticker_df['Close'] - ticker_df['Open']) / ticker_df['Open']

            # renaming "Adj Close" with company ID and dropping everything else
            ticker_df.rename(columns={'Adj Close': ticker}, inplace=True)
            ticker_df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True)

            # adding the Adj Close column for this company to the main dataframe
            if main_df.empty:
                main_df = ticker_df
            else:
                main_df = main_df.join(ticker_df, how='outer')

            if i % 10 == 0:
                print(i)

        except FileNotFoundError:
            print("data for {} not found".format(ticker))

    # checking everythig is ok and saving data
    print(main_df.head())
    io.save_data_to_csv(main_df, os.path.join('data', 'sp500_joined_closes.csv'))


compile_data(sp500tickers_path)
