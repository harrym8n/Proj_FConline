import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import time
import random
from PIL import Image
import io
import numpy as np
from wordcloud import WordCloud

# 페이지 제목 설정
st.title("⚽ 어떤 선수가 궁금하세요?")

# 설명 문구
st.write(
    "이제 인벤 평가를 하나하나 검색하지 말고, 한 번의 검색으로 선수 평가를 한눈에 확인하세요! 🏆"
)

# 사용자 인풋 받기 - 선수 이름 입력
st.write("🏅 평가가 궁금한 선수의 이름을 입력해주세요!")
player_name = st.text_input('이름 입력 후 Enter 클릭')


save_folder = 'loge_image'
files = [f for f in os.listdir(save_folder) if f.endswith('.png')] # 파일명 목록 가져오기
season_dict = {os.path.splitext(f)[0]: f for f in files} # 사전 생성
season_images = [f for f in os.listdir(save_folder) if f.endswith('.png')] # 'logo_image' 폴더 내의 모든 이미지 파일을 가져오기
season_images_path = list(pd.Series(season_images).apply(lambda x : f'loge_image/{x}'))

season_images_path.sort(key=lambda x: os.path.basename(x))  # 파일명만 기준으로 정렬

# 2️⃣ 시즌 이미지 선택
if player_name:
    # 시즌 아이콘 이미지와 라디오 버튼을 나란히 배치
    st.write("📅 어떤 시즌이 궁금하세요?")
    
    # 열을 나누어 이미지를 왼쪽에, 라디오 버튼을 오른쪽에 배치
    cols = st.columns([3, 1])  # 3: 이미지, 1: 버튼

    with cols[0]:
        # 각 시즌의 아이콘 이미지 출력 및 라디오 버튼 선택
        selected_season = st.radio(
            "시즌을 선택해주세요", 
            list(season_dict.keys()), 
            format_func=lambda x: f"{x} 시즌"
        )
        
    with cols[1]:
        # 선택된 시즌 이미지 경로로 이미지 불러오기
        selected_image_path = season_dict[selected_season]
        
        # 이미지 파일을 BytesIO 객체로 읽기
        with open(f'logo_image/{selected_image_path}', "rb") as img_file:
            img_bytes = img_file.read()
            img = Image.open(io.BytesIO(img_bytes))
        
        # 선택된 시즌 이미지 출력
        st.image(img, caption=f"선택된 시즌: {selected_season}", use_container_width=True)
    
    # 선택된 시즌 이름 출력
    st.write(f"선택된 시즌: {selected_season}")

else:
    st.warning("⚠️ 선수를 먼저 입력해주세요!")


############################ 이미지 띄우는 코드 백업 ###############################
# for i in range(0, len(season_images_path)):
#     col = cols[i % 12]  # 열 번호를 20으로 나눈 나머지 값을 사용하여 열 선택
#     with col:
#         try:
#             # 이미지 파일을 열고 BytesIO 객체로 변환
#             with open(season_images_path[i], "rb") as f:
#                 img_bytes = f.read()
#                 img = Image.open(io.BytesIO(img_bytes))
                
#                 # 이미지를 st.image()로 출력
#                 st.image(img_bytes, use_container_width=True)
                
#         except Exception as e:
#             st.error(f"Error loading {season_images_path[i]}: {e}")

#         # 각 이미지 간에 마진을 설정하는 방법
#         st.markdown(
#             f"""
#             <style>
#                 .stImage {{
#                     margin: 5px;
#                 }}
#             </style>
#             """, 
#             unsafe_allow_html=True
#         )
############################ 이미지 띄우는 코드 백업 ###############################
