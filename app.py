import streamlit as st

# 제목 출력
st.title('Hello, Streamlit!')

# 텍스트 출력
st.write("Streamlit으로 만든 웹 앱입니다.")

# 사용자 입력 받기
name = st.text_input("이름을 입력하세요:")

if name:
    st.write(f"안녕하세요, {name}님!")
