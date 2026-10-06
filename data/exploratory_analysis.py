from wrangling import df

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px

churn_df = df[df['Exited'] == True].copy()

salary_labels = ['0-10k', '10k-20k', '20k-30k', '30k-40k', '40k-50k',
                '50k-60k', '60k-70k', '70k-80k', '80k-90k', '90k-100k', 
                '100k-110k', '110k-120k', '120k-130k', '130k-140k', '140k-150k',
                '150k-160k', '160k-170k', '170k-180k', '180k-190k', '190k-200k']
salary_bins = [0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000, 160000, 170000, 180000, 190000, 200000]

credit_labels = ['0-100', '100-200', '200-300', '300-400', '400-500', '500-600', '600-700', '700-800', '800-900', '900-1000']
credit_bins = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

churn_df['SalaryGroup'] = pd.cut(
    churn_df['EstimatedSalary'], 
    bins= salary_bins,
    labels= salary_labels,
    include_lowest= True
    )

churn_df['CreditScoreGroup'] = pd.cut(
    churn_df['CreditScore'], 
    bins= credit_bins,
    labels= credit_labels,
    include_lowest= True
    )

salary_grouped = (
    churn_df.groupby('SalaryGroup', observed=False)
    .agg(Count=('CustomerId', 'count'),
            AvgCreditScore=('CreditScore', 'mean'))
    .reset_index()
)

credit_grouped = (
    churn_df.groupby('CreditScoreGroup', observed=False)
    .agg(Count=('CustomerId', 'count'),
            AvgSalary=('EstimatedSalary', 'mean'))
    .reset_index()
)

salary_group_fig = px.bar(
    salary_grouped, 
    x= 'SalaryGroup',
    y= 'Count'
)

credit_group_fig = px.bar(
    credit_grouped,
    x= 'CreditScoreGroup',
    y= 'Count'
)

credit_group_fig.show()