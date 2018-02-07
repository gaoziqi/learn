class Poker:

    def __init__(self, pok=None):
        self.pok = pok if pok else [0] * 15 # 0x 1~13 14d

    def clone(self):
        return Poker(pok=[i for i in self.pok])

    def isempty(self):
        return sum(self.pok) == 0

    def __eq__(self, other):
        return self.pok == other.pok

    def _islegal(self):
        l, pok = len(self.pok), self.pok
        if l < 2:
            return True
        elif l == 2:
            if pok[0] == 1 and pok[14] == 1:
                return True
            for i in range(1, 14):
                if pok[i] == 2:
                    return True
            return False
        elif l == 3:
            for i in range(1, 14):
                if pok[i] == 3:
                    return True
            return False
        elif l == 4:
            for i in range(1, 14):
                if pok[i] == 4 or pok[i] == 3:
                    return True
            return False
        elif l == 5:
            if pok[0] + pok[14] != 0:
                return False
            for i in range(1, 14):
                if pok[i] == 3:
                    return True
            return False

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
