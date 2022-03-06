import pycoingecko as pycoin
import pandas as pd
import numpy as np

def get_token_list(cg):
    #this will return a list of dic containing ID,syble and name
    temp_list = cg.get_coins_list()
    return pd.DataFrame(temp_list).head()

if __name__ == '__main__':
    cg = pycoin.CoinGeckoAPI()
    print(get_token_list(cg))