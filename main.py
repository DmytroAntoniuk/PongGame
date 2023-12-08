import time
from paddle import Paddle
from pong_field import PongField
from ball import Ball
from scoreboard import Scoreboard
from consts import Side


if __name__ == '__main__':
    right_paddle = Paddle((350, 0), Side.Right)
    left_paddle = Paddle((-350, 0), Side.Left)
    scoreboard = Scoreboard()
    ball = Ball(right_paddle, left_paddle, scoreboard)

    field = PongField(right_paddle, left_paddle)

    game_over = False
    while not game_over:
        time.sleep(0.1)
        field.update()
        ball.move()
