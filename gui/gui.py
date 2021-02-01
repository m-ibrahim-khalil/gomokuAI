import time
import sys
import numpy
import pygame
from pygame.locals import *

from gomoku.board import Board

background_image = 'desk.png'
white_image = 'white1.png'
black_image = 'black1.png'
RED = (255, 0, 0)


class GUI:
    def __init__(self, screen_size, board_size=15):
        pygame.init()
        self._screen_size = screen_size
        self._board_size = board_size
        self.spacing = int(self._screen_size[1] / (board_size + 1))
        self._screen = None
        self._background = None
        self._stone_black = None
        self._stone_white = None
        # self.myfont = pygame.font.SysFont("ubuntumono", 60)
        self.myfont = pygame.font.Font("/usr/share/fonts/truetype/malayalam/Suruma.ttf", 55)

    def run(self, board):
        self._screen = pygame.display.set_mode(self._screen_size, 0, 32)
        self._background = pygame.image.load(background_image).convert()
        self._stone_black = pygame.image.load(black_image).convert_alpha()
        self._stone_white = pygame.image.load(white_image).convert_alpha()
        self._stone_black = pygame.transform.smoothscale(self._stone_black, (self.spacing, self.spacing))
        self._stone_white = pygame.transform.smoothscale(self._stone_white, (self.spacing, self.spacing))
        pygame.display.set_caption('GOMOKU')
        self._paint_background()
        self._read(board)
        pygame.display.update()

    def _paint_background(self):
        self._screen.blit(self._background, (0, 0))
        black_color = (0, 0, 0)

        for i in range(1, self._board_size + 1):
            start_horizontal = (self.spacing, i * self.spacing)
            end_horizontal = (self._screen_size[1] - self.spacing, i * self.spacing)
            start_vertical = (i * self.spacing, self.spacing)
            end_vertical = (i * self.spacing, self._screen_size[1] - self.spacing)

            if i == 1 or i == self._board_size + 1:
                pygame.draw.line(self._screen, black_color, start_horizontal, end_horizontal, 3)
                pygame.draw.line(self._screen, black_color, start_vertical, end_vertical, 3)
            else:
                pygame.draw.line(self._screen, black_color, start_horizontal, end_horizontal, 2)
                pygame.draw.line(self._screen, black_color, start_vertical, end_vertical, 2)

        if self._board_size % 2 == 1:
            mid = (self._board_size + 1) / 2
            start_pos = (self.spacing * int(mid) - 2, self.spacing * int(mid) - 2)
            size = (6, 6)
            pygame.draw.rect(self._screen, black_color, pygame.rect.Rect(start_pos, size))

    def _move(self, player, action):
        position = (int((action[1] + 0.5) * self.spacing), int((action[0] + 0.5) * self.spacing))
        if player == 1:
            self._screen.blit(self._stone_black, position)
        elif player == 2:
            self._screen.blit(self._stone_white, position)

    def _read(self, new_board):
        self._paint_background()
        self._update_read = False
        for row in range(self._board_size):
            for col in range(self._board_size):
                if new_board[row][col] == 1:
                    self._move(1, (row, col))
                elif new_board[row][col] == 2:
                    self._move(2, (row, col))

    def winner(self, who):
        if who == 1:
            label = self.myfont.render("Congrats Human wins!!", True, RED)
            self._screen.blit(label, (40, 10))
        elif who == 2:
            label = self.myfont.render("Congrats Ai wins!!", True, RED)
            self._screen.blit(label, (40, 10))
        else:
            label = self.myfont.render("Tie!", True, RED)
            self._screen.blit(label, (40, 10))
        pygame.display.update()

    def turn (self, who):
        if who == 1:
            label = self.myfont.render("Human turn", True, RED)
            self._screen.blit(label, (40, 10))
        else:
            label = self.myfont.render("Ai turn", True, RED)
            self._screen.blit(label, (40, 10))
        pygame.display.update()
