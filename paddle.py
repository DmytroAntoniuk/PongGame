from enum import Enum
from turtle import Turtle


class Side(Enum):
    Right = 1
    Left = 2


class Paddle(Turtle):
    def __init__(self, position, side):
        super().__init__()
        self.side = side
        self.position = position
        self.setup_props()
        self.height = self.turtlesize()[0]*10

    def setup_props(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(self.position)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
