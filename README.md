# Clustering mammals with the Lempel Ziv Jaccard Distance

This repo contains 12 concatenated mitochondrial proteins from each of 34 mammals in the `data` directory.  The proteins are represented as DNA sequences.  There are also four randomly generated DNA sequences as a sanity check.

To cluster the mammals' proteins, run the following command:
```
python cluster.py data
```

If the LZJD metric works correctly, you should see an intuitive clustering of the mammals, and the random genomes clustered separately from the mammals.  Look in the `results.txt` file to see an example run.

LZJD is parameter free, so you can run this script on any directory of files, and see the results.  Just replace `data` in the previous command with the path to the directory.

## References
Dataset is taken from: 
- https://complearn.org/downloads/libcomplearn-1.1.7.tar.gz

If the link becomes broken, the dataset can be looked up via the paper, which also explains the "Normalized Compression Distance" that inspired the Lempel-Ziv Jaccard Distance:
- Cilibrasi, R., & Vitányi, P. M. (2005). Clustering by compression. IEEE Transactions on Information theory, 51(4), 1523-1545.

The LZJD metric is defined in:
- Raff, E., & Nicholas, C. (2017, August). An alternative to NCD for large sequences, Lempel-Ziv Jaccard distance. In Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 1007-1015).

A much more optimized implementation of LZJD can be found at:
- https://github.com/EdwardRaff/jLZJD

Inspiration for investigating 'alignment free' similarity.
- Ewert, W. (2018). The dependency graph of life. BIO-Complexity, 2018.
