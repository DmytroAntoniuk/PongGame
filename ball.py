from turtle import Turtle
import pong_field
from consts import Axis, Side


class Ball(Turtle):
    def __init__(self, right_paddle, left_paddle, scoreboard):
        super().__init__()
        self.right_paddle = right_paddle
        self.left_paddle = left_paddle
        self.scoreboard = scoreboard
        self.default_speed = 10
        self.moving_speed = self.default_speed
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

        self.detect_collision_with_sides()
        self.detect_collision_with_paddle(self.left_paddle)
        self.detect_collision_with_paddle(self.right_paddle)

        new_x = self.xcor() + self.moving_speed * self.x_direction
        new_y = self.ycor() + self.moving_speed * self.y_direction
        self.goto(new_x, new_y)

    def detect_collision_with_sides(self):
        if self.is_collision_with_top() or self.is_collision_with_bottom():
            self.bounce(Axis.Y)

        if self.is_collision_with_wall(Side.Left):
            self.scoreboard.increase_score(Side.Left)
            self.scoreboard.update()
            self.reset()
        elif self.is_collision_with_wall(Side.Right):
            self.scoreboard.increase_score(Side.Right)
            self.scoreboard.update()
            self.reset()

    def detect_collision_with_paddle(self, paddle):
        if paddle.side == Side.Right and self.distance(paddle) <= paddle.height and self.xcor() >= (
                paddle.xcor() - self.size):
            self.bounce(Axis.X)
        elif paddle.side == Side.Left and self.distance(paddle) <= paddle.height and self.xcor() <= (
                paddle.xcor() + self.size):
            self.bounce(Axis.X)

    def bounce(self, axis):
        if axis == Axis.X:
            self.x_direction *= -1
        elif axis == Axis.Y:
            self.y_direction *= -1
        self.moving_speed += 2

    def is_collision_with_wall(self, side):
        if side == Side.Right:
            return self.xcor() > (pong_field.width / 2) - self.size
        else:
            return self.xcor() < -(pong_field.width / 2 - self.size)

    def is_collision_with_top(self):
        return self.ycor() > (pong_field.height / 2) - self.size

    def is_collision_with_bottom(self):
        return self.ycor() < -(pong_field.height / 2 - self.size)

    def reset(self):
        self.reset_position()
        self.moving_speed = self.default_speed

    def reset_position(self):
        self.goto(0, 0)
        self.bounce(Axis.X)
