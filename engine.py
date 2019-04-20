import random
import sys

import pygame

from board import create_board, print_board, is_valid_location, get_next_open_row, drop_piece, winning_move
from core import HUMAN_PIECE, AI_PIECE
from display import Display, RED, YELLOW

HUMAN = 0
AI = 1

PLAYERS = [HUMAN, AI]
PLAYER_NAMES = ["Human", "AI"]
PLAYER_COLOURS = [RED, YELLOW]


class GameEngine:

    def __init__(self, agent):
        self.agent = agent
        self.turn = random.randint(HUMAN, AI)
        self.board = create_board()
        print_board(self.board)
        pygame.init()
        self.display = Display()
        self.display.draw_board(self.board)
        pygame.display.update()

    def toggle_player(self):
        self.turn = (self.turn + 1) % 2
        print(f"{PLAYER_NAMES[self.turn]}'s turn")

    def main_loop(self):
        game_over = False

        while True:
            # Human's turn
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    if self.turn == HUMAN:
                        self.display.hover_red_token(event.pos[0])
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.turn == HUMAN:
                        game_over = self.play_human_turn(event)
                        pygame.display.update()
                        if game_over:
                            break
                    else:
                        print("Ignoring mouse click outside of human's turn")
            # AI's turn
            if self.turn == AI and not game_over:
                game_over = self.play_ai_turn()
                pygame.display.update()
                if game_over:
                    break

        if game_over:
            self.display.show_message(f"{PLAYER_NAMES[self.turn]} Player wins!!", PLAYER_COLOURS[self.turn])
            pygame.time.wait(3000)

    # Extract common elements from next 2 methods.  Delineate human turn a bit better

    def play_human_turn(self, event):
        column_to_play = self.display.column_under_mouse(event.pos[0])
        return self.play_and_check_win(column_to_play, HUMAN_PIECE, HUMAN)


    def play_ai_turn(self):
        column_to_play = self.agent.play_turn(self.board)
        return self.play_and_check_win(column_to_play, AI_PIECE, AI)

    def play_and_check_win(self, column_to_play, piece, player):
        game_over = False
        if is_valid_location(self.board, column_to_play):
            row = get_next_open_row(self.board, column_to_play)
            drop_piece(self.board, row, column_to_play, piece)
            pygame.display.update()

            print_board(self.board)
            self.display.draw_board(self.board)

            four_in_a_row = winning_move(self.board, piece)
            if four_in_a_row:
                print(f"{PLAYER_NAMES[player]} ({PLAYER_COLOURS[player]} Player) has won")
                game_over = True
            else:
                self.toggle_player()
        else:
            print(f"Ignoring invalid column {column_to_play}")
        return game_over
