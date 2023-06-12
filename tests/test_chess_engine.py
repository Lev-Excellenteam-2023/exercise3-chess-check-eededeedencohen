import os
import sys
import pytest

from Piece import Pawn
from chess_engine import game_state
from enums import Player

sys.path.append(os.path.abspath('../'))


@pytest.fixture
def start_game_state():
    return game_state()


def test_black_wins(start_game_state):
    assert start_game_state.white_turn == True
    assert start_game_state.checkmate_stalemate_checker() == 3
    start_game_state.move_piece((1,2), (2,2), False)

    assert start_game_state.white_turn == False
    assert start_game_state.checkmate_stalemate_checker() == 3
    start_game_state.move_piece((6,3), (4,3), False)

    assert start_game_state.white_turn == True
    assert start_game_state.checkmate_stalemate_checker() == 3
    start_game_state.move_piece((1,1), (3,1), False)

    assert start_game_state.white_turn == False
    assert start_game_state.checkmate_stalemate_checker() == 3
    start_game_state.move_piece((7,4), (3,0), False)

    assert start_game_state.white_turn == True
    assert start_game_state.checkmate_stalemate_checker() == 0


def test_en_passant_move(start_game_state):
    # white pawn moves
    start_game_state.move_piece((1,2), (3,2), False)
    # black pawn moves
    start_game_state.move_piece((6,0), (5,0), False)
    # white pawn moves again
    start_game_state.move_piece((3,2), (4,2), False)
    # black pawn moves 2 steps from starting position
    start_game_state.move_piece((6,3), (4,3), False)

    # Test black pawn at (4,3)
    assert start_game_state.get_piece(4,3).get_name() == "p" and start_game_state.get_piece(4,3).get_player() == Player.PLAYER_2

    # move white pawn to en passant position
    assert start_game_state.white_turn == True
    start_game_state.move_piece((4,2), (5,3), False)

    # Test En Passant 
    assert start_game_state.board[4][3] == Player.EMPTY













