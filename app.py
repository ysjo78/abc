import streamlit as st

# 간단한 단어 리스트 (여기에 더 많은 단어 추가 가능)
valid_words = [
    "바다", "사람", "물고기", "나무", "컴퓨터", "사과", "강아지", "학교",
    "호랑이", "책", "게임", "자동차", "하늘", "별", "음악", "행복"
]

# 게임 상태를 관리
if 'turn' not in st.session_state:
    st.session_state.turn = "사용자"

if 'last_word' not in st.session_state:
    st.session_state.last_word = ""

# 제목
st.title("끝말잇기 게임")

# 사용자가 단어를 입력
user_input = st.text_input("단어를 입력하세요:")

# 사용자 입력이 있다면
if user_input:
    user_input = user_input.strip()
    
    # 마지막 단어와 비교 (끝말이 일치하는지)
    if st.session_state.last_word and user_input[0] != st.session_state.last_word[-1]:
        st.error(f"끝말이 맞지 않습니다. 이전 단어는 {st.session_state.last_word}입니다.")
    elif user_input not in valid_words:
        st.error("유효한 단어가 아닙니다. 표준국어대사전에 없는 단어입니다.")
    else:
        st.session_state.last_word = user_input
        st.session_state.turn = "컴퓨터"
        st.success(f"좋아요! {user_input}는 유효한 단어입니다.")

# 컴퓨터 차례
if st.session_state.turn == "컴퓨터":
    # 컴퓨터는 마지막 단어의 끝 글자와 맞는 단어를 찾음
    last_char = st.session_state.last_word[-1]  # 마지막 글자
    computer_word = next((word for word in valid_words if word[0] == last_char), None)

    if computer_word:
        st.session_state.last_word = computer_word
        st.session_state.turn = "사용자"
        st.success(f"컴퓨터가 선택한 단어: {computer_word}")
    else:
        st.error("컴퓨터가 선택할 수 있는 단어가 없습니다. 게임 종료!")

