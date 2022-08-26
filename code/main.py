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

if uploaded_file is not None:
    print("Hello World")