import sys
import re

d = set()
w = ''
for c in open(sys.argv[1]).read():
    w += c
    if not w in d:
        d.add(w)
        print(w)
        w = ''
