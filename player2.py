from agents.agent import Agent
from core import PLAYER2_ID
from display import RED
from player import Player


class Player2(Player):

    def __init__(self, agent: Agent, name: str) -> object:
        super().__init__(agent, PLAYER2_ID, name, "Red", RED)
