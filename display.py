import math

import pygame

from core import ROW_COUNT, COLUMN_COUNT, HUMAN_PIECE, AI_PIECE

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE / 2 - 5)

class Display:

    def __init__(self):
        self.screen = pygame.display.set_mode(size)
        self.myfont = pygame.font.SysFont("monospace", 75)


    def draw_board(self, board):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(self.screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(self.screen, BLACK, (
                int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if board[r][c] == HUMAN_PIECE:
                    pygame.draw.circle(self.screen, RED, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
                elif board[r][c] == AI_PIECE:
                    pygame.draw.circle(self.screen, YELLOW, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
        pygame.display.update()


    def hover_red_token(self, posx):
        self.clear_top_area()
        pygame.draw.circle(self.screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)


    def clear_top_area(self):
        pygame.draw.rect(self.screen, BLACK, (0, 0, width, SQUARESIZE))


    def show_message(self, message, colour):
        global label
        label = self.myfont.render(message, 1, colour)
        self.screen.blit(label, (40, 10))
        pygame.display.update()


    def column_under_mouse(self, posx):
        return int(math.floor(posx / SQUARESIZE))
