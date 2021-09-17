import tkinter as tk
from settings.settings import Settings
from logic.sudoku_board import SudokuBoard

class SudokuGrid:

    def __init__(self, root):
        self.root = root
        self.sudokuBoard = SudokuBoard()

        self.canvas = None
        self.build_board()

    def build_board(self):
        self.main_frame()

    def main_frame(self):
        frame = tk.Frame(self.root, width=Settings.window_width, height=Settings.window_height, highlightbackground='black', highlightthickness=0.5, highlightcolor="black")
        frame.pack()
        self.inner_frames(frame)

    def inner_frames(self, main_frame):
        for i in range(0 , 3):
            for j in range(0, 3):
                frame = tk.Frame(main_frame, width=(Settings.window_width/3), height=(Settings.window_height/3), highlightbackground='black', highlightthickness=0.5, highlightcolor="black")
                frame.grid(row=i, column=j)
                self.cube_frames(frame, i, j)

    def cube_frames(self, inner_frame, row, column):
        for i in range(0 , 3):
            for j in range(0, 3):

                if self.sudokuBoard.board[i+row*3][j+column*3] != 0:
                    frame = tk.Frame(inner_frame, width=(Settings.window_width/9+2), height=(Settings.window_height/9+2), highlightbackground='black', highlightthickness=0.5)
                    frame.grid(row=i, column=j)
                    label = tk.Label(frame, text=f"{self.sudokuBoard.board[i+row*3][j+column*3]}", font=30)
                    label.place(relx=0.4, rely=0.3)
                else:
                    canvas = tk.Canvas(inner_frame, bg='White', width=(Settings.window_width/9), height=(Settings.window_height/9), highlightbackground='black', highlightthickness=0.5, highlightcolor="#0858d1")
                    canvas.bind("<Key>", lambda event, row=i+row*3, col=j+column*3: self.key(event, row, col))
                    canvas.bind("<Button-1>", self.callback)
                    canvas.bind("<FocusIn>", self.cube_focus)
                    canvas.bind("<FocusOut>", self.cube_lose_focus)
                    canvas.grid(row=i, column=j)
                    
    def key(self, event, row, col):
        #print(f"row: {row}   col: {col}")
        if event.char in Settings.numbers_char:
            event.widget.delete("all")
            event.widget.create_text(Settings.window_width/18, Settings.window_width/18, text=event.char, font="Times 25")
            self.sudokuBoard.add_value(event.char, row, col)
        elif event.char == "\x08":
            event.widget.delete("all")
            self.sudokuBoard.add_value(0, row, col)

    def callback(self, event):
        event.widget.focus_set()

    def cube_focus(self, event):
        event.widget.configure(bg="#bae0f7")
        pass
    
    def cube_lose_focus(self, event):
        event.widget.configure(bg="white")
        pass

# Temporary thoughts: 
# Move the canvas into it's own class named inputBox? 
# Change label in cube frames to create text.
# 
