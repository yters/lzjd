nodes = []
def backtrack(parent, curr, count):
    if parent == -1:
        return curr
    if count == 0:
        return curr
    return backtrack(nodes[parent][0], parent, count-1)
        
def find_candidates(start, depth, symbol):
    candidates = []
    open_list = [(start, 0)]
    closed_list = set()
    while len(open_list) > 0:
        curr, level = open_list.pop()
        if level > depth: continue
        closed_list.add(curr)
        for potential in nodes[curr][2].values():
            if not potential in closed_list:
                open_list.append((potential, level+1))
        if symbol in nodes[curr][2]:
            candidates.append(nodes[curr][2][symbol])
    return candidates

def tree_lzd_list(sequence, backtracking=0):
    global nodes
    tree = (-1, len(nodes), {}, -1)
    nodes += [tree]
    curr = 0
    for i, symbol in enumerate(sequence):
        if symbol == '.': continue
        if symbol in nodes[curr][2]:
            curr = nodes[curr][2][symbol]
        else:
            found_node = None
            candidates = find_candidates(backtrack(nodes[curr][0], curr, backtracking), backtracking, symbol)
            if not candidates:
                new_node = (curr, len(nodes), {}, i, symbol)
                nodes += [new_node]
                found_node = new_node[1]
            else:
                found_node = candidates[0]
            nodes[curr][2][symbol] = found_node
            curr = 0

if __name__ == "__main__":
    seq = 'a.g.t.ag.at.atg.aa.aaa'
    tree = tree_lzd_list(seq,1)
    print(len(nodes))
