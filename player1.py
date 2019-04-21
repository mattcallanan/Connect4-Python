from agent import Agent
from core import PLAYER1_ID
from display import YELLOW
from player import Player


class Player1(Player):

    def __init__(self, agent: Agent, name: str) -> object:
        super().__init__(agent, PLAYER1_ID, name, "Yellow", YELLOW)
