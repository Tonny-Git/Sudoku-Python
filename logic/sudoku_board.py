class SudokuBoard:
    def __init__(self):
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
        self.board_completed = [
            [7, 8, 5, 4, 3, 9, 1, 2, 6],
            [6, 1, 2, 8, 7, 5, 3, 4, 9],
            [4, 9, 3, 6, 2, 1, 5, 7, 8],
            [8, 5, 7, 9, 4, 3, 2, 6, 1],
            [2, 6, 1, 7, 5, 8, 9, 3, 4],
            [9, 3, 4, 1, 6, 2, 7, 8, 5],
            [5, 7, 8, 3, 9, 4, 6, 1, 2],
            [1, 2, 6, 5, 8, 7, 4, 9, 3],
            [3, 4, 9, 2, 1, 6, 8, 5, 7]
        ]

    def create_board(self):
        pass

    def create_puzzle(self):
        pass

    def add_value(self, value, row, col):
        self.board[row][col] = value
        self.check_if_completed()

    def check_if_completed(self):
        if not any(0 in x for x in self.board):
            print(True)
        else:
            print(False)
            for x in range(9):
                print(f"board: {self.board[x]}  completed board: {self.board_completed[x]} \n")
                #print(f"row {x}: ", self.board[x] == self.board_completed[x])
            #print(f"full: {self.board == self.board_completed} \n\n")