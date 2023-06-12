#
# The Chess piece classes
#
# TODO: add checking if check after moving suggested move later

# General chess piece
from enums import Player
# import game_state:


class Piece:
    # Initialize the piece
    def __init__(self, name, row_number, col_number, player):
        """ Piece class

        Attributes:
            name (str): name of the piece - r(rook), n(knight), b(bishop), q(queen), k(king), p(pawn)
            row_number (int): row number of the piece - top is 0, bottom is 7
            col_number (int): column number of the piece - left is 0, right is 7
            player (Player): player of the piece - PLAYER_1(white) or PLAYER_2(black)

        Methods:
            get_row_number: returns the row number of the piece
            get_col_number: returns the column number of the piece
            get_name: returns the name of the piece
            get_player: returns the player of the piece
            is_player: checks if the piece is the same player as the player passed in
            change_row_number: changes the row number of the piece
            change_col_number: changes the column number of the piece
            """
        self._name = name
        self.row_number = row_number
        self.col_number = col_number
        self._player = player

    
    def get_row_number(self):
        return self.row_number
    
    def get_col_number(self):
        return self.col_number
    
    def get_name(self):
        return self._name

    def get_player(self):
        return self._player

    def is_player(self, player_checked):
        """ Checks if the piece is the same player as the player passed in
        """
        return self.get_player() == player_checked
    
    # TO DO: add checking if check after moving suggested move later
    def can_move(self, board, starting_square):
        pass

    # TO DO: add checking if check after moving suggested move later
    def can_take(self, is_check): 
        pass

    def change_row_number(self, new_row_number):
        """ Changes the row number of the piece
        """
        self.row_number = new_row_number

    def change_col_number(self, new_col_number):
        """ Changes the column number of the piece
        """
        self.col_number = new_col_number

    # the inherited classes will implement this method
    def get_valid_piece_takes(self, game_state):
        pass
    
    # the inherited classes will implement this method
    def get_valid_peaceful_moves(self, game_state):
        pass

    # the inherited classes will implement this method
    def get_valid_piece_moves(self, board):
        pass


# Rook (R) - can go straight in the same line or column
class Rook(Piece):
    """ Rook piece class - inherits from Piece class
    
    Attributes:
        name (str): name of the piece - r(rook)
        row_number (int): row number of the piece - top is 0, bottom is 7
        col_number (int): column number of the piece - left is 0, right is 7
        player (Player): player of the piece - PLAYER_1(white) or PLAYER_2(black)
        has_moved (bool): whether the rook has moved or not - used for castling

    Methods:
        get_row_number: returns the row number of the piece
        get_col_number: returns the column number of the piece
        get_name: returns the name of the piece
        get_player: returns the player of the piece
        is_player: checks if the piece is the same player as the player passed in
        change_row_number: changes the row number of the piece
        change_col_number: changes the column number of the piece
        get_valid_peaceful_moves: returns list of the empty squares that the piece can move to
        get_valid_piece_takes: returns list of the valid moves of the piece that takes another piece
        get_valid_piece_moves: returns list of the valid moves of the piece
        traverse: returns 2 lists: valid peaceful moves and valid piece takes
    """
    def __init__(self, name, row_number, col_number, player):
        super().__init__(name, row_number, col_number, player)
        self.has_moved = False 

    def get_valid_peaceful_moves(self, game_state):
        """ Returns list of the empty squares that the piece can move to
        """
        return self.traverse(game_state)[0]

    def get_valid_piece_takes(self, game_state):
        """ Returns list of the valid moves of the piece that takes opponent's piece
        """
        return self.traverse(game_state)[1]

    def get_valid_piece_moves(self, game_state):
        """ Returns list of the valid moves of the piece
        """
        return self.get_valid_peaceful_moves(game_state) + self.get_valid_piece_takes(game_state)

    def traverse(self, game_state):
        _peaceful_moves = []
        _piece_takes = []

        self._up = 1
        self._down = 1
        self._left = 1
        self._right = 1

        # Left of the Rook
        self._breaking_point = False
        while self.get_col_number() - self._left >= 0 and not self._breaking_point:
            # when the square to the left is empty
            if game_state.get_piece(self.get_row_number(), self.get_col_number() - self._left) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number(), self.get_col_number() - self._left))
                self._left += 1
            # when the square contains an opposing piece
            elif game_state.is_valid_piece(self.get_row_number(), self.get_col_number() - self._left) and \
                    not game_state.get_piece(self.get_row_number(), self.get_col_number() - self._left).is_player(self.get_player()):
                _piece_takes.append((self.get_row_number(), self.get_col_number() - self._left))
                self._breaking_point = True
            else:
                self._breaking_point = True

        # Right of the Rook
        self._breaking_point = False
        while self.get_col_number() + self._right < 8 and not self._breaking_point:
            # when the square to the left is empty
            if game_state.get_piece(self.get_row_number(), self.get_col_number() + self._right) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number(), self.get_col_number() + self._right))
                self._right += 1
            # when the square contains an opposing piece
            elif game_state.is_valid_piece(self.get_row_number(), self.get_col_number() + self._right) and \
                    not game_state.get_piece(self.get_row_number(), self.get_col_number() + self._right).is_player(self.get_player()):
                _piece_takes.append((self.get_row_number(), self.get_col_number() + self._right))
                self._breaking_point = True
            else:
                self._breaking_point = True

        # Below the Rook
        self._breaking_point = False
        while self.get_row_number() + self._down < 8 and not self._breaking_point:
            # when the square to the left is empty
            if game_state.get_piece(self.get_row_number() + self._down, self.get_col_number()) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number() + self._down, self.get_col_number()))
                self._down += 1
            # when the square contains an opposing piece
            elif game_state.is_valid_piece(self.get_row_number() + self._down, self.get_col_number()) and \
                    not game_state.get_piece(self.get_row_number() + self._down, self.get_col_number()).is_player(self.get_player()):
                _piece_takes.append((self.get_row_number() + self._down, self.get_col_number()))
                self._breaking_point = True
            else:
                self._breaking_point = True

        # Above the Rook
        self._breaking_point = False
        while self.get_row_number() - self._up >= 0 and not self._breaking_point:
            # when the square to the left is empty
            if game_state.get_piece(self.get_row_number() - self._up, self.get_col_number()) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number() - self._up, self.get_col_number()))
                self._up += 1
            # when the square contains an opposing piece
            elif game_state.is_valid_piece(self.get_row_number() - self._up, self.get_col_number()) and \
                    not game_state.get_piece(self.get_row_number() - self._up, self.get_col_number()).is_player(self.get_player()):
                _piece_takes.append((self.get_row_number() - self._up, self.get_col_number()))
                self._breaking_point = True
            else:
                self._breaking_point = True
        return (_peaceful_moves, _piece_takes)


