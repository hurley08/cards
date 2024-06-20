# cards/test/test_game.py

import pytest
from cards.deck import Deck
from  cards.game_war import War

from cards.game_stats import Stats


@pytest.fixture
def test_war_fixt():
	gam = War()
	return gam

@pytest.fixture
def test_stats_fixt():
	gam = Stats
	gam = gam()
	return gam


def test_game_war_info(test_war_fixt):
	game = test_war_fixt
	game.info()
	#game = game()
 
def test_game_war_begin(test_war_fixt):
	test_war_fixt.begin()

def test_game_stats_info(test_stats_fixt):
	game = test_stats_fixt
	game.info()
	#game = game()


