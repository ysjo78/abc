import streamlit as st

# 제목
st.title("간단한 계산기")

# 두 개의 숫자 입력 받기
num1 = st.number_input("첫 번째 숫자", 0)
num2 = st.number_input("두 번째 숫자", 0)

# 연산자 선택
operation = st.selectbox("연산자 선택", ["+", "-", "*", "/"])

# 계산
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "오류: 0으로 나눌 수 없습니다."

# 결과 출력
st.write(f"결과: {result}")
