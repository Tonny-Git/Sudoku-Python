import tkinter as tk
from interface.sudoku_grid import SudokuGrid
from settings.settings import Settings

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.window_settings()
        self.create_game()

    def window_settings(self):
        self.root.title("Sudoku")
        self.root.geometry(f"{Settings.window_width+30}x{Settings.window_height+30}")

    def create_game(self):
        SudokuGrid(self.root)