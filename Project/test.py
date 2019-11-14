import unittest
from graph import Graph


class GraphTestCase(unittest.TestCase):
    def test_graph_creation(self):
        graph = Graph()
        self.assertEqual(len(graph._vertices), 1)

    def test_add_vertex_to_initial_graph(self):
        graph = Graph()
        graph.add_vertex((2, 4), (0, 2))
        fixture = [
            [(1, 2)],
            [(2, 4), (0, 2)],
            [(1, 4)],
            ]
        graphCorrect = True
        for vertex, case in zip(graph._vertices, fixture):
            for (adj_vertex, cost), (index_case, cost_case) in zip(vertex._edges, case):
                if(adj_vertex._index != index_case or cost != cost_case):
                    graphCorrect = False
        self.assertTrue(graphCorrect)

    def test_add_edge_to_initial_graph(self):
        graph = Graph()
        graph.add_edge(1, 2, 2)
        fixture = [
            [],
            [(2, 2)],
            [(1, 2)],
        ]
        graphCorrect = True
        for vertex, case in zip(graph._vertices, fixture):
            for (adj_vertex, cost), (index_case, cost_case) in zip(vertex._edges, case):
                if(adj_vertex._index != index_case or cost != cost_case):
                    graphCorrect = False
        self.assertTrue(graphCorrect)

    def test_graph_expansion(self):
        graph = Graph()
        graph.expand(0)
        for expansion in range(1):
            graph.expand(0)
        graphSize = len(graph._vertices)
        self.assertEqual(graphSize, 26)

    def test_graph_cloning(self):
        graph = Graph()
        graphEdges = [
            (0, 1, 2),
            (1, 2, 0),
            (2, 3, 1),
        ]
        for first_vertex_index, second_vertex_index, cost in graphEdges:
            graph.add_edge(first_vertex_index, second_vertex_index, cost)
        graph._add_clones(3)
        graphSize = len(graph._vertices)
        self.assertEqual(graphSize, 16)
    
    def test_adding_bridges(self):
        graph = Graph()
        graph.expand(0)
        graph._add_clones(3)
        initial_size = len(graph._vertices)
        graph._add_bridges(0, int(initial_size/4))
        after_adding_bridges_size = len(graph._vertices)
        self.assertEqual(after_adding_bridges_size, initial_size+2)

    def test_brutal_algorithm(self):
        graph = Graph()
        graph.expand(2)
        graph.expand(1)
        solution = graph.count_costs_dfs()
        self.assertEqual(solution, 2641)


if __name__ == "__main__":
    unittest.main()
