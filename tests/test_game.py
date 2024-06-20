# cards/test/test_game.py

import pytest


@pytest.fixture
def test_game_fixt():
	gam = Game()
	gam.info()
	return gam



def test_playthrough(test_game_fixt):
	game = test_game_fixt()
	try:
		game.distribute_cards([game.p1, game.p2])
		game.begin()
	except Exception:
		assert False
