import pycoingecko as pycoin
import pandas as pd
import numpy as np

def testing_code(cg):
    print(cg)
    data_pull = cg.get_price(ids ='bitcoin',vs_currencies = 'usd')
    print(type(data_pull))
    print(pd.DataFrame.from_dict(data_pull))

if __name__ == '__main__':
    cg = pycoin.CoinGeckoAPI()
    testing_code(cg)