import pandas as pd
import numpy as np
import pycoingecko as pycoin
#import matplotlib.pyplot  as plt
import plotext as plt
import datetime

def main():
    cg = pycoin.CoinGeckoAPI()
    raw_data = cg.get_coin_market_chart_by_id(id = 'bitcoin',vs_currency= 'usd',days = 100)

    price_data = pd.json_normalize(raw_data,record_path = 'prices')
    price_data['clean_time'] = pd.to_datetime(price_data[0],unit = 'ms')
    price_data['clean_time'] = pd.to_datetime(price_data['clean_time'],format = '%Y-%m-%d')
    price_data['price'] = price_data[1]
    print(price_data.dtypes)

    MC_data = pd.json_normalize(raw_data,record_path = 'market_caps')
    MC_data['clean_time'] = (pd.to_datetime(MC_data[0],unit = 'ms'))
    MC_data['Market_Cap'] = MC_data[1]

    TV_data = pd.json_normalize(raw_data,record_path = 'total_volumes')
    TV_data['clean_time'] = (pd.to_datetime(TV_data[0],unit = 'ms'))
    TV_data['total_volumes'] = TV_data[1]


    print((price_data.head()))


    dates = list(price_data["clean_time"])
    dates = [plt.datetime.datetime_to_string(el) for el in dates]    
    price = list(price_data['price'])
    
    print(dates)
    
    plt.title("Bitcoin Price Over 100 Days")
    plt.plot_size(150, 30)
    plt.plot_date(dates,price)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()
    
    
if __name__ == "__main__":
    main()
