import sys

print("Please, type in number of steps and then values for edges: ")
steps_number = int(input())
edge_cost = list(map(int, input().strip().split()[:steps_number]))
print(edge_cost)