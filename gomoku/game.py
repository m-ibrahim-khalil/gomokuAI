import math
import pygame
from pygame.locals import *

from gomoku.board import Board
from gomoku.players import HumanPlayer, AiPlayer
from gui.gui import GUI


class Game:
    def __init__(self, screen_size):
        self.Board1 = Board(15, 15)
        self.player1 = HumanPlayer(1)
        self.player2 = AiPlayer(2)
        self.gui = GUI(screen_size, 15)

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
        self.gui.run(self.Board1.board)
        available_cell = {(5, 5)}
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("> exit")
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    col = int((mouse_position[0] / self.gui.spacing) - 0.5)
                    row = int((mouse_position[1] / self.gui.spacing) - 0.5)
                    print(row, col)
                    if turn == 0:
                        if self.Board1.is_valid_cell(row, col):
                            self.Board1.drop_piece(row, col, self.player1.piece)
                            available_cell.add((row, col))
                            available_cell = self.Board1.get_available_cells_copy(row, col, available_cell)
                            # print(self.Board1.board)
                            self.gui.run(self.Board1.board)
                            turn = 1
                        else:
                            print("invalid turn")
                            continue
                        if self.Board1.winning_move(self.player1.piece):
                            print("Player 1 win!!")
                            gameOver = True

                    # elif turn == 1 and not gameOver:  # Ai
                    #     # row, col = self.get_cell(available_cell)
                    #     # print(row, col)
                    #     if self.Board1.is_valid_cell(row, col):
                    #         self.Board1.drop_piece(row, col, self.player2.piece)
                    #         available_cell.add((row, col))
                    #         available_cell = self.Board1.get_available_cells_copy(row, col, available_cell)
                    #         # print(self.Board1.board)
                    #         self.gui.run(self.Board1.board)
                    #         turn = 0
                    #     else:
                    #         print("invalid turn")
                    #         continue
                    #     if self.Board1.winning_move(self.player2.piece):
                    #         print("Congrats Ai win!!")
                    #         gameOver = True

            if turn == 1 and not gameOver:  # Ai
                row, col = self.get_cell(available_cell)
                print(row, col)
                if self.Board1.is_valid_cell(row, col):
                    self.Board1.drop_piece(row, col, self.player2.piece)
                    available_cell.add((row, col))
                    available_cell = self.Board1.get_available_cells_copy(row, col, available_cell)
                    print(self.Board1.board)
                    self.gui.run(self.Board1.board)
                    turn = 0
                else:
                    print("invalid turn")
                    continue
                if self.Board1.winning_move(self.player2.piece):
                    print("Congrats Ai win!!")
                    gameOver = True

            if gameOver:
                pygame.time.wait(3000)
                break

