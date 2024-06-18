# cards/test/test_game.py


import cards.deck as Deck
import pytest
from cards.deck import Deck
from cards.playing_card import PlayingCard
from cards.cardExceptions import DeckException, CardNotViewable
from cards.practice import Game
from cards.game_stats import Stats 

@pytest.fixture
def test_war_fixt(Game):
	gam = Game()
	gam.info()
	return gam

@pytest.fixture
def test_stats_fixt(Stats):
	gam = Stats()
	gam.info()
	return gam



def test_game_war(test_war_fixt):
	game = test_war_fixt()
	try:
		game.distribute_cards([game.p1, game.p2])
		game.begin()
	except Exception:
		assert False


def test_game_stats(test_stats_fixt):
	game = test_stats_fixt()
	try: 
		game.begin(draws=100)
	except Exception:
		assert False