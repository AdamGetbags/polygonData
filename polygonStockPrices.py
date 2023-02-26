# -*- coding: utf-8 -*-
"""
get historical stock price data in python with polygon.io API
@author: adam getbags
"""

#pip OR conda install
#pip install polygon-api-client
#pip install plotly

#import modules
from polygon import RESTClient
import datetime as dt
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot

#api key from config
from polygonAPIkey import polygonAPIkey
# OR just assign your API as a string variable
# polygonAPIkey = 'apiKeyGoesHere'

# create client and authenticate w/ API key // rate limit 5 requests per min
client = RESTClient(polygonAPIkey) # api_key is used

stockTicker = 'AAPL'

# daily bars
dataRequest = client.get_aggs(ticker = stockTicker, 
                              multiplier = 1,
                              timespan = 'day',
                              from_ = '2022-09-01',
                              to = '2100-01-01')

# five minute price bars
# dataRequest = client.get_aggs(ticker = stockTicker, 
#                               multiplier = 5,
#                               timespan = 'minute',
#                               from_ = '2023-02-24',
#                               to = '2100-01-01')

# two hour price bars
# dataRequest = client.get_aggs(ticker = stockTicker, 
#                               multiplier = 2,
#                               timespan = 'hour',
#                               from_ = '2023-01-15',
#                               to = '2100-01-01')

# list of polygon agg objects to DataFrame
priceData = pd.DataFrame(dataRequest)

#create Date column
priceData['Date'] = priceData['timestamp'].apply(
                          lambda x: pd.to_datetime(x*1000000))

priceData = priceData.set_index('Date')

#generate plotly figure
fig = go.Figure(data=[go.Candlestick(x=priceData.index,
                open=priceData['open'],
                high=priceData['high'],
                low=priceData['low'],
                close=priceData['close'])])

#open figure in browser
plot(fig, auto_open=True)