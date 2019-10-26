class Graph:
    def __init__(self):
        self._vertices = []

    def print_vertices(self):
        print(self._vertices)
    
    def add_vertex(self, *edges):
        # Adds vertex to graph first, and then updates adjactent vertices.
        # If adjacent vertex doesn't exist, checks the index correctness and
        # appends the vertex.
        # Adjacent vertex index is correct if the vertex already exists or
        # the index is the same number as the size of _vertices.
        vertex_index = len(self._vertices)
        self._vertices.append({*edges})
        for (adjacent_vertex_index, edge_value) in edges:
            if adjacent_vertex_index > len(self._vertices):
                raise ValueError("Error: Wrong vertex index")
            if edge_value < 0:
                raise ValueError("Error: Edge value < 0")
            other_side_edge = (vertex_index, edge_value)
            if adjacent_vertex_index < len(self._vertices):
                self._vertices[adjacent_vertex_index].append(other_side_edge)
            else:
                self._vertices.append({other_side_edge})

    def add_edge(self, first_vertex, second_vertex, value):
        if first_vertex > len(self._vertices)
            or second_vertex > len(self._vertices)
            or first_vertes == second_vertex
            or value < 0:
                raise ValueError("Error: Wrong values")
        def add_edge_to_vertex(vertex_target, vertex_to_add):
            if vertex_target < len(self._vertices):
                self._vertices[vertex_target].add((vertex_to_add, value))
            else:
                self._vertices.append((vertex_to_add, value))
        addEdgeToVertex(first_vertex, second_vertex)
        addEdgeToVertex(second_vertex, first_vertex)

    def copy_(self):
        pass
