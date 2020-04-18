import os
import sys
from itertools import combinations

def lzd(sequence):
    d = set()
    w = ''
    for c in sequence:
        w += c
        if not w in d:
            d.add(w)
            w = ''
    return d

def js(a, b): return len(a & b)/float(len(a | b))

def nn_cluster(triplets):
    index = {}
    for _, a, b in sorted(triplets, reverse=True):
        if not a in index: 
            cluster = index.get(b, set())
            cluster.update([a, b])
            index[a] = cluster
        if not b in index: 
            cluster = index.get(a, set())
            cluster.update([a, b])
            index[b] = cluster
    return set(tuple(cluster) for cluster in index.values())

if __name__ == "__main__":
    print('Loading sequences')
    path = sys.argv[1]
    sequences = {name: open(os.path.join(path, name)).read() for name in os.listdir(path)}

    print('Creating dictionaries')
    dictionaries = {name: lzd(g) for name, g in sequences.items()}

    print('Calculating pairwise distance')
    dcts = dictionaries
    triplets = [(js(dcts[a], dcts[b]), a, b) for a, b in combinations(dcts.keys(), 2)]

    print('Building clusters')
    clusters = nn_cluster(triplets)

    print('Results')
    for i, cltr in enumerate(clusters):
        print('cluster ' + str(i) + ': ' + ', '.join(cltr))
