import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import pydeck as pdk
from mystlib import explore

st.set_page_config(layout = "wide", page_title = "Streamlit Data-centric App", page_icon = ":taxi:")

data=pd.read_csv('readydataset.csv')

st.header("My First Streamlit Application")



#Provide a list of functionalities to select from
message = """
        __Select a functionality from the list below__
        """
with st.sidebar:
    st.markdown(message)
    page = st.selectbox('Select:',
        ['View Data Using Dropdowns',
        'Visualize Data on a Map',
        '2D Charts and Histograms', 
        '3D Charts and Histograms'])
st.dataframe(data,width=1000)
if page =='View Data Using Dropdowns':
    explore.run(data)


