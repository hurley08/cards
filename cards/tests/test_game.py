# cards/test/test_game.py

import pytest

@pytest.fixture
def test_war_fixt(War):
	gam = War()
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