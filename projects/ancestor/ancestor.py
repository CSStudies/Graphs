
from util import Queue

lineage = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def family_tree(ancestors):
    tree = {}

    for relative in ancestors:
        if relative[1] not in tree:
            tree[relative[1]] = set()
            tree[relative[1]].add(relative[0])
        else:
            tree[relative[1]].add(relative[0])

    print(f'Tree: {tree}')


def earliest_ancestor(ancestors, starting_node):
    """
    1. Preprocess Tuples into a graph of ancestors
    2. Run a BFS against graph to determine longest path. 
    """

if __name__=='__main__':
    family_tree(lineage)