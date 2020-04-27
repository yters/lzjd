import os
import sys
from itertools import combinations
import hamming

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

    print('Calculating pairwise hamming.')
    triplets = []
    if len(sys.argv) > 2:
        for line in open(sys.argv[2]).read().splitlines():
            if not '>' in line: continue
            d, a, b = line.split('>')[1].split('|')
            triplets.append((int(d), a.strip(), b.strip()))
    else:
        for i, (a, b) in enumerate(combinations(sequences.keys(), 2)):
            d = hamming.hamming(sequences[a], sequences[b])
            print(i,'/',len(list(combinations(sequences.keys(), 2))),'>',d,'|',a,'|',b)
            triplets.append((d, a, b))

    print('Building clusters.')
    clusters = nearest_neighbor_cluster(triplets)

    print('Results:')
    for i, cltr in enumerate(clusters):
        print('cluster ' + str(i) + ': ' + ', '.join(cltr))
