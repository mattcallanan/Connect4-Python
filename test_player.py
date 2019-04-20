from unittest import TestCase

from agent import Agent
from core import PLAYER1_ID, PLAYER2_ID
from display import YELLOW
from player import Player


DUMMY_NAME = "Dummy Name"
DUMMY_COLOUR_NAME = "Dummy Colour Name"
INVALID_PLAYER_ID_1 = 0
INVALID_PLAYER_ID_2 = 3
INVALID_COLOUR_RGB = (0, 0, 0)

class TestPlayer(TestCase):

    def test_valid(self):
        dummy_agent = Agent()
        subject = Player(dummy_agent, PLAYER1_ID, DUMMY_NAME, DUMMY_COLOUR_NAME, YELLOW)
        self.assertEqual(subject.agent, dummy_agent)
        self.assertEqual(subject.piece_id, PLAYER1_ID)
        self.assertEqual(subject.name, DUMMY_NAME)
        self.assertEqual(subject.colour_name, DUMMY_COLOUR_NAME)
        self.assertEqual(subject.colour_rgb, YELLOW)

    def test_invalid(self):
        dummy_agent = Agent()
        with self.assertRaises(AssertionError):
            Player(dummy_agent, INVALID_PLAYER_ID_1, DUMMY_NAME, DUMMY_COLOUR_NAME, YELLOW)
        with self.assertRaises(AssertionError):
            Player(dummy_agent, INVALID_PLAYER_ID_2, DUMMY_NAME, DUMMY_COLOUR_NAME, YELLOW)
        with self.assertRaises(AssertionError):
            Player(dummy_agent, PLAYER2_ID, DUMMY_NAME, DUMMY_COLOUR_NAME, INVALID_COLOUR_RGB)
