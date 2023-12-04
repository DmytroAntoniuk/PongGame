from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.setup_props()

    def setup_props(self):
        self.color("white")
        self.shape("circle")
        self.penup()
        self.moving_speed = 10

    def move(self):
        self.goto(self.xcor() + self.moving_speed, self.ycor() + self.moving_speed)
