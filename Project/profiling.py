import cProfile, pstats
import recursive_solution
import graph

"""
To use memory profiling:
Decorate function with @profile
$ python -m memory_profiler example.py
"""

steps_number = 30
amount_of_calculations = 1000000


def profile_calculate_iteratively(steps_number, edge_costs, profiler):
    solution = recursive_solution.RecursiveSolution(edge_costs, steps_number)
    profiler.enable()
    return solution.calculate_path_sum(steps_number, profiler)


def profile_calculate_recursively(steps_number, edge_costs, profiler):
    solution = recursive_solution.RecursiveSolution(edge_costs, steps_number)
    profiler.enable()
    return solution.calculate_path_sum_recursive(steps_number)


def profile_calculate_brute_force(steps_number, edge_costs, profiler):
    graph_instance = graph.Graph()
    profiler.enable()
    for index in range(steps_number):
        graph_instance.expand(edge_costs[index])
    return graph_instance.count_costs_dfs()


if __name__ == "__main__":
    print("Please, type in number of algorythim that you want to calculate the value with")
    print("1 - algorithm using iterative formulas")
    print("2 - algorithm using recursive formulas")
    print("3 - algorithm using Depth First Search")
    number_of_algorithm = int(input())
    edge_costs = []
    for i in range(steps_number):
        edge_costs.append(1)
    profiler = cProfile.Profile()
    for step in range(1, steps_number+1):
        for calculation in range(amount_of_calculations):
            if number_of_algorithm == 1:
                profile_calculate_iteratively(step, edge_costs, profiler)
            elif number_of_algorithm == 2:
                profile_calculate_recursively(step, edge_costs, profiler)
            else:
                profile_calculate_brute_force(step, edge_costs, profiler)
            profiler.disable()
        stats = pstats.Stats(profiler)
        print(f"{step} : {stats.total_tt/amount_of_calculations}")
        profiler.clear()