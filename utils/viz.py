import plotly.express as px
import streamlit as st

def line_chart(df):
    # 时间趋势线图
    fig = px.line(df, x="Year", y="EV_Count", title="Electric Vehicle Population Trend Over Years")
    fig.update_layout(xaxis_title="Year", yaxis_title="Number of EVs", template="plotly_white")
    return fig

def bar_chart(df, x_col, y_col, title):
    # 柱状图
    fig = px.bar(df.sort_values(y_col, ascending=False).head(10), 
                 x=x_col, y=y_col, title=title)
    fig.update_layout(xaxis_title=x_col, yaxis_title=y_col, template="plotly_white")
    return fig

def map_chart(df):
    # 地图可视化（使用经纬度估算，实际效果取决于数据集）
    # 注意：如果数据集没有经纬度，会用邮编/城市名估算
    fig = px.scatter_geo(df, 
                         locations="State",
                         locationmode="USA-states",
                         hover_name="City",
                         size="EV_Count",
                         title="Geospatial Distribution of Electric Vehicles in USA",
                         scope="usa")
    fig.update_layout(template="plotly_white")
    return fig

def pie_chart(df):
    # 饼图（电动车类型分布）
    fig = px.pie(df, values="EV_Count", names="EV_Type_Simple", 
                 title="Distribution of Electric Vehicle Types")
    fig.update_layout(template="plotly_white")
    return fig

