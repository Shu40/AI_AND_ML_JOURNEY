import pandas as pd

# Creating a Pandas Series from a list
data = [10, 20, 30, 40, 50] 
emf = pd.DataFrame(data, columns=['Values'])
print(emf)

ls_of_ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df = pd.DataFrame(ls_of_ls, columns=['A', 'B', 'C'])
print(df)


ls_of_dicts = [{'Name': 'Alice', 'Age': 30}, {'Name': 'Bob', 'Age': 25}, {'Name': 'Charlie', 'Age': 35}]
df_dict = pd.DataFrame(ls_of_dicts) 
print(df_dict)

dic_of_srs = {'Name': pd.Series(['Alice', 'Bob', 'Charlie']), 'Age': pd.Series([30, 25, 35])}
df_srs = pd.DataFrame(dic_of_srs)   
print(df_srs)