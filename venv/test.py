import numpy as np

board = np.zeros((4, 4))
board[1][1]=1
board[2][2]=2
board[3][3]=3
board[3][2] = 5

# for r in range(4):
#     print(board)
#     row_array = [int(i) for i in list(board[r,:])]
#     print(row_array)
#     col_arr = [int(i) for i in list(board[:,r])]
#     print(col_arr)


def get_huScore(board, r, c):
        lr = 0
        hr = 3
        lc = 0
        hc = 3
        if r-3 > 0:
            lr = r-3
        if r+3 < 3:
            hr = r+3
        if c-3 > 0:
            lc = c-3
        if c+3 < 3:
            hc = c+3
        print(lc)
        print(hc)
        l = min(hc-lc, hr-lr)+1
        arr = [board[i][i] for i in range(l)]
        print(arr)

print(board)
get_huScore(board, 1, 0)
