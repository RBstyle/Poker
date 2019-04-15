'''Есть следующая далее структура классов. Надо при помощи класса Deck
получить 7 карт и определить лучшую комбинацию, которая выпала.

Определитель лучшей комбинации оформить все как функцию, которая принимает
список карт и выдает результат типа CombType.

'''
from collections import Counter
from random import randint


class Card(object):
    '''Класс, приводящий номинал карты к читаемому виду'''
    def __init__(self):
        self.name_rank = {
            'TWO': 2,
            'THREE': 3,
            'FOUR': 4,
            'FIVE': 5,
            'SIX': 6,
            'SEVEN': 7,
            'EIGHT': 8,
            'NINE': 9,
            'TEN': 10,
            'JACK': 11,
            'QUEEN': 12,
            'KING': 13,
            'ACE': 14
        }
        self.name_suit = {
            'SPADES': 1,
            'HEARTS': 2,
            'DIAMONDS': 3,
            'CLUBS': 4
        }

    def name_of_card(self, rank, suit):
        rank_card = ''
        suit_card = ''
        for init in self.name_rank:
            if self.name_rank.get(init) == rank:
                rank_card = init
        for init in self.name_suit:
            if self.name_suit.get(init) == suit:
                suit_card = init
        return '%r of %r' % (rank_card, suit_card)

    def elements(self):
        """Returns list of all elements of enum Rank"""
        return [x for x in range(2, 15)]


class Deck(object):
    '''Класс колоды с возможностью вытягивать карты'''
    def __init__(self, cards_count=52):
        self.deck = []
        self.cards_count = cards_count
        for i in range(1, cards_count + 1):
            self.deck.append(i)

    def pop_card(self):
        """Returns Card object taken randomly from a Deck"""
        card_no = randint(1, self.cards_count)
        card = self.deck.pop(card_no - 1)
        self.cards_count -= 1
        rank = card % 13 + 2
        suit = int((card - 1) / 13 + 1)
        return rank, suit


class CombType(object):
    '''Класс, присваивающий имя комбинации'''

    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_KIND = 8
    STRAIGHT_FLUSH = 9

    def __init__(self, num_of_comb):
        self.comb = None
        comb = {
            'HIGH CARD': 1,
            'PAIR': 2,
            'TWO PAIR': 3,
            'THREE OF KIND': 4,
            'STRAIGHT': 5,
            'FLUSH': 6,
            'FULL HOUSE': 7,
            'FOUR OF KIND': 8,
            'STRAIGHT FLUSH': 9,
        }
        for init in comb:
            if comb.get(init) == num_of_comb:
                self.comb = init

    def __str__(self):
        return 'Best combination: {}'.format(self.comb)


class SpotComb:
    '''Класс, определяющий кмобинацию'''
    def __init__(self, r_list, s_list):
        self.r_list = r_list
        self.s_list = s_list
        self.combination = CombType.HIGH_CARD
        self.combination = max(self.check_dubble(), self.find_streight())

    def find_streight(self):
        combination = self.combination
        rank = Card()
        cards = sorted(set(self.r_list))
        ranks = rank.elements()
        straight_comb = None
        s = Counter(self.s_list)
        flash_comb = s.most_common(1)
        flash_list = []

        for c, _ in enumerate(cards):

            if len(cards[c:c+5]) < 5:
                    break

            for r, _ in enumerate(ranks):
                if cards[c] == ranks[r]:
                    if cards[c: c + 5] == ranks[r: r + 5]:
                        straight_comb = (cards[c: c + 5])

        if straight_comb is not None:
            combination = CombType.STRAIGHT
            for i, c in enumerate(self.r_list):
                if c in straight_comb:
                    flash_list.append(self.s_list[i])
                f = Counter(self.s_list)
                straight_flash = f.most_common(1)
                if straight_flash[0][1] == 5:
                    combination = CombType.STRAIGHT_FLUSH

        if flash_comb[0][1] >= 5:
            combination = CombType.FLUSH
        return combination

    def check_dubble(self):
        c = Counter(rank_list)
        combination = self.combination
        most_count = c.most_common(3)
        most_count_list = []

        for item in most_count:
            if item[1] != 1:
                most_count_list.append(item)
        if len(most_count_list) == 1:
            if most_count_list[0][1] >= 4:
                if combination < CombType.FOUR_OF_KIND:
                    combination = CombType.FOUR_OF_KIND
            elif most_count_list[0][1] == 3:
                if combination < CombType.THREE_OF_KIND:
                    combination = CombType.THREE_OF_KIND
            elif most_count_list[0][1] == 2:
                if combination < CombType.PAIR:
                    combination = CombType.PAIR
        elif len(most_count_list) >= 2:
            count = []
            for item in most_count_list:
                count.append(item[1])
            if 2 in count and 3 in count:
                if combination <= CombType.FULL_HOUSE:
                    combination = CombType.FULL_HOUSE
            elif count.count(2) >= 2:
                if combination <= CombType.TWO_PAIR:
                    combination = CombType.TWO_PAIR
        return combination

if __name__ == "__main__":

    game_deck = Deck()
    set_of_cards = []
    for x in range(7):
        set_of_cards.append(game_deck.pop_card())
    card_name = Card()
    magic_set = []

    for card in set_of_cards:
        magic_set.append(card_name.name_of_card(card[0], card[1]))
    cards_on_hand = '\n'.join(magic_set)

    print('Cards on hand: \n%s' % cards_on_hand)

    rank_list = []
    suit_list = []
    for i, c in enumerate(set_of_cards):
        rank_list.append(c[0])
        suit_list.append(c[1])

    x = SpotComb(rank_list, suit_list)
    print(CombType(x.combination))
