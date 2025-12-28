import streamlit as st

# 設定網頁標題與圖示
st.set_page_config(page_title="2026 沖繩家族行", page_icon="🚗", layout="wide")

# 自定義 CSS 讓介面更像旅遊 App
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    .day-header {
        background-color: #007bff;
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌊 2026 沖繩家族自駕五日遊")
st.write("點擊下方景點名稱即可直接開啟 **Google 地圖導航**")

# 行程資料
itinerary = {
    "Day 1：1/1 (週四) 啟程 [cite: 8, 95]": [
        ("16:50 桃園國際機場 [cite: 9, 108, 109]", "https://www.google.com/maps/search/?api=1&query=桃園國際機場"),
        ("19:10 那霸機場 [cite: 10, 113, 115]", "https://www.google.com/maps/search/?api=1&query=那霸機場"),
        ("20:56 住宿：La'gent 飯店 [cite: 22, 122, 123]", "https://www.google.com/maps/search/?api=1&query=La'gent+Hotel+Okinawa+Naha"),
        ("21:58 晚餐：Steak House 88 Jr. [cite: 27, 104, 127]", "https://www.google.com/maps/search/?api=1&query=Steak+House+88+Jr.+Matsuyama")
    ],
    "Day 2：1/2 (週五) 南部之旅 [cite: 11, 133]": [
        ("09:07 取車：relax car rental [cite: 14, 153, 154]", "https://www.google.com/maps/search/?api=1&query=relax+car+rental+okinawa"),
        ("09:41 波上宮 [cite: 21, 158, 160]", "https://www.google.com/maps/search/?api=1&query=波上宮"),
        ("11:02 午餐：Posillipo 海景餐廳 [cite: 25, 166, 167]", "https://www.google.com/maps/search/?api=1&query=Posillipo+Okinawa"),
        ("12:36 瀨長島 [cite: 30, 169, 170]", "https://www.google.com/maps/search/?api=1&query=瀨長島"),
        ("15:04 玉泉洞 [cite: 32, 174, 175]", "https://www.google.com/maps/search/?api=1&query=玉泉洞"),
        ("16:39 國際通屋台村 [cite: 15, 179, 180]", "https://www.google.com/maps/search/?api=1&query=國際通屋台村"),
        ("17:46 國際通逛街 [cite: 17, 185, 186]", "https://www.google.com/maps/search/?api=1&query=國際通")
    ],
    "Day 3：1/3 (週六) 中部購物 [cite: 34, 190]": [
        ("09:16 首里城 [cite: 42, 211, 212]", "https://www.google.com/maps/search/?api=1&query=首里城"),
        ("10:39 PARCO CITY 購物 [cite: 51, 216, 217]", "https://www.google.com/maps/search/?api=1&query=PARCO+CITY+Okinawa"),
        ("11:43 午餐：敘敘苑 燒肉 [cite: 53, 222]", "https://www.google.com/maps/search/?api=1&query=敘敘苑+沖繩浦添"),
        ("13:43 AEON MALL Rycom [cite: 59, 224, 225]", "https://www.google.com/maps/search/?api=1&query=AEON+MALL+Okinawa+Rycom"),
        ("14:44 沖繩寶可夢中心 [cite: 64, 229, 230]", "https://www.google.com/maps/search/?api=1&query=Pokemon+Center+Okinawa"),
        ("15:59 美國村 [cite: 38, 234, 235]", "https://www.google.com/maps/search/?api=1&query=美國村"),
        ("19:02 晚餐：迴轉壽司市場 [cite: 43, 239, 240]", "https://www.google.com/maps/search/?api=1&query=迴轉壽司市場+美濱店")
    ],
    "Day 4：1/4 (週日) 北部景點 [cite: 39, 251]": [
        ("09:57 BANTA CAFE [cite: 48, 271, 272]", "https://www.google.com/maps/search/?api=1&query=BANTA+CAFE"),
        ("11:28 萬座毛 [cite: 50, 276, 277]", "https://www.google.com/maps/search/?api=1&query=萬座毛"),
        ("12:54 古宇利海洋塔 [cite: 57, 280, 281]", "https://www.google.com/maps/search/?api=1&query=古宇利海洋塔"),
        ("13:58 午餐：古宇利蝦蝦飯 [cite: 62, 286, 287]", "https://www.google.com/maps/search/?api=1&query=Kouri+Shrimp"),
        ("15:28 美麗海水族館 [cite: 66, 291, 292]", "https://www.google.com/maps/search/?api=1&query=美麗海水族館"),
        ("17:59 晚餐：百年古家 大家 [cite: 70, 295, 296]", "https://www.google.com/maps/search/?api=1&query=百年古家+大家")
    ],
    "Day 5：1/5 (週一) 南部與歸途 [cite: 68, 306]": [
        ("09:22 DMM Kariyushi 水族館 [cite: 80, 327, 328]", "https://www.google.com/maps/search/?api=1&query=DMM+Kariyushi+Aquarium"),
        ("11:29 午餐：暖暮拉麵 (系滿) [cite: 84, 332, 334]", "https://www.google.com/maps/search/?api=1&query=暖暮拉麵+系滿店"),
        ("12:35 ASHIBINAA Outlet [cite: 86, 337, 338]", "https://www.google.com/maps/search/?api=1&query=ASHIBINAA+Outlet"),
        ("15:52 還車：relax car rental [cite: 89, 342, 343]", "https://www.google.com/maps/search/?api=1&query=relax+car+rental+okinawa"),
        ("16:33 珀塔瑪機場飯糰 [cite: 91, 348, 349]", "https://www.google.com/maps/search/?api=1&query=Potama+Naha+Airport")
    ]
}

# 渲染介面
for day, sites in itinerary.items():
    st.markdown(f"<div class='day-header'><h3>{day}</h3></div>", unsafe_allow_html=True)
    for site_name, map_url in sites:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"📍 {site_name}")
        with col2:
            st.link_button("導航", map_url)

st.divider()
st.info("💡 提示：在手機上點擊『導航』會自動開啟 Google Maps App。")
