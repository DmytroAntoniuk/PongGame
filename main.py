import time

from paddle import Paddle
from pong_field import PongField
from ball import Ball

if __name__ == '__main__':
    right_paddle = Paddle((350, 0))
    left_paddle = Paddle((-350, 0))
    ball = Ball()

    field = PongField(right_paddle, left_paddle)

    game_over = False
    while not game_over:
        time.sleep(0.1)
        field.update()
        ball.move()
