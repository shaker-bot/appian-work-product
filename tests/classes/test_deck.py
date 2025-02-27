import unittest

from classes.deck import Deck
from classes.card import Card

class TestDeck(unittest.TestCase):

    def test_init(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_shuffle(self):
        deck = Deck()
        before = deck.cards.copy()
        deck.shuffle()
        after = deck.cards
        self.assertNotEqual(before, after)

    def test_deal_one_card(self):
        deck = Deck()
        original_length = len(deck.cards)
        card = deck.deal_one_card()
        new_length = len(deck.cards)
        self.assertEqual(original_length, new_length + 1)
        self.assertIsInstance(card, Card)
        self.assertNotIn(card, deck.cards)

    def test_deal_one_card_empty_deck(self):
        deck = Deck()
        # Deal all cards
        while deck.cards:
            deck.deal_one_card()
        
        with self.assertRaises(Exception) as context:
            deck.deal_one_card()
        
        self.assertEqual(str(context.exception), "No more cards in the deck")

