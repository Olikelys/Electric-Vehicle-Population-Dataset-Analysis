# Electric Vehicle Population Dataset Analysis

## 项目简介（Project Introduction）
Analyze EV population’s geospatial distribution, temporal trends & regional dynamics with map visualization.
分析电动车种群的地理空间分布、时间趋势及区域动态，结合地图可视化呈现。

## 项目结构（Project Structure）
Electric-Vehicle-Population-Dataset-Analysis/
├─ sections/ # 页面模块
├─ utils/ # 工具函数（数据加载、清洗、可视化）
├─ data/ # 数据集文件夹
├─ assets/ # 资源文件夹（图片等）
├─ app.py # 主程序文件
├─ requirements.txt# 依赖清单
└─ README.md # 项目说明文档


## 环境配置（Environment Setup）
### 安装依赖（Install Dependencies）
```bash
pip install -r requirements.txt

streamlit run app.py

数据集信息（Dataset Information）
Source: Kaggle - Electric Vehicle Population Dataset
Link: https://www.kaggle.com/datasets/alamshihab075/electric-vehicle-population-dataset
License: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
Key Columns: City, State, Postal Code, Model Year, Electric Vehicle Type
核心功能（Core Features）
关键指标展示（KPIs: Total EVs, Annual Growth, EV Type Percentage）
时间趋势分析（Temporal Trends Over Years）
地理空间分布（Geospatial Visualization with Map）
区域对比分析（Regional Dynamics & EV Type Preferences）
交互式过滤器（Year, State, EV Type Filters）
项目亮点（Project Highlights）
零编程基础友好（No Coding Background Required）
交互式可视化（Interactive Dashboards with Sliders & Tabs）
中英双语文档（Bilingual Documentation）
可部署到 Streamlit Community Cloud
部署链接（Deployment Link）

[Streamlit App URL]（运行后可部署到 Streamlit 社区云，获取公开链接）
运行步骤
确保已安装 Python 和 Git
克隆本仓库：git clone https://github.com/Olikelys/Electric-Vehicle-Population-Dataset-Analysis
进入文件夹：cd Electric-Vehicle-Population-Dataset-Analysis
安装依赖：pip install -r requirements.txt
启动程序：streamlit run app.py
注意事项
数据集需放在data/文件夹下，文件名需与utils/io.py中的路径一致
若地图无法显示，检查网络连接或数据集的地区信息完整性
运行时若报错，优先检查依赖是否安装完整（重新运行pip install -r requirements.txt）


## 运行项目并测试（关键步骤）
### 1. 安装依赖
- 打开VS Code的“终端”（点击菜单栏“终端”→“新建终端”）
- 输入命令：`pip install -r requirements.txt`，等待安装完成（出现Successfully即成功）

### 2. 运行程序
- 在终端输入命令：`streamlit run app.py`
- 会自动打开浏览器，显示你的项目页面（如果没自动打开，复制终端里的本地链接，粘贴到浏览器）
- 测试功能：移动侧边栏的过滤器，看图表是否会更新；点击各个Tab，看页面是否正常显示

## 上传项目到Github（按步骤复制命令）
### 1. 初始化Git仓库
- 在VS Code终端输入以下命令（逐行输入，按回车）：
  ```bash
  git init
  git add .
  git commit -m "Initial commit: EV Population Analysis Project"

2. 关联 Github 仓库并上传
输入命令（替换为你的 Github 仓库链接）：
git remote add origin https://github.com/Olikelys/Electric-Vehicle-Population-Dataset-Analysis.git
git branch -M main
git push -u origin main
