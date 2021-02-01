PLAYER_PIECE = 1
AI_PIECE = 2
EMPTY = 0
COLUMN_COUNT = 10
ROW_COUNT = 10
WINDOW_LENGTH = 5


def evaluate_window(window, piece):
    score = 0
    opp_piece = PLAYER_PIECE
    if piece == PLAYER_PIECE:
        opp_piece = AI_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score


def huristic_score(board, piece):
    score = 0
    #Horizontal
    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(COLUMN_COUNT - 4):
            window = row_array[c:c + WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    #Vertical
    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(ROW_COUNT - 4):
            window = col_array[r:r + WINDOW_LENGTH]
            score += evaluate_window(window, piece)

   # diagonal
    for r in range(ROW_COUNT - 4):
        for c in range(COLUMN_COUNT - 4):
            window = [board[r + i][c + i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    for r in range(ROW_COUNT - 4):
        for c in range(COLUMN_COUNT - 4):
            window = [board[r + 4 - i][c + i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    return score
