import pandas as pd

df = pd.read_csv('C:\\Users\\HP\\Desktop\\Python-DataScience-Journey\\Pandas\\industry.csv',na_values=['NA', 'Missing'])  

print(df)

import pandas as pd

df = pd.read_csv('C:\\Users\\HP\\Desktop\\Python-DataScience-Journey\\Pandas\\industry.csv',na_values={'Name': ['NA', 'Missing'], 'Age': ['NA', 'Missing'], 'City': ['NA', 'Missing']})  


print(df)


import pandas as pd

df = pd.read_csv('C:\\Users\\HP\\Desktop\\Python-DataScience-Journey\\Pandas\\industry.csv',keep_default_na=False, na_values=['NA', 'Missing']l)  

print(df)




