import unittest

from classes.card import Card


class TestCard(unittest.TestCase):
    """Test the Card class."""

    def test_init(self):
        """Test that a Card can be initialized with a rank and suit."""
        card = Card(rank="Ace", suit="Spades")
        self.assertEqual(card.rank, "Ace")
        self.assertEqual(card.suit, "Spades")

    def test_repr(self):
        """Test that the repr method returns a string representing the Card."""
        card = Card(rank="Ace", suit="Spades")
        self.assertEqual(repr(card), "Ace of Spades")
