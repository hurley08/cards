# cards/tables.py 

from dataclasses import dataclass

@dataclass
class Tables:
	suits = {
	 'Club': 0,
	 'Diamond': 2,
	 'Heart': 4,
	 'Spade': 6,
	}

	faces = {	
	 'Two': 2,
	 'Three': 3,
	 'Four': 4,
	 'Five': 5,
	 'Six': 6,
	 'Seven': 7,
	 'Eight': 8,
	 'Nine': 9,
	 'Ten':10,
	 'Jack': 11,
	 'Queen': 12,
	 'King': 13,
	  'Ace': 14,
	}

	# nested dictionary
	rankings_nested_dict ={
		'Club': {
			'Two': 1,
			'Three': 2,
			'Four': 3,
			'Five': 4,
			'Six': 5,
			'Seven': 6,
			'Eight': 7,
			'Nine': 8,
			'Ten': 9,
			'Jack': 10,
			'Queen': 11,
			'King': 12,
			'Ace': 13
			},
		'Diamond': {
			'Two': 14,
			'Three': 15,
			'Four': 16,
			'Five': 17,
			'Six': 18,
			'Seven': 19,
			'Eight': 20,
			'Nine': 21,
			'Ten': 22,
			'Jack': 23,
			'Queen': 24,
			'King': 25,
			'Ace': 26
			},
		'Heart': {
			'Two': 27,
			'Three': 28,
			'Four': 29,
			'Five': 30,
			'Six': 31,
			'Seven': 32,
			'Eight': 33,
			'Nine': 34,
			'Ten': 35,
			'Jack': 36,
			'Queen': 37,
			'King': 38,
			'Ace': 39
			},
		'Spade': {
			'Two': 40,
			'Three': 41,
			'Four': 42,
			'Five': 43,
			'Six': 44,
			'Seven': 45,
			'Eight': 46,
			'Nine': 47,
			'Ten': 48,
			'Jack': 49,
			'Queen': 50,
			'King': 51,
			'Ace': 52
			}
	}


	rankings_single_level = {
		('Club', 'Two'): 1,
		('Club', 'Three'): 2,
		('Club', 'Four'): 3,
		('Club', 'Five'): 4,
		('Club', 'Six'): 5,
		('Club', 'Seven'): 6,
		('Club', 'Eight'): 7,
		('Club', 'Nine'): 8,
		('Club', 'Ten'): 9,
		('Club', 'Jack'): 10,
		('Club', 'Queen'): 11,
		('Club', 'King'): 12,
		('Club', 'Ace'): 13,
		('Diamond', 'Two'): 14,
		('Diamond', 'Three'): 15,
		('Diamond', 'Four'): 16,
		('Diamond', 'Five'): 17,
		('Diamond', 'Six'): 18,
		('Diamond', 'Seven'): 19,
		('Diamond', 'Eight'): 20,
		('Diamond', 'Nine'): 21,
		('Diamond', 'Ten'): 22,
		('Diamond', 'Jack'): 23,
		('Diamond', 'Queen'): 24,
		('Diamond', 'King'): 25,
		('Diamond', 'Ace'): 26,
		('Heart', 'Two'): 27,
		('Heart', 'Three'): 28,
		('Heart', 'Four'): 29,
		('Heart', 'Five'): 30,
		('Heart', 'Six'): 31,
		('Heart', 'Seven'): 32,
		('Heart', 'Eight'): 33,
		('Heart', 'Nine'): 34,
		('Heart', 'Ten'): 35,
		('Heart', 'Jack'): 36,
		('Heart', 'Queen'): 37,
		('Heart', 'King'): 38,
		('Heart', 'Ace'): 39,
		('Spade', 'Two'): 40,
		('Spade', 'Three'): 41,
		('Spade', 'Four'): 42,
		('Spade', 'Five'): 43,
		('Spade', 'Six'): 44,
		('Spade', 'Seven'): 45,
		('Spade', 'Eight'): 46,
		('Spade', 'Nine'): 47,
		('Spade', 'Ten'): 48,
		('Spade', 'Jack'): 49,
		('Spade', 'Queen'): 50,
		('Spade', 'King'): 51,
		('Spade', 'Ace'): 52}
