from rules import rules, rlen

const_str = '34567890JQKA2wW'


class Poker:

    def __init__(self, pok=None):
        self.pok = pok if pok else [0] * 15  # 34567890JQKA2wW

    def clone(self):
        return Poker(pok=[i for i in self.pok])

    def isempty(self):
        return sum(self.pok) == 0

    def __eq__(self, other):
        return self.pok == other.pok

    def __str__(self):
        return ''.join([const_str[i] * j for i, j in enumerate(self.pok)])

    def value(self):
        s = self.__str__()
        l = len(s)
        if l in rlen:
            for j in rlen[l]:
                if s in rules[j]:
                    return [j, rules[j].index(s)]
        return [None, None]

    def islegal(self, other):
        pass


class Player:

    def __init__(self, pok=None, dz=False, count=0):
        self.pok = pok if pok else Poker()
        self.dz = dz
        self.count = count

    def clone(self):
        return Player(pok=self.pok.clone(), dz=self.dz, count=self.count)


class State:

    def __init__(self, up=None, my=None, down=None, last=None):
        self.up = up if up else Player()
        self.my = my if my else Player()
        self.down = down if down else Player()
        self.last = last if last else Poker()

    def clone(self):
        return State(up=self.up.clone(), my=self.my.clone(), down=self.down.clone(), last=self.last.clone())
