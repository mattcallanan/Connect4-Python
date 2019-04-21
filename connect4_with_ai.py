import math

from display import YELLOW, RED
from engine import GameEngine
from human_agent import HumanAgent
from minimax_agent import MiniMaxAgent
from player1 import Player1
from player2 import Player2
from random_agent import RandomAgent


if __name__ == "__main__":

    engine = GameEngine(YELLOW, RED)
    engine.init_display()

    # TODO: Separate AgentGlobalParams (HyperParams?) and AgentTurnParams

    human_agent = HumanAgent(params={'display': engine.display})
    random_agent = RandomAgent()
    minimax_agent = MiniMaxAgent(params={'depth': 5, 'alpha': -math.inf, 'beta': math.inf, 'maximizingPlayer': True})

    human_player1 = Player1(human_agent, "Human 1")
    human_player2 = Player2(human_agent, "Human 2")
    minimax_player1 = Player1(minimax_agent, "MiniMax 1")
    minimax_player2 = Player2(minimax_agent, "MiniMax 2")
    random_player1 = Player1(random_agent, "Random 1")
    random_player2 = Player2(random_agent, "Random 2")

    # engine.start_game(minimax_player1, minimax_player2)
    engine.start_game(random_player1, random_player2)
    # engine.start_game(human_player1, random_player2)
    engine.main_loop()
