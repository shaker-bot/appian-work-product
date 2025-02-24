from classes.deck import Deck


def main():
    deck = Deck()
    deck.shuffle()

    while deck.cards:
        x = deck.deal_one_card()
        print(f"Dealt Card: {x}")
        print(f"Cards Remaining: {deck.count()}")


if __name__ == "__main__":
    main()
