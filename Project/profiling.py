import cProfile, pstats
import recursive_solution
import graph


def profile_calculate_iteratively(steps_number, edge_costs, profiler):
    profiler.enable()
    solution = recursive_solution.RecursiveSolution(edge_costs, steps_number)
    value = solution.calculate_path_sum(steps_number, profiler)
    profiler.disable()
    return value


def profile_calculate_recursively(steps_number, edge_costs, profiler):
    profiler.enable()
    solution = recursive_solution.RecursiveSolution(edge_costs, steps_number)
    value = solution.calculate_path_sum_recursive(steps_number)
    profiler.disable()
    return value


def profile_calculate_brute_force(steps_number, edge_costs, profiler):
    graph_instance = graph.Graph()
    profiler.enable()
    for index in range(steps_number):
        graph_instance.expand(edge_costs[index])
    value = graph_instance.count_costs_dfs()
    profiler.disable()
    return value


if __name__ == "__main__":
    print("Please, type in number of algorithm that you want to calculate the values with")
    print("1 - algorithm using iterative formulas")
    print("2 - algorithm using recursive formulas")
    print("3 - algorithm using Depth First Search")
    number_of_algorithm = int(input())
    print("Please, type in step of increasing expansion values")
    krok = int(input())
    print("Please, type in amount of calculations")
    amount_of_calculations = int(input())
    edge_costs = []
    for i in range(krok*7):
        edge_costs.append(1)
    profiler = cProfile.Profile()
    for step in range(krok, krok*7, krok):
        for calculation in range(amount_of_calculations):
            if number_of_algorithm == 1:
                solution = profile_calculate_iteratively(step, edge_costs, profiler)
            elif number_of_algorithm == 2:
                solution = profile_calculate_recursively(step, edge_costs, profiler)
            else:
                solution = profile_calculate_brute_force(step, edge_costs, profiler)
        stats = pstats.Stats(profiler)
        print(f"{step} : {stats.total_tt/amount_of_calculations}")
        print(f"Solution: {solution}")
        profiler.clear()