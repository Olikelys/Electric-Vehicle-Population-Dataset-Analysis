import streamlit as st
import plotly.express as px # 添加这行

def show_deep_dives(tables):
    st.header("Regional & Geospatial Analysis")
    
    # 地区分布柱状图
    st.subheader("Top 10 Regions with Most EVs")
    # 修改这里：.bar_chart -> ["bar_chart"]
    region_fig = st.session_state["viz"]["bar_chart"](
        tables["by_region"], 
        x_col="City", 
        y_col="EV_Count", 
        title="Top 10 Cities by EV Population"
    )
    st.plotly_chart(region_fig, use_container_width=True)
    
    # 地图可视化
    st.subheader("Geospatial Distribution of EVs")
    # 修改这里：.map_chart -> ["map_chart"]
    map_fig = st.session_state["viz"]["map_chart"](tables["geo_detail"])
    st.plotly_chart(map_fig, use_container_width=True)
    
    # 地区类型分布
    st.subheader("EV Type Distribution by Top Regions")
    top_regions = tables["by_region"].nlargest(5, "EV_Count")["City"].tolist()
    region_type_data = tables["geo_detail"][tables["geo_detail"]["City"].isin(top_regions)]
    region_type_fig = px.bar(region_type_data, 
                             x="City", 
                             y="EV_Count", 
                             color="EV_Type_Simple",
                             title="EV Type Distribution in Top 5 Cities",
                             barmode="group")
    st.plotly_chart(region_type_fig, use_container_width=True)




    