import streamlit as st
import json
import geopy.distance

st.set_page_config(page_title="Taipei ArtMap", layout="wide")
st.title("🎭 Taipei ArtMap — 智慧藝文活動導覽")

with open("../data/events_latest.json", "r", encoding="utf-8") as f:
    events = json.load(f)

user_lat = st.number_input("輸入您的緯度", value=25.033)
user_lon = st.number_input("輸入您的經度", value=121.565)

st.subheader("📍 離您最近的藝文活動")
for e in events:
    # 這裡假設資料中已有地點經緯度，可日後加上 geocoding
    distance = geopy.distance.geodesic((user_lat, user_lon), (25.036, 121.562)).km
    if distance < 3:
        st.markdown(f"**🎨 {e['活動名稱']}** — {e['地點']} ({e['時間']})")
        st.markdown(f"[活動詳情]({e['連結']})")
