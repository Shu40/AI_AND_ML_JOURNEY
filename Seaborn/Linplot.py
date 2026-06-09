import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# days = [1, 2, 3, 4, 5]
# temperature = [30, 32, 31, 29, 28]

# temp_df = pd.DataFrame({'days': days, 'temperature': temperature})

# sns.lineplot(x='days', y='temperature', data = temp_df)
# plt.title('Temperature over Days')

tips_df = sns.load_dataset('tips')
print(tips_df)
sns.lineplot(x='total_bill', y='tip', data = tips_df)
plt.show()


