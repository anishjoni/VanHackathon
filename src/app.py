import streamlit as st
import pandas as pd

# To run the app use the following code on terminal
# streamlit run app.py
st.title('Top 10 Candidates for job')


df = pd.read_csv("resulteda.csv")

option = st.selectbox(
    'Which Job would you like to see the best candidates for?',
     df['jobsposition'].unique())

'You selected: ', option

# Filter dataframe
result_df = df[(df['jobsposition'] == option) ]# write dataframe to screen
result_df.sort_values('match_score', axis = 0, ascending=False, inplace=True)
del result_df['Unnamed: 0']
st.write(result_df)