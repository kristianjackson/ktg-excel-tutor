# data_handling.py
# Functions for file uploads, data processing, and conversions

import pandas as pd
import streamlit as st
import logging


def handle_file_upload():
    uploaded_file = st.sidebar.file_uploader(
        "Upload your file", type=["csv", "xls", "xlsx"]
    )

    if uploaded_file is not None:
        file_type = uploaded_file.type
        try:
            if file_type == "text/csv":
                return pd.read_csv(uploaded_file)
            elif file_type in [
                "application/vnd.ms-excel",
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            ]:
                return pd.read_excel(uploaded_file)
        except Exception as e:
            logging.error(f"Error processing file: {e}")
            st.error(f"An error occurred while processing the file: {e}")
    return None


def convert_df_to_json(df):
    return df.to_json(orient="records", indent=4)
