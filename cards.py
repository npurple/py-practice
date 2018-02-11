#coding=utf8

import collections
import pprint
from common.tools import *


Card = collections.namedtuple('Card', ['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self): 
        return len(self._cards)

    def __getitem__(self, position): 
        return self._cards[position]

suitvs = dict(spades=4, hearts=3, diamonds=2, clubs=1)
def spades_high(card):
    rankv = FrenchDeck.ranks.index(card.rank)
    return rankv * len(suitvs) + suitvs[card.suit]

if __name__ == '__main__':
    beer_card = Card('3', 'hearts')
    p(beer_card)

    deck = FrenchDeck()
    p(len(deck))
    p(deck.suits)

    for card in deck:
        #p(card)
        break

    pprint.pprint(sorted(deck, key=spades_high))

