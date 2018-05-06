import collections
from random import choice, shuffle

Card = collections.namedtuple("Card", ["rank", "suit"])

# 黑桃 > 红桃 > 梅花 > 方块
suit_values = dict(spades=3, hearts=2, clubs=1, diamonds=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


class FrenchDeck:
    """
    扑克牌
    """

    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    # 黑桃 红桃 梅花 方块
    suits = "spades hearts clubs diamonds".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def shuffle(self):
        """
        洗牌
        """
        shuffle(self._cards)


def use_french_deck():
    # 方块7
    beer_card = Card("7", "diamonds")
    print(beer_card)
    # 输出结果：
    """
    Card(rank='7', suit='diamonds')
    """

    deck = FrenchDeck()
    print("牌的数量：", len(deck))
    print("第一张牌：", deck[0])
    print("最后一张牌：", deck[-1])
    # 输出结果：
    """
    牌的数量： 52
    第一张牌： Card(rank='2', suit='spades')
    最后一张牌： Card(rank='A', suit='diamonds')
    """

    # 随机获取一张牌
    print(choice(deck))
    print(choice(deck))
    # 输出结果：
    """
    Card(rank='K', suit='hearts')
    Card(rank='A', suit='hearts')
    """

    # 进行切片操作
    print(deck[:3])
    print(deck[12::13])
    # 输出结果：
    """
    [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
    [Card(rank='A', suit='spades'), Card(rank='A', suit='hearts'), Card(rank='A', suit='clubs'), Card(rank='A', suit='diamonds')]
    """

    # 迭代（实现__getitem__）
    for card in deck[:3]:
        print(card)
    # 输出结果：
    """
    Card(rank='2', suit='spades')
    Card(rank='3', suit='spades')
    Card(rank='4', suit='spades')
    """

    # 反向迭代
    for card in reversed(deck[:3]):
        print(card)
    # 输出结果：
    """
    Card(rank='4', suit='spades')
    Card(rank='3', suit='spades')
    Card(rank='2', suit='spades')
    """

    # 迭代搜索
    print(Card(rank='7', suit='diamonds') in deck)
    # 输出结果：
    """
    True
    """

    # 对牌进行升序排列
    for card in sorted(deck[:3], key=spades_high):
        print(card)
    # 输出结果：
    """
    Card(rank='2', suit='spades')
    Card(rank='3', suit='spades')
    Card(rank='4', suit='spades')
    """

    # 洗牌
    deck.shuffle()
    print(deck[:3])
    # 输出结果：
    """
    [Card(rank='4', suit='hearts'), Card(rank='10', suit='hearts'), Card(rank='2', suit='diamonds')]
    """


if __name__ == '__main__':
    use_french_deck()
