import streamlit as st
import plotly.express as px
import numpy as np

def mean_passenger(df):
    st.subheader("Plot # 01:")
    numeric_cols = df.select_dtypes(include='number').columns
    fig1 = px.bar( 
           df.groupby('passenger_count')[numeric_cols].agg('mean'),
           x='passenger_count',
           y = 'duration', 
           title = "Mean Travel Time for No. of Passangers")
    st.plotly_chart(fig1, use_container_width = True)

def distance_duration(df):
       st.subheader("Plot # 02:")
       fig2 = px.scatter(
           df, x = 'duration', y = 'distance',
           color = 'passenger_count',
           title = "Distance to Duration Relationship" )
       st.plotly_chart(fig2, use_container_width = True)