import pandas as pd

df = pd.read_csv('C:\\Users\\HP\\Desktop\\Python-DataScience-Journey\\Pandas\\industry.csv', nrows=5)
print(df)




df = pd.read_csv('C:\\Users\\HP\\Desktop\\Python-DataScience-Journey\\Pandas\\industry.csv',na_values=['NA', 'Missing'])  

print(df.dropna())

#axis remove columns

print(df.dropna(axis=1))

#how  all null values in a row

print(df.dropna(how='all'))
#thresh how many non null values in a row or column666
print(df.dropna(thresh=2))

#subset remove null values in specific columns
print(df.dropna(subset=['Name', 'Age']))

