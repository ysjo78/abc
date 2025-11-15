import streamlit as st
import time
import random

st.title("🐱‍🏍 파쿠르 미니게임")

# 게임 상태 초기화
if "player_pos" not in st.session_state:
    st.session_state.player_pos = 5   # 캐릭터 위치
if "obstacle_pos" not in st.session_state:
    st.session_state.obstacle_pos = 20  # 장애물 시작점
if "score" not in st.session_state:
    st.session_state.score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# 화면 출력 함수
def draw_game():
    line = ""
    for i in range(21):
        if i == st.session_state.player_pos:
            line += "🙂"
        elif i == st.session_state.obstacle_pos:
            line += "⬛"
        else:
            line += "▢"
    st.write(line)

# 조작 버튼
col1, col2 = st.columns(2)
with col1:
    if st.button("⬅ 왼쪽"):
        if st.session_state.player_pos > 0:
            st.session_state.player_pos -= 1
with col2:
    if st.button("➡ 오른쪽"):
        if st.session_state.player_pos < 20:
            st.session_state.player_pos += 1

# 게임 진행
if not st.session_state.game_over:
    st.session_state.obstacle_pos -= 1

    # 장애물 충돌 체크
    if st.session_state.obstacle_pos == st.session_state.player_pos:
        st.session_state.game_over = True
    else:
        # 장애물이 지나간 경우
        if st.session_state.obstacle_pos < 0:
            st.session_state.score += 1
            st.session_state.obstacle_pos = 20 + random.randint(0, 5)

draw_game()
st.write(f"🏆 점수: {st.session_state.score}")

# 게임 오버 화면
if st.session_state.game_over:
    st.error("💀 게임 오버!")
    if st.button("🔄 다시 시작"):
        st.session_state.player_pos = 5
        st.session_state.obstacle_pos = 20
        st.session_state.score = 0
        st.session_state.game_over = False
