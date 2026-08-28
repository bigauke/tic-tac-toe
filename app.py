import streamlit as st
import time
from logic import check_winner, reset_game, bot_move

VERSION = "1.0.0"


def handle_click(row, col):
    if st.session_state.game_over or st.session_state.board[row][col] != "":
        return
    st.session_state.board[row][col] = st.session_state.current_player
    st.session_state.winner = check_winner(st.session_state.board)

    if st.session_state.winner == "draw":
        st.session_state.scores["draw"] += 1
        st.session_state.game_over = True
    elif st.session_state.winner:
        st.session_state.scores[st.session_state.winner] += 1
        st.session_state.game_over = True
    else:
        st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"


def main():
    st.set_page_config(page_title="Jogo da Velha", layout="centered")

    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("🎮 Jogo da Velha")
    with col2:
        st.markdown(f"<small>Versão {VERSION}</small>", unsafe_allow_html=True)

    # Inicialização do session_state
    if "board" not in st.session_state:
        st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
    if "current_player" not in st.session_state:
        st.session_state.current_player = "X"
    if "game_over" not in st.session_state:
        st.session_state.game_over = False
    if "winner" not in st.session_state:
        st.session_state.winner = None
    if "scores" not in st.session_state:
        st.session_state.scores = {"X": 0, "O": 0, "draw": 0}
    if "game_mode" not in st.session_state:
        st.session_state.game_mode = "human"
    if "board_key" not in st.session_state:
        st.session_state.board_key = 0

    st.subheader("Modo de Jogo")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👤 vs 👤", use_container_width=True):
            st.session_state.game_mode = "human"
            reset_game(st.session_state)
    with col2:
        if st.button("👤 vs 🤖", use_container_width=True):
            st.session_state.game_mode = "bot"
            reset_game(st.session_state)

    st.divider()

    st.subheader("📊 Placar")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Jogador X", st.session_state.scores["X"])
    with col2:
        st.metric("Jogador O", st.session_state.scores["O"])
    with col3:
        st.metric("Empates", st.session_state.scores["draw"])

    st.divider()

    st.subheader("Tabuleiro")

    board_container = st.container()
    with board_container:
        for row in range(3):
            cols = st.columns(3)
            for col in range(3):
                current_value = st.session_state.board[row][col]
                label = current_value if current_value else " "

                if cols[col].button(label, key=f"cell_{row}_{col}_{st.session_state.board_key}", use_container_width=True):
                    handle_click(row, col)
                    st.session_state.board_key += 1
                    st.rerun()

            if row < 2:
                st.divider()

    if (st.session_state.game_mode == "bot" and
            st.session_state.current_player == "O" and
            not st.session_state.game_over):

        st.info("🤖 Bot pensando...")
        time.sleep(0.5)

        move = bot_move(st.session_state.board)
        if move is not None:
            handle_click(*move)
            st.session_state.board_key += 1
            st.rerun()

    if st.session_state.game_over:
        st.divider()
        if st.session_state.winner == "draw":
            st.warning("🤝 Empate!")
        else:
            st.success(f"🏆 Jogador {st.session_state.winner} venceu! 🤷‍♂️")

        if st.button("🔄 Jogar Novamente", use_container_width=True):
            reset_game(st.session_state)

    st.divider()
    if not st.session_state.game_over:
        st.info(f"🎯 Vez do jogador: **{st.session_state.current_player}**")


main()
