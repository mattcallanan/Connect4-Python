import math

import pygame
import pygame.gfxdraw

from board import moves_played
from core import ROW_COUNT, COLUMN_COUNT, PLAYER1_ID, PLAYER2_ID

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (66, 244, 107)
GREY = (128, 128, 128)
FRAME = BLUE
# BACKGROUND = GREY
# BACKGROUND = WHITE
BACKGROUND = BLACK
FOREGROUND = WHITE
HIGHLIGHT = GREEN

SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE / 2 - 5)


class Display:
    bigfont = None

    def __init__(self, player1_colour, player2_colour):
        self.player1_colour = player1_colour
        self.player2_colour = player2_colour
        self.screen = pygame.display.set_mode(size, pygame.HWSURFACE)
        self.bigfont = pygame.font.Font(pygame.font.get_default_font(), 60)
        self.smallfont = pygame.font.Font(pygame.font.get_default_font(), 32)
        self.smallerfont = pygame.font.Font(pygame.font.get_default_font(), 16)

    # TODO: Highlight all tokens connected by winning move (not just first four found)
    def draw_board(self, board, winning_cells=[]):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                self.draw_cell_frame(c, r)
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                self.draw_blank_token(c, r)
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if board[r][c] == PLAYER1_ID:
                    self.draw_player1_token(c, r, (c, r) in winning_cells)
                elif board[r][c] == PLAYER2_ID:
                    self.draw_player2_token(c, r, (c, r) in winning_cells)
        pygame.display.update()

    def draw_cell_frame(self, col, row):
        x = col * SQUARESIZE
        y = row * SQUARESIZE + SQUARESIZE
        pygame.draw.rect(self.screen, FRAME, (x, y, SQUARESIZE, SQUARESIZE))

    def draw_blank_token(self, col, row):
        self.draw_circle_on_board(col, row, BACKGROUND)

    def draw_player1_token(self, col, row, winning):
        if winning:
            self.draw_highlighted_token(col, row, self.player1_colour)
        else:
            self.draw_circle_on_board(col, row, self.player1_colour)

    def draw_player2_token(self, col, row, winning):
        if winning:
            self.draw_highlighted_token(col, row, self.player2_colour)
        else:
            self.draw_circle_on_board(col, row, self.player2_colour)

    def draw_highlighted_token(self, col, row, piece_colour):
        self.draw_hollow_circle(col, row, HIGHLIGHT, piece_colour)

    def draw_hollow_circle(self, col, row, colour, background_colour):
        self.draw_circle_on_board(col, row, colour)
        self.draw_circle_on_board(col, row, background_colour, RADIUS - 10)

    def draw_circle_on_board(self, col, row, colour, radius=RADIUS):
        x = int(col * SQUARESIZE + SQUARESIZE / 2)
        y = height - int(row * SQUARESIZE + SQUARESIZE / 2)
        self.draw_aacircle(x, y, colour, radius)

    def draw_winner(self, player: int):
        x = RADIUS + 5
        y = RADIUS + 5
        if player == PLAYER1_ID:
            colour = self.player1_colour
        else:
            colour = self.player2_colour
        self.draw_aacircle(x, y, colour)
        self.draw_text(self.bigfont, FOREGROUND, " wins", x + RADIUS, y - (RADIUS / 2))

    def draw_aacircle(self, x, y, colour, radius=RADIUS):
        pygame.gfxdraw.aacircle(self.screen, x, y, radius, colour)
        pygame.gfxdraw.filled_circle(self.screen, x, y, radius, colour)

    # def hover_red_token(self, posx):
    #     self.clear_top_area()
    #     pygame.draw.circle(self.screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
    #     # pygame.display.update()

    def clear_top_area(self):
        pygame.draw.rect(self.screen, BACKGROUND, (0, 0, width, SQUARESIZE))

    def show_message(self, message, colour):
        self.draw_text(self.bigfont, colour, message, SQUARESIZE / 2, 10)

    def draw_text(self, font, colour, message, x, y):
        label = font.render(message, 1, colour)
        self.screen.blit(label, (x, y))
        # pygame.display.update()

    def column_under_mouse(self, posx):
        return int(math.floor(posx / SQUARESIZE))

    def capture_screen(self, board):
        filename = f"{moves_played(board)}.jpg"
        pygame.image.save(self.screen, filename)
        print(f"Captured screenshot to {filename}")
