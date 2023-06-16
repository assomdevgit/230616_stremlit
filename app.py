# pip install streamlit
# steamlit hello

import streamlit as st # streamlit

# st. -> ctrl + space

st.title("나의 파이썬 웹 페이지")
st.header("수업 8일차에 만들었어요")
st.subheader("그래도 잘 만들었죠")
st.write("내가 만든 streamlit 페이지, 너를 위해 구었지!!!")

st.write("유트브")
st.video("https://www.youtube.com/watch?v=SaCheA6Njc4")
st.write("이미지")
st.image("https://cdn.pixabay.com/photo/2023/06/02/14/12/woman-8035772_1280.jpg", use_column_width=True)  # 인터넷 링크
st.image("https://cdn.pixabay.com/photo/2023/06/02/14/12/woman-8035772_1280.jpg", width=100)  # 인터넷 링크

# 여러 가지 옵션을 넣어서 세부 기능들을 차이
st.image("img/img.jpg")  # 파일 경로 (app.py)
st.image(image="img/img.jpg")  # 키워드를 사용해서...
st.image("img/img.jpg", use_column_width=True)  # 파일 경로 (app.py)
st.image("img/img.jpg", width=100)  # 파일 경로 (app.py)
# https://imgur.com/

# streamlit run app.py

