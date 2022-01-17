import pycoingecko as pycoin
import pandas as pd
import numpy as np
import testing_connection as tc

cg = pycoin.CoinGeckoAPI()

def testing_code(cg):
    print(cg)
    data_pull = cg.get_price(ids ='bitcoin',vs_currencies = 'usd')
    print(type(data_pull))
    print(pd.DataFrame.from_dict(data_pull))

def testing_function(cg):
    print(cg.get_coin_market_chart_range_from_contract_address_by_id())


def main():
    testing_code(cg)
    print(tc.testing_coin_connection(cg))
    testing_function(cg)

if __name__ == '__main__':
    main ()