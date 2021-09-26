import tkinter as tk
from settings.settings import Settings
from logic.sudoku_board import SudokuBoard

class SudokuGrid:

    def __init__(self, root):
        self.root = root
        self.state = "ongoing"
        self.sudokuBoard = SudokuBoard()
        self.cubes = []
        # Add a state to keep track of error message or victory message
        #self.state = None
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
                    self.cubes.append("None")
                else:
                    canvas = tk.Canvas(inner_frame, bg='White', width=(Settings.window_width/9), height=(Settings.window_height/9), highlightbackground='black', highlightthickness=0.5, highlightcolor="#0858d1")
                    canvas.bind("<Key>", lambda event, row=i+row*3, col=j+column*3: self.key(event, row, col))
                    canvas.bind("<Button-1>", self.callback)
                    canvas.bind("<FocusIn>", self.cube_focus)
                    canvas.bind("<FocusOut>", self.cube_lose_focus)
                    canvas.grid(row=i, column=j)
                    self.cubes.append(canvas)
                    
    def key(self, event, row, col):
        if event.char in Settings.numbers_char and self.state != "completed":
            event.widget.delete("all")
            event.widget.create_text(Settings.window_width/18, Settings.window_width/18, text=event.char, font="Times 25")
            solved = self.sudokuBoard.add_value(int(event.char), row, col)
            if solved == "Error":
                print("Error in board!")
                self.show_error()
            elif solved:
                #Fix this later
                print("Puzzle is solved!")
                self.state = "completed"
                self.victory_screen()
        elif event.char == "\x08":
            event.widget.delete("all")
            self.sudokuBoard.add_value(0, row, col)

    def callback(self, event):
        event.widget.focus_set()

    def cube_focus(self, event):
        if self.state != "completed":
            event.widget.configure(bg="#bae0f7")
    
    def cube_lose_focus(self, event):
        if self.state != "completed":
            event.widget.configure(bg="white")

    def victory_screen(self):
        frame = tk.Frame(self.root, width=(Settings.window_width/4), height=(Settings.window_height/10), highlightbackground='green', highlightthickness=0.5)
        frame.place(x=Settings.window_width/2-Settings.window_width/8, y=Settings.window_width/2-Settings.window_height/20)
        label = tk.Label(frame, text=f"Puzzle solved!", font=30)
        label.place(relx=0.1, rely=0.3)
        for cube in self.cubes:
            if cube != "None":
                cube.configure(bg="green")
                #cube.configure(state="disabled")
    
    # implement later
    def show_error(self):
        error_pos = self.sudokuBoard.get_difference()
        for pos in error_pos:
            #self.cubes[pos[0]][pos[1]].configure(bg="red")
            #print("pos: ", pos)
            #print("both: ", pos[0], pos[1])
            print(self.cubes[pos[0]*10 + pos[1]])
            #print(self.cubes)
            pass
            
        

# Temporary thoughts: 
# Move the canvas into it's own class named inputBox? 
# Change label in cube frames to create text.
# 
