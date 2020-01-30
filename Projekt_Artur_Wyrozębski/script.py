from recursive_solution import calculate_recursively, calculate_iteratively
from graph import calculate_brute_force
import sys
import random
import profiling
import memory_profiling

def choose_algorithm():
    print("Please, type in number of algorithm that you want")
    print("1 - algorithm using iterative formulas")
    print("2 - algorithm using recursive formulas")
    print("3 - algorithm using Depth First Search")
    number_of_algorithm = int(input("Option: ")) 
    if( number_of_algorithm == 1):
        calculating_function = calculate_iteratively
        time_asymptote = lambda x: x
        memory_asymptote = lambda x: 1
    elif (number_of_algorithm == 2):
        calculating_function = calculate_recursively
        time_asymptote = lambda x: x**2
        memory_asymptote = lambda x: x
    else:
        calculating_function = calculate_brute_force
        time_asymptote = lambda x: (4**x)**2
        memory_asymptote = lambda x: 4**x
    return calculating_function, time_asymptote, memory_asymptote

def choose_type_of_input():
    print("Please, choose type of input for algorithm.")
    print("1 - type in amount of steps and values for edges")
    print("2 - type in amount of steps. Values for edges in all steps will be random from 0 to 25")
    print("3 - type in amount of steps. All values for edges in all steps will be 1.")
    number_of_algorithm = int(input("Option: "))
    if(number_of_algorithm == 1):
        func = get_input_for_algorithm
    elif (number_of_algorithm == 2):
        func = random_input
    else:
        func = only_ones
    return func

def get_input_for_algorithm():
    print("Please, type in number of steps, hit enter and then values for edges: ")
    steps_number = int(input("Steps: "))
    edge_cost = list(map(int, input("Edges: ").strip().split(sep='')[:steps_number]))
    if(len(edge_cost) != steps_number):
        raise Exception("Please, type in the same amount of values as there are steps")
    return edge_cost

def random_input():
    print("Please, type in number of steps")
    steps_number = int(input("Steps: "))
    print("Please, type in range of randomness. Type in minimum, hit enter, then maximum")
    minimum = int(input("Min: "))
    maximum = int(input("Max: "))
    edge_cost = [random.randint(minimum, maximum) for edge in range(steps_number)]
    print(f"Edge costs: {edge_cost}")
    return edge_cost

def only_ones():
    print("Please, type in number of steps")
    steps_number = int(input("Steps: "))
    edge_cost = [1 for edge in range(steps_number)]
    return edge_cost

def get_result(calculating_function):
    get_edge_costs = choose_type_of_input()
    edge_cost = get_edge_costs()
    print(calculating_function(len(edge_cost), edge_cost))

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    print("BORG CITY")
    print("Please, choose what you want to do. Type in the number.")
    print("1 - get a result from input")
    print("2 - profile execution time")
    print("3 - profile memory consumption")
    option = int(input("Option: "))
    calculating_function, time_asymptote, memory_asymptote = choose_algorithm()
    if option == 1:
        get_result(calculating_function)
    elif option == 2:
        profiling.profile(calculating_function, time_asymptote)
    elif option == 3:
        memory_profiling.profile(calculating_function, memory_asymptote)