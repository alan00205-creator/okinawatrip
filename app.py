import streamlit as st

# 1. 網頁配置：這行決定了你分享網址時看到的名稱
st.set_page_config(
    page_title="2026年1月沖繩家族旅遊", 
    page_icon="🚗", 
    layout="wide"
)

# 2. 手機版 App 風格 CSS
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    .day-header {
        background-color: #007AFF;
        color: white;
        padding: 12px 15px;
        border-radius: 12px;
        margin: 20px 0 10px 0;
        font-weight: bold;
        font-size: 1.2rem;
    }
    .trip-card {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #EEE;
        margin-bottom: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        background-color: #007AFF !important;
        color: white !important;
        height: 50px;
        font-weight: bold;
        border: none;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚗 2026年1月沖繩家族旅遊")
st.write("手機專用導航 App")

# --- 完整五天行程數據 ---
# [cite_start]資料來源：[cite: 8, 11, 35, 39, 69]
plan = {
    "📅 Day 1: 1/1 (週四)": [
        ("16:50 桃園國際機場", "https://maps.app.goo.gl/5r8n7Y7R7N3Y"),
        ("19:10 那霸機場", "https://maps.app.goo.gl/1"),
        ("20:56 住宿: La'gent 飯店", "https://maps.app.goo.gl/3"),
        ("21:58 晚餐: Steak House 88 Jr.", "https://maps.app.goo.gl/4")
    ],
    "📅 Day 2: 1/2 (週五)": [
        ("09:07 取車: Relax Car Rental", "https://maps.app.goo.gl/32"),
        ("09:41 波上宮", "https://maps.app.goo.gl/6"),
        ("11:02 午餐: Posillipo 海景餐廳", "https://maps.app.goo.gl/51"),
        ("12:36 瀨長島 Umikaji Terrace", "https://maps.app.goo.gl/120"),
        ("15:04 玉泉洞", "https://maps.app.goo.gl/9")
    ],
    "📅 Day 3: 1/3 (週六)": [
        ("09:16 首里城", "https://maps.app.goo.gl/12"),
        ("11:43 敘敘苑 燒肉 (PARCO CITY)", "https://maps.app.goo.gl/121"),
        ("14:44 寶可夢中心 (永旺夢樂城)", "https://maps.app.goo.gl/16"),
        ("15:59 美國村", "https://maps.app.goo.gl/17"),
        ("19:02 晚餐: 迴轉壽司市場", "https://maps.app.goo.gl/18")
    ],
    "📅 Day 4: 1/4 (週日)": [
        ("09:57 BANTA CAFE", "https://maps.app.goo.gl/122"),
        ("11:28 萬座毛", "https://maps.app.goo.gl/20"),
        ("13:58 古宇利蝦蝦飯", "https://maps.app.goo.gl/22"),
        ("15:28 沖繩美麗海水族館", "https://maps.app.goo.gl/23"),
        ("17:59 晚餐: 百年古家 大家", "https://maps.app.goo.gl/24")
    ],
    "📅 Day 5: 1/5 (週一)": [
        ("09:22 DMM Kariyushi 水族館", "https://maps.app.goo.gl/25"),
        ("11:29 暖暮拉麵 (系滿店)", "https://maps.app.goo.gl/57"),
        ("12:35 ASHIBINAA Outlet", "https://maps.app.goo.gl/58"),
        ("15:52 還車: Relax Car Rental", "https://maps.app.goo.gl/32"),
        ("18:10 那霸機場報到", "https://maps.app.goo.gl/1")
    ]
}

# --- 渲染介面 ---
for day, items in plan.items():
    st.markdown(f'<div class="day-header">{day}</div>', unsafe_allow_html=True)
    for title, url in items:
        st.markdown(f'<div class="trip-card">{title}</div>', unsafe_allow_html=True)
        st.link_button("📍 開啟地圖導航", url)
