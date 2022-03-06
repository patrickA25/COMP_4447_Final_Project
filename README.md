# COMP_4447_Final_Project

## Outline of project

[X] Need to set up data pulling process using API from coingeko

* https://www.coingecko.com/en/api/documentation
* https://github.com/man-c/pycoingecko
* 
[ ] Build out plan for what data needs to be pulled

	[] Convert everything to a jupyter notebook
	[] build basic forcasting
	[] list of possibel coins
	[] Fill out README file
		[X] Over view of project
		[X] API information
		[] Data Cleaning steps used
		[] Function list 
			[X] testing_coin_connection
			[] pull_in_top_5_data
			[] make_top_5_table
			[] get_token_list
			[] top_7_table
			[] Chart_anlysis

	[x] market cap
	[x] build time series graph
	[X] Make adjustment to scale to have cleaner look
	[x] trading price finder


---

# Over View of Project
## Goal of Project	
To use the CoinGecko API to pull in different types of data related to the criptto curency. Along with pulling in basic market data, I will also be pulling in a full list of all coins that are in Coingecko and have a person pass a filter critera to make the list of coins much shorter.

## API Information
----------------
The API that is used is the free API that is provided by CoinGecko. All of documentation can be found at [CoinGecko API](https://www.coingecko.com/en/api/documentation). Here is the link to the Github repo that made the API work more seemlessly in python [python coingecko API repo](https://github.com/man-c/pycoingecko).

## Data Cleaning
------------------------------



## Function List
------------------------------

### Testing_coin_connections
```python
testing_coin_connection(CG)
```
#### Overview
This will test the API connection to CoinGecko, and will return weather or not the coneection is good.

#### Inputes

CG => This is the API key for CoinGecko. A free key can be apptaned by running ```CoinGeckoAPI()``` from the pycoingecko package. For more information please see API seciont of the documentation above.

#### Outputs 
A string will be returned stating if the connection is good. If a connection is not good it will return a list with the first element being a stirng stateing connection is not good, and the second element being the return value from the testing the API.

### pull_in_top_5_data
```python
cryp_list = ['bitcoin', 'tether', 'ethereum','solana','binance coin']

pull_in_top_5_data(CG,cryp_list)
```
#### Overview 
This will return the 5 higest coins on CoinGeko in a table format.

#### Inputes

1) CG => This is the API key for CoinGecko. A free key can be apptaned by running ```CoinGeckoAPI()``` from the pycoingecko package. For more information please see API seciont of the documentation above.

2) cryp_list => This is a lit of top 5 current ctypto conins avaiable on CoinGeko.

#### Output 
1) This will output a table to the screen showing coin name and the current pirce in US dollars. 

### get_token_list
```python
get_token_list(CG)
```
#### Overview

The get_token_list function will return all of the current tokens that are avaiable on CoinGeko. It will return a datafrmae that has ID,symbol and the name of the coin.

#### Input

1) CG => This is the API key for CoinGecko. A free key can be apptaned by running ```CoinGeckoAPI()``` from the pycoingecko package. For more information please see API seciont of the documentation above.


#### Outputs

1) Returns a dataframe with all of the coins that are avaible on coinGeko. The dataframe has the columns, ID,symbol and name.

### top_7_table

```python
cg = pycoin.CoinGeckoAPI()
top_7_table(cg)
```

#### Overview

1) The Top_7_table function returns a table of top seven most search coins on CoinGeko and outputs the table to the standerd out. The table will have the coins ranked value,coin name, Coin ID,coin symbol, market cap, current trading price in Bitoin and current price in US dollars.

#### Input

1) CG => This is the API key for CoinGecko. A free key can be apptaned by running ```CoinGeckoAPI()``` from the pycoingecko package. For more information please see API seciont of the documentation above.

#### Outputs

1) stuff

### Chart_Analysis

#### Overview

#### Inputs

#### Outputs
