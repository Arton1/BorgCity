import cProfile, pstats
from recursive_solution import calculate_recursive
from graph import calculate_brute_force

steps_number = 6
amount_of_calculations = 1

if __name__ == "__main__":
    edge_costs = []
    for i in range(steps_number):
        edge_costs.append(1)
    profiler = cProfile.Profile()
    total_time = 0
    for step in range(1, steps_number+1):
        for calculation in range(amount_of_calculations):
            profiler.enable()
            # calculate_recursive(step, edge_costs)
            calculate_brute_force(step, edge_costs)
            profiler.disable()
            stats = pstats.Stats(profiler)
            total_time += stats.total_tt
            profiler.clear()
        print(f"{step} : {total_time/amount_of_calculations}")
