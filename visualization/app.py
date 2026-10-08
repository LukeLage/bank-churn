import sys

import streamlit as st
print(sys.path)
from data.exploratory_analysis import salary_group_fig, credit_group_fig

st.markdown(
    "<h1 style='text-align: center;'>Bank Churn Analysis</h1>",
    unsafe_allow_html=True
)

initial_graphics = None

with st.sidebar:
    with st.container():
        visualization = st.radio(
            'Select a visualization',
            ('Initial graphics'),
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
    if visualization == 'Initial graphics':
        st.header(':green[Initial graphics]')
        if initial_graphics == 'Salary based churn':
            st.header('Churn based on the salary of the customers')
            st.plotly_chart(salary_group_fig, use_container_width=True)
            st.write('The bar chart above show the number of customers who have churned based on their salary group. As we can see, there is not a specific salary group that has a higher churn rate, curiously, the salary group with the highest number of churned customers is the 170k-180k group, but, even then, the difference is not significant when compared to the other groups. This indicates that salary is not a significant factor in determining whether a customer will churn or not.')
        elif initial_graphics == 'Credit score based churn':
            st.header('Churn based on the credit score of the customers')
            st.plotly_chart(credit_group_fig, use_container_width=True)