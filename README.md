# Python and Google Analytics Challenge

### Data Analyst - Challenge

For the challenge, use the Google Analytics Demo Account, Master View.

Exercise:
  1. Create one geolocation segment that combines traffic originating from either RI or NY.
  2. Export January 2019 users and pageviews by day for the segment to a csv file.
  3. Use Python to read the csv file and create the following charts:
     
     a. Pageviews by week for the segment
     
     b. Pageviews/user by day for the segment
    
Requirements:
  1. All code must be written in Python and must be in a Jupyter notebook
  2. Charts must be embedded in the Jupyter notebook

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use('classic')
```

```
pageviews = pd.read_csv("/Users/--/Deskptop/January 2019 pageviews.csv", skiprows=5, sep=',', 
                        thousands=',', nrows=31)
```

```
pageviews.head()
```

| | Day Index | Pageviews |
| --- | --- | --- |
| 0 | 1/1/19 | 229 |
| 1 | 1/2/19 | 521 |
| 2 | 1/3/19 | 467 |
| 3 | 1/4/19 | 572 |
| 4 | 1/5/19 | 426 |

```
pageviews.info()

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 31 entries, 0 to 30
Data columns (total 2 columns):
Day Index    31 non-null object
Pageviews    31 non-null int64
dtypes: int64(1), object(1)
memory usage: 576.0+ bytes
```

```
pageviews['Day Index'] = pd.to_datetime(pageviews['Day Index'])
```

```
pageviews.info()

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 31 entries, 0 to 30
Data columns (total 2 columns):
Day Index    31 non-null datetime64[ns]
Pageviews    31 non-null int64
dtypes: datetime64[ns](1), int64(1)
memory usage: 576.0 bytes
```

```
new_pageviews = pageviews.groupby([
      pd.Grouper(key='Day Index',
                 freq='W-MON')])['Pageviews'].sum().reset_index().sort_values('Day Index')
```

```
new_pageviews
```

| | Day Index | Pageviews |
| --- | --- | --- |
| 0 | 2019-01-07 | 3431 |
| 1 | 2019-01-14 | 4676 |
| 2 | 2019-01-21 | 3240 |
| 3 | 2019-01-28 | 4109 |
| 4 | 2019-02-04 | 2355 |

```
new_pageviews.plot(x='Day Index', y='Pageviews', figsize=(15,8),
                   title="Pageviews by week", legend=False)
plt.xlabel('Week')
plt.ylabel('Day Index')

plt.savefig('Pageviews by week.jpg')
```

![Pageviews by week](https://github.com/gpadolina/pythonAndGoogleAnalyticsChallenge/blob/master/files/Pageviews%20by%20week.jpg)

```
users = pd.read_csv("/Users/--/Desktop/January 2019 users.csv", skiprows=5, sep=',',
                    thousands=',', nrows=31)
```

```
users.head()
```

| | Day index | Users |
| --- | --- | --- |
| 0 | 1/1/19 | 38 |
| 1 | 1/2/19 | 98 |
| 2 | 1/3/19 | 82 |
| 3 | 1/4/19 | 88 |
| 4 | 1/5/19 | 50 |
