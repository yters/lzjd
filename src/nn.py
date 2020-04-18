index = {}
for a, b, _ in triples:
    if not a in index:
        index[b] = index.get(b, set()).add(a)
    if not b in index:
        index[a] = index.get(a, set()).add(b)
clusters = set(index.values())
