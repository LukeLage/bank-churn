import streamlit as st
from data.exploratory_analysis import salary_group_fig, credit_group_fig

st.markdown(
    "<h1 style='text-align: center;'>Bank Churn Analysis</h1>",
    unsafe_allow_html=True
)

with st.container():
    st.header(':green[Initial graphics]')

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
    

if initial_graphics == 'Salary based churn':
    