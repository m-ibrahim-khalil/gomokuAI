from gomoku.game import Game
import pygame

if __name__ == '__main__':
    newGame = Game((700, 700), 10)
    newGame.game_loop()
    # print(pygame.font.get_fonts())
