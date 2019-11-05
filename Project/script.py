import sys
import graph

def func(*args):
    print(args)

if __name__ == "__main__":
    # print("Please, type in number of steps and then values for edges: ")
    # steps_number = int(input())
    # edge_cost = list(map(int, input().strip().split()[:steps_number]))
    # print(edge_cost)
    graph = graph.Graph()
    graph.add_vertex((1, 2), (2, 4), (3, 5))
    graph.print_vertices()
    graph.expand()
    graph.print_vertices()