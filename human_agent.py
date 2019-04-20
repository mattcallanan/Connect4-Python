import sys

import pygame

from agent import Agent


class HumanAgent(Agent):

    def __init__(self, params=None):
        if params is None:
            params = {}
        self.display = params['display']
        self.params = params

    def get_move(self, board):
        self.throw_away_old_events()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # or (event.type == pygame.KEYUP and event.key == 113 and event.mod == 1024):
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    self.display.hover_red_token(event.pos[0])
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    column_to_play = self.display.column_under_mouse(event.pos[0])
                    return column_to_play
                else:
                    print(f"- Ignoring event: {event}")

    def throw_away_old_events(self):
        pygame.event.get()
