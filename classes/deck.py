from typing import List

from .card import Card


class Deck:
    """A class representing a standard deck of 52 cards."""

    def __init__(self) -> None:
        """Initialize a new deck."""
        self.cards: List[Card] = []
        self._build()

    def _build(self) -> None:
        """Helper function to build the initial deck of cards."""
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for rank in [
                "Ace",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "Jack",
                "Queen",
                "King",
            ]:
                self.cards.append(Card(rank, suit))

    def __repr__(self) -> str:
        """Return a string representation of the deck."""
        return f"Deck of {self.count()} cards"

    def count(self) -> int:
        """Return the number of cards in the deck."""
        return len(self.cards)
