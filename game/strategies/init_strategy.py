from abc import ABC, abstractmethod
from typing import List
from random import choice

from schema.board import Board
from schema.pipe import Pipe
from schema.ball import Ball


class InitStrategy(ABC):
    def __init__(
        self,
        num_of_full_pipes: int,
        num_of_empty_pipe: int,
        max_balls_in_pipe: int,
        colors: List[str],
    ) -> None:
        self.num_of_full_pipes = num_of_full_pipes
        self.num_of_empty_pipe = num_of_empty_pipe
        self.max_balls_in_pipe = max_balls_in_pipe
        self.colors = colors

    @abstractmethod
    def initialize() -> Board:
        pass


class UserInitStrategy(InitStrategy):
    def __init__(
        self,
        num_of_full_pipes: int,
        num_of_empty_pipe: int,
        max_balls_in_pipe: int,
        colors: List[str],
    ) -> None:
        super().__init__(
            num_of_full_pipes, num_of_empty_pipe, max_balls_in_pipe, colors
        )

    def initialize() -> Board:
        # You can get initial state from user
        pass


class StaticInitStrategy(InitStrategy):
    def __init__(
        self,
        num_of_full_pipes: int,
        num_of_empty_pipe: int,
        max_balls_in_pipe: int,
        colors: List[str],
    ) -> None:
        super().__init__(
            num_of_full_pipes, num_of_empty_pipe, max_balls_in_pipe, colors
        )

    def initialize() -> Board:
        # You can set static (const) initial state
        pass


class RandomInitStrategy(InitStrategy):
    def __init__(
        self,
        num_of_full_pipes: int,
        num_of_empty_pipe: int,
        max_balls_in_pipe: int,
        colors: List[str],
    ) -> None:
        super().__init__(
            num_of_full_pipes, num_of_empty_pipe, max_balls_in_pipe, colors
        )

    def initialize(self) -> Board:
        pipes = self._init_pipes_randomly()
        board = Board(pipes, self.max_balls_in_pipe)
        return board

    def _init_pipes_randomly(self):
        balls_colors = self._init_balls_colors_randomly()
        pipes = []
        for i in range(self.num_of_full_pipes):
            pipe_balls = self._init_pipe_randomly(balls_colors)
            pipe = Pipe(pipe_balls, self.max_balls_in_pipe)
            pipes.append(pipe)
        for i in range(self.num_of_empty_pipe):
            empty_pipe = Pipe([], self.max_balls_in_pipe)
            pipes.append(empty_pipe)
        return pipes

    def _init_pipe_randomly(self, balls_color):
        pipe_balls = []
        for _ in range(self.max_balls_in_pipe):
            color = choice(balls_color)
            balls_color.remove(color)
            ball = Ball(color)
            pipe_balls.append(ball)
        return pipe_balls

    def _init_balls_colors_randomly(self):
        chosen_colors = []
        while len(chosen_colors) < self.num_of_full_pipes:
            c = choice(self.colors)
            if c not in chosen_colors:
                chosen_colors.append(c)
        balls_colors = chosen_colors * self.max_balls_in_pipe
        return balls_colors
