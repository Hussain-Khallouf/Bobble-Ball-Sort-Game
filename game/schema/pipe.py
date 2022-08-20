# this class demonstrate one pipe

import re
from typing import List
from .ball import Ball


class Pipe:
    def __init__(self, balls: List[Ball], max_balls_in_pipe: int):
        self.balls = balls
        self.max_balls_in_pipe = max_balls_in_pipe

    def __str__(self):
        for i in range(self.max_balls_in_pipe):
            if len(self.balls) >= self.max_balls_in_pipe - i:
                print(f" | {self.balls[self.max_balls_in_pipe - 1 - i ]} | ")
            else:
                print(" |   |")
        print("-------")
        return ""

    def __getitem__(self, i):
        return str(self.balls[i])

    def __eq__(self, other: object) -> bool:
        if len(self.balls) != len(other.balls):
            return False
        length = len(self.balls)
        for i in range(length):
            if self.balls[i] != other.balls[i]:
                return False
        return True

    def push(self, ball):
        self.balls.append(ball)
        return len(self.balls)

    def is_pushable(self, ball):
        return (
            self.is_empty() or ball.color == self.get_pipe_head().color
        ) and not self.is_full()

    def pop(self):
        return self.balls.pop()

    def get_pipe_head(self):
        if self.is_empty():
            return None
        return self.balls[len(self.balls) - 1]

    def is_full(self):
        return len(self.balls) == self.max_balls_in_pipe

    def is_same_color(self):
        color = self.balls[0].color
        for b in self.balls:
            if b.color != color:
                return False
        return True

    def is_currectly_full(self):
        return len(self.balls) == self.max_balls_in_pipe and self.is_same_color()

    def is_empty(self):
        return len(self.balls) == 0
