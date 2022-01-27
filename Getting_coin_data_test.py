import pycoingecko as pycoin
import pandas as pd
import numpy as np
import top_5_data as top
import testing_connection as tc
from rich.console import Console
from rich.table import Table


def main():
    cg = pycoin.CoinGeckoAPI()
    print(tc.testing_coin_connection(cg))
    top.make_top_5_table(cg,['bitcoin', 'tether', 'ethereum','solana','binance coin'])

if __name__ == '__main__':
    main ()