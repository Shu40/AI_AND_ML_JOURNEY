import pandas as pd

df = pd.read_csv('C:\\Users\\HP\\Desktop\\Python-DataScience-Journey\\Pandas\\industry.csv', nrows=5)
print(df.head())
#bottoms rows
print(df.tail())

df = pd.read_csv('C:\\Users\\HP\\Desktop\\Python-DataScience-Journey\\Pandas\\industry.csv', dtype={'Name': str, 'Age': int, 'City': str})
print(df.head()) 