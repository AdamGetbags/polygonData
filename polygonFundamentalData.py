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

#api key from config
from polygonAPIkey import polygonAPIkey
# OR just assign your API as a string variable
# polygonAPIkey = 'apiKeyGoesHere'

# create client and authenticate w/ API key // rate limit 5 requests per min
client = RESTClient(polygonAPIkey) # api_key is used

# assign ticker
stockTicker = 'AAPL'

# empty list
data = []

# request financial statement data // add to list
for t in client.vx.list_stock_financials(ticker=stockTicker,
                                         filing_date_gte='2022-01-01'):
    data.append(t)
    
print(data)
print(dir(data[0]))
print(data[0].financials)
print(dir(data[0].financials))
print(data[0].financials.income_statement)
print(dir(data[0].financials.income_statement))
print(dir(data[0].financials.income_statement.revenues))
print(data[0].financials.income_statement.revenues.value)
