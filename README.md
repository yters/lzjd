# Experiment: clustering mammals with the Lempel Ziv Jaccard Distance

Requirements: In order to run the code, you'll need to be in a Linux environment with either Python2 or Python3 installed.

## Synopsis
Test the Lempel-Ziv Jaccard Distance (LZJD) metric to cluster mitochondrial proteins from 38 mammals.

## Repo Overview
This repo contains 12 concatenated mitochondrial proteins from 38 mammals in the `data` directory.  The proteins are represented as DNA sequences.  There are also four randomly generated DNA sequences as a sanity check.

The scripts to measure the pairwise LZJD between all the mammals is in the `src` directory.

To cluster the mammals' proteins, run the following command:
```
./src/measure_and_cluster.sh
```

You'll see the clustered mammals in:
```
./results/clusters.txt
```

If the LZJD metric works correctly, you should see an intuitive clustering of the mammals, and the random genomes clustered separately from the mammals.

## References
Dataset is taken from: 
- https://complearn.org/downloads/libcomplearn-1.1.7.tar.gz

If the link becomes broken, the dataset can be looked up via the paper, which also explains the "Normalized Compression Distance" that inspired the Lempel-Ziv Jaccard Distance:
- Cilibrasi, R., & Vitányi, P. M. (2005). Clustering by compression. IEEE Transactions on Information theory, 51(4), 1523-1545.

The LZJD metric is defined in:
- Raff, E., & Nicholas, C. (2017, August). An alternative to NCD for large sequences, Lempel-Ziv Jaccard distance. In Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 1007-1015).

A much more optimized implementation of LZJD can be found at:
- https://github.com/EdwardRaff/jLZJD
