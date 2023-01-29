# -*- coding: utf-8 -*-
"""
get market snapshot data in python with polygon.io API
@author: adam getbags
"""

# pip OR conda install
# pip install polygon-api-client
# pip install plotly

# import modules
from polygon import RESTClient
import datetime as dt
import pandas as pd

# api key from config
from polygonAPIkey import polygonAPIkey
# OR just assign your API as a string variable
# polygonAPIkey = 'apiKeyGoesHere'

# create client and authenticate w/ API key // rate limit 5 requests per min
client = RESTClient(polygonAPIkey) # api_key is used

# assign ticker
stockTicker = 'AAPL'

# request single ticker data // market type under ticker types in docs
singleSnap = client.get_snapshot_all(market_type='stocks', tickers=stockTicker)

# review object
dir(singleSnap[0])

# day and previous day
singleSnap[0].day
singleSnap[0].prev_day

# accessing agg data
dir(singleSnap[0].day)
singleSnap[0].day.open

# ticker 
singleSnap[0].ticker

# min = minute snapshot
singleSnap[0].min

# daily change + pct change
singleSnap[0].todays_change
singleSnap[0].todays_change_percent

# time snapshot was updated
singleSnap[0].updated

# request multiple ticker's data // market type under ticker types in docs
marketSnap = client.get_snapshot_all(market_type='stocks')

# loop through to get data
for i in range(0,5):
    print(marketSnap[i].ticker)
    
# request top gainers    
winners = client.get_snapshot_direction(market_type='stocks', 
                                        direction='gainers')
# review data
type(winners)
len(winners)
dir(winners[0])
winners[0].ticker

# get all tickers
for i in winners:
    print(i.ticker)
    
# request top losers
losers = client.get_snapshot_direction(market_type='stocks', 
                                        direction='losers')

# get all tickers
for i in losers:
    print(i.ticker) 