# Knight (N) - can move in an L shape - 2 squares in one direction and 1 in the other
class Knight(Piece): 
    """ Knight piece class

    Attributes:
        name: The name of the piece - 'n
        row_number: The row number of the piece
        col_number: The column number of the piece
        player: The player that owns the piece


    Methods:
        get_row_number: returns the row number of the piece
        get_col_number: returns the column number of the piece
        get_name: returns the name of the piece
        get_player: returns the player of the piece
        is_player: checks if the piece is the same player as the player passed in
        change_row_number: changes the row number of the piece
        change_col_number: changes the column number of the piece
        get_valid_peaceful_moves: returns a list of empty squares that the piece can move to
        get_valid_piece_takes: returns a list squares that contain opposing pieces that the piece can take
        get_valid_moves: returns a list of valid moves for the piece
    """
    def __init__(self, name, row_number, col_number, player):
        super().__init__(name, row_number, col_number, player)


    def get_valid_peaceful_moves(self, game_state): 
        """ Returns a list of valid peaceful moves
        """
        _moves = []
        row_change = [-2, -2, -1, -1, +1, +1, +2, +2]
        col_change = [-1, +1, -2, +2, -2, +2, +1, -1]

        # for each possible move of the knight 
        for i in range(0, 8): 
            new_row = self.get_row_number() + row_change[i]
            new_col = self.get_col_number() + col_change[i]
            evaluating_square = game_state.get_piece(new_row, new_col)
            # when the square with new_row and new_col is empty
            if evaluating_square == Player.EMPTY:
                _moves.append((new_row, new_col))
        return _moves

    def get_valid_piece_takes(self, game_state):
        _moves = []
        row_change = [-2, -2, -1, -1, +1, +1, +2, +2]
        col_change = [-1, +1, -2, +2, -2, +2, +1, -1]

        for i in range(0, 8):
            new_row = self.get_row_number() + row_change[i]
            new_col = self.get_col_number() + col_change[i]
            evaluating_square = game_state.get_piece(new_row, new_col)
            # when the square with new_row and new_col contains an enemy Piece
            if game_state.is_valid_piece(new_row, new_col) and self.get_player() != evaluating_square.get_player():
                _moves.append((new_row, new_col))
        return _moves

    def get_valid_piece_moves(self, game_state):
        return self.get_valid_peaceful_moves(game_state) + self.get_valid_piece_takes(game_state)
    
