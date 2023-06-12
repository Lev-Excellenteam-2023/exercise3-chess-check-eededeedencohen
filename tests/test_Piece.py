import sys
import os

sys.path.append(os.path.abspath('../'))

import pytest
from Piece import Knight, Pawn
from chess_engine import game_state
from enums import Player


@pytest.fixture
def empty_board_game_state():
    empty_board_game_state = game_state()
    empty_board_game_state.board = [[Player.EMPTY for i in range(8)] for j in range(8)]
    return empty_board_game_state


def test_get_valid_piece_takes_knight(empty_board_game_state):
    empty_board_game_state.board[3][4] = Knight('n', 3, 4, Player.PLAYER_1)
    assert empty_board_game_state.board[3][4].get_valid_piece_takes(empty_board_game_state) == []
    empty_board_game_state.board[2][2] = Pawn('p', 2, 2, Player.PLAYER_2)
    assert empty_board_game_state.board[3][4].get_valid_piece_takes(empty_board_game_state) == [(2, 2)]

    empty_board_game_state.board[2][2] = Pawn('p', 2, 2, Player.PLAYER_1)
    assert empty_board_game_state.board[3][4].get_valid_piece_takes(empty_board_game_state) == []

    empty_board_game_state.board[2][2] = Pawn('p', 2, 2, Player.PLAYER_2)
    empty_board_game_state.board[2][6] = Pawn('p', 2, 6, Player.PLAYER_2)
    assert empty_board_game_state.board[3][4].get_valid_piece_takes(empty_board_game_state) == [(2, 2), (2, 6)]

    empty_board_game_state.board[2][2] = Pawn('p', 2, 2, Player.PLAYER_1)
    empty_board_game_state.board[2][6] = Pawn('p', 2, 6, Player.PLAYER_2)
    assert empty_board_game_state.board[3][4].get_valid_piece_takes(empty_board_game_state) == [(2, 6)]

    empty_board_game_state.board[1][3] = Pawn('p', 1, 3, Player.PLAYER_2)
    empty_board_game_state.board[1][5] = Pawn('p', 1, 5, Player.PLAYER_2)
    empty_board_game_state.board[2][2] = Pawn('p', 2, 2, Player.PLAYER_2)
    empty_board_game_state.board[2][6] = Pawn('p', 2, 6, Player.PLAYER_2)
    empty_board_game_state.board[4][2] = Pawn('p', 4, 2, Player.PLAYER_2)
    empty_board_game_state.board[4][6] = Pawn('p', 4, 6, Player.PLAYER_2)
    empty_board_game_state.board[5][3] = Pawn('p', 5, 3, Player.PLAYER_2)
    empty_board_game_state.board[5][5] = Pawn('p', 5, 5, Player.PLAYER_2)
    assert empty_board_game_state.board[3][4].get_valid_piece_takes(empty_board_game_state) == [(1, 3), (1, 5), (2, 2),
                                                                                                (2, 6), (4, 2), (4, 6),
                                                                                                (5, 5), (5, 3)]


def test_get_valid_peaceful_moves_knight(empty_board_game_state):
    empty_board_game_state.board[3][4] = Knight('n', 3, 4, Player.PLAYER_1)
    assert empty_board_game_state.board[3][4].get_valid_peaceful_moves(empty_board_game_state) == [(1, 3), (1, 5),
                                                                                                   (2, 2), (2, 6),
                                                                                                   (4, 2), (4, 6),
                                                                                                   (5, 5), (5, 3)]
    empty_board_game_state.board[2][2] = Pawn('p', 2, 2, Player.PLAYER_1)
    assert empty_board_game_state.board[3][4].get_valid_peaceful_moves(empty_board_game_state) == [(1, 3), (1, 5),
                                                                                                   (2, 6),
                                                                                                   (4, 2), (4, 6),
                                                                                                   (5, 5), (5, 3)]
    empty_board_game_state.board[2][2] = Pawn('p', 2, 2, Player.PLAYER_2)
    assert empty_board_game_state.board[3][4].get_valid_peaceful_moves(empty_board_game_state) == [(1, 3), (1, 5),
                                                                                                   (2, 6),
                                                                                                   (4, 2), (4, 6),
                                                                                                   (5, 5), (5, 3)]

    empty_board_game_state.board[1][3] = Pawn('p', 1, 3, Player.PLAYER_2)
    empty_board_game_state.board[1][5] = Pawn('p', 1, 5, Player.PLAYER_1)
    empty_board_game_state.board[2][6] = Pawn('p', 2, 6, Player.PLAYER_2)
    empty_board_game_state.board[4][2] = Pawn('p', 4, 2, Player.PLAYER_1)
    empty_board_game_state.board[4][6] = Pawn('p', 4, 6, Player.PLAYER_2)
    empty_board_game_state.board[5][3] = Pawn('p', 5, 3, Player.PLAYER_1)
    empty_board_game_state.board[5][5] = Pawn('p', 5, 5, Player.PLAYER_2)
    assert empty_board_game_state.board[3][4].get_valid_peaceful_moves(empty_board_game_state) == []

# ===========================================================
# ==================== Integration Tests ====================
# ===========================================================


def test_get_valid_piece_moves_knight_middle(empty_board_game_state):
    empty_board_game_state.board[3][4] = Knight('n', 3, 4, Player.PLAYER_1)
    assert empty_board_game_state.board[3][4].get_valid_piece_moves(empty_board_game_state) == [(1, 3), (1, 5),
                                                                                                (2, 2), (2, 6),
                                                                                                (4, 2), (4, 6),
                                                                                                (5, 5), (5, 3)]


def test_get_valid_piece_moves_knight_corner(empty_board_game_state):
    empty_board_game_state.board[0][0] = Knight('n', 0, 0, Player.PLAYER_1)
    assert empty_board_game_state.board[0][0].get_valid_piece_moves(empty_board_game_state) == [(1, 2), (2, 1)]


def test_get_valid_piece_moves_knight_edge(empty_board_game_state):
    empty_board_game_state.board[0][4] = Knight('n', 0, 4, Player.PLAYER_1)
    assert empty_board_game_state.board[0][4].get_valid_piece_moves(empty_board_game_state) == [(1, 2), (1, 6), (2, 5),
                                                                                                (2, 3)]


def test_get_valid_piece_moves_knight_middle_with_pieces(empty_board_game_state):
    empty_board_game_state.board[3][4] = Knight('n', 3, 4, Player.PLAYER_1)
    empty_board_game_state.board[2][2] = Pawn('p', 2, 2, Player.PLAYER_1)
    assert empty_board_game_state.board[3][4].get_valid_piece_moves(empty_board_game_state) == [(1, 3), (1, 5),
                                                                                                (2, 6),
                                                                                                (4, 2), (4, 6),
                                                                                                (5, 5), (5, 3)]
