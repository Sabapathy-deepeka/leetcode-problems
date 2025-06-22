# Graphs have vertices and edges - It can have adjacency matrix/ adjacency list
#Big O 
# add new vertex
# - Adjacency list is O(1)

#  remove a new vertex
# - Adjacency matrix is O(V square)
# - Adjacency list is O(V+E) as we need to remove all edges before removing vertex

# To add edges/connect between vertices - both O(1)

class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
        # this try/except block is to handle the edge case where 'D' is a vertex that does not have any connection, we get a valueError
            try: 
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    #Logic: if vertex exists, see the list of other vertices its connected to, 
           #go to every other vertex and remove the actual vertex from the list
    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

    

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'A')
my_graph.add_edge('C', 'D')
my_graph.add_edge('A', 'D')

my_graph.remove_edge('C','A')
my_graph.remove_edge('A','D')
my_graph.remove_vertex('D')
my_graph.print_graph()