from agent import Agent
from core import PLAYER1_ID, PLAYER2_ID
from display import YELLOW, RED


class Player:

    def __init__(self, agent: Agent, piece_id: int, name: str, colour_name: str, colour_rgb: tuple) -> object:
        self.agent = agent
        self.piece_id = piece_id
        self.name = name
        self.colour_name = colour_name
        self.colour_rgb = colour_rgb
        self.validate()

    def validate(self):
        assert self.piece_id == PLAYER1_ID or self.piece_id == PLAYER2_ID
        assert self.colour_rgb == YELLOW or self.colour_rgb == RED

    def __str__(self) -> str:
        return f"'{self.name}' with {self.colour_name} tokens and piece ID: {self.piece_id}"
