import os
from abc import ABC, abstractmethod
from typing import List, Tuple
from termcolor import colored
from schema.board import Board


class SolverStrategy(ABC):
    @abstractmethod
    def play(
        self, board: Board, states_graph: List, full_pipes: int, empty_pipes: int
    ) -> Tuple[List[Board], int]:
        pass


class UserSolverStrategy(SolverStrategy):
    def play(
        self, board: Board, states_graph: List, full_pipes: int, empty_pipes: int
    ) -> Tuple[List[Board], int] :
        print(board)
        cost = 0
        while not board.is_finished():

            states_graph.append(board.copy_current_state())
            try:
                actions = board.get_possible_actions()
                if len(actions) == 0:
                    print("Game over")
                    return states_graph
                print(f"possible actions (S,D):{actions}")
                source = int(input("Move a ball from: "))
                dest = int(input("To: "))
                if (
                    dest > full_pipes + empty_pipes
                    or source > full_pipes + empty_pipes
                    or source == dest
                ):
                    raise ValueError()
            except ValueError:
                print(colored("Bad input", "red"))
                continue
            if board.move(source, dest):
                cost += 1
                os.system("clear")
                print(board)
            else:
                print(colored("Incorrect movement", "red"))
        print(colored("You are Brilliant *_*", "green"))
        return states_graph, cost


class BFSSolverStrategy(SolverStrategy):
    def play(
        self, board: Board, states_graph: List, full_pipes: int, empty_pipes: int
    ) -> Tuple[List[Board], int]:
        bfs_queue = []
        bfs_queue.append(board.copy_current_state())
        is_finished = False
        cost = 0
        while  not is_finished and len(bfs_queue) > 0:
            current_state = bfs_queue.pop(0)
            states_graph.append(current_state)
            actions = current_state.get_possible_actions()
            if len(actions) == 0:
                continue
            for source, dest in actions:
                temp = current_state.copy_current_state()
                if temp.move(source, dest):
                    cost += 1
                    if temp.is_finished():
                        states_graph.append(temp)
                        is_finished = True
                        break
                    if not temp in bfs_queue:
                        bfs_queue.append(temp.copy_current_state())
        return states_graph, cost


class DFSSolverStrategy(SolverStrategy):
    def play(
        self, board: Board, states_graph: List, full_pipes: int, empty_pipes: int
    ) -> Tuple[List[Board], int]:
        dfs_stack = []
        dfs_stack.append(board.copy_current_state())
        is_finished = False
        cost = 0
        while  not is_finished and len(dfs_stack) > 0:
            current_state = dfs_stack.pop()
            states_graph.append(current_state)
            actions = current_state.get_possible_actions()
            if current_state.is_finished():
                return states_graph
            if len(actions) == 0:
                continue
            i = 1
            while i <= len(actions):
                temp = current_state.copy_current_state()
                if temp.move(actions[-i][0], actions[-i][1]):
                    if not temp in states_graph:
                        dfs_stack.append(temp.copy_current_state())
                cost += 1
                i += 1
        return states_graph, cost
