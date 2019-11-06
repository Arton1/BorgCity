import sys
from graph import Graph

if __name__ == "__main__":
    # print("Please, type in number of steps and then values for edges: ")
    # steps_number = int(input())
    # edge_cost = list(map(int, input().strip().split()[:steps_number]))
    # print(edge_cost)
    steps_number = 2
    edge_cost = [2, 1]
    graph = Graph()
    for index in range(steps_number):
        graph.expand(edge_cost[index])
    graph.print_vertices()
    print(graph.count_costs_dfs())