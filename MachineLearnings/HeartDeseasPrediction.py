import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv('C:/Users/HP/Desktop/Python-DataScience-Journey/MachineLearnings/heart.csv')
# print(df.head())

# EDA Process

# print(df.shape)
# print(df.info())
# print(df.describe())


print(df.duplicated().sum())

# df_counts=df['HeartDisease'].value_counts()
# print(df_counts)
# df_counts = df.isnull().sum()
# print(df_counts)


# def plotting(var,num):
#     plt.subplot(2,2,num)
#     sns.histplot(df[var], kde = True)
# plt.figure(figsize=(10,8))
# plotting('Age',1)
# plotting('RestingBP',2)
# plotting('Cholesterol',3)
# plotting('MaxHR',4)
# plt.show()

df_c = df['Cholesterol'].value_counts()
# print(df_c)


#Again Cleaning the data 
ch_mean = df.loc[df['Cholesterol'] != 0, 'Cholesterol'].mean()

df['Cholesterol'] = df['Cholesterol'].replace(to_replace=0, value=ch_mean)
df['Cholesterol'] = df['Cholesterol'].round(2)

resting_bp_mean = df.loc[df['RestingBP'] != 0, 'RestingBP'].mean()
df['RestingBP'] = df['RestingBP'].replace(to_replace=0, value=resting_bp_mean)
df['RestingBP'] = df['RestingBP'].round(2)
# def plotting(var,num):
#     plt.subplot(2,2,num)
#     sns.histplot(df[var], kde = True)
# plt.figure(figsize=(10,8))
# plotting('Age',1)
# plotting('RestingBP',2)
# plotting('Cholesterol',3)
# plotting('MaxHR',4)
# plt.show()

#create count plot
# sns.countplot(x = df['Sex'])
# plt.show()
# sns.countplot(x = df['Sex'], hue = df['HeartDisease'])



# sns.boxplot(x = 'HeartDisease', y ='Cholesterol', data = df)
# plt.show()

# sns.violinplot(x = 'HeartDisease', y ='Age', data = df)
# plt.show()

# sns.heatmap(df.corr(numeric_only=True), annot=True)
# plt.show()


#Data preprocessing

df_encode = pd.get_dummies(df, drop_first=True)
df_encode = df_encode.astype(int)
# print(df_encode)


# Stanadard scalling

numeric_columns = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR',]
scaler = StandardScaler()
df_encode[numeric_columns] = scaler.fit_transform(df_encode[numeric_columns])
print(df_encode)





