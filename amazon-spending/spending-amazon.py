import pandas as pd
import numpy as np
import datetime

import matplotlib
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pylab
import seaborn as sns

df = pd.read_csv('/Users/dinchaney/amazon-spending/orders-amazon.csv')
df2 = pd.read_csv('/Users/dinchaney/amazon-spending/orders-amazon2.csv')
df3 = pd.read_csv('/Users/dinchaney/amazon-spending/orders-amazon3.csv')

itemsdf = pd.read_csv('/Users/dinchaney/amazon-spending/items-amazon.csv')
itemsdf2 = pd.read_csv('/Users/dinchaney/amazon-spending/items-amazon2.csv')
itemsdf3 = pd.read_csv('/Users/dinchaney/amazon-spending/items-amazon3.csv')

refundsdf = pd.read_csv('/Users/dinchaney/amazon-spending/refunds-amazon.csv')
refundsdf2 = pd.read_csv('/Users/dinchaney/amazon-spending/refunds-amazon2.csv')
refundsdf3 = pd.read_csv('/Users/dinchaney/amazon-spending/refunds-amazon3.csv')

df = df.fillna(0)
df2 = df2.fillna(0)
df3 = df3.fillna(0)

itemsdf = itemsdf.fillna(0)
itemsdf2 = itemsdf2.fillna(0)
itemsdf3 = itemsdf3.fillna(0)

refundsdf = refundsdf.fillna(0)
refundsdf2 = refundsdf2.fillna(0)
refundsdf3 = refundsdf3.fillna(0)

# print(df.head())
# print(df.shape)
# print(df2.head())
# print(df2.shape)

# print(df.columns)
# print(df2.columns)

df['Total Charged'] = df['Total Charged'].str.replace('$', '').astype(float)
itemsdf['Item Total'] = itemsdf['Item Total'].str.replace('$', '').astype(float)
refundsdf['Refund Amount'] = refundsdf['Refund Amount'].str.replace('$', '').astype(float)
# print(df.head())

df2['Total Charged'] = df2['Total Charged'].str.replace('$', '').astype(float)
itemsdf2['Item Total'] = itemsdf2['Item Total'].str.replace('$', '').astype(float)
refundsdf2['Refund Amount'] = refundsdf2['Refund Amount'].str.replace('$', '').astype(float)

df3['Total Charged'] = df3['Total Charged'].str.replace('$', '').astype(float)
itemsdf3['Item Total'] = itemsdf3['Item Total'].str.replace('$', '').astype(float)
refundsdf3['Refund Amount'] = refundsdf3['Refund Amount'].str.replace('$', '').astype(float)
# print(df2.head())

# print(df["Total Charged"].sum())
# print(df2["Total Charged"].sum())

# print(df["Total Charged"].mean())
# print(df2["Total Charged"].mean())

spendTotal = df['Total Charged'].sum() + df2['Total Charged'].sum() + df3['Total Charged'].sum()
totalCharges = len(df['Total Charged']) + len(df2['Total Charged'] + len(df3['Total Charged']))
spendAvg = spendTotal / totalCharges

# combine the dataframes
frames = [df, df2, df3]
amazonSpend = pd.concat(frames)
# items
itemsframes = [itemsdf, itemsdf2, itemsdf3]
amazonItems = pd.concat(itemsframes)
# refunds
refundsframes = [refundsdf, refundsdf2, refundsdf3]
amazonRefunds = pd.concat(refundsframes)
# sort
amazonSpend = amazonSpend.sort_values(by=['Order Date'])
amazonItems = amazonItems.sort_values(by=['Order Date'])
amazonRefunds = amazonRefunds.sort_values(by=['Order Date'])

spendMost = amazonSpend['Total Charged'].max()
itemMost = amazonItems['Item Total'].max()
spendLeast = amazonSpend['Total Charged'].min()
itemLeast = amazonItems['Item Total'].min()
itemAvg = amazonItems['Item Total'].mean()
# print('Total spent on Amazon since 2006 is $' + str(spendTotal))
# print('Average purchase amount on Amazon since 2006 is $' + str(spendAvg) + ' and average item amount is $' + str(
# itemAvg))
# print('The highest amount spent in a single purchase on Amazon since 2006 is $' + str(
# spendMost) + ' and the most expensive item is $' + str(itemMost))
# print('The lowest amount spent in a single purchase on Amazon since 2006 is $' + str(
# spendLeast) + ' and the least expensive item is $' + str(itemLeast))

