import streamlit as st
import pandas as pd

# 1. 網頁配置：手機優先，響應式設計
st.set_page_config(page_title="2026 沖繩家族自駕 App", page_icon="🐢", layout="wide")

# 2. 可愛旅遊風 CSS 樣式 (客製化 UI)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Noto Sans TC', sans-serif; }
    
    .stApp { background: #F7F9FC; }
    
    /* 卡片設計：區分景點、餐廳、交通 */
    .trip-card {
        background-color: white;
        padding: 1.2rem;
        border-radius: 18px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
        border-left: 8px solid #FF8C94; /* 預設景點紅色 */
    }
    .restaurant-card { border-left-color: #FFD54F; } /* 餐廳黃色 */
    .transport-card { border-left-color: #4FC3F7; }  /* 交通藍色 */
    
    /* 攻略標籤樣式 */
    .tag {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: bold;
        margin: 4px 4px 4px 0;
        color: white;
    }
    .tag-must-eat { background-color: #FF5252; }
    .tag-must-buy { background-color: #7E57C2; }
    .tag-tips { background-color: #26A69A; }
    .tag-important { background-color: #FB8C00; }

    /* 天氣區塊樣式 */
    .weather-box {
        background: linear-gradient(135deg, #6DD5FA 0%, #2980B9 100%);
        color: white;
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 20px;
        text-align: center;
    }

    /* 手機導航按鈕優化 */
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        height: 3rem;
        background-color: #007AFF !important;
        color: white !important;
        font-weight: bold;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 頂部導覽列
tab1, tab2, tab3, tab4 = st.tabs(["🗓 行程規劃", "✈️ 交通/住宿", "💡 攻略百科", "💰 預算表"])

# --- Tab 1: 每日行程 (含天氣與自動導航) ---
with tab1:
    st.title("🌊 2026 沖繩自駕趣")
    
    # 行程資料庫 (分析 PDF 內容)
    daily_plan = {
        "Day 1: 1/1 (週四) 啟程": {
            "weather": "☁️ 那霸 18°C / 21°C",
            "items": [
                {"type": "transport", "time": "16:50", "name": "桃園國際機場", "url": "https://www.google.com/maps/search/?api=1&query=桃園國際機場", "info": "航班 IT232 [cite: 9, 109]"},
                {"type": "spot", "time": "19:10", "name": "那霸機場", "url": "https://www.google.com/maps/search/?api=1&query=那霸機場", "info": "抵達沖繩 [cite: 10, 115]"},
                {"type": "restaurant", "time": "21:58", "name": "Steak House 88 Jr.", "url": "https://www.google.com/maps/search/?api=1&query=Steak+House+88+Jr+Matsuyama", "tags": [("必吃", "龍蝦牛排餐"), ("攻略", "營業至深夜，附自助沙拉吧 [cite: 127, 128]")]}
            ]
        },
        "Day 2: 1/2 (週五) 南部文化": {
            "weather": "☀️ 南部 20°C / 23°C",
            "items": [
                {"type": "transport", "time": "09:07", "name": "Relax Car Rental 取車", "url": "https://www.google.com/maps/search/?api=1&query=Relax+car+rental+okinawa", "info": "自駕開始 [cite: 153, 154]"},
                {"type": "spot", "time": "11:02", "name": "瀬長島 Umikaji Terrace", "url": "https://www.google.com/maps/search/?api=1&query=瀨長島", "tags": [("必吃", "幸福鬆餅"), ("必買", "手作帆布包 [cite: 167]")]},
                {"type": "spot", "time": "15:04", "name": "玉泉洞", "url": "https://www.google.com/maps/search/?api=1&query=玉泉洞", "tags": [("攻略", "百萬鐘乳石柱，洞內涼爽 [cite: 174, 175]")]}
            ]
        },
        "Day 3: 1/3 (週六) 中部潮流": {
            "weather": "☁️ 中部 19°C / 22°C",
            "items": [
                {"type": "restaurant", "time": "11:43", "name": "敘敘苑 燒肉 (PARCO CITY)", "url": "https://www.google.com/maps/search/?api=1&query=敘敘苑+沖繩浦添", "tags": [("必吃", "商業午餐"), ("重要", "建議提前預約 [cite: 222]")]},
                {"type": "spot", "time": "14:44", "name": "沖繩寶可夢中心", "url": "https://www.google.com/maps/search/?api=1&query=Pokemon+Center+Okinawa", "tags": [("必買", "沖繩限定皮卡丘 [cite: 229, 230]")]},
                {"type": "spot", "time": "15:59", "name": "美國村", "url": "https://www.google.com/maps/search/?api=1&query=美國村", "tags": [("必點", "A&W 麥根沙士"), ("攻略", "夕陽與摩天輪必拍 [cite: 234, 235]")]}
            ]
        },
        "Day 4: 1/4 (週日) 北部秘境": {
            "weather": "🌊 名護 21°C / 24°C",
            "items": [
                {"type": "restaurant", "time": "13:58", "name": "古宇利蝦蝦飯", "url": "https://www.google.com/maps/search/?api=1&query=古宇利蝦蝦飯", "tags": [("必吃", "蒜味奶油蝦"), ("攻略", "景觀台風景絕佳 [cite: 286, 287]")]},
                {"type": "spot", "time": "15:28", "name": "美麗海水族館", "url": "https://www.google.com/maps/search/?api=1&query=美麗海水族館", "tags": [("攻略", "黑潮之海餵食秀時間為 15:00/17:00 [cite: 291, 292]")]}
            ]
        }
    }

    for day, data in daily_plan.items():
        st.markdown(f'<div class="weather-box">{day}<br><b>{data["weather"]}</b></div>', unsafe_allow_html=True)
        for item in data["items"]:
            # 決定卡片樣式
            card_class = "transport-card" if item['type'] == 'transport' else ("restaurant-card" if item['type'] == 'restaurant' else "")
            
            # 渲染卡片
            st.markdown(f"""
            <div class="trip-card {card_class}">
                <small>⏰ {item['time']}</small><br>
                <b style="font-size:1.1rem;">{item['name']}</b>
            </div>
            """, unsafe_allow_html=True)
            
            # 渲染自動生成的標籤 (必吃/必買/攻略)
            if "tags" in item:
                tag_html = ""
                for t_type, t_text in item['tags']:
                    t_class = "tag-must-eat" if t_type in ["必吃", "必點"] else ("tag-must-buy" if t_type == "必買" else "tag-tips")
                    tag_html += f'<span class="tag {t_class}">{t_type}: {t_text}</span>'
                st.markdown(tag_html, unsafe_allow_html=True)
            
            # 導航按鈕
            st.link_button(f"🚀 導航至 {item['name']}", item['url'])
            st.write("")

# --- Tab 2: 住宿/航班後勤 ---
with tab2:
    st.header("✈️ 航班資訊")
    st.info("**去程**：1/1 IT232 16:50-19:10 [cite: 9, 10]  \n**回程**：1/5 IT233 20:10-21:10 [cite: 72, 79]")
    
    st.header("🏨 住宿點")
    st.success("**沖繩那霸 La'gent 飯店** \n地址：〒900-0014 沖縄県那覇市松尾２丁目１−１   \n電話：098-860-0300")
    
    st.header("📞 緊急聯絡")
    st.warning("警察：110 | 急救：119  \n租車客服 (Relax)：+81 98-xxx-xxxx [cite: 153]")

# --- Tab 3: 攻略百科 ---
with tab3:
    st.header("🍱 沖繩必吃清單")
    st.markdown("""
    * **阿古豬火鍋**：百年古家 大家 [cite: 70, 295]
    * **沖繩飯糰**：機場內 珀塔瑪 [cite: 91, 348]
    * **海邊咖啡**：BANTA CAFE 看夕陽 [cite: 48, 271]
    """)
    st.header("🛍️ 必買伴手禮")
    st.markdown("""
    * **紅芋塔**：御菓子御殿
    * **Pokemon 限定版**：寶可夢中心 [cite: 64, 229]
    * **國際精品**：ASHIBINAA Outlet [cite: 86, 337]
    """)

# --- Tab 4: 預算記帳 ---
with tab4:
    st.header("💰 家族旅遊預算")
    st.write("目前預估總額：NT$ 120,000")
    budget_data = pd.DataFrame([
        {"項目": "機票費用", "預算": 45000, "狀態": "已付"},
        {"項目": "租車費用", "預算": 15000, "狀態": "預訂"},
        {"項目": "住宿費用", "預算": 30000, "狀態": "已付"},
        {"項目": "餐飲雜費", "預算": 30000, "狀態": "預計"}
    ])
    st.table(budget_data)
