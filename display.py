import math

import pygame

from core import ROW_COUNT, COLUMN_COUNT, PLAYER1_ID, PLAYER2_ID

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

    def __init__(self, player1_colour, player2_colour):
        self.player1_colour = player1_colour
        self.player2_colour = player2_colour
        self.screen = pygame.display.set_mode(size)
        self.myfont = pygame.font.SysFont("monospace", 75)


    def draw_board(self, board):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                self.draw_blue_square(r, c)
                self.draw_black_circle(r, c)
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if board[r][c] == PLAYER1_ID:
                    self.draw_circle(r, c, self.player1_colour)
                elif board[r][c] == PLAYER2_ID:
                    self.draw_circle(r, c, self.player2_colour)
        pygame.display.update()

    def draw_blue_square(self, row, col):
        pygame.draw.rect(self.screen, BLUE, (col * SQUARESIZE, row * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))

    def draw_black_circle(self, row, col):
        pygame.draw.circle(self.screen, BLACK, (
            int(col * SQUARESIZE + SQUARESIZE / 2), int(row * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    def draw_circle(self, row, col, colour):
        pygame.draw.circle(self.screen, colour, (
            int(col * SQUARESIZE + SQUARESIZE / 2), height - int(row * SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    def hover_red_token(self, posx):
        self.clear_top_area()
        pygame.draw.circle(self.screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
        pygame.display.update()


    def clear_top_area(self):
        pygame.draw.rect(self.screen, BLACK, (0, 0, width, SQUARESIZE))


    def show_message(self, message, colour):
        global label
        label = self.myfont.render(message, 1, colour)
        self.screen.blit(label, (40, 10))
        pygame.display.update()


    def column_under_mouse(self, posx):
        return int(math.floor(posx / SQUARESIZE))
