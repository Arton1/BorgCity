from recursive_solution import RecursiveSolution
from graph import calculate_brute_force
import sys
import random

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

def get_input():
    print("Please, type in amount of target expansions")
    amount_of_target_expansions = int(input("Amount: "))
    print("Please, type in value of incrementing target expansion")
    krok = int(input("Step: "))
    return amount_of_target_expansions, krok

def random_costs(amount_of_target_expansions, incrementing_step):
    print("Please, type in range of randomness. Type in minimum, hit enter, then maximum")
    minimum = int(input("Min: "))
    maximum = int(input("Max: "))
    edge_cost = [random.randint(minimum, maximum) for edge in range(incrementing_step*amount_of_target_expansions)]
    return edge_cost

def choose_type_of_input():
    print("Please, choose type of input for algorithm.")
    print("1 - values for edges in all steps will be random from 0 to 25")
    print("2 - all values for edges in all steps will be 1.")
    number_of_algorithm = int(input("Option: "))
    if (number_of_algorithm == 1):
        func = random_costs
    elif number_of_algorithm == 2:
        func = only_ones
    return func

def only_ones(amount_of_target_expansions, incrementing_step):
    edge_cost = [1 for edge in range(amount_of_target_expansions*incrementing_step)]
    return edge_cost

def print_table(values, asymptote):
    median = int(len(values)/2)
    step, memory, result = values[median]
    factor = asymptote(step)/memory
    print("Step Bytes   q(n)    Result")
    for step, memory, result in values:
        print(f"{step:4} {memory:<7} {memory*factor/asymptote(step):<7.4f} {result:<}")

def profile(calculating_function, asymptote):
    get_edge_costs = choose_type_of_input()
    amount_of_target_expansions, incrementing_step = get_input()
    edge_costs = get_edge_costs(amount_of_target_expansions, incrementing_step)
    values = []
    prof = memory_profiler()
    for step in range(incrementing_step, incrementing_step*amount_of_target_expansions+1, incrementing_step):
        result = calculating_function(step, edge_costs, memory_profiler=prof)
        values.append((step, prof.get_sum_of_memory_values(), result))
        prof.clear_memory_value_holder()
    print_table(values, asymptote)
