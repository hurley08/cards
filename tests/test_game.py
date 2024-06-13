# cards/test/test_game.py
from cards.deck import Deck
from cards.practice import Game
from cards.playing_card import PlayingCard, suits, faces
from loguru import logger
from dataclasses import dataclass
from cardExceptions import *

import random
import sys
import time


@pytest.fixture
def test_game_fixt(Game):
	gam = Game()
 	gam.info()
 	return gam



def test_playthrough(test_game_fixt):
	game = test_game_fixt()
	try:
		game.distribute_cards([game.p1, game.p2])
		game.begin()
	except:
		assert False
