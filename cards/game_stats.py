# cards/game_stats.py

from cards.deck import Deck 
from cards.tables import Tables
from loguru import logger
import pandas as pd

import time


t = Tables().rankings_single_level_dict

class Stats:

	def __init__(self, draws=100, verbosity=False):
		# Verbosity is currently not implemented
		self.info(slp=2)
		logger.info(f"Stats for {draws=} has been initiated")
		self.count = 0
		self.limit = draws
		self.dealer = Deck(name="House")
		self.hand = Deck(name="Hand")
		self.verbose = verbosity
		self.stats = {}
		self.history = []
		for i in list(t):
			self.stats[i] = 0 

	def info(self, message=None, slp=5):
		# Just to explain the rules of the game
		if message is None:
			message=((
			"This game is called Stats."
			" The dealer will draw the number of "
			" cards specified by draws and perform"
			" statistical analysis on the results"
		))
		logger.debug(f"Displaying game info {message} for {slp} seconds")
		print(f"\n{message:}")
		time.sleep(slp)


	def begin(self):
		# Begins drawing and logging
		logger.info("The draws will begin now")
		self.dealer.generate_deck()
		for i in range(self.limit):
			if self.count % 10 == 0:
				print(f"\n\n{self.count=}")
			self.dealer.deal(1, self.hand)

			index = list(self.hand.deck)[0]
			crd = self.hand.deck[index]
			self.stats[(crd._suit, crd._face)] += 1
			self.history.append((crd._suit, crd._face))
			self.hand.deal(1, self.dealer)
			
			self.count += 1
			


	def results(self):
		# Calculate the percent draw of each of the 52 cards
		self.stats.values()
		for i in self.stats:
			self.stats[i] = {self.stats[i]:self.stats[i]/self.limit}
		print(self.stats)
		print(self.history)
		return self.stats


	def df(self):
		# Generate a dataframe object from which more stats may be derived
		df = pd.DataFrame(self.stats.keys())
		df2 = pd.DataFrame(self.stats.items())
		
		pcnt = []
		freq = []
		for i in df2[1]:
			pcnt.append(list(i.values())[0])
			freq.append(list(i.keys())[0])
		df.columns = ["suit", "face"]
		df['freq'] = pd.DataFrame(freq)
		df['%'] = pd.DataFrame(pcnt)
		return df 


'''
add probability for a suit to be drawn (1/4)
add probability for a face to be drawn (4/52)
add probability for an even or odd card (1/2)

'''

