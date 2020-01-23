import bs4 as bs
import pickle
import requests
import os

sp500tickers_filename = 'sp500tickers.pickle'

def save_sp500_tickers(save_dir):

    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})

    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        ticker = ticker.replace('\n', '')
        tickers.append(ticker)

    save_path = os.path.join(save_dir, sp500tickers_filename)
    with open(save_path, 'wb') as f:
        pickle.dump(tickers, f)

def test_script():

    save_sp500_tickers('data')

    debug_list = pickle.load(open(os.path.join('data', sp500tickers_filename), 'rb'))
    print(debug_list)

test_script()
