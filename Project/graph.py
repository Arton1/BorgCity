class Graph:
    def __init__(self):
        self._vertices = []

    def print_vertices(self):
        print(self._vertices)
    
    def add_vertex(self, *edges):
        vertex_index = len(self._vertices)
        self._vertices.append({*edges})
        for (adjacent_vertex_index, edge_value) in edges:
            other_side_edge = (vertex_index, edge_value)
            if adjacent_vertex_index < len(self._vertices):
                self._vertices[adjacent_vertex_index].append(other_side_edge)
            else:
                self._vertices.append({other_side_edge})

    def add_edge(self, first_vertex, second_vertex):
        pass

    def copy_(self):
        pass
