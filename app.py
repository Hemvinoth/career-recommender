import streamlit as st
import pandas as pd

st.title("Career Recommender system")
st.write("Welcome to my career analysis project!")

df = pd.read_csv('vinoth_career_gap_analysis (1).ipynb')
st.write(df.head())