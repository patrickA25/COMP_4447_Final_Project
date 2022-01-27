import pycoingecko as pycoin
import pandas as pd
import numpy as np
from rich.console import Console
from rich.table import Table


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