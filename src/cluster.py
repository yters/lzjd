import sys
from collections import Counter

pairs = []
for line in open(sys.argv[1]).read().splitlines():
    a, b, d = line.split('|')
    d = int(d)
    pairs += [(a,b,d)]

clusters = []
for p in pairs:
    a, b, d = p
    c_a = None
    c_b = None
    for c in clusters:
        if a in c and b in c: c_a = c; c_b = c
        elif a in c: c_a = c
        elif b in c: c_b = c 
        if c_a and c_b: break
    if not c_a and not c_b: clusters += [set([a, b])]
    elif not c_a: c_b.add(a)
    elif not c_b: c_a.add(b)

for i, c in enumerate(clusters):
    print('cluster ' + str(i) + ': ' + ', '.join(c))
