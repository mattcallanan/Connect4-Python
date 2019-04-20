import math

from core import PLAYER1_ID, PLAYER2_ID
from display import YELLOW, RED
from engine import GameEngine
from human_agent import HumanAgent
from random_agent import RandomAgent
from minimax_agent import MiniMaxAgent
from player import Player

# TODO: Separate AgentGlobalParams (HyperParams?) and AgentTurnParams

engine = GameEngine(YELLOW, RED)

human_agent = HumanAgent(params={'display': engine.display})
random_agent = RandomAgent()
minimax_agent = MiniMaxAgent(params={'depth': 5, 'alpha': -math.inf, 'beta': math.inf, 'maximizingPlayer': True})

# player1 = Player(agent1, PLAYER1_ID, "Human", "Yellow", YELLOW)
# player2 = Player(minimax_agent, PLAYER2_ID, "AI", "Red", RED)
player1 = Player(random_agent, PLAYER1_ID, "Random 1", "Yellow", YELLOW)
player2 = Player(random_agent, PLAYER2_ID, "Random 2", "Red", RED)

engine.start_game(player1, player2)
engine.main_loop()

