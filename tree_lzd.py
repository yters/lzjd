nodes = []
def tree_lzd_list(sequence):
    global nodes
    tree = (-1, len(nodes), {}, -1)
    nodes += [tree]
    curr = 0
    for i, symbol in enumerate(sequence):
        if symbol in nodes[curr][2]:
            curr = nodes[curr][2][symbol]
        else:
            new_node = None
            if not nodes[curr][0] == -1:
                for ancestor in nodes[nodes[curr][0]][2].values():
                    if symbol in nodes[ancestor][2]:
                        new_node = nodes[nodes[ancestor][2][symbol]]
            if not new_node:
                new_node = (curr, len(nodes), {}, i)
                nodes += [new_node]
            nodes[curr][2][symbol] = new_node[1]
            curr = 0

if __name__ == "__main__":
    seq = 'aagttgccgggg'
    tree = tree_lzd_list(seq)
    print(nodes)
