import json

with open('rules.json') as r:
    rules = json.load(r)

rlen = {7: ['seq_single7'], 12: ['seq_pair6', 'seq_single12', 'seq_trio_single3', 'seq_trio4'], 6: ['bomb_single', 'seq_pair3', 'seq_trio2', 'seq_single6'], 10: ['seq_trio_pair2', 'seq_single10', 'seq_pair5'], 25: ['seq_trio_pair5'], 14: ['seq_pair7'], 4: ['trio_single', 'bomb'], 11: ['seq_single11'], 18: ['seq_trio6', 'seq_pair9'], 16: ['seq_pair8', 'seq_trio_single4'], 20: ['seq_trio_pair4', 'seq_trio_single5', 'seq_pair10'], 9: ['seq_single9', 'seq_trio3'], 5: ['seq_single5', 'trio_pair'], 2: ['pair', 'rocket'], 3: ['trio'], 15: ['seq_trio5', 'seq_trio_pair3'], 8: ['bomb_pair', 'seq_single8', 'seq_pair4', 'seq_trio_single2'], 1: ['single']}