# Bishop - can move diagonally in any direction 
class Bishop(Piece):
    """ Bishop piece class

        Attributes:
            name (str): name of the piece - r(rook), n(knight), b(bishop), q(queen), k(king), p(pawn)
            row_number (int): row number of the piece - top is 0, bottom is 7
            col_number (int): column number of the piece - left is 0, right is 7
            player (Player): player of the piece - PLAYER_1(white) or PLAYER_2(black)

        Methods:
            get_row_number: returns the row number of the piece
            get_col_number: returns the column number of the piece
            get_name: returns the name of the piece
            get_player: returns the player of the piece
            is_player: checks if the piece is the same player as the player passed in
            change_row_number: changes the row number of the piece
            change_col_number: changes the column number of the piece
            get_valid_peaceful_moves: returns a list of empty squares that the piece can move to
            get_valid_piece_takes: returns a list squares that contain opposing pieces that the piece can take
            get_valid_moves: returns a list of valid moves for the piece
            traverse: returns a list of valid peaceful moves and a list of valid piece takes
    """
    def __init__(self, name, row_number, col_number, player):
        super().__init__(name, row_number, col_number, player)

    def get_valid_piece_takes(self, game_state):
        return self.traverse(game_state)[1]

    def get_valid_peaceful_moves(self, game_state):
        return self.traverse(game_state)[0]

    def get_valid_piece_moves(self, game_state):
        return self.get_valid_piece_takes(game_state) + self.get_valid_peaceful_moves(game_state)

    def traverse(self, game_state):
        _peaceful_moves = []
        _piece_takes = []

        # Up left of the bishop 
        self._breaking_point = False
        self._up = 1
        self._down = 1
        self._left = 1
        self._right = 1
        while self.get_col_number() - self._left >= 0 and self.get_row_number() - self._up >= 0 and not self._breaking_point:
            # when the square is empty
            if game_state.get_piece(self.get_row_number() - self._up, self.get_col_number() - self._left) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number() - self._up, self.get_col_number() - self._left))
                self._left += 1
                self._up += 1
            # when the square contains an opposing piece
            elif game_state.is_valid_piece(self.get_row_number() - self._up, self.get_col_number() - self._left) and \
                    not game_state.get_piece(self.get_row_number() - self._up, self.get_col_number() - self._left).is_player(self.get_player()):
                _piece_takes.append((self.get_row_number() - self._up, self.get_col_number() - self._left))
                self._breaking_point = True
            # when the square contains a piece of the same color as the bishop
            else:
                self._breaking_point = True

        # Right up of the bishop
        self._breaking_point = False
        self._up = 1
        self._down = 1
        self._left = 1
        self._right = 1
        while self.get_col_number() + self._right < 8 and self.get_row_number() - self._up >= 0 and not self._breaking_point:
            # when the square is empty
            if game_state.get_piece(self.get_row_number() - self._up, self.get_col_number() + self._right) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number() - self._up, self.get_col_number() + self._right))
                self._right += 1
                self._up += 1
            # when the square contains an opposing piece
            elif game_state.is_valid_piece(self.get_row_number() - self._up, self.get_col_number() + self._right) and \
                    not game_state.get_piece(self.get_row_number() - self._up, self.get_col_number() + self._right).is_player(self.get_player()):
                _piece_takes.append((self.get_row_number() - self._up, self.get_col_number() + self._right))
                self._breaking_point = True
            else:
                self._breaking_point = True

        # Down left of the bishop
        self._breaking_point = False
        self._up = 1
        self._down = 1
        self._left = 1
        self._right = 1
        while self.get_col_number() - self._left >= 0 and self.get_row_number() + self._down < 8 and not self._breaking_point:
            # when the square is empty
            if game_state.get_piece(self.get_row_number() + self._down, self.get_col_number() - self._left) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number() + self._down, self.get_col_number() - self._left))
                self._down += 1
                self._left += 1
            # when the square contains an opposing piece
            elif game_state.is_valid_piece(self.get_row_number() + self._down, self.get_col_number() - self._left) and \
                    not game_state.get_piece(self.get_row_number() + self._down, self.get_col_number() - self._left).is_player(self.get_player()):
                _piece_takes.append((self.get_row_number() + self._down, self.get_col_number() - self._left))
                self._breaking_point = True
            else:
                self._breaking_point = True

        # Down right of the bishop
        self._breaking_point = False
        self._up = 1
        self._down = 1
        self._left = 1
        self._right = 1
        while self.get_col_number() + self._right < 8 and self.get_row_number() + self._down < 8 and not self._breaking_point:
            # when the square is empty
            if game_state.get_piece(self.get_row_number() + self._down, self.get_col_number() + self._right) is Player.EMPTY:
                _peaceful_moves.append((self.get_row_number() + self._down, self.get_col_number() + self._right))
                self._down += 1
                self._right += 1
            # when the square contains an opposing piece
            elif game_state.is_valid_piece(self.get_row_number() + self._down, self.get_col_number() + self._right) and \
                    not game_state.get_piece(self.get_row_number() + self._down, self.get_col_number() + self._right).is_player(
                        self.get_player()):
                _piece_takes.append((self.get_row_number() + self._down, self.get_col_number() + self._right))
                self._breaking_point = True
            else:
                self._breaking_point = True
        return (_peaceful_moves, _piece_takes)


