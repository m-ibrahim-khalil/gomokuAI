import numpy as np

from minimax_algorithm import AI

board = np.zeros((7, 7))
board[3][1]=1
board[2][1]=1
board[1][1]=1
board[0][1]=1
board[4][1] = 1
board[5][5] = 2
board[3][3] = 1
board[3][2]=1
board[2][2]=1
board[1][3]=1
board[0][4]=1
board[4][5] = 1
board[5][6] = 2
board[3][6] = 1
board[1][4]=1
board[2][5] = 1
board[5][6] = 2
board[6][6] = 1

ai = AI(7, 7)
print(ai.winning_move(board, 1))
print(len(ai.get_available_cells_incomplete(board)))
