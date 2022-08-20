import os

from strategies.solver_strategy import (
    UserSolverStrategy,
    BFSSolverStrategy,
    DFSSolverStrategy,
)
from strategies.init_strategy import RandomInitStrategy
from bobble_ball_sort_game import BobbleBallSortGame
from config.settings import settings


solvers = {
    "user": UserSolverStrategy(),
    "bfs": BFSSolverStrategy(),
    "dfs": DFSSolverStrategy(),
}


def welcome():
    os.system("clear")
    print("Welcome To Bobble Ball Sort Game@_@.")
    print("The mission is: Sorting balls with the same color in one pipe.\n")
    


def get_solver_from_user():
    while True:
        print("Please choose the game solver")
        print("User Solver (user)")
        print("BFS algorithm Solver (bfs)")
        print("DFS algorithm Solver (dfs)")
        user_input = input()
        solver = solvers.get(user_input, None)
        if solver != None:
            return solver
        print(
            "Bad input! Please try again (choose a solver name whith it is in bracts.)"
        )

def main():
    welcome()
    solver = get_solver_from_user()
    # getint the initializer from user is in the next version
    initializer = RandomInitStrategy(
        settings.num_of_full_pipes,
        settings.num_of_empty_pipe,
        settings.max_balls_in_pipe,
        settings.colors,
    )
    game = BobbleBallSortGame(initializer, solver)
    game.start()
    user_input = input("Do you want to print all movements? (y/n)")
    if user_input.lower() == "y":
        game.print_states_graph()
        game.print_solving_cost()
    print("Thank you.")


main()
