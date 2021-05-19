import random


class Game:
    matrix = [
        ['w', 'x', 'w', 'x', 'w', 'x', 'w', 'x'],
        ['x', 'w', 'x', 'w', 'x', 'w', 'x', 'w'],
        ['w', 'x', 'w', 'x', 'w', 'x', 'w', 'x'],
        ['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w'],
        ['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'],
        ['o', 'w', 'o', 'w', 'o', 'w', 'o', 'w'],
        ['w', 'o', 'w', 'o', 'w', 'o', 'w', 'o'],
        ['o', 'w', 'o', 'w', 'o', 'w', 'o', 'w'],
    ]

    its_player_x_turn = True
    selected_row = None
    selected_column = None
    count_pieces_x = None
    count_pieces_o = None

    def __init__(self):
        self.its_player_x_turn = bool(random.getrandbits(1))
        self.update_count_pieces_per_player()

    def get_matrix_row_len(self):
        return self.matrix.__len__()

    def get_matrix_column_len(self):
        return self.matrix[0].__len__()

    def get_matrix_piece(self, row, column):
        return self.matrix[row][column]

    def get_count_pieces_x(self):
        return self.count_pieces_x

    def get_count_pieces_o(self):
        return self.count_pieces_o

    def get_its_player_x_turn(self):
        return self.its_player_x_turn

    def update_count_pieces_per_player(self):
        count_x = 0
        count_o = 0
        for row in self.matrix:
            count_x = count_x + row.count('x') + row.count('xs') + row.count('xq') + row.count('xsq')
            count_o = count_o + row.count('o') + row.count('os') + row.count('oq') + row.count('osq')

        self.count_pieces_x = count_x
        self.count_pieces_o = count_o

    def switch_turn(self):
        self.selected_row = None
        self.selected_column = None
        self.its_player_x_turn = not self.its_player_x_turn
        self.update_count_pieces_per_player()

    def reset(self):
        self.matrix = [
            ['w', 'x', 'w', 'x', 'w', 'x', 'w', 'x'],
            ['x', 'w', 'x', 'w', 'x', 'w', 'x', 'w'],
            ['w', 'x', 'w', 'x', 'w', 'x', 'w', 'x'],
            ['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w'],
            ['w', 'b', 'w', 'b', 'w', 'b', 'w', 'b'],
            ['o', 'w', 'o', 'w', 'o', 'w', 'o', 'w'],
            ['w', 'o', 'w', 'o', 'w', 'o', 'w', 'o'],
            ['o', 'w', 'o', 'w', 'o', 'w', 'o', 'w'],
        ]
        self.selected_row = None
        self.selected_column = None
        self.its_player_x_turn = bool(random.getrandbits(1))
        self.update_count_pieces_per_player()

    def handle_click(self, row, column):
        pieces = self.select_piece(row, column)
        if pieces.__len__() > 0:
            return pieces
        else:
            pieces = self.deselect_piece(row, column)
            if pieces.__len__() > 0:
                return pieces
            else:
                pieces = self.its_a_permitted_move(row, column)
                if pieces.__len__() > 0:
                    return pieces
                else:
                    pieces = self.its_a_permitted_move_with_eat(row, column)
                    return pieces

    def update_piece(self, row, column, piece):
        if piece in ['x', 'o', 'xs', 'os']:
            if self.its_a_queen(row, column):
                piece = f'{piece}q'

        self.matrix[row][column] = piece
        return {'row': row, 'column': column, 'piece': piece}

    def select_piece(self, row, column):
        pieces = []
        if ((self.matrix[row][column] == 'x' or self.matrix[row][column] == 'xq') and self.its_player_x_turn) or (
                (self.matrix[row][column] == 'o' or self.matrix[row][column] == 'oq') and not self.its_player_x_turn):
            piece = self.update_piece(row, column, f'{self.matrix[row][column][0]}s{(self.matrix[row][column][1] if self.matrix[row][column].__len__() == 2 else "")}')
            pieces.append(piece)
            if self.selected_row is not None and self.selected_column is not None:
                piece = self.update_piece(self.selected_row, self.selected_column,
                                          self.matrix[self.selected_row][self.selected_column].replace('s', ''))
                pieces.append(piece)
            self.selected_row = row
            self.selected_column = column
        return pieces

    def deselect_piece(self, row, column):
        pieces = []
        if self.selected_row == row and self.selected_column == column:
            piece = self.update_piece(row, column,
                                      self.matrix[self.selected_row][self.selected_column].replace('s', ''))
            pieces.append(piece)
            self.selected_row = None
            self.selected_column = None
        return pieces

    def its_a_permitted_move(self, row, column):
        pieces = []
        if self.selected_row is not None and self.selected_column is not None:
            if self.matrix[row][column] == 'b':
                if self.its_a_queen(self.selected_row, self.selected_column):
                    if (self.selected_row + 1) == row or (self.selected_row - 1) == row:
                        if (self.selected_column - 1) == column or (self.selected_column + 1) == column:
                            piece = self.update_piece(row, column,
                                                      f'{self.matrix[self.selected_row][self.selected_column][0]}q')
                            pieces.append(piece)
                            piece = self.update_piece(self.selected_row, self.selected_column, 'b')
                            pieces.append(piece)
                            self.switch_turn()
                else:
                    if ((self.selected_row + 1) == row and self.its_player_x_turn) or (
                            (self.selected_row - 1) == row and not self.its_player_x_turn):
                        if (self.selected_column - 1) == column or (self.selected_column + 1) == column:
                            piece = self.update_piece(row, column,
                                                      self.matrix[self.selected_row][self.selected_column][0])
                            pieces.append(piece)
                            piece = self.update_piece(self.selected_row, self.selected_column, 'b')
                            pieces.append(piece)
                            self.switch_turn()
        return pieces

    def its_a_permitted_move_with_eat(self, row, column):
        pieces = []
        if self.selected_row is not None and self.selected_column is not None:
            if self.matrix[row][column] == 'b':
                if self.its_a_queen(self.selected_row, self.selected_column):
                    if (self.selected_row - 2) == row:
                        if (self.selected_column - 2) == column:
                            if self.matrix[self.selected_row - 1][self.selected_column - 1] in (
                                    ['o', 'oq'] if self.its_player_x_turn else ['x', 'xq']):
                                piece = self.update_piece(self.selected_row - 1, self.selected_column - 1, 'b')
                                pieces.append(piece)
                                piece = self.update_piece(row, column,
                                                          f'{self.matrix[self.selected_row][self.selected_column][0]}q')
                                pieces.append(piece)
                                piece = self.update_piece(self.selected_row, self.selected_column, 'b')
                                pieces.append(piece)
                                self.switch_turn()
                        elif (self.selected_column + 2) == column:
                            if self.matrix[self.selected_row - 1][self.selected_column + 1] in (
                                    ['o', 'oq'] if self.its_player_x_turn else ['x', 'xq']):
                                piece = self.update_piece(self.selected_row - 1, self.selected_column + 1, 'b')
                                pieces.append(piece)
                                piece = self.update_piece(row, column,
                                                          f'{self.matrix[self.selected_row][self.selected_column][0]}q')
                                pieces.append(piece)
                                piece = self.update_piece(self.selected_row, self.selected_column, 'b')
                                pieces.append(piece)
                                self.switch_turn()
                    elif (self.selected_row + 2) == row:
                        if (self.selected_column - 2) == column:
                            if self.matrix[self.selected_row + 1][self.selected_column - 1] in (
                                    ['o', 'oq'] if self.its_player_x_turn else ['x', 'xq']):
                                piece = self.update_piece(self.selected_row + 1, self.selected_column - 1, 'b')
                                pieces.append(piece)
                                piece = self.update_piece(row, column,
                                                          f'{self.matrix[self.selected_row][self.selected_column][0]}q')
                                pieces.append(piece)
                                piece = self.update_piece(self.selected_row, self.selected_column, 'b')
                                pieces.append(piece)
                                self.switch_turn()
                        elif (self.selected_column + 2) == column:
                            if self.matrix[self.selected_row + 1][self.selected_column + 1] in (
                                    ['o', 'oq'] if self.its_player_x_turn else ['x', 'xq']):
                                piece = self.update_piece(self.selected_row + 1, self.selected_column + 1, 'b')
                                pieces.append(piece)
                                piece = self.update_piece(row, column,
                                                          f'{self.matrix[self.selected_row][self.selected_column][0]}q')
                                pieces.append(piece)
                                piece = self.update_piece(self.selected_row, self.selected_column, 'b')
                                pieces.append(piece)
                                self.switch_turn()
                else:
                    if self.its_player_x_turn:
                        if (self.selected_row + 2) == row:
                            if (self.selected_column - 2) == column:
                                if self.matrix[self.selected_row + 1][self.selected_column - 1] in ['o', 'oq']:
                                    piece = self.update_piece(self.selected_row + 1, self.selected_column - 1, 'b')
                                    pieces.append(piece)
                                    piece = self.update_piece(row, column, 'x')
                                    pieces.append(piece)
                                    piece = self.update_piece(self.selected_row, self.selected_column, 'b')
                                    pieces.append(piece)
                                    self.switch_turn()
                            elif (self.selected_column + 2) == column:
                                if self.matrix[self.selected_row + 1][self.selected_column + 1] in ['o', 'oq']:
                                    piece = self.update_piece(self.selected_row + 1, self.selected_column + 1, 'b')
                                    pieces.append(piece)
                                    piece = self.update_piece(row, column, 'x')
                                    pieces.append(piece)
                                    piece = self.update_piece(self.selected_row, self.selected_column, 'b')
                                    pieces.append(piece)
                                    self.switch_turn()
                    else:
                        if (self.selected_row - 2) == row:
                            if (self.selected_column - 2) == column:
                                if self.matrix[self.selected_row - 1][self.selected_column - 1] in ['x', 'xq']:
                                    piece = self.update_piece(self.selected_row - 1, self.selected_column - 1, 'b')
                                    pieces.append(piece)
                                    piece = self.update_piece(row, column, 'o')
                                    pieces.append(piece)
                                    piece = self.update_piece(self.selected_row, self.selected_column, 'b')
                                    pieces.append(piece)
                                    self.switch_turn()
                            elif (self.selected_column + 2) == column:
                                if self.matrix[self.selected_row - 1][self.selected_column + 1] in ['x', 'xq']:
                                    piece = self.update_piece(self.selected_row - 1, self.selected_column + 1, 'b')
                                    pieces.append(piece)
                                    piece = self.update_piece(row, column, 'o')
                                    pieces.append(piece)
                                    piece = self.update_piece(self.selected_row, self.selected_column, 'b')
                                    pieces.append(piece)
                                    self.switch_turn()
        return pieces

    def its_a_queen(self, row, column):
        if self.matrix[row][column].count('q') == 1:
            return True
        elif self.its_player_x_turn:
            if row == (self.matrix.__len__() - 1):
                return True
        else:
            if row == 0:
                return True
