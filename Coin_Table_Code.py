import pycoingecko as pycoin
import pandas as pd
import numpy as np
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
