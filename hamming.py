import sys

def hamming(s1, s2):
    best_hamming = 0
    s1shorter = True
    if len(s1) > len(s2): s2shorter = False
    for i in range(abs(len(s1)-len(s2))):
        if s1shorter:
            hamming = sum([c1 == c2 for c1, c2 in zip(s1, s2[i:])])
        else:
            hamming = sum([c1 == c2 for c1, c2 in zip(s1[i:], s2)])
        if hamming > best_hamming:
            best_hamming = hamming
    return best_hamming

if __name__ == "__main__":
    s1 = open(sys.argv[1]).read()
    s2 = open(sys.argv[2]).read()
    print(hamming(s1,s2))
