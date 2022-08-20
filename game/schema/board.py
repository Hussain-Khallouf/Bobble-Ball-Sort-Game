import copy

import os

from typing import List, Tuple
from .pipe import Pipe
from termcolor import colored


class Board:
    pipes: List[Pipe]

    def __init__(self, pipes: List[Pipe], max_balls_in_pipe: int):
        self.pipes = pipes
        self.max_balls_in_pipe = max_balls_in_pipe

    def __str__(self):
        stick = colored("|", "white", "on_white")
        print("\n" * 5)
        for i in range(self.max_balls_in_pipe):
            for pipe in self.pipes:
                if len(pipe.balls) >= self.max_balls_in_pipe - i:
                    print(
                        f"{stick}\t{colored('⬤',pipe[ self.max_balls_in_pipe -i -1])}\t{stick} ",
                        end=" ",
                    )
                else:
                    print(f"{stick}\t\t{stick} ", end=" ")
            print("")
        print(
            colored(" ============   " * len(self.pipes), "white", "on_white"), end=""
        )
        print(colored("_", "white", "on_white"))
        # print("_______________\t" * len(self.pipes))
        # print(colored("\t\t\t"*(settings.num_of_full_pipes+settings.num_of_empty_pipe),'white','on_white') )
        return ""

    def move(self, source: int, dest: int) -> bool:
        source_pipe = self.pipes[source - 1]
        dest_pipe = self.pipes[dest - 1]
        if self.is_movable(source, dest):
            ball = source_pipe.pop()
            dest_pipe.push(ball)
            return True
        else:
            return False

    def is_movable(self, source, dest) -> bool:
        if source == dest:
            return False
        source_pipe = self.pipes[source - 1]
        dest_pipe = self.pipes[dest - 1]
        source_head = source_pipe.get_pipe_head()
        return dest_pipe.is_pushable(source_head)

    def is_finished(self) -> bool:
        for pipe in self.pipes:
            if not (pipe.is_currectly_full() or pipe.is_empty()):
                return False
        return True

    def get_possible_actions(self) -> List[Tuple]:
        actions = []
        num_of_pip = len(self.pipes)
        for source in range(num_of_pip):
            if self.pipes[source].is_empty():
                continue
            for dest in range(source, num_of_pip):
                if self.is_movable(source + 1, dest + 1):
                    actions.append((source + 1, dest + 1))
        return actions

    def copy_current_state(self):
        return copy.deepcopy(self)

    def to_list(self):
        balls = []
        for pipe in self.pipes:
            balls.extend(pipe)
        return balls

    def __eq__(self, game_state):
        length = len(self.pipes)
        for i in range(length):
            if self.pipes[i] != game_state.pipes[i]:
                return False
        return True

        # for b1, b2 in zip(self.to_list(), game_state.to_list()):
        #     if b1 != b2:
        #         return False
        # return True
