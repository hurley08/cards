# cards/practice.py
 
from cards.deck import Deck
from cards.playing_card import PlayingCard
from cards.cardExceptions import *
from cards.tables import Tables 
import random
import logging
import sys 

logger = logging.getLogger(__name__)
logging.basicConfig(filename="cards.log", filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
stdout = logging.StreamHandler(stream=sys.stdout)


rankings = Tables().rankings_single_level_dict

def generate_std_deck(suits, faces):
	std_deck = []
	for i in suits:
		for j in faces:
			tup =f"('{i}', '{j}')"
			std_deck.append(tup)
			logging.debug(tup,',')
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
#print(d.deck)
#print(d.binned())
#
# print(d.count)
#L = d.binned(["Hearts"])
#for i in L:
#	print(i)
	#print(L[i], '\n')


d1 = Deck(name="Player1")
d2 = Deck(name="Player2")
#d.deal_card(d.count()/2,d1)
#d.deal_card(d.count(), d2)
d1.count
d2.count



def distribute_to_players(decks):
	count = d.count
	while count >= 1:
		for i in decks:
			d.deal(1, i)
		count = d.count



class Game:
	# Class to manage objects and rules 
	def __init__(self, Player1, Player2):
		self.gameover = None
		self.winner = None
		self.p1 = Player1
		self.p2 = Player2
		self.p1.stage = Deck(name="p1_stage")
		self.p2.stage = Deck(name="p2_stage")
		self.p1_cards = self.p1.count
		self.p2_cards = self.p2.count
		#self.players = [self.p1_deck, self.p2_deck]		


	def begin(self):
		self.gameover = False
		self.winner = False
		self.turn = 0
		Player1 = self.p1
		Player2 = self.p2
		print(f"{id(Player1)=} | {self.p1=}")
		print(f"{id(Player2)=} | {self.p2=}")

			#Previous approach
			#self.p1_deck.deal(1, self.p1_deck.stage, True)
			#self.p2_deck.deal(1, self.p2_deck.stage, True)
			#indexp1 = list(self.p1_deck.stage.deck.keys())[0]
			#indexp2 = list(self.p1_deck.stage.deck.keys())[0]
			#print(f"{self.p1_deck.stage.deck[indexp1]=}")
			#print(f"{self.p2_deck.stage.deck[indexp2]=}")


		while (self.p1_cards > 0 and self.p2_cards > 0):
			Player1.deal(1, Player1.stage, True)
			Player2.deal(1, Player2.stage, True)
			key1 = list(self.p1.stage.deck)[0]
			key2 = list(self.p2.stage.deck)[0]

			card1 = self.p1.stage.deck[key1]
			card2 = self.p2.stage.deck[key2]
			if rankings[card1.show()] > rankings[card2.show()]:
				self.p2.stage.deal(1, self.p1, True)
				print(f"{self.p2.stage.count=}, {self.p2.stage.deck=}")
			else:
				Player1.stage.deal(1, self.p2, True)
			#if Player2.stage.count > 0:
			#	Player2.stage.deal(Player2.stage.count, Player2, True)
			#if Player1.stage.count > 0:
		#		Player1.stage.deal(Player1.stage.count, Player1, True)

			
			self.turn += 1 
			self.update_counts()
		print("turn: ", self.turn)
		print(f"")

	def update_counts(self):
		self.p1_cards = self.p1.count

		self.p2_cards = self.p2.count





				


distribute_to_players([d1,d2])
print(d1.count)
print(d2.count)

game = Game(d1, d2)

game.begin()

print(game.p1.count, game.p1.stage.count)
print(game.p2.count, game.p2.stage.count)


#p1card = (game.p1_deck.stage.suit, game.p1_deck.stage.face)
#p2card = (game.p2_deck.stage.suit, game.p2_deck.stage.face)