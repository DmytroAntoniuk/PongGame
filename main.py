import time

from paddle import Paddle, Side
from pong_field import PongField
from ball import Ball

if __name__ == '__main__':
    right_paddle = Paddle((350, 0), Side.Right)
    left_paddle = Paddle((-350, 0), Side.Left)

    ball = Ball(right_paddle, left_paddle)

    field = PongField(right_paddle, left_paddle)

    game_over = False
    while not game_over:
        time.sleep(0.1)
        field.update()
        ball.move()
