import random

from agents.agent import Agent
from board import get_valid_locations


class RandomAgent(Agent):
    def __init__(self, params=None):
        if params is None:
            params = {}
        self.params = params

    def get_move(self, board):
        return random.sample(get_valid_locations(board), 1)[0]
