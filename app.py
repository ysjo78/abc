import streamlit as st
import random

st.set_page_config(page_title="간단 파쿠르 게임")

# 초기 상태 설정
if "player_x" not in st.session_state:
    st.session_state.player_x = 0          # 플레이어 위치 (x축: 0부터 오른쪽)
if "player_y" not in st.session_state:
    st.session_state.player_y = 0          # 플레이어 높이(0=땅, 1=공중)
if "obstacles" not in st.session_state:
    # 장애물 목록: 각 아이템은 x 위치. 게임 길이는 20으로 제한
    st.session_state.obstacles = sorted(random.sample(range(5, 19), 4))
if "score" not in st.session_state:
    st.session_state.score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# 간단 화면
st.title("미니 파쿠르 (버튼으로 플레이)")
st.write("목표: 장애물을 피해서 최대한 오른쪽으로 가기")

# 게임 보드 그리기 (길이 20)
def render_board():
    length = 20
    row_ground = []
    for x in range(length):
        if x == st.session_state.player_x and st.session_state.player_y == 0:
            row_ground.append("😀")   # 플레이어 땅에 있을 때
        elif x in st.session_state.obstacles and (st.session_state.player_y == 0):
            row_ground.append("🪨")   # 장애물
        else:
            row_ground.append("·")
    # 공중(위쪽 줄)
    row_air = []
    for x in range(length):
        if x == st.session_state.player_x and st.session_state.player_y == 1:
            row_air.append("😀")     # 플레이어 점프 중
        else:
            row_air.append(" ")
    st.write("".join(row_air))
    st.write("".join(row_ground))
    st.write(f"점수: {st.session_state.score}")

render_board()

# 게임 동작: 이동과 점프
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("오른쪽으로 이동"):
        if not st.session_state.game_over:
            st.session_state.player_x += 1
            st.session_state.player_y = 0  # 이동하면 땅에 있다고 가정
            st.session_state.score += 1
with col2:
    if st.button("점프"):
        if not st.session_state.game_over:
            # 한 턴 동안 공중에 있고 그 다음 자동으로 땅으로 내려옴
            st.session_state.player_y = 1
            # 점프 후 한 칸 전진 (선택사항 — 더 현실적으로 하려면 빼도 됨)
            st.session_state.player_x += 1
            st.session_state.score += 1
with col3:
    if st.button("다음 턴(장애물 이동)"):
        if not st.session_state.game_over:
            # 장애물을 플레이어 쪽으로 한 칸 이동시키거나 게임 길이를 넘어가면 제거
            # (여기선 간단히 장애물은 고정으로 둠 — 필요하면 움직이게 수정 가능)
            pass

# 충돌 검사
if st.session_state.player_x in st.session_state.obstacles and st.session_state.player_y == 0:
    st.session_state.game_over = True
    st.error("충돌! 게임 오버.")
elif st.session_state.player_x >= 19:
    st.success("끝까지 도착했어요! 축하합니다 🎉")
    st.session_state.game_over = True

# 재시작 버튼
if st.button("다시 시작"):
    st.session_state.player_x = 0
    st.session_state.player_y = 0
    st.session_state.obstacles = sorted(random.sample(range(5, 19), 4))
    st.session_state.score = 0
    st.session_state.game_over = False
    st.experimental_rerun()
