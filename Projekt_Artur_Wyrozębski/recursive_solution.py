import decimal
from decimal import Decimal
from fractions import Fraction

class RecursiveSolution:
    def __init__(self, edge_costs, steps_amount=-1, memory_profiler=None):
        if steps_amount < 0:
            self._steps_amount = len(edge_costs)
        else:
            self._steps_amount = steps_amount
        self._edge_costs = edge_costs
        self._memory_profiler = memory_profiler

    def calculate_max_path(self, step):
        if step <= 0:
            return 0
        max_path = Decimal()
        for index, edge_cost in zip(range(step), self._edge_costs):
            max_path = Decimal(2*max_path + 3*Decimal(edge_cost))
        return max_path
    def calculate_vertices_amount(self, step=None):
        if step is None:
            step = Decimal(self._steps_amount)
        return Decimal(int((Fraction(numerator=5, denominator=3)*(4**step)-Fraction(numerator=2,denominator=3))))

    def calculate_border_sum(self, step):
        if step <= 0:
            return Decimal()
        vertices_amount = self.calculate_vertices_amount(step-1)
        sum = Decimal(4*self.calculate_border_sum(step-1) + Decimal(3*vertices_amount+2)*self.calculate_max_path(step-1) + Decimal(8*vertices_amount+3)*self._edge_costs[step-1])
        return sum

    def calculate_path_sum_recursive(self, step):
        if step <= 0:
            return Decimal()
        vertices_amount = Decimal(self.calculate_vertices_amount(step-1))
        sum = Decimal(Decimal(4)*self.calculate_path_sum_recursive(step-1)+Decimal(12*vertices_amount+8)*self.calculate_border_sum(step-1)+(16*Decimal(vertices_amount**Decimal(2))+Decimal(12)*vertices_amount+Decimal(1))*self._edge_costs[step-1])
        if self._memory_profiler:
            self._memory_profiler.save_memory_values(sum, vertices_amount, step)
        return sum

    def calculate_path_sum(self, amount_of_steps):
        sum = Decimal()
        power = decimal.Decimal(decimal.Decimal(4)**decimal.Decimal(amount_of_steps-1))
        vertices_amount = decimal.Decimal(1)
        border_sum = decimal.Decimal()
        max_path = decimal.Decimal()
        for step in range(1, amount_of_steps+1):
            sum += decimal.Decimal(power*((12*vertices_amount+8)*border_sum + ((16*(vertices_amount**2) + 12*vertices_amount + 1)*self._edge_costs[step-1])))
            power = power / decimal.Decimal(4)
            border_sum = 4*border_sum + (3*vertices_amount+2)*max_path + (8*vertices_amount+3)*self._edge_costs[step-1]
            max_path = 2*max_path + 3*self._edge_costs[step-1]
            vertices_amount = 4*vertices_amount+2
        if self._memory_profiler:
            self._memory_profiler.save_memory_values(sum, power, vertices_amount, border_sum, max_path)
        return sum


def calculate_recursively(steps_number, edge_costs, memory_profiler=None):
    context = decimal.Context(prec=50)
    decimal.setcontext(context)
    recursive_solution = RecursiveSolution(edge_costs, steps_number, memory_profiler)
    return recursive_solution.calculate_path_sum_recursive(steps_number)


def calculate_iteratively(steps_number, edge_costs, memory_profiler=None):
    context = decimal.Context(prec=50)
    decimal.setcontext(context)
    recursive_solution = RecursiveSolution(edge_costs, steps_number, memory_profiler)
    return recursive_solution.calculate_path_sum(steps_number)
