import math
import random

import numpy as np


class AI:
    def __init__(self, COLUMN_COUNT, ROW_COUNT):
        self.ROW_COUNT = ROW_COUNT
        self.COLUMN_COUNT = COLUMN_COUNT
        self.humanPiece = 1
        self.AiPiece = 2

    # def get_huScore(self, board, r, c):
    #     lr = 0
    #     hr = self.ROW_COUNT-1
    #     lc = 0
    #     hc = self.COLUMN_COUNT-1
    #     if r-3 > 0:
    #         lr = r-3
    #     if r+3 < self.ROW_COUNT-1:
    #         hr = r+3
    #     if c-3 > 0:
    #         lc = c-3
    #     if c+3 < self.COLUMN_COUNT-1:
    #         hc = c+3
    #     score = 0
    #     for i in range(lr, hr):
    #         if board[i][c] != 0:
    #             score+=1
    #     for i in range(lc, hc):
    #         if board[r][i] != 0:
    #             score+=1
    #
    #     for i in range(3):
    #         nr1 = r+i+1
    #         nr2 = r-i-1
    #         nc1 = c+i+1
    #         nc2 = c-i-1
    #         if(nr1 > hr):
    #             nr1 = hr
    #         if(nr2 < lr):
    #             nr2 = lr
    #         if(nc1 > hc):
    #             nc1 = hc
    #         if(nc2 < lr):
    #             nc2 = lc
    #
    #         if board[nr1][nc1] != 0:
    #             score+=1
    #         if board[nr2][nc2] != 0:
    #             score+=1
    #         if board[nr1][nc2] != 0:
    #             score+=1
    #         if board[nr2][nc1] != 0:
    #             score+=1
    #
    #     return score

    def is_terminal(self, r, c):
        if r>=0 and r<self.ROW_COUNT and c>=0 and c<self.COLUMN_COUNT:
            return True
        else:
            return False

    def get_available_cells_incomplete(self, board):
        valid_locations = []
        board1 = board.copy()
        fx = [+0, +0, +1, -1, -1, +1, -1, +1]
        fy = [-1, +1, +0, +0, +1, +1, -1, -1]
        for r in range(self.ROW_COUNT):
            for c in range(self.COLUMN_COUNT):
                if board[r][c] != 0:
                    for i in range(8):
                        if self.is_terminal(r+fx[i], c+fy[i]):
                            if board1[r+fx[i]][c+fy[i]] == 0:
                                board1[r+fx[i]][c+fy[i]] = 1
                                valid_locations.append([r+fx[i], c+fy[i]])
        return valid_locations

    def get_available_cells(self, board):
        valid_cells = []
        for r in range(self.ROW_COUNT):
            for c in range(self.COLUMN_COUNT):
                if board[r][c] == 0:
                    valid_cells.append([r, c])
        return valid_cells

    def drop_piece(self, board, row, col, piece):
        board[row][col] = piece

    def evaluate_window(self, window, piece):
        score = 0
        opp_piece = self.humanPiece
        if piece == self.humanPiece:
            opp_piece = self.AiPiece
        if window.count(piece) == 5:
            score += 100
        elif window.count(piece) == 4 and window.count(0) == 1:
            score += 5
        # elif window[0] == 0 and window[4] == 0 and window.count(piece) == 3:
        #     score += 5
        elif window.count(piece) == 3 and window.count(0) == 2:
            score += 2
        if window.count(opp_piece) == 4 and window.count(0) == 1:
            score -= 4
        # elif window[0] == 0 and window[4] == 0 and window.count(opp_piece) == 3:
        #     score -= 100

        return score

    def intermediate_score(self, board, piece):
        score = 0
        # Score center column
        center_col = [int(i) for i in list(board[:, self.COLUMN_COUNT//2])]
        # print(center_col)
        center_count = center_col.count(piece)
        score += center_count * 3
        #
        # ## Score center column
        # center_row = [int(i) for i in list(board[self.ROW_COUNT//2, :])]
        # # print(center_row)
        # center_count = center_row.count(piece)
        # score += center_count * 3
        #Score Horizontal
        for r in range(self.ROW_COUNT):
            row_array = [int(i) for i in list(board[r,:])]
            for c in range(self.COLUMN_COUNT-4):
                window = row_array[c:c+5]
                score += self.evaluate_window(window, piece)

        ## Score Vertical
        for c in range(self.COLUMN_COUNT):
            col_array = [int(i) for i in list(board[:,c])]
            for r in range(self.ROW_COUNT-4):
                window = col_array[r:r+5]
                score += self.evaluate_window(window, piece)

        ## Score posiive sloped diagonal
        for r in range(self.ROW_COUNT-4):
            for c in range(self.COLUMN_COUNT-4):
                window = [board[r+i][c+i] for i in range(5)]
                score += self.evaluate_window(window, piece)

        for r in range(self.ROW_COUNT-4):
            for c in range(self.COLUMN_COUNT-4):
                window = [board[r+4-i][c+i] for i in range(5)]
                score += self.evaluate_window(window, piece)
        # print(f'Score: {score}')
        return score

    def winning_move(self, board, piece):
        # case: 1 Horizontal check
        for c in range(self.COLUMN_COUNT - 4):
            for r in range(self.ROW_COUNT):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and \
                        board[r][c + 3] == piece and board[r][c + 4] == piece:
                    return True
        # case: 2 Vertical check
        for r in range(self.ROW_COUNT - 4):
            for c in range(self.COLUMN_COUNT):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and \
                        board[r + 3][c] == piece and board[r + 4][c] == piece:
                    return True
        # case: 3 Negatively sloped diagonals check
        for c in range(self.COLUMN_COUNT - 4):
            for r in range(self.ROW_COUNT - 4):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                        board[r + 3][c + 3] == piece and board[r + 4][c + 4] == piece:
                    return True
        # case: 4 positively sloped diagonals check
        for c in range(self.COLUMN_COUNT - 4):
            for r in range(4, self.ROW_COUNT):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                        board[r - 3][c + 3] == piece and board[r - 4][c + 4] == piece:
                    return True
        return False

    def minimax(self, board, depth, alpha, beta, turnAI):
        availableCells = self.get_available_cells_incomplete(board)
        if self.winning_move(board, self.AiPiece):
            return None, 100*depth
        elif self.winning_move(board, self.humanPiece):
            return None, -100*depth
        elif len(availableCells) == 0:
            return None, 0
        elif depth == 0:
            # if turnAI:
            #     return None, self.intermediate_score(board, self.AiPiece)
            # else:
            #     return None, self.intermediate_score(board, self.humanPiece)
            return None, 0

        if turnAI:
            value = -math.inf
            cell = random.choice(availableCells)
            for cel in availableCells:
                b_copy = board.copy()
                self.drop_piece(b_copy, cel[0], cel[1], self.AiPiece)
                new_score = self.minimax(b_copy, depth-1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    cell = cel
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return cell, value

        else:
            value = math.inf
            cell = random.choice(availableCells)
            for cel in availableCells:
                b_copy = board.copy()
                self.drop_piece(b_copy, cel[0], cel[1], self.humanPiece)
                new_score = self.minimax(b_copy, depth-1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    cell = cel
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return cell, value

    def move(self, board):
        cell, value = self.minimax(board, 5, -math.inf, math.inf, True)
        print(value)
        return cell

# if __name__ == '__main__':
#     board = np.zeros((9, 9))
#     ai = AI(board,9,9)
#     board[5][5] = 1
#     print(ai.get_available_cells(board))






