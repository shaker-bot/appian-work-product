from dataclasses import dataclass

@dataclass(frozen=True)
class Card:
    """Class representing a 'Card' in a deck"""
    rank: str
    suit: str

    def __repr__(self) -> str:
        """Return a string representation of the Card."""
        return f"{self.rank} of {self.suit}"
