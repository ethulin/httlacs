#Modify __cmp__ so that Aces are ranked higher than Kings.

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = [False, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
             "Jack", "Queen", "King"]

    def __str__(self):
        return "{} of {}".format(self.ranks[self.rank],self.suits[self.suit])

    def __cmp__(self, other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        #check to see if either is uniquely an ace
        if self.rank == 1 and other.rank != 1: return 1
        if self.rank != 1 and other.rank ==1: return -1
        #if neither is uniquely an ace
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        #if both suits and ranks are the same, it is a tie, return 0
        return 0
