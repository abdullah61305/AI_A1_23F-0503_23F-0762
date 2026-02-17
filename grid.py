import pygame
from settings import *

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self): return self.color == RED
    def is_open(self): return self.color == GREEN
    def is_barrier(self): return self.color == BLACK
    def is_start(self): return self.color == ORANGE
    def is_end(self): return self.color == TURQUOISE

    def make_closed(self): self.color = RED
    def make_open(self): self.color = GREEN
    def make_barrier(self): self.color = BLACK
    def make_start(self): self.color = ORANGE
    def make_end(self): self.color = TURQUOISE
    def make_path(self): self.color = PURPLE
    def reset(self): self.color = WHITE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        for dr, dc in STRICT_MOVES:
            nr, nc = self.row + dr, self.col + dc
            
            if 0 <= nr < self.total_rows and 0 <= nc < self.total_rows:
                if not grid[nr][nc].is_barrier():
                    self.neighbors.append(grid[nr][nc])

    def __lt__(self, other):
        return False