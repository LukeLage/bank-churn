import pandas as pd

data = pd.read_csv('scr\Churn Modeling.csv')

df = pd.DataFrame(data)
#print(df.head())

df['Exited'] = df['Exited'].astype(bool)
df['HasCrCard'] = df['HasCrCard'].astype(bool)

print(df.info())