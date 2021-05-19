from tkinter import PhotoImage
import os


class PieceImage:
    img_white = None
    img_black = None
    img_player_x = None
    img_player_o = None
    img_player_x_selected = None
    img_player_o_selected = None
    img_player_x_q = None
    img_player_o_q = None
    img_player_x_q_selected = None
    img_player_o_q_selected = None
    img_player_x_turn = None
    img_player_o_turn = None

    def __init__(self):
        self.img_white = PhotoImage(file=os.path.join("images", 'white.png'))
        self.img_black = PhotoImage(file=os.path.join("images", 'black.png'))
        self.img_player_x = PhotoImage(file=os.path.join("images", 'red.png'))
        self.img_player_o = PhotoImage(file=os.path.join("images", 'blue.png'))
        self.img_player_x_selected = PhotoImage(file=os.path.join("images", 'red-selected.png'))
        self.img_player_o_selected = PhotoImage(file=os.path.join("images", 'blue-selected.png'))
        self.img_player_x_q = PhotoImage(file=os.path.join("images", 'red-queen.png'))
        self.img_player_o_q = PhotoImage(file=os.path.join("images", 'blue-queen.png'))
        self.img_player_x_q_selected = PhotoImage(file=os.path.join("images", 'red-queen-selected.png'))
        self.img_player_o_q_selected = PhotoImage(file=os.path.join("images", 'blue-queen-selected.png'))
        self.img_player_x_turn = PhotoImage(file=os.path.join("images", 'red-turn.png'))
        self.img_player_o_turn = PhotoImage(file=os.path.join("images", 'blue-turn.png'))

    def get_image(self, piece):
        if piece == 'w':
            return self.img_white
        elif piece == 'b':
            return self.img_black
        elif piece == 'x':
            return self.img_player_x
        elif piece == 'o':
            return self.img_player_o
        elif piece == 'xs':
            return self.img_player_x_selected
        elif piece == 'os':
            return self.img_player_o_selected
        elif piece == 'xq':
            return self.img_player_x_q
        elif piece == 'oq':
            return self.img_player_o_q
        elif piece == 'xsq':
            return self.img_player_x_q_selected
        elif piece == 'osq':
            return self.img_player_o_q_selected
        elif piece == 'xt':
            return self.img_player_x_turn
        elif piece == 'ot':
            return self.img_player_o_turn
        else:
            raise ValueError('Error image not found! ')
