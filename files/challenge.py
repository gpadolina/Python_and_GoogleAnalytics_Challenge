import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use('classic')

pageviews = pd.read_csv("/Users/--/Desktop/January 2019 pageviews.csv",
                        skiprows=5, sep=',', thousands=',', nrows=31)

pageviews.head()

pageviews.info()

pageviews['Day Index'] = pd.to_datetime(pageviews['Day Index'])
pageviews.info()

new_pageviews = pageviews.groupby([
  pd.Grouper(key='Day Index',
             freq='W-MON')])['Pageviews'].sum().reset_index().sort_values('Day Index')
new_pageviews

new_pageviews.plot(kind='barh',
                   x='Day Index',
                   y='Pageviews',
                   figsize=(15, 8),
                   title='Pageviews by week',
                   legend=False)
plt.xlabel('Pageviews')
plt.ylabel('Day Index')
plt.xticks(rotation=70)

plt.savefig('pageviews.png')

pageviews.plot(figsize=(15, 8),
               x='Day Index',
               y='Pageviews',
               title='Pageviews by day',
               legend=False)
plt.ylabel('Pageviews')
plt.xlabel('Day Index')
plt.grid(True)

plt.savefig('pageviews2.png')

users = pd.read_csv("/Users/--/Desktop/January 2019 users.csv",
                    skiprows=5, sep=',', thousands=',', nrows=31)

users.head()

users.info()

users['Day Index'] = pd.to_datetime(users['Day Index'])

users.info()

users.plot(figsize=(15, 8),
           x='Day Index',
           y='Users',
           title='Users by day',
           legend=False)
plt.ylabel('Users')
plt.xlabel('Day Index')
plt.grid(True)

plt.savefig('users.png')
