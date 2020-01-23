import pickle
import pandas as pd
import pandas_datareader.data as web

def read_data_from_web(company_id, service, start_date, end_date):
    # download company data from service API
    try:
        df = web.DataReader(company_id, service, start_date, end_date)

        # set new index of the dataframe to 'Date' column only
        df.reset_index(inplace=True)
    
        df.set_index('Date', inplace=True)
    except KeyError:
        print("cannot load {}".format(company_id))
        return None

    return df

def read_data_from_csv(file_path):
    df = pd.read_csv(file_path, parse_dates=True, index_col=0)

    # set new index of the dataframe to 'Date' column only
    df.reset_index(inplace=True)
    try:
        df.set_index('Date', inplace=True)
    except KeyError:
        print(df.head())
        a = input()

    return df

def save_data_to_csv(df, file_path):
    df.to_csv(file_path)

def read_tickers(tickers_path):
    tickers = []
    with open(tickers_path, 'rb') as tickers_file:
        tickers = pickle.load(tickers_file)
    return tickers
