

# The aim is to build a dataset of S & P 500 data.
# The information we want is the S & P 500 index for each year
#NYSE
import pandas as pd
import pandas_datareader.data as data
import numpy as np
import datetime as dt
#Load the data with pandas

start = '1950-01-01'
end = '2017-03-16'
tickers = '^GSPC'
data_source = 'yahoo'

#We create a stock market data frame by retrieving S&P 500 data from yahoo finance between the years 1950 to 2017
df1 = data.DataReader(tickers, data_source, start, end)

#Make a write to csv file name stock_data.csv
df1.to_csv('stock_data.csv')

#display stock_data.csv info90
print df1.info()

#Index dataframe consists of interest rates, inflation and gdp growth rate data which is hosted on kaggle.
df2 = pd.read_csv('index.csv', parse_dates=True)

print df2.info

# Combine the year, month, column to a single datetime column and then make this an index in the df2 data frame
df2['Date'] = pd.to_datetime((df2['Year']*10000+df2['Month']*100+df2['Day']).apply(str),format='%Y%m%d')
df2.set_index('Date', inplace=True)

# We drop the fed target rate, fed upper target, fed lower target due to loads of NaN values and year, month and day columns since they were combined into a  datetime index
df2 = df2.drop('Federal Funds Target Rate',1)
df2 = df2.drop('Federal Funds Upper Target',1)
df2 = df2.drop('Federal Funds Lower Target',1)
df2 = df2.drop('Year',1)
df2 = df2.drop('Month',1)
df2 = df2.drop('Day',1)

#We then write to a new csv file named economic_data.csv
df2.to_csv('economic_data.csv')

#display index_refactor.csv info90
print df2.info()

# Now that the data frame consisting of the interest rate, inflation and GDP growth data is ready we merge with our stock market data we collection from yahoo finance.
df = df1.merge(df2, left_index=True, right_index=True, how='inner')

# We finally turn our formated data frame into an csv titled 'merged_table' for our data analysis.
df.to_csv('merged_table.csv')

#print merged_table info()
print df.info()

#remove all rows with any NaN values
revised_table = df.dropna()

# write to csv file
revised_table.to_csv('multi_linear_table.csv')

# print table info
print revised_table.info()
