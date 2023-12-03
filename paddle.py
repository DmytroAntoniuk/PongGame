from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(350, 0)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)
