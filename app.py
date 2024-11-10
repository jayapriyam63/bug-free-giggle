import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit App Title
st.title("AI Agent Dashboard")

# File Upload Section
st.header("Upload a CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

# Check if a file is uploaded
if uploaded_file is not None:
    # Read the CSV file using pandas
    df = pd.read_csv(uploaded_file)

    # Display a preview of the uploaded data
    st.subheader("Preview of Uploaded Data")
    st.dataframe(df.head())

    # Column Selection
    st.subheader("Select the Main Column for Querying")
    column_name = st.selectbox("Choose a column", options=df.columns.tolist())
    st.write(f"You selected: **{column_name}**")

    # Display Sample Values
    st.subheader("Sample Values from the Selected Column")
    st.write(df[column_name].unique()[:10])

    # Query Input Section
    st.subheader("Define Your Search Prompt")
    query_template = st.text_input(
        "Enter your query template (use {entity} as a placeholder)",
        value="Find the contact email for {entity}"
    )

    # Show a sample of the dynamic queries
    if column_name:
        sample_entity = df[column_name].iloc[0]
        sample_query = query_template.replace("{entity}", sample_entity)
        st.write(f"Example Query: **{sample_query}**")

else:
    st.info("Please upload a CSV file to proceed.")
