import sys
sys.path.insert(0, '/mnt/c/Projects/ppi/tic-tac-toe')

from app import check_winner, bot_move, reset_game


def test_check_winner_horizontal_x():
    board = [["X", "X", "X"], ["", "", ""], ["", "", ""]]
    assert check_winner(board) == "X"


def test_check_winner_horizontal_o():
    board = [["", "", ""], ["O", "O", "O"], ["", "", ""]]
    assert check_winner(board) == "O"


def test_check_winner_vertical_x():
    board = [["X", "", ""], ["X", "", ""], ["X", "", ""]]
    assert check_winner(board) == "X"


def test_check_winner_vertical_o():
    board = [["", "O", ""], ["", "O", ""], ["", "O", ""]]
    assert check_winner(board) == "O"


def test_check_winner_diagonal_x():
    board = [["X", "", ""], ["", "X", ""], ["", "", "X"]]
    assert check_winner(board) == "X"


def test_check_winner_diagonal_o():
    board = [["", "", "O"], ["", "O", ""], ["O", "", ""]]
    assert check_winner(board) == "O"


def test_check_winner_draw():
    board = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
    assert check_winner(board) == "draw"


def test_check_winner_incomplete():
    board = [["X", "", ""], ["", "", ""], ["", "", ""]]
    assert check_winner(board) is None


def test_bot_move():
    board = [["X", "", ""], ["", "O", ""], ["", "", ""]]
    result = bot_move(board)
    assert result in [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]


def test_bot_move_no_empty():
    board = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
    result = bot_move(board)
    assert result is None


class MockState:
    def __init__(self):
        self.board = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
        self.current_player = "O"
        self.game_over = True
        self.winner = "X"
        self.scores = {"X": 5, "O": 3, "draw": 2}
        self.board_key = 10


def test_reset_game():
    state = MockState()
    reset_game(state)
    assert state.board == [["", "", ""] for _ in range(3)]
    assert state.current_player == "X"
    assert state.game_over is False
    assert state.winner is None
    assert state.board_key == 11
