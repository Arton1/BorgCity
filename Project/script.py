from recursive_solution import calculate_recursively, calculate_iteratively
from graph import calculate_brute_force

if __name__ == "__main__":
    print("Please, type in number of algorithm that you want to calculate the value with")
    print("1 - algorithm using iterative formulas")
    print("2 - algorithm using recursive formulas")
    print("3 - algorithm using Depth First Search")
    number_of_algorithm = int(input())
    print("Please, type in number of steps and then values for edges: ")
    steps_number = int(input())
    edge_cost = list(map(int, input().strip().split()[:steps_number]))
    if(len(edge_cost) != steps_number):
        print("Please, type in the same amount of values as there are steps")
    else:
        if(number_of_algorithm == 1):
            print(calculate_iteratively(steps_number, edge_cost))
        elif (number_of_algorithm == 2):
            print(calculate_recursively(stps_number, edge_cost))
        else:
            print(calculate_brute_force(steps_number, edge_cost))
