# COMP_4447_Final_Project

## Outline of project

[X] Need to set up data pulling process using API from coingeko

* https://www.coingecko.com/en/api/documentation
* https://github.com/man-c/pycoingecko
* 
[ ] Build out plan for what data needs to be pulled

	[] Convert everything to a jupyter notebook
	[] build basic forcasting
	[] Fill out README file
		[X] Over view of project
		[X] API information
		[X] make table of contents
		[X] Data Cleaning steps used
		[] Function list 
			[X] testing_coin_connection
			[X] pull_in_top_5_data
			[X] make_top_5_table
			[X] get_token_list
			[X] top_7_table
			[] Chart_anlysis
			[] basic forcasting
	[X] list of possibel coins
	[x] market cap
	[x] build time series graph
	[X] Make adjustment to scale to have cleaner look
	[x] trading price finder

# Table of Contents
1. [Project Overview](#projectoverview)
2. [API Information](#APIinformation)
3. [Data Cleaning](#DataCleaning)
4. [Function List](#Functionlist)
	1. [Test_coin_connection](#testcoinconnection)
	3. [pull_in_top_5_data](#pullintop5data)
	4. [get_token_list](#gettokenlist)
	5. [top_7_table](#top7table)
	6. [Chart Analysis](#chartanalysis)
	7. [forcasting](#basicforcasting)

---

# Over View of Project <a name="projectoverview"></a>	
To use the CoinGecko API to pull in different types of data related to the criptto curency. Along with pulling in basic market data, I will also be pulling in a full list of all coins that are in Coingecko and have a person pass a filter critera to make the list of coins much shorter.

# API Information <a name="APIinformation"></a>
----------------
The API that is used is the free API that is provided by CoinGecko. All of documentation can be found at [CoinGecko API](https://www.coingecko.com/en/api/documentation). Here is the link to the Github repo that made the API work more seemlessly in python [python coingecko API repo](https://github.com/man-c/pycoingecko).

# Data Cleaning <a name="DataCleaning"></a>
------------------------------
A lot of the data cleaning was made easy because of the pycoingecko python packages. Most of the data from CoinGeck API would come back in a dictionary. Below are some examples of how the data would come back.

## Getting Price data
```python
cg.get_price(ids='bitcoin',vs_currencies='usd')
{'bitcoin'
	{'usd' : 38258}}
	
cg.get_price(ids = ['bitcoin','litecoin'],vs_currencies='usd')
{'bitcoin': 
	{'usd': 38242}, 
'litecoin': 
	{'usd': 99.21}}
```

## Getting Markget data
```python
cg.get_coin_market_chart_by_id(id = 'bitcoin',vs_currency= 'usd',days = 1)

{'prices':
	{[1646699541000, 38242.27428142403]},
 'market_caps':
 	{[1646699541000, 725275467246.7909]},
 'total_volumes':
 	{[1646699541000, 24057303397.88596]}}
```
The above code is returning a dictionary with keys of prices,market_caps,and total_volumnes with each element being a list of values. The first value in the list is a time stamp in the format of "find the format name" and the second value being the value of the dictorny key. The way I would extract infromation for a given key I would run ```pd.json_normalize(raw_data,record_path = 'prices')```, to convert the time into standered datetime format I would run the following command ```pd.to_datetime(price_data[0],unit = 'ms')```

# Function List <a name="Functionlist"></a>
------------------------------

## Testing_coin_connections <a name="testcoinconnection"></a>
```python
cg = pycoin.CoinGeckoAPI()
testing_coin_connection(CG)
```
### Overview
This will test the API connection to CoinGecko, and will return weather or not the coneection is good.

### Inputes

CG => This is the API key for CoinGecko. A free key can be apptaned by running ```CoinGeckoAPI()``` from the pycoingecko package. For more information please see API seciont of the documentation above.

### Outputs 
A string will be returned stating if the connection is good. If a connection is not good it will return a list with the first element being a stirng stateing connection is not good, and the second element being the return value from the testing the API.

## pull_in_top_5_data <a name="pullintop5data"></a>
```python

cg = pycoin.CoinGeckoAPI()
cryp_list = ['bitcoin', 'tether', 'ethereum','solana','binance coin']

pull_in_top_5_data(CG,cryp_list)
```
### Overview 
This will return the 5 higest coins on CoinGeko in a table format.

### Inputes

1) CG => This is the API key for CoinGecko. A free key can be apptaned by running ```CoinGeckoAPI()``` from the pycoingecko package. For more information please see API seciont of the documentation above.

2) cryp_list => This is a lit of top 5 current ctypto conins avaiable on CoinGeko.

### Output 
1) This will output a table to the screen showing coin name and the current pirce in US dollars. 

## get_token_list <a name="gettokenlist"></a>
```python
cg = pycoin.CoinGeckoAPI()
get_token_list(CG)
```
### Overview

The get_token_list function will return all of the current tokens that are avaiable on CoinGeko. It will return a datafrmae that has ID,symbol and the name of the coin.

### Input

1) CG => This is the API key for CoinGecko. A free key can be apptaned by running ```CoinGeckoAPI()``` from the pycoingecko package. For more information please see API seciont of the documentation above.


### Outputs

1) Returns a dataframe with all of the coins that are avaible on coinGeko. The dataframe has the columns, ID,symbol and name.

## top_7_table <a name="top7table"></a>

```python
cg = pycoin.CoinGeckoAPI()
top_7_table(cg)
```

### Overview

1) The Top_7_table function returns a table of top seven most search coins on CoinGeko and outputs the table to the standerd out. The table will have the coins ranked value,coin name, Coin ID,coin symbol, market cap, current trading price in Bitoin and current price in US dollars.

### Input

1) CG => This is the API key for CoinGecko. A free key can be apptaned by running ```CoinGeckoAPI()``` from the pycoingecko package. For more information please see API seciont of the documentation above.

### Outputs
1) Returns a dataframe with all of the top 7 coins being search for on CoinGecko.
1) stuff 

## Chart_Analysis <a name="chartanalysis"></a>
```python 
cg = pycoin.CoinGeckoAPI()
Chart_Analysis(api_key = cg, 
	       days_back = 90,
	       coin = 'bitcoin',
	       info = ['Price','Market Cap','Total Volumes'])
	       
```
### Overview
1) The Chart analysis fucnctions can return upto 3 charts related to any one given coin. That charts that can be returned are price over time, market cap over time and total volume over time.
 
### Inputs
1) api_key => This is the API key for CoinGecko. A free key can be apptaned by running ```CoinGeckoAPI()``` from the pycoingecko package. For more information please see API seciont of the documentation above.
2) days_back => How many days back you would like to pull coin information.
3) coin => The name of the coin that you want to pull information for.
4) info => A list of graphs that you would like to see. The three graphs that can be inputed Price, Market Cap and total volume.
### Outputs

## Forcasting_a_Coin <a name="basicforcasting"></a>
