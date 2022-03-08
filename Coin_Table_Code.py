import pycoingecko as pycoin
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from rich.console import Console
from rich.table import Table


def testing_coin_connection(cg):
    test_con_value = cg.ping()
    if test_con_value == {'gecko_says': '(V3) To the Moon!'}:
        return 'Connection is good'
    else:
        return ['Connection not good',test_con_value]

def pull_in_top_5_data(cg,cryp_list):
    data_pull = cg.get_price(ids =cryp_list,vs_currencies = 'usd')
    data_pull_DF =pd.DataFrame.from_dict(data_pull,orient='index')
    data_pull_DF.index.name = 'coin_name'
    data_pull_DF.reset_index(inplace=True)
    data_pull_DF = data_pull_DF.sort_values(by=['usd'],ascending=False)
    return data_pull_DF


def make_top_5_table(cg,cryp_list):
    data_pull_DF = pull_in_top_5_data(cg,cryp_list)
    
    table = Table(title="Top 5 Coins")
    table.add_column("Coin",justify="right",style="cyan")
    table.add_column("Price",justify="right",style="green")
    
    table.add_row(str(data_pull_DF.iloc[0]["coin_name"]),str(data_pull_DF.iloc[0]["usd"]))
    table.add_row(str(data_pull_DF.iloc[1]["coin_name"]),str(data_pull_DF.iloc[1]["usd"]))
    table.add_row(str(data_pull_DF.iloc[2]["coin_name"]),str(data_pull_DF.iloc[2]["usd"]))
    table.add_row(str(data_pull_DF.iloc[3]["coin_name"]),str(data_pull_DF.iloc[3]["usd"]))
    table.add_row(str(data_pull_DF.iloc[4]["coin_name"]),str(data_pull_DF.iloc[4]["usd"]))
    console = Console()
    console.print(table)

def top_7_table(cg):
    raw_data = cg.get_search_trending()
    bt_price = cg.get_price('bitcoin',vs_currencies = 'usd')
    bt_price = ((pd.json_normalize(bt_price)))
    #top_7_data_DF =pd.DataFrame.from_dict(raw_data['coins'],orient='index')
    top_7_data_DF = (pd.json_normalize(raw_data,record_path = ['coins']))
    top_7_data_DF['US_Value'] = top_7_data_DF['item.price_btc']/int(bt_price['bitcoin.usd'])

    table = Table(title="Top 7 Searched Coins on CoinGecko")
    table.add_column("Rank",justify="center",style="white")
    table.add_column("Coin Name",justify="center",style="cyan")
    table.add_column("Coin ID",justify="center",style="white")
    table.add_column("Coin Symbol",justify="center",style="white")
    table.add_column("Market Cap",justify="center",style="white")
    table.add_column("Price BTC",justify="center",style="green")
    table.add_column("Price USD",justify="center",style="green")

    for i in top_7_data_DF.index:
        table.add_row(str(top_7_data_DF.iloc[i]["item.score"]+1),
                    str(top_7_data_DF.iloc[i]["item.name"]),
                    str(top_7_data_DF.iloc[i]["item.id"]),
                    str(top_7_data_DF.iloc[i]["item.symbol"]),
                    str(top_7_data_DF.iloc[i]["item.market_cap_rank"]),
                    str(top_7_data_DF.iloc[i]["item.price_btc"]),
                    str(top_7_data_DF.iloc[i]["US_Value"]))

    console = Console()
    console.print(table)

def get_token_list(cg):
    cg.get_coins_list()
    print((cg.get_coins_list()))
    
def testing_code(cg):
    print(cg)
    data_pull = cg.get_price(ids ='bitcoin',vs_currencies = 'usd')
    print(type(data_pull))
    print(pd.DataFrame.from_dict(data_pull))
    
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
