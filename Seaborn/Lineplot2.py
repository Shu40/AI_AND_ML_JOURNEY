import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

tips_df = sns.load_dataset('tips')
print(tips_df)
sns.lineplot(x='total_bill', y='tip', data = tips_df, hue = "sex", style = "time", markers = True)
plt.show()