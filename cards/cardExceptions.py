
class CountException(Exception):
	"""Raised when count values do not make sense"""

class DeckException(Exception):
	"""Raised for anomalies and violations pertaining to deck"""

class CardNotVisible(Exception):
	"""When someone attempts to peek at a facedown card"""

