#!/bin/sh

echo 'Generating Lempel-Ziv dictionaries (LZD) for mammals'
for animal in `cat info/animals.txt`
do
    echo "- Generating scratch/$animal.lzd"
    python src/lzd.py data/$animal > scratch/$animal.lzd
done
echo

echo 'Measuring all pairs Lempel-Ziv Jaccard Distance (LZJD)'
echo '- Generating scratch/all_lzd.pairs'
python src/all_pairs_dist.py info/animals.txt scratch lzd | sort -n -k 3 -t '|' > results/all_lzd.pairs
echo 

echo 'Generating results/clusters.txt from results/all_lzd.pairs'
python src/cluster.py results/all_lzd.pairs lzd > results/clusters.txt
echo

echo 'All done!'
