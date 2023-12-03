from turtle import Screen


class PongField:
    def __init__(self, right_paddle, left_paddle):
        self.instance = Screen()
        self.right_paddle = right_paddle
        self.left_paddle = left_paddle
        self.setup_props()
        self.setup_signals()

    def setup_props(self):
        self.instance.bgcolor("black")
        self.instance.setup(width=800, height=600)
        self.instance.title("Pong")

    def setup_signals(self):
        self.instance.listen()
        self.setup_right_paddle_signals()
        self.setup_left_paddle_signals()

    def setup_right_paddle_signals(self):
        self.instance.onkey(self.right_paddle.go_up, "Up")
        self.instance.onkey(self.right_paddle.go_down, "Down")

    def setup_left_paddle_signals(self):
        self.instance.onkey(self.left_paddle.go_up, "w")
        self.instance.onkey(self.left_paddle.go_down, "s")

    def update(self):
        self.instance.update()
