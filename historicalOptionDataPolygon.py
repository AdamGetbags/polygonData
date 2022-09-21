# -*- coding: utf-8 -*-
"""

get historical option price data in python with polygon.io API
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

#create client and authenticate w/ API key // rate limit 5 requests per min
client = RESTClient(polygonAPIkey) # api_key is used

contractNames = []
for c in client.list_options_contracts(underlying_ticker = 'AAPL', limit = 1000):
    contractNames.append(c)
print(contractNames)

#polygon data structure
#type(contractNames[398])

#to view individual contract general data
contractData = contractNames[398]

#get options ticker
optionsTicker = contractData.ticker

#daily options price bars
dailyOptionData = client.get_aggs(ticker = optionsTicker, 
                             multiplier = 1,
                             timespan = 'day',
                             from_ = '1900-01-01',
                             to = '2100-01-01')

#five minute price bars
# intradayOptionData = client.get_aggs(ticker = optionsTicker, 
#                              multiplier = 5,
#                              timespan = 'minute',
#                              from_ = '1900-01-01',
#                              to = '2100-01-01')

#two hour price bars
# hourlyOptionData = client.get_aggs(ticker = optionsTicker, 
#                              multiplier = 2,
#                              timespan = 'hour',
#                              from_ = '1900-01-01',
#                              to = '2100-01-01')

#list of polygon OptionsContract objects to DataFrame
optionDataFrame = pd.DataFrame(dailyOptionData)

#create Date column
optionDataFrame['Date'] = optionDataFrame['timestamp'].apply(
                          lambda x: pd.to_datetime(x*1000000))

optionDataFrame = optionDataFrame.set_index('Date')

#generate plotly figure
fig = go.Figure(data=[go.Candlestick(x=optionDataFrame.index,
                open=optionDataFrame['open'],
                high=optionDataFrame['high'],
                low=optionDataFrame['low'],
                close=optionDataFrame['close'])])

#open figure in browser
plot(fig, auto_open=True)
