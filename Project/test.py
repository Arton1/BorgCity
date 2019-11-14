import unittest
from graph import Graph


class GraphTestCase(unittest.TestCase):
    def test_graph_creation(self):
        graph = Graph()
        self.assertEqual(len(graph._vertices), 1)

    def test_graph_add_vertex(self):
        graph = Graph()
        graph.add_vertex((2, 4), (0, 2))
        fixture = [
            [(1, 2)],
            [(2, 4), (0, 2)],
            [(1, 4)],
            ]
        correct = True
        for vertex, case in zip(graph._vertices, fixture):
            for (adj_vertex, cost), (index_case, cost_case) in zip(vertex._edges, case):
                if(adj_vertex._index != index_case or cost != cost_case):
                    correct = False
        self.assertTrue(correct)

if __name__ == "__main__":
    unittest.main()
