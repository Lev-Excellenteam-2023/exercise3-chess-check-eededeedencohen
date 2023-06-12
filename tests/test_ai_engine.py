import sys
import os

sys.path.append(os.path.abspath('../'))

import pytest
from ai_engine import chess_ai
from Piece import Knight, Pawn, King, Queen, Rook, Bishop
from chess_engine import game_state
from enums import Player


# Test for evaluate_board:
@pytest.fixture
def empty_board_game_state():
    empty_board_game_state = game_state()
    empty_board_game_state.board = [[Player.EMPTY for i in range(8)] for j in range(8)]
    return empty_board_game_state


def test_evaluate_board_empty_board(empty_board_game_state):
    ai = chess_ai()
    assert ai.evaluate_board(empty_board_game_state, Player.PLAYER_1) == 0


def test_evaluate_board_black_ai(empty_board_game_state):
    ai = chess_ai()
    empty_board_game_state.board[0][0] = Knight("n", 0, 0, Player.PLAYER_1)
    assert ai.evaluate_board(empty_board_game_state, Player.PLAYER_1) == -30

    empty_board_game_state.board[0][0] = Knight("n", 0, 0, Player.PLAYER_2)
    assert ai.evaluate_board(empty_board_game_state, Player.PLAYER_1) == 30

    empty_board_game_state.board[0][0] = Pawn("p", 0, 0, Player.PLAYER_2)
    empty_board_game_state.board[0][1] = King("k", 0, 1, Player.PLAYER_2)
    empty_board_game_state.board[0][2] = Queen("q", 0, 2, Player.PLAYER_2)
    empty_board_game_state.board[0][3] = Rook("r", 0, 3, Player.PLAYER_2)
    empty_board_game_state.board[0][4] = Bishop("b", 0, 4, Player.PLAYER_2)
    empty_board_game_state.board[0][5] = Knight("n", 0, 5, Player.PLAYER_2)
    assert ai.evaluate_board(empty_board_game_state, Player.PLAYER_1) == 1220

    empty_board_game_state.board[0][0] = Pawn("p", 0, 0, Player.PLAYER_1)
    empty_board_game_state.board[0][1] = King("k", 0, 1, Player.PLAYER_1)
    empty_board_game_state.board[0][2] = Queen("q", 0, 2, Player.PLAYER_1)
    empty_board_game_state.board[0][3] = Rook("r", 0, 3, Player.PLAYER_1)
    empty_board_game_state.board[0][4] = Bishop("b", 0, 4, Player.PLAYER_1)
    empty_board_game_state.board[0][5] = Knight("n", 0, 5, Player.PLAYER_1)
    assert ai.evaluate_board(empty_board_game_state, Player.PLAYER_1) == -1220

    empty_board_game_state.board[0][0] = Pawn("p", 0, 0, Player.PLAYER_1)
    empty_board_game_state.board[0][1] = King("k", 0, 1, Player.PLAYER_1)
    empty_board_game_state.board[0][2] = Queen("q", 0, 2, Player.PLAYER_1)
    empty_board_game_state.board[0][3] = Rook("r", 0, 3, Player.PLAYER_1)
    empty_board_game_state.board[0][4] = Bishop("b", 0, 4, Player.PLAYER_1)
    empty_board_game_state.board[0][5] = Knight("n", 0, 5, Player.PLAYER_1)
    empty_board_game_state.board[0][6] = Pawn("p", 0, 6, Player.PLAYER_2)
    empty_board_game_state.board[0][7] = King("k", 0, 7, Player.PLAYER_2)
    empty_board_game_state.board[1][0] = Queen("q", 1, 0, Player.PLAYER_2)
    empty_board_game_state.board[1][1] = Rook("r", 1, 1, Player.PLAYER_2)
    empty_board_game_state.board[1][2] = Bishop("b", 1, 2, Player.PLAYER_2)
    empty_board_game_state.board[1][3] = Knight("n", 1, 3, Player.PLAYER_2)
    assert ai.evaluate_board(empty_board_game_state, Player.PLAYER_1) == 0


def test_evaluate_board_white_ai(empty_board_game_state):
    ai = chess_ai()
    empty_board_game_state.board[0][0] = Knight("n", 0, 0, Player.PLAYER_2)
    assert ai.evaluate_board(empty_board_game_state, Player.PLAYER_2) == -30

    empty_board_game_state.board[0][0] = Knight("n", 0, 0, Player.PLAYER_1)
    assert ai.evaluate_board(empty_board_game_state, Player.PLAYER_2) == 30

    empty_board_game_state.board[0][0] = Pawn("p", 0, 0, Player.PLAYER_1)
    empty_board_game_state.board[0][1] = King("k", 0, 1, Player.PLAYER_1)
    empty_board_game_state.board[0][2] = Queen("q", 0, 2, Player.PLAYER_1)
    empty_board_game_state.board[0][3] = Rook("r", 0, 3, Player.PLAYER_1)
    empty_board_game_state.board[0][4] = Bishop("b", 0, 4, Player.PLAYER_1)
    empty_board_game_state.board[0][5] = Knight("n", 0, 5, Player.PLAYER_1)
    assert ai.evaluate_board(empty_board_game_state, Player.PLAYER_2) == 1220

    empty_board_game_state.board[0][0] = Pawn("p", 0, 0, Player.PLAYER_2)
    empty_board_game_state.board[0][1] = King("k", 0, 1, Player.PLAYER_2)
    empty_board_game_state.board[0][2] = Queen("q", 0, 2, Player.PLAYER_2)
    empty_board_game_state.board[0][3] = Rook("r", 0, 3, Player.PLAYER_2)
    empty_board_game_state.board[0][4] = Bishop("b", 0, 4, Player.PLAYER_2)
    empty_board_game_state.board[0][5] = Knight("n", 0, 5, Player.PLAYER_2)
    assert ai.evaluate_board(empty_board_game_state, Player.PLAYER_2) == -1220

    empty_board_game_state.board[0][0] = Pawn("p", 0, 0, Player.PLAYER_2)
    empty_board_game_state.board[0][1] = King("k", 0, 1, Player.PLAYER_2)
    empty_board_game_state.board[0][2] = Queen("q", 0, 2, Player.PLAYER_2)
    empty_board_game_state.board[0][3] = Rook("r", 0, 3, Player.PLAYER_2)
    empty_board_game_state.board[0][4] = Bishop("b", 0, 4, Player.PLAYER_2)
    empty_board_game_state.board[0][5] = Knight("n", 0, 5, Player.PLAYER_2)
    empty_board_game_state.board[0][6] = Pawn("p", 0, 6, Player.PLAYER_1)
    empty_board_game_state.board[0][7] = King("k", 0, 7, Player.PLAYER_1)
    empty_board_game_state.board[1][0] = Queen("q", 1, 0, Player.PLAYER_1)
    empty_board_game_state.board[1][1] = Rook("r", 1, 1, Player.PLAYER_1)
    empty_board_game_state.board[1][2] = Bishop("b", 1, 2, Player.PLAYER_1)
    empty_board_game_state.board[1][3] = Knight("n", 1, 3, Player.PLAYER_1)
    assert ai.evaluate_board(empty_board_game_state, Player.PLAYER_2) == 0









