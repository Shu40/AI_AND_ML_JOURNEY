#fillina fills the NaN Value with given value

import pandas as pd

df = pd.read_csv('C:\\Users\\HP\\Desktop\\Python-DataScience-Journey\\Pandas\\industry.csv')

print(df.fillna())

#fillna with specific value

print(df.fillna(0).value_counts())


# method fillna with method parameter

print(df.fillna(method='ffill',axis=0))

print(df.fillna(method='bfill',axis=0))

