from classes.deck import Deck


def main():
    deck = Deck()
    deck.shuffle()

    # Automatic Simulate Card Dealing
    while deck.cards:
        card = deck.deal_one_card()
        print(f"Dealt Card: {card}")
        print(f"Cards Remaining: {deck.count()}")

    # Attempt to deal a new card (Should get None)
    try:
        card = deck.deal_one_card()
        print(f"Dealt Card: {card}")
    except:
        print("There are no more cards in the deck!")


    # Interactive Simulation
    # print("Welcome to the deck simulator.")
    # print("Commands: shuffle, deal, remaining, reset, quit")

    # while True:
    #     command = input("Enter command:").strip().lower()
    #     if command == "shuffle":
    #         deck.shuffle()
    #         print("Deck shuffled :)")
    #     elif command == "deal":
    #         try:
    #             card = deck.deal_one_card()
    #             print(f"Dealt Card: {card}")
    #         except:
    #             print("There are no more cards in the deck!")
    #     elif command == "remaining":
    #         print(f"Remaining cards: {deck.count()}")
    #     elif command == "reset":
    #         deck = Deck()
    #         print("Deck has been reset to starting state!")
    #     elif command == "quit":
    #         print("Bye!")
    #         break
    #     else:
    #         print("Invalid command. Valid commands are shuffle, deal, remaining, reset, and quit")



if __name__ == "__main__":
    main()
