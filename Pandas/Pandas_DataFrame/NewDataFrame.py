import pandas as pd

data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo']
}
df = pd.DataFrame(data_dict)
print(df)

data_dict2 = {
    'Name': ['David', 'Eve', 'Frank'],
    'Age': [40, 45, 50],
    'City': ['Paris', 'Berlin', 'Sydney']
}
df2 = pd.DataFrame(data_dict2)
print(df2)