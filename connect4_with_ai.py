import math

from engine import GameEngine
from minimax_agent import MiniMaxAgent

agent = MiniMaxAgent(params={'depth': 5, 'alpha': -math.inf, 'beta': math.inf, 'maximizingPlayer': True})
engine = GameEngine(agent)
engine.main_loop()
