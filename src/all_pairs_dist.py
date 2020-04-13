from os import listdir
from os.path import isfile, join
from sys import argv

animals = open(argv[1]).read().splitlines()
lzd_path = argv[2]
suffix = argv[3]

for a in animals:
    for b in animals:
        if a == b: continue
        file_a = open(join(lzd_path, a) + '.' + suffix)
        file_b = open(join(lzd_path, b) + '.' + suffix)
        lzd_a = set(file_a.read().splitlines())
        lzd_b = set(file_b.read().splitlines())
        lzjd = 1 - len(lzd_a & lzd_b) / float(len(lzd_a | lzd_b))
        print(a + '|' + b + '|' + str(int(lzjd * 100)))
