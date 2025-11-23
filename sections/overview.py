import streamlit as st
import plotly.express as px # 添加这行

def show_overview(tables):
    st.header("Key Performance Indicators (KPIs)")
    
    # 计算核心KPI
    total_ev = tables["timeseries"]["EV_Count"].sum()
    latest_year = tables["timeseries"]["Year"].max()
    latest_ev = tables["timeseries"][tables["timeseries"]["Year"] == latest_year]["EV_Count"].iloc[0]
    bev_count = tables["by_ev_type"][tables["by_ev_type"]["EV_Type_Simple"].str.contains("BEV")]["EV_Count"].iloc[0]
    bev_percent = (bev_count / total_ev) * 100
    
    # 展示KPI
    col1, col2, col3 = st.columns(3)
    col1.metric("Total EVs", f"{total_ev:,}")
    col2.metric(f"EVs in {latest_year}", f"{latest_ev:,}")
    col3.metric("BEV Percentage", f"{bev_percent:.1f}%")
    
    # 时间趋势图
    st.subheader("EV Population Trend Over Years")
    # 修改这里：.line_chart -> ["line_chart"]
    trend_fig = st.session_state["viz"]["line_chart"](tables["timeseries"])
    st.plotly_chart(trend_fig, use_container_width=True)
    
    # 电动车类型分布
    st.subheader("EV Type Distribution")
    # 修改这里：.pie_chart -> ["pie_chart"]
    pie_fig = st.session_state["viz"]["pie_chart"](tables["by_ev_type"])
    st.plotly_chart(pie_fig, use_container_width=True)


    