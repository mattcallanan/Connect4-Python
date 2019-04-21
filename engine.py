import sys
from timeit import default_timer as timer

import pygame

from board import create_board, print_board, is_valid_location, drop_piece, winning_move
from display import Display


class GameEngine:

    def __init__(self, player1_colour, player2_colour):
        self.player1_colour = player1_colour
        self.player2_colour = player2_colour
        self.player1 = None
        self.player2 = None
        self.board = create_board()
        print_board(self.board)
        self.clock = pygame.time.Clock()

    def init_display(self):
        pygame.init()
        pygame.display.set_caption("Connect 4")
        self.display = Display(self.player1_colour, self.player2_colour)
        self.display.draw_board(self.board)

    def start_game(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1
        print(f"Player 1 is {player1}")
        print(f"Player 2 is {player2}")

    # TODO: Don't start loop until ready
    def main_loop(self):
        game_over = False

        while not game_over:
            column_to_play, elapsed = self.get_timed_move()
            print(f"{self.current_player.name}'s turn took {elapsed}s")
            game_over = self.draw_move_and_check_win(column_to_play, self.current_player)
            self.display.capture_screen(self.board)
            pygame.display.flip()
            # pygame.time.wait(1000)
            if not game_over:
                self.toggle_player()
            # self.clock.tick(1)

        if game_over:
            self.display.draw_winner(self.current_player.piece_id)
            pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    sys.exit()

    def get_timed_move(self):
        start = timer()
        column_to_play = self.current_player.agent.get_move(self.board)
        elapsed = timer() - start
        return column_to_play, elapsed

    def draw_move_and_check_win(self, column_to_play, player):
        game_over = False
        if is_valid_location(self.board, column_to_play):
            drop_piece(self.board, column_to_play, player.piece_id)

            print_board(self.board)
            four_in_a_row = winning_move(self.board, player.piece_id)
            self.display.draw_board(self.board, four_in_a_row)
            if four_in_a_row:
                print(f"{player.name} ({player.colour_name}) has won!")
                game_over = True
        else:
            print(f"Ignoring invalid column {column_to_play}")
        return game_over

    def toggle_player(self):
        self.current_player = self.player2 if (self.current_player == self.player1) else self.player1
        print(f"Now it's {self.current_player.name}'s turn")
