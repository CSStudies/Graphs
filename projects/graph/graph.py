"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue/stack as appropriate
        # Put the starting vert in queue or stack
        # Make a set to visit edges
        # While queue/stack not empty 
        ## Pop the first item 
        ## If not visited
        ### add it to visted
        ### For each edge
        #### add edge to stack/queue  

        q = Queue()
        q.enqueue(starting_vertex)

        visited = set()
        while q.size() > 0:
            vert = q.dequeue()
            if vert not in visited:
                visited.add(vert)
                for edge in self.get_neighbors(vert):
                    q.enqueue(edge)
        print(visited)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a queue/stack as appropriate
        # Put the starting vert in queue or stack
        # Make a set to visit edges
        # While queue/stack not empty 
        ## Pop the first item 
        ## If not visited
        ### add it to visted
        ### For each edge
        #### add edge to stack/queue  

        s = Stack()
        s.push(starting_vertex)
        visited = set()
        print(f'visited: {visited}')
        while s.size() > 0:
            vert = s.pop()
            if vert not in visited:
                print(f'current vertex: {vert}')
                visited.add(vert)
                print(f'visited: {visited}')
                for edge in self.get_neighbors(vert):
                    print(f' push edge onto stack: {edge}')
                    s.push(edge)
        print(visited)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue/stack as appropriate
        # Put a list with the starting vert in queue or stack
        # Make a set to visit edges
        # While queue/stack not empty 
        ## Pop the list out of stack or queue
        ## vertex is last item in list
        ## If vertex not visited
        ### add it to visted
        ### For each edge
        #### add edge to list 
        #### add list to queue of stack

        pass # TODO: IF destination_vertex not in self.vertices

        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()
        while q.size() > 0:
            path = q.dequeue()
            vert = path[-1]
            if vert not in visited:
                if vert == destination_vertex:
                    print(f'BFS path: {path} ')
                    return path
                for edge in self.get_neighbors(vert):
                    path_list = list(path)
                    path_list.append(edge)
                    q.enqueue(path_list)

        # q = Queue()
        # q.enqueue(starting_vertex)
        # visited = set()
        # path = list()
        # while q.size() > 0:
        #     vert = q.dequeue()            
        #     if vert not in visited:
        #         if vert is destination_vertex:
        #             return path
        #         visited.add(vert)
        #         # path.append(vert)
        #         for edge in self.get_neighbors(vert):
        #             q.enqueue(edge)
        #             path.append(vert)
        # print(f'BFS Path: {path}')
        # return path

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a queue/stack as appropriate
        # Put a list with the starting vert in queue or stack
        # Make a set to visit edges
        # While queue/stack not empty 
        ## Pop the list out of stack or queue
        ## vertex is last item in list
        ## If vertex not visited
        ### add it to visted
        ### For each edge
        #### add edge to list 
        #### add list to queue of stack

        s = Stack()
        s.push([starting_vertex])
        visited = set()
        while s.size() > 0 :
            path = s.pop()
            vert = path[-1]
            if vert not in visited:
                if vert == destination_vertex:
                    print(f'DFS Path: {path} ')
                    return path
                for edge in self.get_neighbors(vert):
                    path_list = list(path)
                    path_list.append(edge)
                    s.push(path_list)

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
