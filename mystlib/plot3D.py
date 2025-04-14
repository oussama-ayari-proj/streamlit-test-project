import streamlit as st
import plotly.express as px
import pydeck as pdk

def plot1(df):
    st.subheader("Plot # 01:")
    fig1 = px.scatter_3d(df, 
           x = 'passenger_count', 
           y = 'distance', 
           z = 'duration',
           color = 'passenger_count', 
           title = "3D Scatter plot",
           width = 800, 
           height = 600)
    st.plotly_chart(fig1)