# dollar amounts by day
ordersByDay = amazonSpend.groupby('Order Date').sum()['Total Charged']
HighSpendDay = ordersByDay.max()
# print('The most amount spent in one day on Amazon since 2006 is $' + str(HighSpendDay))
refundTotal = amazonRefunds['Refund Amount'].sum()
# print('Total amount of refunds from Amazon since 2006 is $' + str(refundTotal))
itemCats = amazonItems['Category'].unique()
# print('Purchases were made in these categories: ' + str(itemCats))
refundPercent = (refundTotal / spendTotal) * 100
# print('The percent of total spent that was refunded is ' + str(refundPercent) + '%')


# convert to datetime
amazonSpend['Order Date'] = pd.to_datetime(amazonSpend['Order Date'])
amazonItems['Order Date'] = pd.to_datetime(amazonItems['Order Date'])
amazonRefunds['Order Date'] = pd.to_datetime(amazonRefunds['Order Date'])
amazonRefunds['Refund Date'] = pd.to_datetime(amazonRefunds['Refund Date'])

amazonSpend = amazonSpend.set_index('Order Date')
amazonSpend['Year'] = amazonSpend.index.year
amazonSpend['Month'] = amazonSpend.index.month
amazonSpend['Weekday Name'] = amazonSpend.index.weekday_name
# print(amazonSpend.sample(5, random_state=0))

amazonItems = amazonItems.set_index('Order Date')
amazonItems['Year'] = amazonItems.index.year
amazonItems['Month'] = amazonItems.index.month
amazonItems['Weekday Name'] = amazonItems.index.weekday_name
# print(amazonItems.sample(5, random_state=0))

amazonRefunds = amazonRefunds.set_index('Order Date')
amazonRefunds['Year'] = amazonRefunds.index.year
amazonRefunds['Month'] = amazonRefunds.index.month
amazonRefunds['Weekday Name'] = amazonRefunds.index.weekday_name
# print(amazonRefunds.sample(5, random_state=0))

monthsdict = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct',
              11: 'Nov', 12: 'Dec'}
amazonSpend['MonthName'] = amazonSpend['Month'].map(monthsdict)
amazonItems['MonthName'] = amazonItems['Month'].map(monthsdict)
amazonRefunds['MonthName'] = amazonRefunds['Month'].map(monthsdict)

amazonSpend['labels'] = amazonSpend.MonthName.astype(str).str.cat(amazonSpend.Year.astype(str), sep=' ')
amazonRefunds['labels'] = amazonRefunds.MonthName.astype(str).str.cat(amazonRefunds.Year.astype(str), sep=' ')
amazonItems['labels'] = amazonItems.MonthName.astype(str).str.cat(amazonItems.Year.astype(str), sep=' ')

# print(amazonSpend.shape, amazonItems.shape, amazonRefunds.shape)
# print(amazonSpend.columns, amazonItems.columns, amazonRefunds.columns)
# print(amazonSpend.dtypes, amazonItems.dtypes, amazonRefunds.dtypes)
RorderID = amazonRefunds['Order ID'].to_list()
SorderID = amazonSpend['Order ID'].to_list()
Stotal = amazonSpend['Total Charged'].to_list()
spromos = amazonSpend['Total Promotions'].to_list()
refunds = amazonRefunds['Refund Amount'].to_list()
refundcat = amazonRefunds['Category'].to_list()
totaldict = dict(zip(SorderID, Stotal))
promodict = dict(zip(SorderID, spromos))
refundsdict = dict(zip(RorderID, refunds))
refundcatdict = dict(zip(RorderID, refundcat))

amazonTxns = pd.DataFrame()
amazonTxns['Order ID'] = amazonItems['Order ID']
amazonTxns['Year'] = amazonItems['Year']
amazonTxns['Month'] = amazonItems['Month']
amazonTxns['Weekday Name'] = amazonItems['Weekday Name']
amazonTxns['Total Promotions'] = amazonItems['Order ID'].map(promodict)
amazonTxns['Total Charged'] = amazonItems['Order ID'].map(totaldict)
amazonTxns['Category'] = amazonItems['Category']
amazonTxns['Item Total'] = amazonItems['Item Total']
amazonTxns['Refunds'] = amazonItems['Order ID'].map(refundsdict)
amazonTxns['Refund Category'] = amazonItems['Order ID'].map(refundcatdict)
amazonTxns['labels'] = amazonItems['labels']
amazonTxns = amazonTxns.replace(np.nan, 0)
amazonTxns.to_csv('amazon-transactions.csv')

# dollar amounts by day
ordersByMonth = amazonTxns.groupby('labels').sum()['Total Charged']
# itemsByDay = amazonItems.groupby('Order Date').sum()['Item Total']
returnsByMonth = amazonTxns.groupby('labels').sum()['Refunds']
# number of entries (items) for each category
itemsByCat = amazonTxns['Category'].value_counts()
# dollar amount of items by categories by day
itemsAmtByCat = amazonTxns.groupby('Category')['Item Total'].sum()
# number of entries (items) for each category that was refunded
returnsByCat = amazonTxns['Refund Category'].value_counts()
# dollar amount of returns by category
returnsAmtByCat = amazonTxns.groupby('Refund Category').sum()['Refunds']

