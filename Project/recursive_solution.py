

class RecursiveSolution:
    def __init__(self, edge_costs, steps_amount=-1):
        if steps_amount < 0:
            self._steps_amount = len(edge_costs)
        else:
            self._steps_amount = steps_amount
        self._edge_costs = edge_costs
        pass

    def calculate_max_path(self, step):
        if step <= 0:
            return 0
        max_path = 0
        for index, edge_cost in zip(range(step), self._edge_costs):
            max_path = 2*max_path + 3*edge_cost
        return max_path

    def calculate_vertices_amount(self, step=None):
        if step is None:
            step = self._steps_amount
        return int((5/3)*(4**step)-(2/3))

    def calculate_border_sum(self, step):
        if step <= 0:
            return 0
        vertices_amount = self.calculate_vertices_amount(step-1)
        sum = 4*self.calculate_border_sum(step-1) + (3*vertices_amount+2)*self.calculate_max_path(step-1) + (8*vertices_amount+3)*self._edge_costs[step-1]
        return sum

    def calculate_path_sum(self, step):
        if step <= 0:
            return 0
        vertices_amount = self.calculate_vertices_amount(step-1)
        sum = 4*self.calculate_path_sum(step-1)+(12*vertices_amount+8)*self.calculate_border_sum(step-1)+(16*vertices_amount**2+12*vertices_amount+1)*self._edge_costs[step-1]
        return sum


def calculate_recursive(steps_number, edge_costs):
    recursive_solution = RecursiveSolution(edge_costs, steps_number)
    return recursive_solution.calculate_path_sum(steps_number)