class Pawn(Piece):
    """ Pawn piece class:

    Attributes:
        name (str): name of the piece - r(rook), n(knight), b(bishop), q(queen), k(king), p(pawn)
        row_number (int): row number of the piece - top is 0, bottom is 7
        col_number (int): column number of the piece - left is 0, right is 7
        player (Player): player of the piece - PLAYER_1(white) or PLAYER_2(black)

    Methods:
        get_row_number: returns the row number of the piece
        get_col_number: returns the column number of the piece
        get_name: returns the name of the piece
        get_player: returns the player of the piece
        is_player: checks if the piece is the same player as the player passed in
        change_row_number: changes the row number of the piece
        change_col_number: changes the column number of the piece
        get_valid_peaceful_moves: returns a list of empty squares that the piece can move to
        get_valid_piece_takes: returns a list squares that contain opposing pieces that the piece can take
        get_valid_moves: returns a list of valid moves for the piece
    """

    def __init__(self, name, row_number, col_number, player):
        super().__init__(name, row_number, col_number, player)
        self._has_moves_two_squares = False  # if the pawn has moved two squares in the previous move
    def get_valid_piece_takes(self, game_state):
        """  Returns a list of squares that contain opposing pieces that the piece can take.
             TO DO: ADDING EN PASSANT
        """
        _moves = []
        # case the pawn is white
        if self.is_player(Player.PLAYER_1): 
            # when the square to the bottom left of the starting_square has a black piece
            if game_state.is_valid_piece(self.get_row_number() + 1, self.get_col_number() - 1) and \
                    game_state.get_piece(self.get_row_number() + 1, self.get_col_number() - 1).is_player(Player.PLAYER_2):
                _moves.append((self.get_row_number() + 1, self.get_col_number() - 1))
            # when the square to the bottom right of the starting_square has a black piece
            if game_state.is_valid_piece(self.get_row_number() + 1, self.get_col_number() + 1) and \
                    game_state.get_piece(self.get_row_number() + 1, self.get_col_number() + 1).is_player(Player.PLAYER_2):
                _moves.append((self.get_row_number() + 1, self.get_col_number() + 1))
            # En Passant case:
            ''' the previous code for en passant 
            if game_state.can_en_passant(self.get_row_number(), self.get_col_number()):
                _moves.append((self.get_row_number() + 1, game_state.previous_piece_en_passant()[1]))
            '''
            # my code for en passant
            if game_state.is_valid_piece(self.get_row_number(), self.get_col_number() + 1) and \
                    game_state.get_piece(self.get_row_number(), self.get_col_number() + 1).is_player(Player.PLAYER_2) and \
                    game_state.get_piece(self.get_row_number(), self.get_col_number() + 1).get_name() == 'p' and \
                    game_state.get_piece(self.get_row_number(), self.get_col_number() + 1).has_moved_two_squares():
                _moves.append((5, self.get_col_number() + 1))
            if game_state.is_valid_piece(self.get_row_number(), self.get_col_number() - 1) and \
                    game_state.get_piece(self.get_row_number(), self.get_col_number() - 1).is_player(Player.PLAYER_2) and \
                    game_state.get_piece(self.get_row_number(), self.get_col_number() - 1).get_name() == 'p' and \
                    game_state.get_piece(self.get_row_number(), self.get_col_number() - 1).has_moved_two_squares():
                _moves.append((5, self.get_col_number() - 1))



        # when the pawn is a black piece
        elif self.is_player(Player.PLAYER_2):
            # when the square to the top left of the starting_square has a white piece
            if game_state.is_valid_piece(self.get_row_number() - 1, self.get_col_number() - 1) and \
                    game_state.get_piece(self.get_row_number() - 1, self.get_col_number() - 1).is_player(Player.PLAYER_1):
                _moves.append((self.get_row_number() - 1, self.get_col_number() - 1))
            # when the square to the top right of the starting_square has a white piece
            if game_state.is_valid_piece(self.get_row_number() - 1, self.get_col_number() + 1) and \
                    game_state.get_piece(self.get_row_number() - 1, self.get_col_number() + 1).is_player(Player.PLAYER_1):
                _moves.append((self.get_row_number() - 1, self.get_col_number() + 1))
            ''' the previous code for en passant
            if game_state.can_en_passant(self.get_row_number(), self.get_col_number()):
                _moves.append((self.get_row_number() - 1, game_state.previous_piece_en_passant()[1]))
            '''
            # my code for en passant
            if game_state.is_valid_piece(self.get_row_number(), self.get_col_number() + 1) and \
                    game_state.get_piece(self.get_row_number(), self.get_col_number() + 1).is_player(Player.PLAYER_1) and \
                    game_state.get_piece(self.get_row_number(), self.get_col_number() + 1).get_name() == 'p' and \
                    game_state.get_piece(self.get_row_number(), self.get_col_number() + 1).has_moved_two_squares():
                _moves.append((2, self.get_col_number() + 1))
            if game_state.is_valid_piece(self.get_row_number(), self.get_col_number() - 1) and \
                    game_state.get_piece(self.get_row_number(), self.get_col_number() - 1).is_player(Player.PLAYER_1) and \
                    game_state.get_piece(self.get_row_number(), self.get_col_number() - 1).get_name() == 'p' and \
                    game_state.get_piece(self.get_row_number(), self.get_col_number() - 1).has_moved_two_squares():
                _moves.append((2, self.get_col_number() - 1))
        return _moves

    def has_moved_two_squares(self):
        return self._has_moves_two_squares

    def set_has_moved_two_squares(self, has_moved_two_squares):
        self._has_moves_two_squares = has_moved_two_squares

    def get_valid_peaceful_moves(self, game_state):
        _moves = []
        # when the pawn is a white piece: column always goes up by 1
        if self.is_player(Player.PLAYER_1):
            # when the square right below the starting_square is empty
            if game_state.get_piece(self.get_row_number() + 1, self.get_col_number()) == Player.EMPTY:
                # when the pawn has not been moved yet
                if self.get_row_number() == 1 and game_state.get_piece(self.get_row_number() + 2,
                                                                       self.get_col_number()) == Player.EMPTY:
                    _moves.append((self.get_row_number() + 1, self.get_col_number()))
                    _moves.append((self.get_row_number() + 2, self.get_col_number()))
                # when the pawn has already been moved
                else:
                    _moves.append((self.get_row_number() + 1, self.get_col_number()))
        # when the pawn is a black piece
        elif self.is_player(Player.PLAYER_2):
            # when the square right above is empty
            if game_state.get_piece(self.get_row_number() - 1, self.get_col_number()) == Player.EMPTY:
                # when the pawn has not been moved yet
                if self.get_row_number() == 6 and game_state.get_piece(self.get_row_number() - 2,
                                                                       self.get_col_number()) == Player.EMPTY:
                    _moves.append((self.get_row_number() - 1, self.get_col_number()))
                    _moves.append((self.get_row_number() - 2, self.get_col_number()))
                # when the pawn has been moved
                else:
                    _moves.append((self.get_row_number() - 1, self.get_col_number()))
        return _moves

    def get_valid_piece_moves(self, game_state):
        return self.get_valid_peaceful_moves(game_state) + self.get_valid_piece_takes(game_state)


