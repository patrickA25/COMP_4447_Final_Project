import pandas as pd
import numpy as np
import pycoingecko as pycoin
import matplotlib.pyplot as plt
import datetime

def Chart_Analysis(api_key,days_back,Coin,info):
    if info == [] or type(info) != list:
        raise ValueError('Check if info list is populated.')
    info_set = ['Price','Total Volumes','Market Cap']
    if not(set(info).issubset(info_set)):
        raise ValueError('Check all items in info variable.')
    
    raw_data = api_key.get_coin_market_chart_by_id(id = Coin,vs_currency= 'usd',days = days_back)
    
    fig, axs = plt.subplots(1,len(info),squeeze=False)
    for plot in range(len(info)):
        if info[plot] == 'Price':
            price_data = pd.json_normalize(raw_data,record_path = 'prices')
            price_data['clean_time'] = pd.to_datetime(price_data[0],unit = 'ms')
            price_data['clean_time'] = pd.to_datetime(price_data['clean_time'],format = '%Y-%m-%d')
            price_data['price'] = price_data[1]
            axs[0,plot].plot(price_data['clean_time'],price_data['price'])
            axs[0,plot].set_title(f'{Coin.capitalize()} Price Vs Time')
            axs[0,plot].tick_params(labelrotation=45)
            axs[0,plot].yaxis.set_major_formatter('${x:,.0f}')
        elif info[plot] == 'Market Cap':
            MC_data = pd.json_normalize(raw_data,record_path = 'market_caps')
            MC_data['clean_time'] = (pd.to_datetime(MC_data[0],unit = 'ms'))
            MC_data['Market_Cap'] = MC_data[1]
            axs[0,plot].plot(MC_data['clean_time'],MC_data['Market_Cap'])
            axs[0,plot].set_title(f'{Coin.capitalize()} Market Cap Vs Time')
            axs[0,plot].tick_params(labelrotation=45)
        elif info[plot] == 'Total Volumes':
            TV_data = pd.json_normalize(raw_data,record_path = 'total_volumes')
            TV_data['clean_time'] = (pd.to_datetime(TV_data[0],unit = 'ms'))
            TV_data['total_volumes'] = TV_data[1]
            axs[0,plot].plot(TV_data['clean_time'],TV_data['total_volumes'])
            axs[0,plot].set_title(f'{Coin.capitalize()} Total Volumes VS Time')
            axs[0,plot].tick_params(labelrotation=45)
    plt.show()


if __name__ == '__main__':
    cg = pycoin.CoinGeckoAPI()
    Chart_Analysis(api_key = cg
                ,days_back = 100, 
                Coin = 'bitcoin',
                info = ['Market Cap','Price','Total Volumes'])