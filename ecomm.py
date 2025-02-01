import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

def main():
    st.title("This is an app for e-commerce data analysis")
    st.sidebar.title("You can upload your file here")

    upload_file = st.sidebar.file_uploader("Upload your file here", type=["csv", "xlsx"])

    if upload_file is not None:
        try:
            if upload_file.name.endswith(".csv"):
                data = pd.read_csv(upload_file)
            elif upload_file.name.endswith(".xlsx"):
                data = pd.read_excel(upload_file)
            st.sidebar.success("File uploaded successfully")

            st.subheader("I am going to show you the data details")
            st.dataframe(data.head())
        except Exception as e:
            st.sidebar.error(e)

        st.subheader("Let's see some more details in the data")
        st.write("Shape of the data:", data.shape)
        st.write("Columns of the data:", data.columns)
        st.write("Missing values in the data:", data.isnull().sum())
        
        st.subheader("Here I will show you some of the stats")
        st.write(data.describe())

if __name__ == "__main__":
    main()