import os

from strategies.init_strategy import InitStrategy
from strategies.solver_strategy import SolverStrategy
from config.settings import settings


class BobbleBallSortGame:
    def __init__(
        self, init_strategy: InitStrategy, solver_strategy: SolverStrategy
    ) -> None:
        self._solver_strategy = solver_strategy
        self.borad = init_strategy.initialize()
        self.states_graph = []
        self.cost = 0

    def print_states_graph(self):
        os.system("clear")
        for state in self.states_graph:
            print(state)

    def print_solving_cost(self):
        print(f"The cost of the solution is: {self.cost}")

    def start(self):
        states_graph, cost = self._solver_strategy.play(
            self.borad,
            self.states_graph,
            settings.num_of_full_pipes,
            settings.num_of_empty_pipe,
        )
        self.states_graph = states_graph
        self.cost = cost
