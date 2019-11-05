class Graph:
    def __init__(self):
        self._vertices = [set()]
        self._expansion_count = 0

    def print_vertices(self):
        print(self._vertices)
    
    def _add_edge_to_vertex(self, vertex_target, vertex_to_add, value):
        if value < 0:
            raise ValueError(f"Edge value: {value} < 0")
        if vertex_target == vertex_to_add:
            raise ValueError("Vertex can't point to himself")
        edge = (vertex_to_add, value)
        if vertex_target < len(self._vertices):
            if not all(vertex_to_add != edge[0] for edge in self._vertices[vertex_target]):
                raise ValueError(
                    f"There already exists an edge from " 
                    f"{vertex_target} to {vertex_to_add}"
                    )
            self._vertices[vertex_target].add(edge)
        else:
            if vertex_target == len(self._vertices):
                self._vertices.append({edge})
            else:
                raise ValueError(f"Wrong vertex target: {vertex_target}")

    def add_vertex(self, *edges):
        vertex_index = len(self._vertices)
        self._vertices.append({*edges})
        for (adjacent_vertex_index, edge_value) in edges:
            self._add_edge_to_vertex(
                adjacent_vertex_index, 
                vertex_index, 
                edge_value
                )

    def add_edge(self, first_vertex, second_vertex, value):
        self._add_edge_to_vertex(first_vertex, second_vertex, value)
        self._add_edge_to_vertex(second_vertex, first_vertex, value)

    def expand(self, edge_costs, steps=1):
        #City growth
        #Clone graph 4 times and shift pointers of newly created graphs, so 
        #all the graphs can be merged.
        #Newly created bridge vertices are added after merging.
        initial_size = len(self._vertices)
        for copy_step in range(1, 4):
            for vertex in self._vertices[:initial_size]:
                vertex_copy = set()    
                for (vertex_index, value) in vertex:
                    vertex_copy.add(
                        (vertex_index + initial_size*copy_step, value)
                        )
                self._vertices.append(vertex_copy)
        expansion_edge_cost  = edge_costs[self._expansion_count]
        if self._expansion_count > 0:
            prev_bridge_vertices_count = 2
        else:
            prev_bridge_vertices_count = 0
        self.add_vertex(
            (initial_size - prev_bridge_vertices_count - 1, expansion_edge_cost),
            (initial_size*2 - prev_bridge_vertices_count - 1, expansion_edge_cost),  
            )
        self.add_vertex(
            (initial_size*3 - prev_bridge_vertices_count - 1, expansion_edge_cost),
            (initial_size*4 - prev_bridge_vertices_count - 1, expansion_edge_cost),
            (len(self._vertices) - 1, expansion_edge_cost),
            )
        self._expansion_count += 1