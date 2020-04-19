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

# Merge dictionaries using uniqueness prefix to preserve metric.
prefix = '_' # Ok if part of the alphabet.
def merge_dcts(a, b):
    d = set()
    a_s = sorted(a, reverse=True)
    b_s = sorted(b, reverse=True)
    while a_s or b_s:
        if a_s and (not b_s or a_s[-1] <= b_s[-1]):
            w = a_s[-1]
            while w in d:
                w = prefix + w
                d.add(w)
            a_s.pop()
        if b_s and (not a_s or a_s[-1] >= b_s[-1]):
            w = b_s[-1]
            while w in d:
                w = prefix + w
                d.add(w)
            b_s.pop()
    return d

# Break sequence into smaller blocks, create LZ dictionaries, then merge the dictionaries.
def lzd_blocks(sequence, block_size):
    d = set()
    for i in range(0, len(sequence), block_size):
        d = merge_dcts(d, sequence[i:i+block_size])
    return d

# Probability of randomly selected item appearing in both sets.
def js(a, b): return len(a & b)/float(len(a | b))

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
    dictionaries = {name: lzd_blocks(g, 16) for name, g in sequences.items()}

    print('Calculating pairwise distance.')
    dcts = dictionaries
    triplets = [(js(dcts[a], dcts[b]), a, b) for a, b in combinations(dcts.keys(), 2)]

    print('Building clusters.')
    clusters = nearest_neighbor_cluster(triplets)

    print('Results:')
    for i, cltr in enumerate(clusters):
        print('cluster ' + str(i) + ': ' + ', '.join(cltr))
