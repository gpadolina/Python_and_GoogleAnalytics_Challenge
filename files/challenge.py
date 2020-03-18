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
