# Code for 'data.py' file
# Import necessary modules
import numpy as np
import pandas as pd
import streamlit as st

# Define a function 'app()' which accepts 'cc_df' as an input.
def app(cc_df):
    st.header("View Data")
    # Add an expander and display the dataset as a static table within the expander.
    with st.beta_expander("View Dataset"):
        st.table(cc_df)

    st.subheader("Data Description:")
    if st.checkbox("Show summary"):
        st.table(cc_df.info())

    beta_col1, beta_col2, beta_col3 = st.beta_columns(3)

    # Add a checkbox in the first column. Display the column names of 'cc_df' on the click of checkbox.
    with beta_col1:
        if st.checkbox("Show all column names"):
            st.table(list(cc_df.columns))

    # Add a checkbox in the second column. Display the column data-types of 'cc_df' on the click of checkbox.
    with beta_col2:
        if st.checkbox("View column data-type"):
            st.table(cc_df.dtypes)

    # Add a checkbox in the third column followed by a selectbox which accepts the column name whose data needs to be displayed.
    with beta_col3:
        if st.checkbox("View column data"):
            column_data = st.selectbox('Select column', tuple(cc_df.columns))
            st.write(cc_df[column_data])
