import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



plt.title("Histogram plots")

df = pd.DataFrame(np.random.randn(1000), columns=['data'])
sns.histplot(data=df, x='data', kde=True)

df = sns.load_dataset('iris')


df = sns.load_dataset('tips')
sns.histplot(data=df, x='total_bill', kde=True)
df = sns.histoplot(data=df, x='total_bill', hue='sex', kde=True)
plt.show()


