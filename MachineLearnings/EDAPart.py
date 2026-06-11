import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy.stats import pearsonr
from scipy.stats import chi2_contingency
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv(r"C:\Users\HP\Desktop\Python-DataScience-Journey\MachineLearnings\insurance.csv")

# print(data.head())


#EDA
# print(data.info())

#mean median mode part data extraction
# print(data.describe())

# data cleaning

# print(data.isnull().sum())


#visulizations

numeric_col = ['age', 'bmi', 'children', 'charges']

# for col in numeric_col:
#     plt.figure(figsize=(10, 5))
#     sns.histplot(data[col], kde=True)
#     plt.title(f"Distribution of {col}")
#     plt.show()

# categorical_col = ['sex', 'smoker', 'region']
# for col in categorical_col:
#     plt.figure(figsize=(10, 5))
#     sns.countplot(data[col])
#     plt.title(f"Count of {col}")
#     plt.show()
# sns.countplot(data=data, x='smoker')

# plt.title("Count of smokers and non-smokers")
# plt.show()


# for nums in numeric_col:
#     plt.figure(figsize=(10, 5))
#     sns.boxplot(x= data[nums])
#     plt.title(f"Boxplot of {nums}")
#     plt.show()

# plt.figure(figsize=(10, 5))
# sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
# plt.title(f"Correlation Heatmap")
# plt.show()


# Data Preprocessing and Prediction

df_cleaned = data.copy()
# print(df_cleaned.head())

df_cleaned.drop_duplicates(inplace=True)
df_cleaned.dropna(inplace=True)
# print(df_cleaned.shape)

#value counts of categorical columns
# print(df_cleaned['sex'].value_counts())
st = df_cleaned['sex'].value_counts()
# print(st)

#covert object into numerical values
df_cleaned['sex'] = df_cleaned['sex'].map({'male': 0, 'female': 1})
df_cleaned['smoker'] = df_cleaned['smoker'].map({'no': 0, 'yes': 1})
# print(df_cleaned.head())


#region encoded(one hot encoding)
df_cleaned = pd.get_dummies(df_cleaned, columns=['region'], drop_first=True)
# print(df_cleaned.astype(int))

#Feture and target variable
sns.histplot( df_cleaned['bmi'], kde=True)
# plt.show()
df_cleaned['bmi_category'] = pd.cut(df_cleaned['bmi'], bins=[0, 18.5, 24.9, 29.9, np.inf], labels=['Underweight', 'Normal weight', 'Overweight', 'Obese'])      
# print(df_cleaned.head())
df_cleaned = pd.get_dummies(df_cleaned, columns=['bmi_category'], drop_first=True)

# print(df_cleaned.astype(int))

#Feature Scalling

# print(df_cleaned.columns)

cols = ['age','bmi','children']
scaler = StandardScaler()
df_cleaned[cols] = scaler.fit_transform(df_cleaned[cols])
# print(df_cleaned.astype(int))


# data scalling using scipy
# 
selected_feature = ['age', 'sex', 'bmi', 'children', 'smoker', 'charges',
       'region_northwest', 'region_southeast', 'region_southwest',
       'bmi_category_Normal weight', 'bmi_category_Overweight',
       'bmi_category_Obese']
correlation = {
    
    feature: pearsonr(df_cleaned[feature], df_cleaned['charges'])[0]
    for feature in selected_feature 
}

correlation_item = pd.DataFrame(list(correlation.items()), columns=['Feature', 'Correlation'])
correlation_item.sort_values(by='Correlation', ascending=False)
# print(correlation_item)


# chi square test on categrical

cat_test = ['smoker','age','region_northwest', 'region_southeast', 'region_southwest',
       'bmi_category_Normal weight', 'bmi_category_Overweight',
       'bmi_category_Obese']
alpha = 0.05
df_cleaned['charges_bin'] = pd.qcut(df_cleaned['charges'], q=4, labels=False)

chi2_result = {}
for col in cat_test:
    contigency_table = pd.crosstab(df_cleaned[col], df_cleaned['charges_bin'])
    chi2_stat, p_val, _, _ = chi2_contingency(contigency_table)
    decision = "Reject Null" if p_val < alpha else "Accept"
    chi2_result[col] = {'chi2_statistic': chi2_stat, 'p_value': p_val, 'decision': decision}
    
chi2_df=pd.DataFrame(chi2_result).T
chi2_df=chi2_df.sort_values(
by='p_value')
# print(chi2_df)

final_df = df_cleaned[['smoker','age','region_southwest' ]]

print(final_df)
