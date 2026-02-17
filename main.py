import pygame
from settings import *
from grid import Node
from algorithms import bfs, dfs, ucs, dls, iddfs, bidirectional

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Pathfinder")

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    return grid

def draw_grid_lines(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (WIDTH, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, HEIGHT))

def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(win)
    draw_grid_lines(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col

def main():
    grid = make_grid(ROWS, WIDTH)
    start = None
    end = None
    run = True

    while run:
        draw(WIN, grid, ROWS, WIDTH)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]: 
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, WIDTH)
                node = grid[row][col]
                
                if not start and node != end:
                    start = node
                    start.make_start()
                elif not end and node != start:
                    end = node
                    end.make_end()
                elif node != end and node != start:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]: 
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, WIDTH)
                node = grid[row][col]
                node.reset()
                if node == start: start = None
                if node == end: end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, WIDTH)

                if start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    
                    draw_func = lambda: draw(WIN, grid, ROWS, WIDTH)

                    if event.key == pygame.K_1:
                        bfs(draw_func, grid, start, end)
                    elif event.key == pygame.K_2:
                        dfs(draw_func, grid, start, end)
                    elif event.key == pygame.K_3:
                        ucs(draw_func, grid, start, end)
                    elif event.key == pygame.K_4:
                        dls(draw_func, grid, start, end, 10)
                    elif event.key == pygame.K_5:
                        iddfs(draw_func, grid, start, end)
                    elif event.key == pygame.K_6:
                        bidirectional(draw_func, grid, start, end)

    pygame.quit()

if __name__ == "__main__":
    main()