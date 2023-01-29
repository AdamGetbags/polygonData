# -*- coding: utf-8 -*-
"""
get historical dividend data in python with polygon.io API
@author: adam getbags
"""

# pip OR conda install
# pip install polygon-api-client
# pip install plotly

# import modules
from polygon import RESTClient
import datetime as dt
import pandas as pd
from datetime import datetime

# api key from config
from polygonAPIkey import polygonAPIkey
# OR just assign your API as a string variable
# polygonAPIkey = 'apiKeyGoesHere'

# create client and authenticate w/ API key // rate limit 5 requests per min
client = RESTClient(polygonAPIkey) # api_key is used

# assign ticker
stockTicker = 'AAPL'

# empty list
divData = []
dividendHistory = []
counter = 0

# paginated end point
for t in client.list_dividends(ticker=stockTicker, limit=1000):
    
    #add object to list
    divData.append(t)
    
    #create tuple and add to list
    tempTuple = (datetime.strptime(t.ex_dividend_date, '%Y-%m-%d'),
                 t.cash_amount)
    dividendHistory.append(tempTuple)

    print(counter)
    counter += 1

print(divData)
type(divData)
dir(divData[0])

print(divData[0].ticker + ' went ex-div on ' +
      divData[0].ex_dividend_date + ' and the dividend was $' +
      str(divData[0].cash_amount))

dividendHistory.reverse()

# create dataframe
divTimeSeries = pd.DataFrame(dividendHistory, 
                             columns =['Date', 'Dividend'])

divTimeSeries = divTimeSeries.set_index('Date')