import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import time
import random
from PIL import Image
import numpy as np
from wordcloud import WordCloud

# 페이지 제목 설정
st.title("⚽ 어떤 선수가 궁금하세요?")

# 설명 문구
st.write(
    "이제 인벤 평가를 하나하나 검색하지 말고, 한 번의 검색으로 선수 평가를 한눈에 확인하세요! 🏆"
)

# 사용자 인풋 받기 - 선수 이름 입력
player_name = st.text_input("🏅 평가가 궁금한 선수의 이름을 입력해주세요!", "")

# 시즌 아이콘 이미지 선택
st.write("📅 어떤 시즌이 궁금하세요?")
season_dict = {
    "TOTY": "image/toty.png",
    "TOTS": "tots.png",
    "ICON": "icon.png",
}

# selected_season = None
# cols = st.columns(len(season_dict))  # 시즌별 컬럼 생성

# for idx, (season, img_path) in enumerate(season_dict.items()):
#     with cols[idx]:
#         img = Image.open(img_path)
#         if st.button(season):
#             selected_season = season

# # 3️⃣ 분석 버튼 클릭 시 로딩 효과 및 결과 출력
# if player_name and selected_season:
#     with st.spinner("🔍 분석중입니다... 잠시만 기다려 주세요!"):
#         time.sleep(2)  # 로딩 시간 (백엔드 실행 시 대체)

#         # 선수 데이터 분석
#         rating = 평점코드넣기  # 임의의 평점 생성 (예제 코드)
#         recommendation = 추천여부넣기

#         # 💡 감정 분석 결과 (워드 클라우드 생성)
#         sample_text = "좋아요 최고 최악 별로 추천 훌륭함 대박 별로 좋은 선수 능력 좋음 매우 빠름 기대 이하"
#         wordcloud = WordCloud(
#             font_path=None, background_color="white", width=400, height=200
#         ).generate(sample_text)

#         # 결과 출력
#         st.success(f"🎉 {player_name} ({selected_season}) 선수 분석 완료!")

#         # 선수 평점
#         st.subheader("📊 선수 평점")
#         st.write(f"⭐ 평점: {rating} / 5.0")

#         # 감정 분석 결과 (워드 클라우드)
#         st.subheader("💬 유저 리뷰 감정 분석 결과")
#         fig, ax = plt.subplots()
#         ax.imshow(wordcloud, interpolation="bilinear")
#         ax.axis("off")
#         st.pyplot(fig)

#         # 추천 여부
#         st.subheader("🧐 추천 정도")
#         st.write(recommendation)

# else:
#     st.warning("⚠️ 선수 이름과 시즌을 선택해주세요!")