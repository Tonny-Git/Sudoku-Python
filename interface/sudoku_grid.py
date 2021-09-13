import tkinter as tk
from settings.settings import Settings

class SudokuGrid:

    def __init__(self, root):
        self.root = root
        #Temporary, make into a function later!
        self.board = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]

        self.canvas = None
        self.build_board()

    def build_board(self):
        self.main_frame()

    def main_frame(self):
        print(self.canvas)
        frame = tk.Frame(self.root, width=Settings.window_width, height=Settings.window_height, highlightbackground='black', highlightthickness=0.5)
        frame.pack()
        self.inner_frames(frame)

    def inner_frames(self, main_frame):
        for i in range(0 , 3):
            for j in range(0, 3):
                frame = tk.Frame(main_frame, width=(Settings.window_width/3), height=(Settings.window_height/3), highlightbackground='black', highlightthickness=0.5)
                frame.grid(row=i, column=j)
                self.cube_frames(frame, i, j)

    def cube_frames(self, inner_frame, row, column):
        for i in range(0 , 3):
            for j in range(0, 3):

                if self.board[i+row*3][j+column*3] != 0:
                    frame = tk.Frame(inner_frame, width=(Settings.window_width/9+2), height=(Settings.window_height/9+2), highlightbackground='black', highlightthickness=0.5)
                    frame.grid(row=i, column=j)
                    label = tk.Label(frame, text=f"{self.board[i+row*3][j+column*3]}", font=30)
                    label.place(relx=0.4, rely=0.3)
                else:
                    canvas = tk.Canvas(inner_frame, bg='White', width=(Settings.window_width/9), height=(Settings.window_height/9), highlightbackground='black', highlightthickness=0.5)
                    canvas.bind("<Key>", self.key)
                    canvas.bind("<Button-1>", self.callback)
                    canvas.grid(row=i, column=j)
                    
    def key(self, event):
        if event.char in Settings.numbers_char:
            event.widget.delete("all")
            event.widget.create_text(Settings.window_width/18, Settings.window_width/18, text=event.char, font="Times 25")
        elif event.char == "\x08":
            event.widget.delete("all")

    def callback(self, event):
        event.widget.focus_set()