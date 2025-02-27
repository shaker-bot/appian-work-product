import unittest

from classes.deck import Deck
from classes.card import Card

class TestDeck(unittest.TestCase):

    def test_init(self):
        """Test that a new deck has 52 cards"""
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_shuffle(self):
        """Test that shuffling the deck changes the order of the cards"""
        deck = Deck()
        before = deck.cards.copy()
        deck.shuffle()
        after = deck.cards
        self.assertNotEqual(before, after)

    def test_deal_one_card(self):
        """Test that dealing one card removes and returns the top card"""
        deck = Deck()
        original_length = len(deck.cards)
        card = deck.deal_one_card()
        new_length = len(deck.cards)
        self.assertEqual(original_length, new_length + 1)
        self.assertIsInstance(card, Card)
        self.assertNotIn(card, deck.cards)
