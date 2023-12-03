from turtle import Screen


class PongField:
    def __init__(self, paddle):
        self.instance = Screen()
        self.paddle = paddle
        self.setup_props()
        self.setup_signals()
        self.instance.exitonclick()

    def setup_props(self):
        self.instance.bgcolor("black")
        self.instance.setup(width=800, height=600)
        self.instance.title("Pong")

    def setup_signals(self):
        self.instance.listen()
        self.instance.onkey(self.paddle.go_up, "Up")