# plot
plotDF = pd.read_csv('/Users/dinchaney/amazon-spending/amazon-transactions-all.csv')
plotDF = plotDF.fillna(0)
# print(plotDF.columns)
labels = plotDF['xlabel'].unique()
monthlyOrders = plotDF.groupby('xlabel').sum()['Total Charged']
monthlyReturns = plotDF.groupby('xlabel').sum()['Refunds']

x = ['Jan 06', 'Feb 06', 'Mar 06', 'Apr 06', 'May 06', 'Jun 06', 'Jul 06', 'Aug 06', 'Sep 06', 'Oct 06', 'Nov 06',
     'Dec 06',
     'Jan 07', 'Feb 07', 'Mar 07', 'Apr 07', 'May 07', 'Jun 07', 'Jul 07', 'Aug 07', 'Sep 07', 'Oct 07', 'Nov 07',
     'Dec 07',
     'Jan 08', 'Feb 08', 'Mar 08', 'Apr 08', 'May 08', 'Jun 08', 'Jul 08', 'Aug 08', 'Sep 08', 'Oct 08', 'Nov 08',
     'Dec 08',
     'Jan 09', 'Feb 09', 'Mar 09', 'Apr 09', 'May 09', 'Jun 09', 'Jul 09', 'Aug 09', 'Sep 09', 'Oct 09', 'Nov 09',
     'Dec 09',
     'Jan 10', 'Feb 10', 'Mar 10', 'Apr 10', 'May 10', 'Jun 10', 'Jul 10', 'Aug 10', 'Sep 10', 'Oct 10', 'Nov 10',
     'Dec 10',
     'Jan 11', 'Feb 11', 'Mar 11', 'Apr 11', 'May 11', 'Jun 11', 'Jul 11', 'Aug 11', 'Sep 11', 'Oct 11', 'Nov 11',
     'Dec 11',
     'Jan 12', 'Feb 12', 'Mar 12', 'Apr 12', 'May 12', 'Jun 12', 'Jul 12', 'Aug 12', 'Sep 12', 'Oct 12', 'Nov 12',
     'Dec 12',
     'Jan 13', 'Feb 13', 'Mar 13', 'Apr 13', 'May 13', 'Jun 13', 'Jul 13', 'Aug 13', 'Sep 13', 'Oct 13', 'Nov 13',
     'Dec 13',
     'Jan 14', 'Feb 14', 'Mar 14', 'Apr 14', 'May 14', 'Jun 14', 'Jul 14', 'Aug 14', 'Sep 14', 'Oct 14', 'Nov 14',
     'Dec 14',
     'Jan 15', 'Feb 15', 'Mar 15', 'Apr 15', 'May 15', 'Jun 15', 'Jul 15', 'Aug 15', 'Sep 15', 'Oct 15', 'Nov 15',
     'Dec 15',
     'Jan 16', 'Feb 16', 'Mar 16', 'Apr 16', 'May 16', 'Jun 16', 'Jul 16', 'Aug 16', 'Sep 16', 'Oct 16', 'Nov 16',
     'Dec 16',
     'Jan 17', 'Feb 17', 'Mar 17', 'Apr 17', 'May 17', 'Jun 17', 'Jul 17', 'Aug 17', 'Sep 17', 'Oct 17', 'Nov 17',
     'Dec 17',
     'Jan 18', 'Feb 18', 'Mar 18', 'Apr 18', 'May 18', 'Jun 18', 'Jul 18', 'Aug 18', 'Sep 18', 'Oct 18', 'Nov 18',
     'Dec 18',
     'Jan 19', 'Feb 19', 'Mar 19', 'Apr 19', 'May 19', 'Jun 19', 'Jul 19', 'Aug 19', 'Sep 19', 'Oct 19']
width = .50

# fig, ax = plt.subplots(figsize=(20, 10))
# orders = ax.bar(labels, monthlyOrders, width, label='Order Total', color='#00ffff')
# returns = ax.bar(labels, monthlyReturns, width, label='Refund Total', color='#ff00ff')
# ax.set_ylabel('Amount')
# ax.set_title('Total Amount for Amazon Orders and Refunds Each Month Since 2006  (Total Spent: $24,830.42)')
# ax.set_xticks(x)
# ax.set_xticklabels(labels, rotation=90)
# ax.legend()
# plt.tight_layout
# plt.savefig('AmountByMonth.png')
# plt.show()

