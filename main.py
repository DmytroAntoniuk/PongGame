from paddle import Paddle
from pong_field import PongField

if __name__ == '__main__':
    right_paddle = Paddle((350, 0))
    left_paddle = Paddle((-350, 0))

    field = PongField(right_paddle, left_paddle)

    game_over = False
    while not game_over:
        field.update()
