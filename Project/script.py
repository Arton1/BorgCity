from recursive_solution import RecursiveSolution
from graph import calculate_brute_force, calculate_border

if __name__ == "__main__":
    # print("Please, type in number of steps and then values for edges: ")
    # steps_number = int(input())
    # edge_cost = list(map(int, input().strip().split()[:steps_number]))
    # print(edge_cost)
    steps_number = 50
    edge_costs = []
    for i in range(steps_number):
        edge_costs.append(1)
    recursive_solution = RecursiveSolution(edge_costs, steps_number)
    # print(calculate_border(steps_number, edge_costs))
    # print(recursive_solution.calculate_border_sum(steps_number))
    print(recursive_solution.calculate_path_sum(steps_number))
    # print(calculate_brute_force(steps_number, edge_costs))
