import random
from typing import List

from .card import Card
from .enums import Rank, Suit


class Deck:
    """A class representing a standard deck of 52 cards."""

    def __init__(self) -> None:
        """Initialize a new deck."""
        self.cards: List[Card] = []
        self.__build()

    def __build(self) -> None:
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
        i = 0

        # Traverses list "at least once"
        while i < len(self.cards):
            j = random.randint(0, len(self.cards) - 1)
            k = random.randint(0, len(self.cards) - 1)
            self.cards[j], self.cards[k] = self.cards[k], self.cards[j]
            i += 1

    def deal_one_card(self) -> Card | None:
        """Remove and return the top card from the deck."""
        try:
            return self.cards.pop()
        except IndexError as e:
            raise Exception("No more cards in the deck")
