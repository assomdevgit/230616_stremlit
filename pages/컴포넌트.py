import streamlit as st

st.title("컴포넌트")

st.write("❤️")
cols = st.columns(2) # 컬럼 리스트
cols[0].write("❤️")
cols[1].write("❤️")

cols = st.columns(3)
# 🐦 -> n등분 -> 3등분
cols[0].write("🐦")
cols[1].write("🐦")
cols[-1].write("🐦")
cols = cols[0].columns(3) # 열의 열인 거임
cols[0].write("🐦")
cols[1].write("🐦")
cols[-1].write("🐦")

col1, col2 = st.columns(2)
col1.write("왼쪽 열")
col2.write("오른쪽 열")
with col1:
    st.write("왼쪽")
with col2:
    st.write("오른쪽")

l1 = "markdown"
st.write("""
* [표시할 텍스트]({l1})
""")

# tabs = st.tabs(["김치찌개", "된장찌개", "로제마라어묵찌개"])
tab_menus = ["김치찌개", "된장찌개", "로제마라어묵찌개"]
tab1, tab2, tab3 = st.tabs(tab_menus)
img1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4MFBhxEu7tdtEmSpJ-DEzVl9si8NYOiYmbruRyOr7vYS8ZMLSpu60YsPo5WtmB5xg_F0&usqp=CAU"
tab1.image(img1)
with tab2:
    img2 = "https://imagescdn.gettyimagesbank.com/500/201708/jv10940386.jpg"
    st.image(img2)
tab3.write("이런 건 없어요... 상상도 마라요")

exp = st.expander("Surprise!!!", expanded=False)
exp.image("https://i.namu.wiki/i/5lWwYGj-VC8ZqJxug7Exm5-7rHE97fdZui3DWEAjm0zdLiBCbcdw4mLyGhcbZ_KecZOQr4rtwNJSFs63Rsdd_Q.webp")
# with exp: ...

# 입력
st.title("입력")
name = st.text_input("나의 이름은")
name2 = st.text_input("너의 이름은")
# st.text_input("")
st.write(name)
st.write(name2)
st.write(f"신랑 {name} 과 신부 {name2}는...")

age = st.number_input("당신의 나이는?", step=1)
st.write(f"나의 나이는 {age}세")

st.divider()
mode = st.checkbox("강사님 잔소리모드")  # bool (T/F)
col1, col2, col3 = st.columns(3)
r = col1.radio("잔소리 내용 선택", ["취업", "코딩", "지각"])
s = col2.slider("잔소리 강도 선택", min_value=1, max_value=10)
b = col3.selectbox("잔소리 말투 선택", ["친절하게", "반말", "모욕적"])
if mode:
    # r -> 취업, 코딩, 지각
    format = None
    if b == "친절하게":
        format = lambda x: f"여러분~ {x}"
    elif b == "반말":
        format = lambda x: f"야! {x}"
    elif b == "모욕적":
        format = lambda x: f"XXXXXX! {x}"
    if r == "취업":
        for i in range(s):
            st.write(format("8월에는 자소서 넣어야겠죠?"))
    elif r == "코딩":
        st.write(format("저보다 파이썬 잘해요?"))
    elif r == "지각":
        st.write(format("9시랑 9시 1분은 다른 거에요."))



