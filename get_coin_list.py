import pycoingecko as pycoin
import pandas as pd
import numpy as np

def get_token_list(cg):
    cg.get_coins_list()
    print((cg.get_coins_list()))
    
if __name__ == '__main__':
    cg = pycoin.CoinGeckoAPI()
    get_token_list(cg)