# pip install streamlit
# steamlit hello

import streamlit as st  # streamlit

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

# 마크다운
# https://heropy.blog/2017/09/30/markdown/

# st.write / st.markdown
# st.write -> 입력하는 것에 맞춰서 알아서 결정 => 마크다운
# st.markdown -> 명백하게 마크다운을 사용하겠다.

# # = <h1>
st.write("""
# 가장 큰 제목 테스트 (h1 - headline1 -st.title)
## 그 다음 큰 제목 (h2 - headline2 - st.header)
### 그것보단 작은 제목 (h3 - headlin3 - st.subheader)
#### 좀 더 작은 제목 (h4)

""")
st.divider()

# 서식
text = """
기울임 *별표* 또는 _언더바_ 를 하나씩 써주면

진하게(bold) : **별포**를 하나씩 써주면

기울임 + 진하게(bold) : ***별표***를 세개씩 서부면

취소선 : ~물결표~

밑줄 : <u>밑줄</u>

형광펜 : <mark>형광펜</mark>
"""
st.markdown(text, unsafe_allow_html=True)

# 레이아웃
st.subheader("레이아웃")
st.write("""
    ### 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
        * 들여쓰기1
            * 들여쓰기2
                * 들여쓰기3
    - (-)를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    - (-_를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    - (-)를 여백 1칸 이상과 사용하면 순서가 없는 리스트
        - 들여쓰기1
            - 들여쓰기2
                - 들여쓰기3
""")

st.write("""
    ### 순서가 있는 리스트
    1. 순서가
    2. 있는
    3. 리스트
        1. 들여쓰기
            1. 들여쓰기

    1. 순서가
    1. 1로 넣어도
    1. 증가됨
    ### 가로줄
    ---
    (---)
    ___
    (___)

    ### 테이블 (표(
    |이름|직업|
    |-|-|
    |파이썬|백수|
    |자바|일잘러|
""")

# 링크
st.divider()
st.subheader("링크")
l1 = "https://naver.com"
l2 = "https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg"
st.write(f"""
    * [표시할 텍스트](https://naver.com)
    * [표시할 텍스트]({l1})
    * ![이미지에 대한 설명](https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg)
    * ![이미지에 대한 설명]({l2})
    * [![이미지에 대한 설명](https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg)](https://naver.com)
""")

# 인용
st.divider()
st.subheader("인용")
st.write(f"""
    > 무언가 멋진 말 - 유명한 사람

    > 진입장벽은 수익이다 - 어느 코딩 갓아

    책이나, 사람말 인용할 때...
    > 인용 첫줄
    > > 인용문 안에 인용임

    ### 코드
    ` 코드를 나타낼 때 주로 쓰이는 묶음 표시 (한줄)`
    ```
    여러 줄로 코드를 나타내고
    줄바꿈도 반영하고 싶으면...
    ```
    ```python
    print("파이썬")
    ```
""")