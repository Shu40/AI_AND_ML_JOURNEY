import pandas as pd

df = pd.read_csv('C:\\Users\\HP\\Desktop\\Python-DataScience-Journey\\Pandas\\industry.csv')

print(df.isnull())
# how much null values in each column
print(df.isnull().sum())

print(df.isnull().sum().sum())