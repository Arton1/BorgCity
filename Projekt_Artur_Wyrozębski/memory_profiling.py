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

def get_input():
    print("Please, type in amount of target expansions")
    amount_of_target_expansions = int(input("Amount: "))
    print("Please, type in value of incrementing target expansion")
    krok = int(input("Step: "))
    return amount_of_target_expansions, krok

def random_costs(amount_of_target_expansions, incrementing_step):
    edge_cost = [random.randint(0, 25) for edge in range(incrementing_step*amount_of_target_expansions)]
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
    print("Please, type in number of steps")
    edge_cost = [1 for edge in range(11*incrementing_step)]
    return edge_cost

def print_table(values):
    pass

def profile(calculating_function):
    get_edge_costs = choose_type_of_input()
    amount_of_target_expansions, incrementing_step = get_input()
    edge_costs = get_edge_costs(amount_of_target_expansions, incrementing_step)
    values = []
    prof = memory_profiler()
    for step in range(incrementing_step, incrementing_step*amount_of_target_expansions+1, incrementing_step):
        calculating_function(step, edge_costs, memory_profiler=prof)
        values = [(step, prof.get_sum_of_memory_values())]
        prof.clear_memory_value_holder()
    print_table(values)
