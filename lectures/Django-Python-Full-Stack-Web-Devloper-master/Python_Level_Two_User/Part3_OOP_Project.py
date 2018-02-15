#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        self.cards = []
        for suite in SUITE:
            for rank in RANKS:
                card = "{}{}".format(rank, suite)
                self.cards.append(card)

    def split(self):
        split_len = len(self.cards)//2
        return (self.cards[:split_len], self.cards[split_len:])

    def shuffle(self):
        shuffle(self.cards)

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,cards):
        self.cards = cards

    def add(self,card):
        self.cards.append(card)

    def remove(self):
        return self.cards.pop(0)

    def __len__(self):
        return len(self.cards)
class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """
    def __init__(self, hand):
        self.hand = hand
        self.cards = []

    def play(self, number=1):
        if len(self.hand) < number:
            print("Player lost")
            return None
        cards = []
        for i in range(number):
            cards.append(self.hand.remove())
        self.cards += cards
        return cards

    def add(self, cards):
        for card in cards:
            self.hand.add(card)

    def last_card(self):
        if len(self.cards):
            return self.cards[-1]
        else:
            return None

    def last_card_value(self):
        last_card = self.last_card()
        if last_card:
            return RANKS.index(last_card[:-1])
        return -1

    def clean_cards(self):
        self.cards = []

    def has_cards(self):
        return len(self) != 0

    def __len__(self):
        return len(self.hand)

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

def card_val(card):
    return RANKS.index(card[:-1])

# Use the 3 classes along with some logic to play a game of war!
deck = Deck()
deck.shuffle()

(list_hand1, list_hand2) = deck.split()

hand1 = Hand(list_hand1)
hand2 = Hand(list_hand2)

player1 = Player(hand1)
player2 = Player(hand2)

for i in range(10):
    player1.play()
    player2.play()
    print("{} vs {}".format(player1.last_card(), player2.last_card()))
    v1 = player1.last_card_value()
    v2 = player2.last_card_value()
    while v1 == v2:
        print("War!!")
        player1.play(2)
        player2.play(2)
        print("In War: {} vs {}".format(player1.last_card(), player2.last_card()))
        v1 = player1.last_card_value()
        v2 = player2.last_card_value()

    if v1 > v2:
        player1.add(player1.cards + player2.cards)
        print(len(player1))
        print(len(player2))
    else:
        player2.add(player1.cards + player2.cards)
        print(len(player1))
        print(len(player2))
    player1.clean_cards()
    player2.clean_cards()
