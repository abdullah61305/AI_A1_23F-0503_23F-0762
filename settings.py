import pygame

WIDTH, HEIGHT = 800, 800
ROWS = 20
SQUARE_SIZE = WIDTH // ROWS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
TURQUOISE = (64, 224, 208)
PURPLE = (128, 0, 128)
GREY = (128, 128, 128)

STRICT_MOVES = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (1, 1),
    (0, -1),
    (-1, -1)
]