import numpy as np

PLAYER_PIECE = 1
AI_PIECE = 2
EMPTY = 0
COLUMN_COUNT = 4
ROW_COUNT = 4
WINDOW_LENGTH = 2


def get_rows(grid):
    return [[c for c in r] for r in grid]


def get_cols(grid):
    return zip(*grid)


def get_backward_diagonals(grid):
    b = [None] * (len(grid) - 1)
    grid = [b[i:] + r + b[:i] for i, r in enumerate(get_rows(grid))]
    return [[c for c in r if c is not None] for r in get_cols(grid)]


def get_forward_diagonals(grid):
    b = [None] * (len(grid) - 1)
    grid = [b[:i] + r + b[i:] for i, r in enumerate(get_rows(grid))]
    return [[c for c in r if c is not None] for r in get_cols(grid)]


def huristic_score(board, piece):
    rcount = 0
    colcount = 0
    v1Count = 0
    v2Count = 0
    if piece == 2:
        return 0

    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r, :])]
        count = 0
        for i in range(len(row_array)-1):
            if row_array[i] == piece:
                if row_array[i+1] == 2:
                    count +=1
                elif row_array[i+1] == 0:
                    count+=1
                else:
                    count -= 2
        if(rcount < count):
            rcount = count

    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:, c])]
        count = 0
        for i in range(len(col_array)-1):
            if col_array[i] == piece:
                if col_array[i+1] == 2:
                    count +=2
                elif col_array[i+1] == 0:
                    count+=1
                else:
                    count -= 2
        if(colcount < count):
            colcount = count

    v1 = get_backward_diagonals(board)
    for i in range(4, len(v1)-4):
        count = 0
        for j in range(len(v1[i])-1):
            if v1[i][j+1] == 2:
                    count +=2
            elif v1[i][j+1] == 0:
                count+=1
            else:
                count -= 2
        if(v1Count < count):
            v1Count = count

    v2 = get_forward_diagonals(board)
    for i in range(4, len(v2)-4):
        count = 0
        for j in range(len(v2[i])-1):
            if v2[i][j+1] == 2:
                    count +=2
            elif v2[i][j+1] == 0:
                count+=1
            else:
                count -= 2
        if(v2Count < count):
            v2Count = count

    # print(rcount, colcount, v1Count, v2Count)
    score = max(rcount, colcount, v1Count, v2Count)
    # print(score)
    return score
