class Graph:
    def __init__(self):
        self.vertices = [Vertex()]

class Vertex:
    def __init__(self, list_of_edges = []):
        self.edges = list_of_edges

class Edge:
    def __init__(self, left_vertex, right_vertex, value):
        self.vertices = (left_vertex, right_vertex)
        self.value = value

