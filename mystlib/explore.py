import streamlit as st
import pandas as pd


def run(df):
   
   st.title("Single-column Selection")
   col = st.selectbox('select one column:', df.columns)
   st.write('You selected:', col)
   st.write(df[col].unique())

   st.title("Multi-column Selection")
   cols = st.multiselect('select column(s):', df.columns, default = [])
   st.write('You selected:', cols)
   st.write(df[cols])