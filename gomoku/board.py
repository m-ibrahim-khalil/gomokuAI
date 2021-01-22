import numpy as np


class Board:
    def __init__(self, row_count, col_count):
        self.ROW_COUNT = row_count
        self.COLUMN_COUNT = col_count
        self.board = np.zeros((self.ROW_COUNT, self.COLUMN_COUNT))

    # def create_board(self):
    #     self.board = np.zeros((self.ROW_COUNT, self.COLUMN_COUNT))
        # return self.board

    def is_valid_cell(self, row, col):
        if row >= self.ROW_COUNT or row < 0 or col >= self.COLUMN_COUNT or col < 0:
            return False
        return self.board[row][col] == 0

    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece

    def remove_piece(self, row, col):
        self.board[row][col] = 0

    def is_terminal(self, r, c):
        if 0 <= r < self.ROW_COUNT and 0 <= c < self.COLUMN_COUNT:
            return True
        else:
            return False

    # def get_available_cells1(self, board, r, c):
    #     fx = [+0, +0, +1, -1, -1, +1, -1, +1]
    #     fy = [-1, +1, +0, +0, +1, +1, -1, -1]
    #     for i in range(8):
    #         if self.is_terminal(r+fx[i], c+fy[i]):
    #             if board[r+fx[i]][c+fy[i]] == 0:
    #                 self.available_cell.add((r+fx[i], c+fy[i]))
    #     # self.available_cell.remove((r, c))

    def get_available_cells_copy(self, r, c, available_cell):
        fx = [+0, +0, +1, -1, -1, +1, -1, +1]
        fy = [-1, +1, +0, +0, +1, +1, -1, -1]
        for i in range(8):
            if self.is_terminal(r+fx[i], c+fy[i]):
                if self.board[r+fx[i]][c+fy[i]] == 0:
                    available_cell.add((r+fx[i], c+fy[i]))
        available_cell.remove((r, c))
        return available_cell

    # def get_available_cells(self):
    #     valid_locations = []
    #     board1 = self.board.copy()
    #     fx = [+0, +0, +1, -1, -1, +1, -1, +1]
    #     fy = [-1, +1, +0, +0, +1, +1, -1, -1]
    #     for r in range(self.ROW_COUNT):
    #         for c in range(self.COLUMN_COUNT):
    #             if self.board[r][c] != 0:
    #                 for i in range(8):
    #                     if self.is_terminal(r+fx[i], c+fy[i]):
    #                         if board1[r+fx[i]][c+fy[i]] == 0:
    #                             board1[r+fx[i]][c+fy[i]] = 1
    #                             valid_locations.append([r+fx[i], c+fy[i]])
    #     return valid_locations

    def winning_move(self, piece):
        # case: 1 Horizontal check
        for c in range(self.COLUMN_COUNT - 4):
            for r in range(self.ROW_COUNT):
                if self.board[r][c] == piece and self.board[r][c + 1] == piece and self.board[r][c + 2] == piece and \
                        self.board[r][c + 3] == piece and self.board[r][c + 4] == piece:
                    return True
        # case: 2 Vertical check
        for r in range(self.ROW_COUNT - 4):
            for c in range(self.COLUMN_COUNT):
                if self.board[r][c] == piece and self.board[r + 1][c] == piece and self.board[r + 2][c] == piece and \
                        self.board[r + 3][c] == piece and self.board[r + 4][c] == piece:
                    return True
        # case: 3 Negatively sloped diagonals check
        for c in range(self.COLUMN_COUNT - 4):
            for r in range(self.ROW_COUNT - 4):
                if self.board[r][c] == piece and self.board[r + 1][c + 1] == piece and self.board[r + 2][c + 2] == piece and \
                        self.board[r + 3][c + 3] == piece and self.board[r + 4][c + 4] == piece:
                    return True
        # case: 4 positively sloped diagonals check
        for c in range(self.COLUMN_COUNT - 4):
            for r in range(4, self.ROW_COUNT):
                if self.board[r][c] == piece and self.board[r - 1][c + 1] == piece and self.board[r - 2][c + 2] == piece and \
                        self.board[r - 3][c + 3] == piece and self.board[r - 4][c + 4] == piece:
                    return True
