import numpy as np

ROW_COUNT = 9
COLUMN_COUNT = 9


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid(board, row, col):
    return board[row][col] == 0


def winning_move(board, piece):
    # case: 1 Horizontal check
    for c in range(COLUMN_COUNT - 4):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and \
                    board[r][c + 3] == piece and board[r][c + 4] == piece:
                return True
    # case: 2 Vertical check
    for r in range(ROW_COUNT - 4):
        for c in range(COLUMN_COUNT):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and \
                    board[r + 3][c] == piece and board[r + 4][c] == piece:
                return True
    # case: 3 Negatively sloped diagonals check
    for c in range(COLUMN_COUNT - 4):
        for r in range(ROW_COUNT - 4):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                    board[r + 3][c + 3] == piece and board[r + 4][c + 4] == piece:
                return True
    # case: 4 positively sloped diagonals check
    for c in range(COLUMN_COUNT - 4):
        for r in range(4, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                    board[r - 3][c + 3] == piece and board[r - 4][c + 4] == piece:
                return True


board = create_board()
print(board)
gameOver = False
turn = 0

while not gameOver:
    if turn == 0:
        rowSelection = int(input("Make your row selection (1-9): ")) - 1
        colSelection = int(input("Make your column selection (1-9): ")) - 1
        if is_valid(board, rowSelection, colSelection):
            drop_piece(board, rowSelection, colSelection, 1)
        else:
            print("invalid turn")
            continue
        if winning_move(board, 1):
            print("Player 1 win!!")
            gameOver = True

    else:
        rowSelection = int(input("Make your row selection (1-9): ")) - 1
        colSelection = int(input("Make your column selection (1-9): ")) - 1
        if is_valid(board, rowSelection, colSelection):
            drop_piece(board, rowSelection, colSelection, 2)
        else:
            print("invalid turn")
            continue
        if winning_move(board, 2):
            print("Player 2 win!!")
            gameOver = True

    print(board)
    turn += 1
    turn %= 2
