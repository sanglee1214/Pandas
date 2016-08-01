# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 08:55:04 2016

@author: JosephNelson
"""

# load the data
import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/generalassembly-studio/dsi-course-materials/master/curriculum/04-lessons/week-09/2.2-lesson/assets/datasets/rossmann.csv?token=ANUte3zX50f5qIbSRNvrjB6usVHFbLJtks5XaStVwA%3D%3D', skipinitialspace=True)
import seaborn as sns

data.head() # check it out

# Most interested in date - format properly and convert to index
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# create new columns for year and month 
data['Year'] = data.index.year
data['Month'] = data.index.month

data.head() # check it out (see what happened?)

# easily filter by date
data['2014']        # by year
data['2015-05']     # by particular month

# There are over a million sales data points in this dataset, so for some simple EDA we will focus on just one store.
store1_data = data[data.Store == 1]
store1_data.head()

'''
As we begin to study the sales from this drugstore, we also want to know both the time dependent elements of sales as 
well as whether promotions or holidays effected these sales. To start, we can compare the average sales on those events.

To compare sales on holidays, we can compare the sales using box-plots, which allows us to compare the distribution of 
sales on holidays against all other days. On state holidays the store is closed (which means there are 0 sales), and 
on school holidays the sales are relatively similar. These types of insights represent the contextual knowledge needed 
to truly explain time series phenomenon. Can you think of any other special considerations we should make when tracking sales?

'''

# check similarity between School Holiday and Sales
sns.factorplot(
    x='SchoolHoliday',
    y='Sales',
    data=store1_data,
    kind='box'
)

#  We can see that there is a difference in sales on promotion days
sns.factorplot(
    col='Open',
    x='Promo',
    y='Sales',
    data=store1_data,
    kind='box'
)

'''
Why is it important to separate out days where the store is closed? 
Because there aren't any promotions on those days either, so including 
them will bias your sales data on days without promotions! Remember: 
Data Scientists needs to think about the business logic (context) as well as 
analyzing the raw data.
'''

# perhaps plot sales across day of the week
sns.factorplot(
    col='Open',
    x='DayOfWeek',
    y='Sales',
    data=store1_data,
    kind='box',
)

# Consider sales across multiple years. How did sales change from 2014-2015?

# Filter to days store 1 was open
store1_open_data = store1_data[store1_data.Open==1]
store1_open_data[['Sales']].plot()          # sales over time
store1_open_data[['Customers']].plot()      # customers over time

# EXERCISE: Use filtering to show the trend in 2015 alone

store1_data_2015 = store1_data['2015']
store1_data_2015[
    store1_data_2015.Open==1
][['Sales']].plot()


'''
Computing Autocorrelation

To measure how much the sales are correlated with each other, we want to compute 
the autocorrelation of the 'Sales' column. In pandas, we'll do this with the 
autocorr function.

autocorr takes one argument, the lag - which is how many prior data points 
should be used to compute the correlation. If we set the lag to 1, we compute 
the correlation between every point and the point directly preceding it, 
while setting lag to 10. This computes the correlation between every point 
and the point 10 days earlier:
'''

data['Sales'].resample('D', how='mean').autocorr(lag=1)

'''
If we want to investigate trends over time in sales, as always, we will 
start by computing simple aggregates. We want to know: what were the mean 
and median sales in each month and year?

In Pandas, this is performed using the resample command, which is very 
similar to the groupby command. It allows us to group over different 
time intervals.

We can use data.resample and provide as arguments: - The level on 
which to roll-up to, 'D' for day, 'W' for week, 'M' for month, 'A' 
for year - The aggregation to perform: 'mean', 'median', 'sum', etc.
'''

# Here we can see again that December 2013 and 2014 were the highest average sale months.
data[['Sales']].resample('A', how=['median', 'mean'])
data.resample('A', how=['median', 'mean'])              # whole dataframe


data[['Sales']].resample('M', how=['median', 'mean'])

# Resample to have the daily total over all stores
# Alternatively, this could a daily average over all store with how='mean'
daily_store_sales = data[['Sales']].resample('D', how='sum')

# CHECK: What is a rolling mean? Why might it be useful?

# 3-day rolling mean of daily store sales
pd.rolling_mean(daily_store_sales, window=3, center=True)
pd.rolling_mean(daily_store_sales, window=3, center=True)['2015']   # filter to 2015 only
pd.rolling_mean(daily_store_sales, window=10, center=True).plot()   # plot

# We can also use exponential moving average. CHECK: What is the difference?
pd.ewma(data['Sales'], span=10)

'''
WINDOW FUNCTIONS

Pandas rolling_mean and rolling_median are only two examples of Pandas
window function capabilities. Window functions operate on a set of N
consecutive rows (i.e.: a window) and produce an output.

n addition to rolling_mean and rolling_median, there are rolling_sum,
rolling_min, rolling_max... and many more.

Another common one is diff, which takes the difference over time.
pd.diff takes one argument: periods, which measures how many rows
prior to use for the difference.

For example, if we want to compute the difference in sales,
day by day, we could compute:
'''

daily_store_sales.diff(periods=1) # day by day difference in sales
daily_store_sales.diff(periods=7) # compare same day each week

# Difference functions allow us to identify seasonal changes when we see repeated up or downswings.
# An example from FiveThirtyEight:
# http://i2.wp.com/espnfivethirtyeight.files.wordpress.com/2015/03/casselman-datalab-wsj2.png?quality=90&strip=all&w=575&ssl=1

'''
Pandas Expanding Functions

In addition to the set of rolling_* functions, Pandas also 
provides a similar collection of expanding_* functions, which, 
instead of using a window of N values, uses all values up until 
that time.
'''


pd.expanding_mean(daily_store_sales) # average date from first till last date specified
pd.expanding_sum(daily_store_sales) # sum of average sales per store until that date

'''
EXERCISES

1. Plot the distribution of sales by month and compare the effect of promotions.
hint: try using hue in sns
2. Are sales more correlated with the prior date, a similar date last year, or a similar date last month?
3. Plot the 15 day rolling mean of customers in the stores.
4. Identify the date with largest drop in sales from the same date in the previous week.
5. Compute the total sales up until Dec. 2014.
6. When were the largest differences between 15-day moving/rolling averages? HINT: Using rolling_mean and diff
'''

# Plot the distribution of sales by month and compare the effect of promotions
sns.factorplot(
    col='Open',
    hue='Promo',
    x='Month',
    y='Sales',
    data=store1_data,
    kind='box'
)

# Are sales more correlated with the prior date, a similar date last year, or a similar date last month?
# Compare the following:
average_daily_sales = data[['Sales', 'Open']].resample('D', how='mean')

average_daily_sales['Sales'].autocorr(lag=1)        # day

average_daily_sales['Sales'].autocorr(lag=30)       # month  

average_daily_sales['Sales'].autocorr(lag=365)      # year

# Plot the 15 day rolling mean of customers in the stores:
pd.rolling_mean(data[['Customers']], window=15, freq='D').plot()

# Identify the date with largest drop in average store sales from the same date in the previous month:
average_daily_sales = data[['Sales', 'Open']].resample('D', how='mean')
average_daily_sales['DiffVsLastWeek'] = average_daily_sales[['Sales']].diff(periods=7)

average_daily_sales.sort(['DiffVsLastWeek']).head

# Unsurprisingly, this day is Dec. 25 and Dec. 26 in 2014 and 2015, when the store is closed and there are many sales in the preceding week. How about when the store is open?
average_daily_sales[average_daily_sales.Open == 1].sort(['DiffVsLastWeek'])

# Compute the total sales up until Dec. 2014:
total_daily_sales = data[['Sales']].resample('D', how='sum')
pd.expanding_sum(total_daily_sales)['2014-12']
# THIS IS NOT pd.expanding_sum(data['Sales'])['2014-12']


# When were the largest differences between 15-day moving/rolling averages? HINT: Using rolling_mean and diff
pd.rolling_mean(total_daily_sales, window=15).diff(1).sort('Sales')
