import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('scr/Churn Modeling.csv')
#10k lines

df = pd.DataFrame(data)
#print(df.head())

df['Exited'] = df['Exited'].astype(bool)
df['HasCrCard'] = df['HasCrCard'].astype(bool)

print(df.duplicated())
# No duplicated data

print(df.isna().sum()) 
# No null data

sns.boxplot(data= df, x=df['CreditScore'])
#No outliers on the credit score line
sns.boxplot(data=df, x= df['Balance'])
plt.show()

gender_map = {
    'Male': 0,
    'Female': 1
}

df = df.replace({'Gender': gender_map})