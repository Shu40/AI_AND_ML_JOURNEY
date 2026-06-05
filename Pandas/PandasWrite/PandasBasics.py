import pandas as pd

df = pd.read_csv('C:\\Users\\HP\\Desktop\\Python-DataScience-Journey\\Pandas\\industry.csv', nrows=5)
print(df)

#replace null values with 0
print(df.replace(to_replace=pd.NA, value=0))

#interpolate method to fill null values
print(df.interpolate(method='linear', axis=0))
print(df.interpolate(method='quadratic', axis=0))
print(df.interpolate(method='cubic', axis=0))


#.loc[] and .iloc[] to fill null values
print(df.loc[0:4, 'Age'].fillna(0))
print(df.iloc[0:5, 1].fillna(0))
print(df.loc[0:4, 'Age'].interpolate(method='linear', axis=0))
print(df.iloc[0:5, 1].interpolate(method='linear', axis=0))


#grouby method to fill null values
print(df.groupby('City')['Age'].transform(lambda x: x.fillna(x.mean())))
print(df.groupby('City')['Age'].transform(lambda x: x.interpolate(method='linear', axis=0)))

#merge two dataframes to fill null values
df1 = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
                    'Age': [25, 30, 35, 40, 45],
                    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']})
print(df1)
df2 = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
                    'Age': [pd.NA, pd.NA, pd.NA, pd.NA, pd.NA],
                    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']})
print(df2)
df_merged = pd.merge(df1, df2, on='Name', how='left')
print(df_merged)


#concat two dataframes to fill null values
df_concat = pd.concat([df1, df2], axis=0)
print(df_concat)

#apend two dataframes to fill null values
df_appended = df1.append(df2, ignore_index=True)

#ds.pivot_table to fill null values
df_pivot = df.pivot_table(index='City', values='Age', aggfunc='mean')
print(df_pivot)

#pd.melt to fill null values
df_melted = pd.melt(df, id_vars=['Name', 'City'], value_vars=['Age'])
print(df_melted)
                    
                          
