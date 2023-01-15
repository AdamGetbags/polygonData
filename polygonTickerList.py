# -*- coding: utf-8 -*-
"""
get historical stock price data in python with polygon.io API
@author: adam getbags
"""

#pip install polygon-api-client

# import modules
from polygon import RESTClient
import pandas as pd

# api key from config
from polygonAPIkey import polygonAPIkey
# OR just assign your API as a string variable
# polygonAPIkey = 'apiKeyGoesHere'

# create client and authenticate w/ API key
client = RESTClient(polygonAPIkey) # api_key is used

# get grouped daily aggs
mktData = pd.DataFrame(client.get_grouped_daily_aggs(date='2023-01-13'))

# # get grouped daily aggs + OTC
# mktData2 = pd.DataFrame(client.get_grouped_daily_aggs(date='2023-01-13',
                                                      # include_otc=True))

# # dataframe column to list
# tickerList = list(mktData.ticker)

# # WARNING - unequal amounts of tickers from day to day
# test1 = pd.DataFrame(client.get_grouped_daily_aggs(date='2023-01-12'))
# test2 = pd.DataFrame(client.get_grouped_daily_aggs(date='2023-01-11'))
# test3 = pd.DataFrame(client.get_grouped_daily_aggs(date='2023-01-10'))

# # example of getting one ticker
# # create empty list
# tickers = []
# # page through response
# for t in client.list_tickers(ticker='AAPL'):
# # add to list
#     tickers.append(t)
    
# print(tickers)
# print(tickers[0])
# print(tickers[0].ticker)
# print(t.ticker)

# # get active tickers 
# counter = 0 
# # create empty list
# activeTickers = []
# # page through response
# for t in client.list_tickers(market='stocks',
#                              limit=1000):
# # add to list
#     activeTickers.append(t.ticker)
# # increment counter
#     counter += 1
#     print(counter)

# # # get active + inactive tickers 
# counter = 0 
# # create empty list
# allTickers = []
# # page through response
# for t in client.list_tickers(market='stocks', 
#                               active=False,
#                               limit=1000):
# # add to list
#     allTickers.append(t.ticker)
# # increment counter
#     counter += 1
#     print(counter)
        
# # get exchanges
exchanges = pd.DataFrame(client.get_exchanges(asset_class='stocks',
                                              locale='us'))

# # exchanges MIC for use in list tickers
# print(exchanges.mic)

# # remove duplicates and remove None
exchangeList = list(set(exchanges.mic))
exchangeList.remove(None)

# get all tickers from all US exchanges
usTickers = []
for x in exchangeList:
    # page through response
    for t in client.list_tickers(market='stocks',
                                 exchange=x,
                                 active=False,
                                 limit=1000):
        # add to list
        usTickers.append(t.ticker)
    # print exchange when finished   
    print(x)
        
# final ticker list
finalTickerList = set(usTickers)
