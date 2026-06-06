import matplotlib.pyplot as plt

import pandas as pd
from matplotlib import style

style.use('ggplot')
df = pd.read_csv('C:\\Users\\HP\\Desktop\\Python-DataScience-Journey\\Matplotlib\\googleplaystore.csv', nrows=100)
print(df)

x = df['Rating']
y = df['Reviews']

plt.scatter(x,y, color='blue', label='Reviews', alpha=0.5, edgecolor='black')
plt.xlabel('Rating')
plt.ylabel('Reviews')
plt.title('Scatter Plot of Rating vs Reviews')
plt.legend()
plt.show()