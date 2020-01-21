from recursive_solution import RecursiveSolution
from graph import calculate_brute_force
import sys


class memory_profiler:

    def __init__(self):
        self._memory_value_holder = []

    def save_memory_values(self, *args):
        self._memory_value_holder.append([sys.getsizeof(arg) for arg in args])

    def get_sum_of_memory_values(self):
        sum = 0
        for table in self._memory_value_holder:
            for value in table:
                sum += value
        return sum

    def clear_memory_value_holder(self):
        self._memory_value_holder = []


if __name__ == "__main__":
    print("Please, type in number of algorithm that you want to calculate the values with")
    print("1 - algorithm using iterative formulas")
    print("2 - algorithm using recursive formulas")
    print("3 - algorithm using Depth First Search")
    number_of_algorithm = int(input())
    print("Please, type in step of increasing expansion values")
    krok = int(input())
    prof = memory_profiler()
    for steps_number in range(1, krok*6+1, krok): 
        edge_costs = []
        for step in range(steps_number):
            edge_costs.append(1)
        if number_of_algorithm == 1:
            recursive_solution = RecursiveSolution(edge_costs, memory_profiler=prof)
            recursive_solution.calculate_path_sum(steps_number)
        elif number_of_algorithm == 2:
            recursive_solution = RecursiveSolution(edge_costs, memory_profiler=prof)
            recursive_solution.calculate_path_sum_recursive(steps_number)
        else:
            calculate_brute_force(steps_number, edge_costs, prof)
        print(f"{steps_number}: {prof.get_sum_of_memory_values()} bytes")
        prof.clear_memory_value_holder()
