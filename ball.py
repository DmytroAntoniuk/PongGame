from turtle import Turtle
from enum import Enum
import pong_field
from paddle import Side


class Axis(Enum):
    X = 1
    Y = 2


class Ball(Turtle):
    def __init__(self, right_paddle, left_paddle):
        super().__init__()
        self.right_paddle = right_paddle
        self.left_paddle = left_paddle
        self.moving_speed = 10
        self.x_direction = 1
        self.y_direction = 1
        self.size = 20
        self.setup_props()

    def setup_props(self):
        self.color("white")
        self.shape("circle")
        self.penup()

    def move(self):
        x = self.xcor()
        y = self.ycor()

        self.detect_collision_with_wall()
        self.detect_collision_with_paddle(self.left_paddle)
        self.detect_collision_with_paddle(self.right_paddle)

        new_x = self.xcor() + self.moving_speed * self.x_direction
        new_y = self.ycor() + self.moving_speed * self.y_direction
        self.goto(new_x, new_y)

    def detect_collision_with_wall(self):
        x = self.xcor()
        y = self.ycor()

        if (y > (pong_field.height / 2) - self.size) or (y < -(pong_field.height / 2 - self.size)):
            self.bounce(Axis.Y)

        if (x > (pong_field.width / 2) - self.size) or (x < -(pong_field.width / 2 - self.size)):
            self.bounce(Axis.X)

    def detect_collision_with_paddle(self, paddle):
        if paddle.side == Side.Right and self.distance(paddle) <= paddle.height and self.xcor() >= (paddle.xcor() - self.size):
            self.bounce(Axis.X)
        elif paddle.side == Side.Left and self.distance(paddle) <= paddle.height and self.xcor() <= (paddle.xcor() + self.size):
            self.bounce(Axis.X)

    def bounce(self, axis):
        if axis == Axis.X:
            self.x_direction *= -1
        elif axis == Axis.Y:
            self.y_direction *= -1

