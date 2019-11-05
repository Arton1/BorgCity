class Graph:
    class Vertex:
        def __init__(self, *edges):
            self._edges = list(edges)
            self._visited = False
            
        def is_visited(self):
            return self._visited
        
        def set_visited(self, value=True):
            self._visited = value

        def add_edges(self, *edges):
            self._edges.extend(edges)

        def get_edges(self):
            return self._edges
        
        def edge_exists(self, edge):
            if not all( edge[0] != adjacent_vertex for (adjacent_vertex, cost) in self._edges):
                return True

        def get_copy(self, edges_shift=0):
            vertex_copy = Graph.Vertex()
            for (vertex_index, value) in self._edges:
                vertex_copy.add_edges((vertex_index + edges_shift, value))
            return vertex_copy

        def get_edges_text(self):
            return str(self._edges)

    def __init__(self):
        self._vertices = [self.Vertex()]
        self._expansion_count = 0 

    def print_vertices(self):
        for vertex, index in zip(self._vertices, range(len(self._vertices))):
            print(f"{index}: " + vertex.get_edges_text())
    
    def _add_edge_to_vertex(self, vertex_target, vertex_to_add, value):
        if value < 0:
            raise ValueError(f"Edge value: {value} < 0")
        if vertex_target == vertex_to_add:
            raise ValueError("Vertex can't point to himself")
        edge = (vertex_to_add, value)
        if vertex_target < len(self._vertices):
            if self._vertices[vertex_target].edge_exists(edge):
                raise ValueError(
                    f"There already exists an edge from " 
                    f"{vertex_target} to {vertex_to_add}"
                    )
            self._vertices[vertex_target].add_edges(edge)
        else:
            if vertex_target == len(self._vertices):
                self._vertices.append(self.Vertex(edge))
            else:
                raise ValueError(f"Wrong vertex target: {vertex_target}")

    def add_vertex(self, *edges):
        vertex_index = len(self._vertices)
        self._vertices.append(self.Vertex(*edges))
        for (adjacent_vertex_index, edge_value) in edges:
           self._add_edge_to_vertex(
               adjacent_vertex_index, 
                vertex_index, 
                edge_value
                )

    def add_edge(self, first_vertex, second_vertex, edge_value):
        self._add_edge_to_vertex(first_vertex, second_vertex, edge_value)
        self._add_edge_to_vertex(second_vertex, first_vertex, edge_value)

    def expand(self, edge_costs, steps=1):
        #City growth
        #Clone graph 4 times and shift pointers of newly created graphs, so 
        #all the graphs can be merged.
        #Newly created bridge vertices are added after merging.
        initial_size = len(self._vertices)
        for copy_step in range(1, 4):
            for vertex in self._vertices[:initial_size]:
                self._vertices.append(vertex.get_copy(initial_size*copy_step))
        expansion_edge_cost = edge_costs[self._expansion_count]
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
        
    def count_costs_dfs(self) -> int:
        paths_sum = 0
        edge_stack = []
        vertex = self._vertices[0]
        current_path_cost = 0
