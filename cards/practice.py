# cards/practice.py
 
from cards.deck import Deck
from cards.playing_card import PlayingCard
from cards.cardExceptions import *
from loguru import logger
import random

import sys 

#logger = logging.getLogger(__name__)
#logging.basicConfig(filename="cards.log", filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
#stdout = logger.StreamHandler(stream=sys.stdout)


def generate_std_deck(suits, faces):
	std_deck = []
	for i in suits:
		for j in faces:
			tup =f"('{i}', '{j}')"
			std_deck.append(tup)
			logger.debug(tup,',')
	return std_deck



def seq():
	d = Deck(name="Ron")
	d.generate_deck
	d2 = Deck(name="Player2")
	tw = d.just_draw(3)
	for i in tw:
		d.remove_card(i)


d = Deck(name="Dealer")
d.generate_deck()
d1 = Deck(name="Player1")
d2 = Deck(name="Player2")
d1.count()
d2.count()



def distribute_to_players(decks):
	count = d.count()
	while count >= 1:
		for i in decks:
			d.deal(1, i)
		count = d.count()


class Game:
	# Class to manage objects and rules 
	def __init__(self, Player1, Player2):
		self.gameover = None
		self.winner = None
		self.p1_deck = Player1
		self.p2_deck = Player2
		self.p1_deck.stage = None
		self.p2_deck.stage = None
		self.p1_cards = self.p1_deck.count()
		self.p2_cards = self.p2_deck.count()
		self.players = [self.p1_deck, self.p2_deck]


	def begin(self):
		self.gameover = False
		self.winner = False
		self.turn = 0

		while (self.p1_cards > 0 and self.p2_cards > 0):

			for playr in self.players:
				temp = playr.just_draw(1)
				#print(temp)
				playr.stage = temp[0]
				#print(playr.stage)
			
			if self.p1_deck.stage > self.p2_deck.stage:
				self.p1_deck.add_card(self.p2_deck.stage)
				self.p2_deck.remove_card(self.p2_deck.stage)
			else:
				self.p2_deck.add_card(self.p1_deck.stage)
				self.p1_deck.remove_card(self.p1_deck.stage)
			self.turn += 1 
			
			self.update_counts()
		print("turn: ", self.turn)
		print(f"")

	def update_counts(self):
		self.p1_cards = self.p1_deck.count()

		self.p2_cards = self.p2_deck.count()





				


distribute_to_players([d1,d2])

game = Game(d1, d2)

game.begin()

p1card = (game.p1_deck.stage._suit, game.p1_deck.stage._face)
p2card = (game.p2_deck.stage._suit, game.p2_deck.stage._face)