categories = plotDF['Category'].unique()
categoryColors = ['blue', 'lime', 'fuchsia', 'slategrey', 'aqua', 'crimson', 'darkviolet', 'darkcyan', 'lightpink',
                  'black', 'coral', 'lightskyblue', 'yellow', 'tan', 'olive', 'deepskyblue', 'mediumspringgreen',
                  'dimgrey', 'gold', 'tomato', 'mediumorchid', 'deeppink', 'midnightblue', 'darkseagreen',
                  'springgreen',
                  'darkorange', 'khaki', 'gainsboro', 'rosybrown', 'darkgreen', 'mediumvioletred', 'paleturquoise',
                  'darkslateblue', 'lavender', 'hotpink', 'moccasin', 'maroon', 'darkolivegreen', 'aquamarine']

categorycolordict = dict(zip(categories, categoryColors))

categoryplotDF = pd.DataFrame()
categoryplotDF = plotDF.drop(columns=['labels'])
categoryplotDF['color'] = categoryplotDF['Category'].map(categorycolordict)
categoryplotDF = categoryplotDF.drop(columns=['Order ID', 'Year', 'Month', 'Weekday Name', 'Total Promotions',
                                              'Total Charged', 'Refunds', 'Refund Category'])
categoryplotDF['Order Date'] = pd.to_datetime(categoryplotDF['Order Date'])

print(categoryplotDF.index)
categoryplotDF['xMonth'] = pd.to_datetime(categoryplotDF['Order Date']).dt.to_period('M')
print(categoryplotDF.head(), categoryplotDF.dtypes)
categoryplotDF = categoryplotDF.set_index('Order Date')
print(categoryplotDF.index)

date_rng = pd.date_range(start='3/1/2006', end='10/15/2019', freq='D')
# categoryplotDF.plot.scatter(categoryplotDF.index, categoryplotDF['Item Total'], c = 'Category',
#                          colormap='spring', figsize=(20, 10))

categoryPlot = plt.scatter(categoryplotDF.index, categoryplotDF['Item Total'])
# ax2 = categoryplotDF.plot.scatter(x='xMonth', y='Item Total', c='Category', colormap='spring')
# ax2.set_title('Amount Spent on Amazon Orders by Category Since 2006')
# ax2.set_xticklabels('xlabel', rotation=90)
# plt.savefig('CategoryByMonth.png')
# plt.show('categoryPlot')

# print(categoryplotDF.head(30))

categoryOrders = categoryplotDF.groupby(['Order Date', 'Category']).sum()['Item Total'].reset_index()
categoryCounts = categoryplotDF['Category'].reset_index()

categoryCounts['Category2'] = categoryCounts['Category']
countCats = categoryCounts.groupby(['Order Date', 'Category']).count()['Category2']

#print(categoryplotDF.head())
#print(countCats.head())
#print(categoryOrders.head(10))

countCatsL = countCats.to_list()
categoryOrders['Number Items'] = countCatsL

xlabelList = categoryplotDF['xlabel'].to_list()
dateList = categoryplotDF.index.to_list()
xlabelDict = dict(zip(dateList, xlabelList))

categoryOrders['xlabel'] = categoryOrders['Order Date'].map(xlabelDict)
categoryOrders['color'] = categoryOrders['Category'].map(categorycolordict)
categoryOrders['niceDate'] = categoryOrders['Order Date'].map(lambda x: 100 * x.year + x.month)

print(categoryOrders.head(20))
categoryOrders.to_csv('categoryOrders.csv')

data = [
    go.Scatter(
           x = categoryOrders['Order Date'],
           y = categoryOrders.groupby('Order Date').sum()['Item Total'],
           text = categoryOrders['Category'],
           mode='markers',
           marker=dict(
                sizemin=10,
                size = categoryOrders['Number Items'],
                sizeref = 2.*max(categoryOrders['Number Items'])/(22.**2),
                colorscale='Rainbow',
                showscale=True,
                color=categoryOrders['color'],
                line=dict(color='black', width=1.2)))
]

figure = go.Figure(
            data = data,
            layout = go.Layout(
                #xaxis = dict(title = 'Spent per Month', tickvals = x),
                xaxis = dict(title = 'Spent per Month'),
                yaxis = dict(title = 'Amount Spent'),
                title = 'Aamazon Spending by Category'
    ))

#figure.show()
#figure.save('amazonCategories.png')

dfPivot = categoryOrders.pivot('Order Date', 'Category', 'Item Total')
dfPivot['niceDate'] = dfPivot.index.map(lambda x: 100 * x.year + x.month)
dfPivot = dfPivot.fillna(0)
dfPivot.to_csv('dfPivot.csv')
print(dfPivot.head())