# Queen
class Queen(Rook, Bishop):
    """ Queen piece class:
    Inherits from Rook and Bishop

    Attributes:
        name (str): name of the piece - r(rook), n(knight), b(bishop), q(queen), k(king), p(pawn)
        row_number (int): row number of the piece - top is 0, bottom is 7
        col_number (int): column number of the piece - left is 0, right is 7
        player (Player): player of the piece - PLAYER_1(white) or PLAYER_2(black)

    Methods:
        get_row_number: returns the row number of the piece
        get_col_number: returns the column number of the piece
        get_name: returns the name of the piece
        get_player: returns the player of the piece
        is_player: checks if the piece is the same player as the player passed in
        change_row_number: changes the row number of the piece
        change_col_number: changes the column number of the piece
        get_valid_peaceful_moves: returns a list of empty squares that the piece can move to
        get_valid_piece_takes: returns a list squares that contain opposing pieces that the piece can take
        get_valid_moves: returns a list of valid moves for the piece
    """
    def get_valid_peaceful_moves(self, game_state):
        return (Rook.get_valid_peaceful_moves(Rook(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), game_state) +
                Bishop.get_valid_peaceful_moves(Bishop(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), game_state))

    def get_valid_piece_takes(self, game_state):
        return (Rook.get_valid_piece_takes( Rook(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), game_state) +
                Bishop.get_valid_piece_takes(Bishop(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), game_state))

    def get_valid_piece_moves(self, game_state):
        return (Rook.get_valid_piece_moves(Rook(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), game_state) +
                Bishop.get_valid_piece_moves(Bishop(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), game_state))

