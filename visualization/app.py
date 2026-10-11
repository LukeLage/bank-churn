import sys

import streamlit as st
print(sys.path)
from data.exploratory_analysis import *

st.markdown(
    "<h1 style='text-align: center;'>Bank Churn Analysis</h1>",
    unsafe_allow_html=True
)

initial_graphics = None
metrics_controller = None

with st.sidebar:
    with st.container():
        visualization = st.radio(
            'Select a visualization',
            ('Initial graphics', 'Insights'),
            index= None
        )
        
    if visualization == 'Initial graphics':
        with st.container():
            initial_graphics = st.radio(
            'Select a graphic to display in the initial graphics section:',
            ['Salary based churn', 'Credit score based churn']
        )
            
    with st.container():
        st.write('Analyst: Luke Malaquias Lage')
        st.write('Email: lukelage646@gmail.com')
        st.write('LinkedIn: https://www.linkedin.com/in/luke-malaquias-lage-ciencia-de-dados/')
    

with st.container():
    st.markdown(
        "<h2 style='text-align: center;'>Churn Metrics Analysis</h2>",
        unsafe_allow_html=True
    )
    metrics1, metrics2, metrics3 = st.columns(3)
    metrics1.metric(
        label= 'Churn rate',
        value= f'{churn_number/df.shape[0]:.2%}', 
        border = True
    )
    metrics2.metric(
        label= 'Mode of credit score churned',
        value= credit_mode_churn,
        border= True
    )
    metrics3.metric(
        label= 'Mode of products churned',
        value= product_mode_churn,
        border= True
    )

with st.container():
    if visualization == 'Initial graphics':
        if initial_graphics == 'Salary based churn':
            st.markdown(
                "<h3 style='text-align: center;'>Churn based on salary groups</h3>",
                unsafe_allow_html=True
            )
            st.plotly_chart(salary_group_fig, use_container_width=True)
            st.write('The bar chart above show the number of customers who have churned based on their salary group. As we can see, there is not a specific salary group that has a higher churn rate, curiously, the salary group with the highest number of churned customers is the 170k-180k group, but, even then, the difference is not significant when compared to the other groups. This indicates that salary is not a significant factor in determining whether a customer will churn or not.')
        elif initial_graphics == 'Credit score based churn':
            st.markdown(
                "<h3 style='text-align: center;'>Churn based on credit score groups</h3>",
                unsafe_allow_html=True
            )
            st.plotly_chart(credit_group_fig, use_container_width=True)
            st.write('The bar chart above show the number of customers who have churned based on their credit score, grouped by the hundreds. The chart shows that customers with credit scores between 600 and 700 have the highest churn rate with 753 customers in this group who churned, and the lowest group is, curiously, the 300 to 400 group with 19 customers who churned. That shows that customers with middle to high credit scores are more likely to churned. This is a interesting insight, as it is contrary to what one would expect, but we can understand that we need to give more support to customers who are trying to improve their credit score.')
    elif visualization == 'Insights':
        st.markdown(
            "<h3 style='text-align: center;'>Insights</h3>",
            unsafe_allow_html=True
        ) 
        with st.container():
            st.write(
                f'The mean age of customers who have churned is {mean_age_churn:.0f} years old and the group with the most churned customers is the one with 600-700 credit score and the mode of the credit score is {credit_mode_churn}, so, we can understand that customers who are more likely to churn are those who are trying to improve their credit score, preparing themselves for a big financial decision and/or retirement.',
            )
            st.write(
                'With 20.47% of the customers churned, we can see that the bank is losing a significant number of customers,'
            )