from poker import Poker


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
