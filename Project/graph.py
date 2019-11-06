import copy

class Graph:
    class Vertex:
        def __init__(self, index, *edges):
            self._index = index
            self._edges = list(edges)
            self._visited = False
            
        def is_visited(self):
            return self._visited
        
        def set_visited(self, value=True):
            self._visited = value

        def add_edge(self, vertex, cost):
            edge = (vertex, cost)
            self._edges.append(edge)

        def get_edges(self):
            return self._edges
        
        def edge_exists(self, vertex):
            if not all( vertex is not adjacent_vertex for (adjacent_vertex, cost) in self._edges):
                return True
            return False

        def get_edges_text(self):
            for_printing = []
            for vertex, cost in self._edges:
                for_printing.append((vertex.get_index(), cost))
            return str(for_printing)
        
        def get_index(self):
            return self._index
        
        def shift_index(self, shift):
            self._index += shift

        def all_edges_visited(self):
            if all(vertex.is_visited() for (vertex, cost) in self._edges):
                return True
            return False

        def get_edge_to_visit(self):
            for vertex, cost in self._edges:
                if(not vertex.is_visited()):
                    return (vertex, cost)
            return None

    def __init__(self):
        self._vertices = [self.Vertex(0)]
        self._expansion_count = 0 

    def print_vertices(self):
        for vertex, index in zip(self._vertices, range(len(self._vertices))):
            print(f"{index}: " + vertex.get_edges_text())

    def get_vertex(self, index):
        #Creates vertex if index equals size of graph
        if index < len(self._vertices):
            vertex = self._vertices[index]
        else:
            if index == len(self._vertices):
                vertex = self.Vertex(len(self._vertices))
                self._vertices.append(vertex)
            else:
                raise ValueError(f"Wrong vertex index: {index}")
        return vertex

    def reset_as_unvisited(self):
        for vertex in self._vertices:
            vertex.set_visited(False)

    def _add_edge_to_vertices(self, vertex_target_index, vertex_to_add_index, cost):
        if cost < 0:
            raise ValueError(f"Edge cost: {cost} < 0")
        if vertex_target_index == vertex_to_add_index:
            raise ValueError("Vertex can't point to himself")
        vertex_target = self.get_vertex(vertex_target_index)
        vertex_to_add = self.get_vertex(vertex_to_add_index)
        if vertex_target.edge_exists(vertex_to_add):
            raise ValueError(f"There already exists an edge from {vertex_target} to {vertex_to_add}")
        else:
            vertex_target.add_edge(vertex_to_add, cost)
            vertex_to_add.add_edge(vertex_target, cost)

    def add_vertex(self, *edges):
        vertex_index = len(self._vertices)
        for (adjacent_vertex_index, cost) in edges:
           self._add_edge_to_vertices(
                vertex_index,
                adjacent_vertex_index,
                cost,
                )

    def add_edge(self, first_vertex, second_vertex, cost):
        self._add_edge_to_vertices(first_vertex, second_vertex, cost)

    def add_clones(self, amount = 3):
        # Able to optimize
        initial_size = len(self._vertices)
        for clone_number in range(1, amount+1):
            graph_copy = copy.deepcopy(self._vertices[:initial_size])
            for vertex in graph_copy:
                vertex.shift_index((clone_number)*initial_size)
            self._vertices.extend(graph_copy)

    def add_bridges(self, edges_cost, graph_prev_size):
        if self._expansion_count > 0:
            prev_bridge_vertices_count = 2
        else:
            prev_bridge_vertices_count = 0
        self.add_vertex(
            (graph_prev_size - prev_bridge_vertices_count - 1, edges_cost),
            (graph_prev_size*2 - prev_bridge_vertices_count - 1, edges_cost),  
            )
        self.add_vertex(
            (graph_prev_size*3 - prev_bridge_vertices_count - 1, edges_cost),
            (graph_prev_size*4 - prev_bridge_vertices_count - 1, edges_cost),
            (len(self._vertices) - 1, edges_cost),
            )
        
    def expand(self, new_edges_cost):
        #City growth
        #Clone graph 4 times and change indexes of newly created vertices, so 
        #all the graphs can be merged.
        #Newly created bridge vertices are added after merging.
        initial_size = len(self._vertices)
        self.add_clones(3)
        self.add_bridges(new_edges_cost, initial_size) 
        self._expansion_count += 1
        
    def count_costs_dfs(self) -> int:
        paths_sum = 0
        edges_stack = []
        current_path_cost = 0
        for start_vertex in self._vertices:
            vertex = start_vertex
            while(True):
                edge = vertex.get_edge_to_visit()
                if edge is None:
                    if len(edges_stack)>0:
                        vertex.set_visited()
                        (prev_vertex, prev_cost) = edges_stack.pop()
                        current_path_cost -= prev_cost
                        vertex = prev_vertex
                        continue
                    else:
                        break 
                (adjacent_vertex, cost) = edge
                current_path_cost += cost
                if(adjacent_vertex.get_index() > start_vertex.get_index()):
                    paths_sum += current_path_cost
                edges_stack.append((vertex, cost))
                vertex.set_visited()
                vertex = adjacent_vertex
            self.reset_as_unvisited()
        return paths_sum
                
def print_info(vertex_index, adjacent_vertex_index, cost, paths_cum, current_path_cost):
    print(str(vertex_index) + " -> " + str((adjacent_vertex_index, cost)))
