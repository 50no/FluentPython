"""create cards"""
import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck(object):
    ranks = [str(i) for i in range(2, 10)] + list('JQKA')
    suits = '黑桃 红桃 梅花 方片'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]


suit_values = dict(黑桃=3, 红桃=2, 方片=1, 梅花=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return  rank_value * len(suit_values) + suit_values[card.suit]




cards = FrenchDeck()
for card in sorted(cards, key=spades_high, reverse=True):
    print(card)
# print(cards.ranks)
# print(len(cards))
# print(cards[0])  # 由于实现了__getitem__
# print(choice(cards))  # 由于实现了__getitem__，reversed（）方法也是同理,同样还有 in，sort（需要一点改造）
# print(Card('Q', '红桃') in cards)





