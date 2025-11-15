import streamlit as st

# 원소 번호와 이름을 딕셔너리로 설정
elements = {
    1: "수소",
    2: "헬륨",
    3: "리튬",
    4: "베릴륨",
    5: "붕소",
    6: "탄소",
    7: "질소",
    8: "산소",
    9: "플루오린",
    10: "네온",
    11: "나트륨",
    12: "마그네슘",
    13: "알루미늄",
    14: "규소",
    15: "인",
    16: "황",
    17: "염소",
    18: "아르곤",
    19: "칼륨",
    20: "칼슘",
    # 원소 추가할 수 있음
}

# 제목
st.title("원소 기호 번호 맞추기 게임")

# 사용자 입력
element_number = st.number_input("원소 번호를 입력하세요 (1~20)", min_value=1, max_value=10)

# 정답 입력 받기
user_answer = st.text_input("원소 이름을 입력하세요")

# 원소 맞추기
if user_answer:
    if user_answer.strip().lower() == elements[element_number].lower():
        st.success(f"정답! {element_number}번 원소는 {elements[element_number]}입니다.")
    else:
        st.error(f"틀렸습니다. {element_number}번 원소는 {elements[element_number]}입니다.")
