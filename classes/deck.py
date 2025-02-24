import random
from typing import List

from .card import Card
from .enums import Rank, Suit


class Deck:
    """A class representing a standard deck of 52 cards."""

    def __init__(self) -> None:
        """Initialize a new deck."""
        self.cards: List[Card] = []
        self._build()

    def _build(self) -> None:
        """Helper function to build the initial deck of cards."""
        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card(rank.value, suit.value))

    def __repr__(self) -> str:
        """Return a string representation of the deck."""
        return f"Deck of {self.count()} cards"

    def count(self) -> int:
        """Return the number of cards in the deck."""
        return len(self.cards)

    def shuffle(self) -> None:
        """'Shuffle' the deck so that self.cards is randomly permuted"""

        # Initial implementation to simply swap two elements (only randomizing the "swap with" index)
        # for i in range(len(self.cards)):
        #     j = random.randint(0, len(self.cards)-1)
        #     self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

        # Second thought, randomize both indexes, iterate only as long as the current deck
        i = 0
        while i < len(self.cards):
            j = random.randint(0, len(self.cards) - 1)
            k = random.randint(0, len(self.cards) - 1)
            self.cards[j], self.cards[k] = self.cards[k], self.cards[j]
            i += 1

        # Sorted allows you to define a key that "determines sorting order"
        # self.cards = sorted(self.cards, key=lambda x: random.random())

    def deal_one_card(self) -> Card | None:
        """Remove and return the top card from the deck."""
        return self.cards.pop()
