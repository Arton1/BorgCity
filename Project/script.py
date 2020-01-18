from recursive_solution import calculate_recursively, calculate_iteratively
from graph import calculate_brute_force

if __name__ == "__main__":
    print("Please, type in number of steps and then values for edges: ")
    steps_number = int(input())
    edge_cost = list(map(int, input().strip().split()[:steps_number]))
    if(len(edge_cost) != steps_number):
        print("Please, type in the same amount of values as there are steps")
    else:
        print(calculate_recursively(steps_number, edge_cost))
        print(calculate_iteratively(steps_number, edge_cost))
        print(calculate_brute_force(steps_number, edge_cost))
