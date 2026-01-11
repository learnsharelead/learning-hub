import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide", page_title="Data Explorer")

st.title("📊 Interactive Data Explorer")

st.markdown("""
Welcome to the Data Explorer! Upload your dataset to get started.
""")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(df.head())
    
    st.write("### Statistics")
    st.write(df.describe())
    
    st.write("### Visualization")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) >= 2:
        x_col = st.selectbox("X Axis", numeric_cols)
        y_col = st.selectbox("Y Axis", numeric_cols)
        fig = px.scatter(df, x=x_col, y=y_col)
        st.plotly_chart(fig)
else:
    st.info("Please upload a CSV file.")
    
    # Demo data button
    if st.button("Load Demo Data"):
        df = px.data.iris()
        st.write("### Demo Data (Iris)")
        st.dataframe(df.head())
        fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
        st.plotly_chart(fig)
