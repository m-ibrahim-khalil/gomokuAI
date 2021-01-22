import math

from gomoku.board import Board
from gomoku.players import HumanPlayer, AiPlayer


class Game:
    def __init__(self):
        self.Board1 = Board(9, 9)
        self.player1 = HumanPlayer(1)
        self.player2 = AiPlayer(2)

    def minimax(self, depth, alpha, beta, turnAI, available_cell):
        if self.Board1.winning_move(self.player2.piece):
            return None, 100*depth
        elif self.Board1.winning_move(self.player1.piece):
            return None, -100*depth
        elif len(available_cell) == 0:
            return None, 0
        elif depth == 0:
            return None, 0

        if turnAI:
            value = -math.inf
            cell = (5, 5)
            for cel in available_cell:
                self.Board1.drop_piece(cel[0], cel[1], self.player2.piece)
                available_cell.add((cel[0], cel[1]))
                available_cell_copy = self.Board1.get_available_cells_copy(cel[0], cel[1], available_cell.copy())
                new_score = self.minimax(depth-1, alpha, beta, False, available_cell_copy)[1]
                self.Board1.remove_piece(cel[0], cel[1])
                if new_score > value:
                    value = new_score
                    cell = cel
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return cell, value

        else:
            value = math.inf
            cell = None
            for cel in available_cell:
                self.Board1.drop_piece(cel[0], cel[1], self.player1.piece)
                available_cell_copy = self.Board1.get_available_cells_copy(cel[0], cel[1], available_cell.copy())
                new_score = self.minimax(depth-1, alpha, beta, True, available_cell_copy)[1]
                self.Board1.remove_piece(cel[0], cel[1])
                if new_score < value:
                    value = new_score
                    cell = cel
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return cell, value

    def get_cell(self, available_cell):
        cell, value = self.minimax(5, -math.inf, math.inf, True, available_cell.copy())
        return cell[0], cell[1]

    def game_loop(self):
        gameOver = False
        turn = 0
        available_cell = {(5, 5)}
        while not gameOver:
            if turn == 0:
                row, col = self.player1.get_cell()
                if self.Board1.is_valid_cell(row, col):
                    self.Board1.drop_piece(row, col, self.player1.piece)
                    available_cell.add((row, col))
                    available_cell = self.Board1.get_available_cells_copy(row, col, available_cell)
                else:
                    print("invalid turn")
                    continue
                if self.Board1.winning_move(self.player1.piece):
                    print("Player 1 win!!")
                    gameOver = True
            else:  # Ai
                row, col = self.get_cell(available_cell)
                if self.Board1.is_valid_cell(row, col):
                    self.Board1.drop_piece(row, col, self.player2.piece)
                    available_cell.add((row, col))
                    available_cell = self.Board1.get_available_cells_copy(row, col, available_cell)
                else:
                    print("invalid turn")
                    continue
                if self.Board1.winning_move(self.player2.piece):
                    print("Player 2 win!!")
                    gameOver = True

            print(self.Board1.board)
            turn += 1
            turn %= 2
