import streamlit as st
import pandas as pd
from utils.io import load_data, DATA_SOURCE, DATA_URL, LICENSE
from utils.prep import clean_data, make_tables
from utils.viz import line_chart, bar_chart, map_chart, pie_chart
from sections.intro import show_intro
from sections.overview import show_overview
from sections.deep_dives import show_deep_dives
from sections.conclusions import show_conclusions
import os  # 用于路径处理

# 设置页面配置
st.set_page_config(
    page_title="EV Population Dataset Analysis",
    layout="wide",
    page_icon="🚗"
)

# 定义图片文件夹路径和图片路径
ASSETS_FOLDER = r"D:\AaEfrei\DataVisualization\Electric-Vehicle-Population-Dataset-Analysis\assets"
LOGO_EFREI_PATH = os.path.join(ASSETS_FOLDER, "logo_efrei.jpg")
LOGO_WUT_PATH = os.path.join(ASSETS_FOLDER, "logo_WUT.jpg")

# 缓存数据（加快加载速度）
@st.cache_data(show_spinner=False)
def get_processed_data():
    df_raw = load_data()
    df_clean = clean_data(df_raw)
    tables = make_tables(df_clean)
    return df_raw, df_clean, tables

# 存储可视化工具到session state
st.session_state["viz"] = {
    "line_chart": line_chart,
    "bar_chart": bar_chart,
    "map_chart": map_chart,
    "pie_chart": pie_chart
}

# 加载数据
df_raw, df_clean, tables = get_processed_data()

# 页面标题和来源
st.title("🚗 Electric Vehicle Population Dataset Analysis")
st.caption(f"Source: {DATA_SOURCE} | [Link]({DATA_URL}) | License: {LICENSE}")

# 侧边栏（左侧介绍面板）- 展示上传的两张照片和过滤器
with st.sidebar:
    # 侧边栏顶部展示机构logo
    st.subheader("Institutions")
    
    # 检查并展示第一张图片，使用新参数use_container_width替代use_column_width
    if os.path.exists(LOGO_EFREI_PATH):
        st.image(LOGO_EFREI_PATH, caption="EFREI Logo", use_container_width=True)
    else:
        st.warning(f"EFREI logo not found at {LOGO_EFREI_PATH}")
    
    # 添加适当间距
    st.write("")
    
    # 检查并展示第二张图片，使用新参数use_container_width替代use_column_width
    if os.path.exists(LOGO_WUT_PATH):
        st.image(LOGO_WUT_PATH, caption="WUT Logo", use_container_width=True)
    else:
        st.warning(f"WUT logo not found at {LOGO_WUT_PATH}")
    
    # 添加分隔线，区分logo区域和过滤器区域
    st.markdown("---")
    
    # 过滤器部分
    st.header("Filters")
    
    # 年份过滤器
    years = sorted(tables["timeseries"]["Year"].unique())
    selected_years = st.slider("Select Year Range", min_value=years[0], max_value=years[-1], value=(years[0], years[-1]))
    
    # 电动车类型过滤器
    ev_types = tables["by_ev_type"]["EV_Type_Simple"].unique()
    selected_types = st.multiselect("Select EV Types", ev_types, default=ev_types)
    
    # 地区过滤器
    states = sorted(tables["by_region"]["State"].unique())
    selected_states = st.multiselect("Select States", states, default=states[:3])

# 过滤数据（根据侧边栏选择）
filtered_timeseries = tables["timeseries"][
    (tables["timeseries"]["Year"] >= selected_years[0]) & 
    (tables["timeseries"]["Year"] <= selected_years[1])
]
filtered_by_region = tables["by_region"][tables["by_region"]["State"].isin(selected_states)]
filtered_by_type = tables["by_ev_type"][tables["by_ev_type"]["EV_Type_Simple"].isin(selected_types)]
filtered_geo = tables["geo_detail"][
    (tables["geo_detail"]["State"].isin(selected_states)) & 
    (tables["geo_detail"]["EV_Type_Simple"].isin(selected_types))
]

# 更新过滤后的表格到session state
st.session_state["filtered_tables"] = {
    "timeseries": filtered_timeseries,
    "by_region": filtered_by_region,
    "by_ev_type": filtered_by_type,
    "geo_detail": filtered_geo
}

# 页面导航
tab1, tab2, tab3, tab4 = st.tabs(["Introduction", "Overview", "Deep Dives", "Conclusions"])
with tab1:
    show_intro()
with tab2:
    show_overview(st.session_state["filtered_tables"])
with tab3:
    show_deep_dives(st.session_state["filtered_tables"])
with tab4:
    show_conclusions()

# 底部数据质量部分
st.markdown("---")
st.header("Data Quality & Limitations")
st.write("""
- **Missing Data**: Removed rows with missing critical fields (City, State, Model Year)
- **Duplicates**: No duplicate entries found in the dataset
- **Validation**: Model Year ranges from {} to {} (valid range)
""".format(years[0], years[-1]))


