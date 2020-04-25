import os
import sys
from itertools import combinations
from collections import Counter

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

# Turn set into hashmap.
def mapify(d): return {w: 1 for w in d}

# Merge dictionaries using uniqueness suffix to preserve metric.
def merge_dcts(a, b): return {w: a.get(w, 0) + 1 for w in b}

# Break sequence into smaller blocks, create LZ dictionaries, then merge the dictionaries.
def lzd_blocks(seq, block_size):
    d = {}
    for i in range(0, len(seq), block_size):
        d = merge_dcts(d, mapify(lzd(seq[i:i+block_size])))
    return d

# Make duplicates unique with a unique prefix.
# Prefix cannot be part of alphabet.
prefix = '_'
def uniquify(d): 
    u = set()
    for w, v in d.items():
        for i in range(v):
            u.add(w + prefix * i)
    return u

# Probability of randomly selected item appearing in both sets.
def js(a, b): return len(a & b) / len(a | b)

# Test the triangle inequality.
def count_tests(n):
    count = 0
    for i in range(n):
        for j in range(0, i):
            if i == j: continue
            for k in range(j, i):
                if i == k: continue
                if j == k: continue
                count += 1
    return count

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
            for k in range(0, j):
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
    block_size = 4096
    if len(sys.argv) > 2: block_size = int(sys.argv[2])
    bottom_size = 2048
    if len(sys.argv) > 3: bottom_size = int(sys.argv[3])

    print('Loading sequences.')
    path = sys.argv[1]
    sequences = {name: open(os.path.join(path, name)).read().rstrip() for name in os.listdir(path)}

    print('Creating dictionaries.')
    dictionaries = {}
    for name, seq in sequences.items():
        uniq_dct = uniquify(lzd_blocks(seq, block_size))
        min_hash = set(sorted(uniq_dct, key=lambda x: hash(x))[0:bottom_size])
        dictionaries[name] = min_hash

    print('Calculating pairwise distance.')
    dcts = dictionaries
    triplets = [(js(dcts[a], dcts[b]), a, b) for a, b in combinations(dcts.keys(), 2)]

    print('Test triangle inequality:')
    pairs = {}
    items = set()
    for d, a, b in triplets:
        pairs[tuple(sorted([a, b]))] = d
        items.add(a)
        items.add(b)
    violations = triangle(pairs)
    tests = count_tests(len(items))
    print(str(violations) + ' violations out of ' + str(tests) + ' tests, ' + str(int(round(violations/tests,2)*100)) + '%.')

    print('Building clusters.')
    clusters = nearest_neighbor_cluster(triplets)

    print('Results:')
    for i, cltr in enumerate(clusters):
        print(', '.join(sorted(cltr)))
