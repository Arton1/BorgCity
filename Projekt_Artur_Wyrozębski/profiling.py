import cProfile, pstats
import recursive_solution
import graph
import random

def get_input():
    print("Please, type in amount of target expansions")
    amount_of_target_expansions = int(input("Amount: "))
    print("Please, type in value of incrementing target expansion")
    krok = int(input("Step: "))
    print("Please, type in amount of calculations per target expansion")
    amount_of_calculations = int(input("Amount: "))
    return amount_of_target_expansions, krok, amount_of_calculations

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
    step, time, result = values[median]
    factor = asymptote(step)/time
    print("Step Time    q(n)    Result")
    for step, time, result in values:
        print(f"{step:4} {time:<5.5f} {time*factor/asymptote(step):<7.4f} {result:<}")

def profile(calculating_function, asymptote):
    profiler = cProfile.Profile()
    get_edge_costs = choose_type_of_input()
    amount_of_target_expansions, incrementing_step, amount_of_calculations = get_input()
    edge_costs = get_edge_costs(amount_of_target_expansions, incrementing_step)
    values = []
    for step in range(incrementing_step, incrementing_step*amount_of_target_expansions+1, incrementing_step):
        profiler.enable()
        for calculation in range(amount_of_calculations):
            result = calculating_function(step, edge_costs)
        profiler.disable()
        stats = pstats.Stats(profiler)
        values.append((step, stats.total_tt/amount_of_calculations, result))
        profiler.clear()
    print_table(values, asymptote)