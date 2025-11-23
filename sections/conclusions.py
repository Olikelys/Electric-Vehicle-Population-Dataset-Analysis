import streamlit as st

def show_conclusions():
    st.header("Key Insights")
    st.success("""
    1. **Geospatial Pattern**: EVs are concentrated in major cities (top 10 cities account for most EV population)
    2. **Temporal Trend**: EV adoption has grown steadily over the years, with a sharp increase in recent years
    3. **Type Preference**: Battery Electric Vehicles (BEV) are more popular than Plug-in Hybrid EV (PHEV) in most regions
    """)
    
    st.subheader("Implications & Next Steps")
    st.write("""
    - Policy Makers: Focus on charging infrastructure in high-EV-density regions
    - Automakers: Prioritize BEV models for regions with high adoption rates
    - Future Analysis: Add charging station data to explore infrastructure gaps
    """)
    
    st.subheader("Limitations")
    st.warning("""
    - Dataset lacks exact latitude/longitude for more precise geospatial analysis
    - No economic data (e.g., income, fuel prices) to correlate with EV adoption
    - Limited to historical data (no forecast for future trends)
    """)

    