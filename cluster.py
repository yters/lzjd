import os
import sys
from itertools import combinations
from collections import Counter

# Dictionary of unique subsequences, built from previous unique subsequences.
def lzd(sequence):
    d = {}
    w = ''
    for c in sequence:
        w += c
        if not w in d:
            d[w] = 1
            w = ''
    return d

# Merge dictionaries using uniqueness suffix to preserve metric.
def merge_dcts(a, b):
    for w in b:
        a[w] = a.get(w, 0) + 1
    return a

# Break sequence into smaller blocks, create LZ dictionaries, then merge the dictionaries.
def lzd_blocks(sequence, block_size):
    d = {}
    for i in range(0, len(sequence), block_size):
        d = merge_dcts(d, lzd(sequence[i:i+block_size]))
    return d

# Sort set by hashcode and take the lower 2048.
def min_hash(dictionary, bottom_count=2048): 
    min_hash_keys = sorted(dictionary.keys(), key=lambda x: hash(x))[0:bottom_count]
    min_hash_dictionary = {}
    dct_size = 0
    for k in min_hash_keys:
        count = dictionary[k] - max(dct_size - bottom_count, 0)
        min_hash_dictionary[k] = count
        dct_size += count
        if dct_size == bottom_count:
            break
    return min_hash_dictionary

# Probability of randomly selected item appearing in both sets.
def js(a, b): 
    inter_keys = set(a.keys()) & set(b.keys())
    inter_count = sum([min(a[w], b[w]) for w in inter_keys])
    union_keys = set(a.keys()) | set(b.keys())
    union_count = sum([max(a.get(w, 0), b.get(w, 0)) for w in inter_keys])
    return inter_count/float(union_count)

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
    block_size = 4096
    if len(sys.argv) > 2: block_size = int(sys.argv[2])
    bottom_size = 2048
    if len(sys.argv) > 3: bottom_size = int(sys.argv[3])

    print('Loading sequences.')
    path = sys.argv[1]
    sequences = {name: open(os.path.join(path, name)).read() for name in os.listdir(path)}

    print('Creating dictionaries.')
    dictionaries = {name: min_hash(lzd_blocks(g, block_size), bottom_size) for name, g in sequences.items()}

    print('Calculating pairwise distance.')
    dcts = dictionaries
    triplets = [(js(dcts[a], dcts[b]), a, b) for a, b in combinations(dcts.keys(), 2)]

    print('Building clusters.')
    clusters = nearest_neighbor_cluster(triplets)

    print('Results:')
    for i, cltr in enumerate(clusters):
        print('cluster ' + str(i) + ': ' + ', '.join(cltr))
