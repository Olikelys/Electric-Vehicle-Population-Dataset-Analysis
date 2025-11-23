import streamlit as st

def show_intro():
    st.header("Project Introduction")
    st.write("""
    This project analyzes the electric vehicle (EV) population dataset to explore:
    - Geospatial distribution of EVs across regions
    - Temporal trends of EV adoption over years
    - Regional dynamics and EV type preferences
    
    **Dataset Source**: Kaggle - Electric Vehicle Population Dataset
    **Analysis Period**: Based on Model Year in the dataset
    """)
    
    st.subheader("Data Caveats")
    st.info("""
    - Missing values in non-critical columns have been removed
    - EV types are simplified into BEV and PHEV for better readability
    - Geospatial data is based on State/City information from the dataset
    """)
    