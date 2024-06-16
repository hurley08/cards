# cards/game_stats.py


from cards.deck import Deck 
from cards.tables import Tables
import pandas as pd


t = Tables().rankings_single_level_dict

class Stats:

	def __init__(self, draws=1000, verbosity=True):
		self.count = 0
		self.limit = draws
		self.dealer = Deck(name="House")
		self.hand = Deck(name="Hand")
		self.verbose = verbosity
		self.stats = {}
		self.history = []
		for i in list(t):
			self.stats[i] = 0 

	def begin(self):
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


		vals = self.stats.values()
		for i in self.stats:
			self.stats[i] = {self.stats[i]:self.stats[i]/self.limit}
		print(self.stats)
		print(self.history)
		return self.stats

	def df(self):
		df = pd.DataFrame(self.stats.items())
		df.columns = ["card", "int"]
		df[['freq'],['intern']] = pd.DataFrame(df['int'].tolist(), index=df.index)
		return df 


g = Stats()
g.begin()
gg = g.results()
ggg = g.df()