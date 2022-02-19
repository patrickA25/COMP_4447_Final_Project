import pycoingecko as pycoin
import pandas as pd
import numpy as np
import Coin_Table_Code as ctc
from rich.console import Console
from rich.table import Table


def main():
    cg = pycoin.CoinGeckoAPI()
    print(ctc.testing_coin_connection(cg))
    ctc.make_top_5_table(cg,['bitcoin', 'tether', 'ethereum','solana','binance coin'])
    ctc.top_7_table(cg)

if __name__ == '__main__':
    main ()
