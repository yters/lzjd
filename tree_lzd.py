nodes = []
def backtrack(parent, curr, count):
    if parent == -1:
        return curr
    if count == 0:
        return curr
    return backtrack(nodes[parent][0], parent, count-1)
        
def find_candidates(start, symbol):
    candidates = []
    open_list = nodes[start][2].values()
    closed_list = set()
    while len(open_list) > 0:
        curr = open_list.pop()
        closed_list.add(curr)
        for potential in nodes[curr][2].values():
            if not potential in closed_list:
                open_list.append(potential)
        if symbol in nodes[curr][2]:
            candidates.append(nodes[curr][2][symbol])
    return candidates

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
            print(find_candidates(nodes[curr][0], symbol))
            if not nodes[curr][0] == -1:
                for ancestor in nodes[nodes[curr][0]][2].values():
                    if symbol in nodes[ancestor][2]:
                        new_node = nodes[nodes[ancestor][2][symbol]]
            #new_node = None
            if not new_node:
                new_node = (curr, len(nodes), {}, i, symbol)
                nodes += [new_node]
            nodes[curr][2][symbol] = new_node[1]
            curr = 0

if __name__ == "__main__":
    seq = 'aagttg'
    tree = tree_lzd_list(seq)
    print(nodes)
    print(len(nodes))
