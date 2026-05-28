import pandas as pd

# Creating a Pandas Series from a list
data = [10, 20, 30, 40, 50,'data']
print(data)

series = pd.Series(data)
print(series)

print(type(series))

series = pd.Series(['a', 'b', 'c', 'd', 'e','f'])
print(series)

empty_series = pd.Series([])
print(empty_series)

series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(series)

series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'], dtype='float' )
print(series)

series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'], dtype='float', name='numbers')    
print(series)