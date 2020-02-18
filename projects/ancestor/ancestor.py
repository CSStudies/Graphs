
from util import Queue

lineage = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def family_tree(ancestors):
    tree = {}

    for relative in ancestors:
        if relative[1] not in tree:
            tree[relative[1]] = set()
        tree[relative[1]].add(relative[0])
        if relative[0] not in tree: 
            tree[relative[0]] = set()
            

        #     tree[relative[1]].add(relative[0])
        # else:
        #     tree[relative[1]].add(relative[0])
        # if relative[0] not in tree:
        #     tree[relative[0]] = None #may need to change to empty set

    print(f'Tree: {tree}')
    return tree


def earliest_ancestor(ancestors, person):
    """
    1. Preprocess Tuples into a graph of ancestors
    2. Run a BFS against graph to determine longest path. 
    """

    tree = family_tree(ancestors)

    # if person not in tree: 
    #     return person
    
    q = Queue()
    q.enqueue([person])
    visited = set()
    og_list = [ ]
    while q.size() > 0:
        path = q.dequeue()
        relative = path[-1]
        if relative not in visited:
            visited.add(relative)
            for ancestor in tree[relative]:
                # if tree[relative] is False:
                #     tree[relative].add(-1)
                #     print(f'updated tree {tree}')
                # else:
                path_list = list(path)
                path_list.append(ancestor)
                og_list.append(ancestor)
                q.enqueue(path_list)
                
        print(f'Relative: {relative} \nvisited: {visited} \npath {path} \n')
    print(f'OG List: {og_list} \n')
    
    if len(og_list) > 0:
        return og_list[-1]
    else:
        return -1
        


if __name__=='__main__':
    family_tree(lineage)
    earliest_ancestor(lineage, 2)
    earliest_ancestor(lineage, 6)

    # them : Who are you
    # me: Who handles all the decisions that happen transparently around us?
    # them: I don't know 
    # me: I'm with them same group different department.
    #     Think of me as a sort of middle man.
