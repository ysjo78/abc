import streamlit as st
import random
import time

st.set_page_config(page_title="파쿠르 게임", layout="wide")

# 제목
st.markdown("<h1 style='text-align:center;'>🐱‍🏍 점프 파쿠르 게임</h1>", unsafe_allow_html=True)

# --- 난이도 선택 ---
difficulty = st.sidebar.selectbox("난이도 선택", ["쉬움", "보통", "어려움"])

speed = {"쉬움": 0.35, "보통": 0.25, "어려움": 0.15}[difficulty]
obstacle_num = {"쉬움": 1, "보통": 2, "어려움": 3}[difficulty]

bg_color = st.sidebar.color_picker("배경 색 선택", "#FFFFFF")

st.markdown(
    f"""
    <style>
    body {{
        background-color: {bg_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- 게임 상태 초기화 ---
if "player_y" not in st.session_state:
    st.session_state.player_y = 0  # 0 = 바닥, 1 = 점프 중
if "jump_timer" not in st.session_state:
    st.session_state.jump_timer = 0
if "obstacles" not in st.session_state:
    st.session_state.obstacles = []
if "score" not in st.session_state:
    st.session_state.score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "start" not in st.session_state:
    st.session_state.start = False


# --- 장애물 생성 ---
def spawn_obstacles():
    obs = []
    for _ in range(obstacle_num):
        obs.append(random.randint(20, 40))
    return obs


# --- 게임 화면 출력 ---
def draw_game():
    ground = ""
    air = ""
    for i in range(50):
        char = "▢"

        # 캐릭터 위치
        if i == 5 and st.session_state.player_y == 0:
            char = "🙂"
        elif i == 5 and st.session_state.player_y == 1:
            char = "😺"

        # 장애물 위치
        if i in st.session_state.obstacles:
            char = "⬛"

        if st.session_state.player_y == 0:
            ground += char
            air += "▢"
        else:
            air += char
            ground += "▢"

    st.write(air)
    st.write(ground)


# --- 게임 실행 버튼 ---
if not st.session_state.start:
    if st.button("▶ 게임 시작"):
        st.session_state.start = True
        st.session_state.obstacles = spawn_obstacles()
else:
    # 점프 버튼
    if st.button("⤴ 점프"):
        if st.session_state.player_y == 0:  # 바닥에 있을 때만 점프 가능
            st.session_state.player_y = 1
            st.session_state.jump_timer = 3

    # 점프 시간 감소
    if st.session_state.jump_timer > 0:
        st.session_state.jump_timer -= 1
    else:
        st.session_state.player_y = 0

    # 장애물 이동
    st.session_state.obstacles = [x - 1 for x in st.session_state.obstacles]

    # 장애물이 지나가면 새로 생성
    for i in range(len(st.session_state.obstacles)):
        if st.session_state.obstacles[i] < 0:
            st.session_state.obstacles[i] = random.randint(30, 50)
            st.session_state.score += 1

    # 충돌 체크
    for obs in st.session_state.obstacles:
        if obs == 5 and st.session_state.player_y == 0:
            st.session_state.game_over = True

    # 화면 출력
    draw_game()

    st.write(f"🏆 점수: **{st.session_state.score}**")

    # 게임 오버 처리
    if st.session_state.game_over:
        st.error("💀 게임 오버!")
        if st.button("🔄 다시 시작"):
            st.session_state.start = False
            st.session_state.game_over = False
            st.session_state.player_y = 0
            st.session_state.score = 0
            st.session_state.obstacles = spawn_obstacles()

    time.sleep(speed)
