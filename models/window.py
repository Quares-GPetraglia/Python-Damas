from tkinter import *
from functools import partial
from models.game import Game
from models.piece_image import PieceImage
import os

class Window:
    window = None
    board = None
    statistics = None
    piece_image = None
    game = None

    def __init__(self):
        self.game = Game()
        self.render_window()
        self.render_menu()
        self.piece_image = PieceImage()
        self.render_board()
        self.render_statistics()
        self.open_window()

    def render_window(self):
        self.window = Tk()
        self.window.title('Damas')
        self.window.resizable(0, 0)
        self.window.iconbitmap(os.path.join("images", 'icon.ico'))

    def open_window(self):
        self.window.mainloop()

    def reset_window(self):
        self.game.reset()
        self.render_board()
        self.render_statistics()

    def render_menu(self):
        menu = Menu(self.window)
        submenu = Menu(menu, tearoff=0)
        submenu.add_command(label="Nueva partida", command=self.reset_window)
        submenu.add_separator()
        submenu.add_command(label="Salir", command=self.window.quit)
        menu.add_cascade(label="Juego", menu=submenu)
        self.window.config(menu=menu)

    def render_board(self):
        self.board = {}
        frame = Frame(self.window).grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        for row in range(0, self.game.get_matrix_row_len()):
            for column in range(0, self.game.get_matrix_column_len()):
                image = self.piece_image.get_image(self.game.get_matrix_piece(row, column))
                button = Button(frame, image=image, command=partial(self.handle_click, [row, column]), bd=0, padx=0,
                                pady=0, highlightthickness=0)
                button.grid(row=row, column=column)
                self.board[(row, column)] = button

    def update_board(self, pieces):
        for piece in pieces:
            image = self.piece_image.get_image(piece.get('piece'))
            self.board.get((piece.get('row'), piece.get('column'))).configure(image=image)

    def render_statistics(self):
        self.statistics = {}
        frame = Frame(self.window).grid()
        player_x_text = Label(frame, text=f'ROJO: {self.game.get_count_pieces_x()}')
        player_x_text.grid(row=1, column=9, sticky="nsew", padx=100, pady=10)
        self.statistics['player_x'] = player_x_text
        player_o_text = Label(frame, text=f'AZUL: {self.game.get_count_pieces_o()}')
        player_o_text.grid(row=2, column=9, sticky="nsew", padx=100, pady=10)
        self.statistics['player_o'] = player_o_text
        turn_text = Label(frame, text='Turno:')
        turn_text.grid(row=3, column=9, sticky="nsew", padx=100, pady=10)
        self.statistics['turn_text'] = turn_text
        turn = Label(frame, image=(self.piece_image.get_image('xt' if self.game.get_its_player_x_turn() else 'ot')))
        turn.grid(row=4, column=9)
        self.statistics['turn'] = turn
        Button(frame, text='Reiniciar', command=self.reset_window, bd=0, padx=0, pady=0, highlightthickness=0).grid(
            row=5,
            column=9)

    def update_statistics(self):
        self.statistics.get('turn').configure(
            image=(self.piece_image.get_image('xt' if self.game.get_its_player_x_turn() else 'ot')))
        self.statistics.get('player_x').configure(text=f'ROJO: {self.game.get_count_pieces_x()}')
        self.statistics.get('player_o').configure(text=f'AZUL: {self.game.get_count_pieces_o()}')
        if self.game.get_count_pieces_x() == 0:
            self.statistics.get('turn').configure(image=self.piece_image.get_image('ot'))
            self.statistics.get('turn_text').configure(text=f'GANADOR: Azul')
        if self.game.get_count_pieces_o() == 0:
            self.statistics.get('turn').configure(image=self.piece_image.get_image('xt'))
            self.statistics.get('turn_text').configure(text=f'GANADOR: Rojo')

    def handle_click(self, position):
        row = position[0]
        column = position[1]
        pieces = self.game.handle_click(row, column)
        self.update_board(pieces)
        self.update_statistics()
