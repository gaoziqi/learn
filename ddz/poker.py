import collections
from rules import rules, rlen, const_str, root

cachePokers = {}


class Poker():

    def __new__(cls, s='', pok=None):
        if not s:
            s = ''.join([i * pok.get(i, 0) for i in const_str]) if pok else ''
        if s in cachePokers:
            obj = cachePokers[s]
        else:
            obj = super(Poker, cls).__new__(cls)
            obj.pok = collections.Counter(s)
        return obj

    def __add__(self, other):
        return Poker(pok=self.pok + other.pok)

    def __iadd__(self, other):
        return Poker(pok=self.pok + other.pok)

    def __sub__(self, other):
        return Poker(pok=self.pok - other.pok)

    def __isub__(self, other):
        return Poker(pok=self.pok - other.pok)

    def __eq__(self, other):
        return self.pok == other.pok

    def __contains__(self, other):
        c = other.pok if isinstance(other, Poker) else collections.Counter(other)
        return all([self.pok.get(i, 0) >= c[i] for i in c])

    def __str__(self):
        return ''.join([i * self.pok.get(i, 0) for i in const_str])

    def __repr__(self):
        return "Poker('%s')" % self

    def __len__(self):
        return sum(self.pok.values())

    def clone(self):
        return Poker(s=str(self))


def getValue(p):
    s, l = str(p), len(p)
    if l in rlen:
        for j in rlen[l]:
            if s in rules[j]:
                return j, rules[j].index(s)
    return '', 0


def getSteps(p, value=('', 0)):
    if value[0]:
        if value[0] == 'rocket':
            return []
        res = []
        d = rules[value[0]]
        for i in range(value[1] + 1, len(d)):
            if d[i] in p:
                res.append(Poker(d[i]))
        if value[0] != 'bomb':
            for i in rules['bomb']:
                if i in p:
                    res.append(Poker(i))
        if 'wW' in p:
            res.append(Poker('wW'))
        return res
    else:
        return _find(root, p.pok, 0)


def _find(ptr, pok, index):
    res = []
    for i in range(index, 15):
        s = const_str[i]
        if pok.get(s, 0) > 0 and s in ptr.node:
            pok[s] -= 1
            if ptr.node[s].end:
                res.append(Poker(ptr.node[s].end))
            res += _find(ptr.node[s], pok, i)
            pok[s] += 1
    return res


cachePokers = {str(i): i for i in getSteps(Poker('34567890JQKA2' * 4 + 'wW'))}
