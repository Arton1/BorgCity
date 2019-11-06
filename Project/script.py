import sys
import graph

def func(*args):
    print(args)

if __name__ == "__main__":
    # print("Please, type in number of steps and then values for edges: ")
    # steps_number = int(input())
    # edge_cost = list(map(int, input().strip().split()[:steps_number]))
    # print(edge_cost)
    steps_number = 1
    edge_cost = [3, 1]
    graph = graph.Graph()
    # graph.add_vertex((1, 1), (2, 5))
    # graph.add_edge(1, 2, 10)
    graph.expand(3)
    graph.expand(1)
    graph.print_vertices()