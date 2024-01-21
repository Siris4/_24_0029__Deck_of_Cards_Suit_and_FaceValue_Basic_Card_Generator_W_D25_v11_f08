import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def represent(self):
        # Convert values 1, 11, 12, 13 to 'Ace', 'Jack', 'Queen', 'King'
        special_cards = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
        display_value = special_cards.get(self.value, self.value)
        print("Card:", display_value, "of", self.suit)

def random_value_generator():
    # Return randomly generated number 1-13 for value, with 1 representing Ace
    return random.randint(1, 13)

def random_suit_generator():
    suits = ["Spades", "Diamonds", "Clubs", "Hearts"]
    return random.choice(suits)

# Example testing:
card1 = Card(random_suit_generator(), random_value_generator())
card1.represent()

print()

# Additional format Testing:
card2 = Card("Heart", 2)
card2.represent()
