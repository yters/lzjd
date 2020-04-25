import os
import sys
from itertools import combinations

# Dictionary of unique subsequences, built from previous unique subsequences.
def lzd(sequence):
    d = set()
    w = ''
    for c in sequence:
        w += c
        if not w in d:
            d.add(w)
            w = ''
    return d

# Probability of randomly selected item appearing in both sets.
def js(a, b): return len(a & b)/float(len(a | b))

# Test the triangle inequality.
def triangle(pairs):
    violations = 0
    items = set()
    for a, b in pairs.keys():
        items.add(a)
        items.add(b)
    items = list(items)
    for i in range(len(items)):
        for j in range(0, i):
            if i == j: continue
            c = tuple(sorted([items[i], items[j]]))
            for k in range(j, i):
                if i == k: continue
                if j == k: continue
                a = tuple(sorted([items[i], items[k]]))
                b = tuple(sorted([items[j], items[k]]))
                if pairs[c] > pairs[a] + pairs[b]:
                    violations += 1
    return violations

# Add each sequence to the cluster with the most similar sequence.
def nearest_neighbor_cluster(triplets):
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
    print('Loading sequences.')
    path = sys.argv[1]
    sequences = {name: open(os.path.join(path, name)).read() for name in os.listdir(path)}

    print('Creating dictionaries.')
    dictionaries = {name: lzd(g) for name, g in sequences.items()}

    print('Calculating pairwise distance.')
    dcts = dictionaries
    triplets = [(js(dcts[a], dcts[b]), a, b) for a, b in combinations(dcts.keys(), 2)]

    print('Test triangle inequality:')
    pairs = {}
    for d, a, b in triplets:
        pairs[tuple(sorted([a, b]))] = d
    violations = triangle(pairs)
    print(str(violations) + ' violations.')

    print('Building clusters.')
    clusters = nearest_neighbor_cluster(triplets)

    print('Results:')
    for i, cltr in enumerate(clusters):
        print('cluster ' + str(i) + ': ' + ', '.join(cltr))
