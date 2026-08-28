import random


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]
    if all(cell != "" for row in board for cell in row):
        return "draw"
    return None


def reset_game(state):
    state.board = [["" for _ in range(3)] for _ in range(3)]
    state.current_player = "X"
    state.game_over = False
    state.winner = None
    state.board_key += 1


def bot_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]
    if empty_cells:
        return random.choice(empty_cells)
    return None
