import pycoingecko as pycoin
import pandas as pd
import numpy as np
from rich.console import Console
from rich.table import Table



cg = pycoin.CoinGeckoAPI()
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

table.add_row(str(top_7_data_DF.iloc[0]["item.score"]+1),str(top_7_data_DF.iloc[0]["item.name"]),str(top_7_data_DF.iloc[0]["item.id"]),str(top_7_data_DF.iloc[0]["item.symbol"]),
            str(top_7_data_DF.iloc[0]["item.market_cap_rank"]),str(top_7_data_DF.iloc[0]["item.price_btc"]),str(top_7_data_DF.iloc[0]["US_Value"]))

table.add_row(str(top_7_data_DF.iloc[1]["item.score"]+1),str(top_7_data_DF.iloc[1]["item.name"]),str(top_7_data_DF.iloc[1]["item.id"]),str(top_7_data_DF.iloc[1]["item.symbol"]),
            str(top_7_data_DF.iloc[1]["item.market_cap_rank"]),str(top_7_data_DF.iloc[1]["item.price_btc"]),str(top_7_data_DF.iloc[1]["US_Value"]))

table.add_row(str(top_7_data_DF.iloc[2]["item.score"]+1),str(top_7_data_DF.iloc[2]["item.name"]),str(top_7_data_DF.iloc[2]["item.id"]),str(top_7_data_DF.iloc[2]["item.symbol"]),
            str(top_7_data_DF.iloc[2]["item.market_cap_rank"]),str(top_7_data_DF.iloc[2]["item.price_btc"]),str(top_7_data_DF.iloc[2]["US_Value"]))

table.add_row(str(top_7_data_DF.iloc[3]["item.score"]+1),str(top_7_data_DF.iloc[3]["item.name"]),str(top_7_data_DF.iloc[3]["item.id"]),str(top_7_data_DF.iloc[3]["item.symbol"]),
            str(top_7_data_DF.iloc[3]["item.market_cap_rank"]),str(top_7_data_DF.iloc[3]["item.price_btc"]),str(top_7_data_DF.iloc[3]["US_Value"]))

table.add_row(str(top_7_data_DF.iloc[4]["item.score"]+1),str(top_7_data_DF.iloc[4]["item.name"]),str(top_7_data_DF.iloc[4]["item.id"]),str(top_7_data_DF.iloc[4]["item.symbol"]),
            str(top_7_data_DF.iloc[4]["item.market_cap_rank"]),str(top_7_data_DF.iloc[4]["item.price_btc"]),str(top_7_data_DF.iloc[4]["US_Value"]))

table.add_row(str(top_7_data_DF.iloc[5]["item.score"]+1),str(top_7_data_DF.iloc[5]["item.name"]),str(top_7_data_DF.iloc[5]["item.id"]),str(top_7_data_DF.iloc[5]["item.symbol"]),
            str(top_7_data_DF.iloc[5]["item.market_cap_rank"]),str(top_7_data_DF.iloc[5]["item.price_btc"]),str(top_7_data_DF.iloc[5]["US_Value"]))

table.add_row(str(top_7_data_DF.iloc[6]["item.score"]+1),str(top_7_data_DF.iloc[6]["item.name"]),str(top_7_data_DF.iloc[6]["item.id"]),str(top_7_data_DF.iloc[6]["item.symbol"]),
            str(top_7_data_DF.iloc[6]["item.market_cap_rank"]),str(top_7_data_DF.iloc[6]["item.price_btc"]),str(top_7_data_DF.iloc[6]["US_Value"]))

console = Console()
console.print(table)
