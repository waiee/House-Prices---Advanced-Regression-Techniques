import streamlit as st
import plotly_express as px
import pandas as pd

#Configuration
st.set_option('deprecation.showfileUploaderEncoding', False)

#App Title
st.title("Data Visualization App")

#Add a sidebar
st.sidebar.subheader("Visualization Settings")

#Setup file upload
uploaded_file = st.sidebar.file_uploader(label="Upload your CSV or Excel file",
                        type=['csv', 'xlsx']) 

global df
if uploaded_file is not None:
    print(uploaded_file)
    print("Hello World")
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)

try:
st.write(df)

