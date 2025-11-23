import pandas as pd
import numpy as np

def clean_data(df):
    # 处理缺失值
    df = df.dropna(subset=["City", "State", "Postal Code", "Model Year", "Electric Vehicle Type"])
    # 转换年份为整数
    df["Model Year"] = df["Model Year"].astype(int)
    # 提取年份（如果有日期列）
    if "Date" in df.columns:
        df["Year"] = pd.to_datetime(df["Date"]).dt.year
    else:
        df["Year"] = df["Model Year"]
    # 简化电动车类型
    df["EV_Type_Simple"] = df["Electric Vehicle Type"].apply(
        lambda x: "Battery Electric Vehicle (BEV)" if "Battery" in x else "Plug-in Hybrid Electric Vehicle (PHEV)"
    )
    return df

def make_tables(df):
    # 按地区统计
    by_region = df.groupby(["State", "City"]).size().reset_index(name="EV_Count")
    # 按年份统计趋势
    timeseries = df.groupby("Year").size().reset_index(name="EV_Count")
    # 按电动车类型统计
    by_ev_type = df.groupby("EV_Type_Simple").size().reset_index(name="EV_Count")
    # 地理数据（用于地图）
    geo_data = df[["City", "State", "Postal Code", "EV_Type_Simple"]].drop_duplicates()
    # 计算每个地区的电动车类型分布
    geo_detail = df.groupby(["State", "City", "EV_Type_Simple"]).size().reset_index(name="EV_Count")
    return {
        "by_region": by_region,
        "timeseries": timeseries,
        "by_ev_type": by_ev_type,
        "geo_data": geo_data,
        "geo_detail": geo_detail
    }