# King
class King(Piece):
    """ King piece class:

    Attributes:
        name (str): name of the piece - r(rook), n(knight), b(bishop), q(queen), k(king), p(pawn)
        row_number (int): row number of the piece - top is 0, bottom is 7
        col_number (int): column number of the piece - left is 0, right is 7
        player (Player): player of the piece - PLAYER_1(white) or PLAYER_2(black)
        has_moved (bool): whether the king has moved or not - for castling

    Methods:
        get_row_number: returns the row number of the piece
        get_col_number: returns the column number of the piece
        get_name: returns the name of the piece
        get_player: returns the player of the piece
        is_player: checks if the piece is the same player as the player passed in
        change_row_number: changes the row number of the piece
        change_col_number: changes the column number of the piece
        get_valid_peaceful_moves: returns a list of empty squares that the piece can move to
        get_valid_piece_takes: returns a list squares that contain opposing pieces that the piece can take
        get_valid_moves: returns a list of valid moves for the piece
    """
    def __init__(self, name, row_number, col_number, player, has_moved=False):
        super().__init__(name, row_number, col_number, player)
        self.has_moved = has_moved

    def get_valid_piece_takes(self, game_state):
        _moves = []
        row_change = [-1, +0, +1, -1, +1, -1, +0, +1]
        col_change = [-1, -1, -1, +0, +0, +1, +1, +1]

        for i in range(0, 8):
            new_row = self.get_row_number() + row_change[i]
            new_col = self.get_col_number() + col_change[i]
            evaluating_square = game_state.get_piece(new_row, new_col)
            # when the square with new_row and new_col contains a valid piece
            if game_state.is_valid_piece(new_row, new_col):
                # when the king is white and the piece near the king is black
                if self.is_player(Player.PLAYER_1) and evaluating_square.is_player(Player.PLAYER_2):
                    _moves.append((new_row, new_col))
                # when the king is black and the piece near the king is white
                elif self.is_player(Player.PLAYER_2) and evaluating_square.is_player(Player.PLAYER_1):
                    _moves.append((new_row, new_col))
        return _moves

    def get_valid_peaceful_moves(self, game_state):
        _moves = []
        row_change = [-1, +0, +1, -1, +1, -1, +0, +1]
        col_change = [-1, -1, -1, +0, +0, +1, +1, +1]

        for i in range(0, 8):
            new_row = self.get_row_number() + row_change[i]
            new_col = self.get_col_number() + col_change[i]
            evaluating_square = game_state.get_piece(new_row, new_col)
            # when the square with new_row and new_col is empty
            if evaluating_square == Player.EMPTY:
                _moves.append((new_row, new_col))

        if game_state.king_can_castle_left(self.get_player()):
            if self.is_player(Player.PLAYER_1):
                _moves.append((0, 1))
            elif self.is_player(Player.PLAYER_2):
                _moves.append((7, 1))
        elif game_state.king_can_castle_right(self.get_player()):
            if self.is_player(Player.PLAYER_1):
                _moves.append((0, 5))
            elif self.is_player(Player.PLAYER_2):
                _moves.append((7, 5))
        return _moves

    def get_valid_piece_moves(self, game_state):
        ''' Returns a list of tuples of valid moves for the piece.
        '''
        return self.get_valid_peaceful_moves(game_state) + self.get_valid_piece_takes(game_state)
    
