from gomoku.game import Game
import pygame

if __name__ == '__main__':
    newGame = Game((600, 600), 10)
    newGame.game_loop()
    # print(pygame.font.get_fonts())
