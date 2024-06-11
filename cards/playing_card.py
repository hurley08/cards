# cards/cards.py

from dataclasses import dataclass
from cards import cardExceptions
from cards.tables import Tables
from loguru import logger
table = Tables().rankings_single_level_dict



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

@dataclass
class PlayingCard:
    def __init__(self, suit, face, face_up=True, in_hand=False, in_deck=None):
        # Playing card class will query a ranking table when initiated 
        # Must ensure that there's a mechanism that protects the table from being manipulated
        # or create a process that will allow a change to this.
        self._suit = suit
        self._face = face
        self.rankings = self.get_rankings()
        self._id = self.rankings[(self._suit,self._face)]
        self.face_up = face_up
        self.in_hand = in_hand
        self.in_deck = in_deck
        logger.success(f"Card Initialized: {self._face}, {self._suit}")

        #print(f"The card {self._suit:} of {self._face:} with a value of {self._id:} has been created")

    def get_rankings(self, table=None):
        # Retrieves a table that ranks every card
        try: 
            if table is None:
                table = Tables().rankings_single_level_dict
            logger.success("Rankings table retrieved")
        except Exception as e:
            logger.error(f"Something's wrong")
            logger.debug(e)
        return table



    def __gt__(self, other):
        # Card _id can be used to compare the value of a card
        return self._id > other._id 
        logger.debug("GT comparison used")


    def __lt__(self, other):
        # Defined explicitly
        logger.debug("LT comparison used")
        return self._id < other._id


    def show(self):
        # It's difficult to keep changing an obkects visibility through the
        # use of aattributes. The intention of this is to return the
        # details of a card if they are visible
        logger.debug(f"show, {self._id=}, {self._face=}, {self._suit=}, {self.face_up=}, {self.in_hand=}")
        if self.in_hand is True or self.face_up is True:
            pass
            #print(f"{self._id=} (value), {self,_suit=}, {self._face=}")
        else:
            raise CardNotViewable("A card must be faced up or in hand to be visible")
            logger.critical(CardNotViewable("A card must be faced up or in hand to be visible"))


    def flip(self):
        # Toggles the face_up status of a card thereby modifiying 
        # whether it is visible
        pre_val = self.face_up
        try:
            self.face_up = True if self.face_up is False else False
            if self.face_up is not pre_val:
                logger.success("Flipped card!")
                return True
        except DeckException as e:
            raise(e, "Something is wrong")
            logger.error(e)
        return False
