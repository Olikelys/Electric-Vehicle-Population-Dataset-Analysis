import pandas as pd
import streamlit as st

@st.cache_data(show_spinner=False)
def load_data():
    # 读取数据集（确保CSV文件名和这里一致）
    df = pd.read_csv("data/Electric_Vehicle_Population_Data.csv")
    return df

# 数据集来源信息
DATA_SOURCE = "Kaggle - Electric Vehicle Population Dataset"
DATA_URL = "https://www.kaggle.com/datasets/alamshihab075/electric-vehicle-population-dataset"
LICENSE = "CC0 1.0 Universal (CC0 1.0) Public Domain Dedication"