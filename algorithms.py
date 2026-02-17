import pygame
import queue
from collections import deque
import heapq

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        if current is None:
            break
        if not current.is_start() and not current.is_end():
            current.make_path()
        draw()

def bfs(draw, grid, start, end):
    count = 0
    open_set = queue.Queue()
    open_set.put(start)
    came_from = {}
    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            return True

        for neighbor in current.neighbors:
            if neighbor not in came_from and neighbor != start:
                came_from[neighbor] = current
                open_set.put(neighbor)
                open_set_hash.add(neighbor)
                neighbor.make_open()

        draw()
        if current != start:
            current.make_closed()

    return False

def dfs(draw, grid, start, end):
    stack = [start]
    came_from = {}
    visited = {start}

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()

        current = stack.pop()

        if current == end:
            reconstruct_path(came_from, end, draw)
            return True

        for neighbor in reversed(current.neighbors):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                stack.append(neighbor)
                neighbor.make_open()

        draw()
        if current != start:
            current.make_closed()
            
    return False

def ucs(draw, grid, start, end):
    pq = []
    heapq.heappush(pq, (0, 0, start))
    came_from = {}
    cost_so_far = {start: 0}

    count = 0 
    
    while pq:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()

        current_cost, _, current = heapq.heappop(pq)

        if current == end:
            reconstruct_path(came_from, end, draw)
            return True

        for neighbor in current.neighbors:
            move_cost = 1.4 if abs(neighbor.row - current.row) + abs(neighbor.col - current.col) > 1 else 1
            new_cost = cost_so_far[current] + move_cost

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                count += 1
                heapq.heappush(pq, (new_cost, count, neighbor))
                came_from[neighbor] = current
                neighbor.make_open()

        draw()
        if current != start:
            current.make_closed()

    return False

def dls(draw, grid, start, end, limit):
    stack = [(start, 0)]
    came_from = {}
    visited_depth = {start: 0}

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()

        current, depth = stack.pop()

        if current == end:
            reconstruct_path(came_from, end, draw)
            return True

        if depth < limit:
            for neighbor in reversed(current.neighbors):
                if neighbor not in visited_depth or visited_depth[neighbor] > depth + 1:
                    visited_depth[neighbor] = depth + 1
                    came_from[neighbor] = current
                    stack.append((neighbor, depth + 1))
                    neighbor.make_open()

        draw()
        if current != start:
            current.make_closed()
            
    return False

def iddfs(draw, grid, start, end):
    limit = 0
    while True:
        if dls(draw, grid, start, end, limit):
            return True
        limit += 1
        if limit > 100: 
            return False

def bidirectional(draw, grid, start, end):
    q_start = deque([start])
    q_end = deque([end])
    
    came_from_start = {start: None}
    came_from_end = {end: None}
    
    while q_start and q_end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()

        if q_start:
            curr_s = q_start.popleft()
            
            if curr_s in came_from_end:
                reconstruct_path(came_from_start, curr_s, draw)
                reconstruct_path(came_from_end, curr_s, draw)
                return True
                
            for neighbor in curr_s.neighbors:
                if neighbor not in came_from_start:
                    came_from_start[neighbor] = curr_s
                    q_start.append(neighbor)
                    neighbor.make_open()
            
            if curr_s != start: curr_s.make_closed()

        if q_end:
            curr_e = q_end.popleft()
            
            if curr_e in came_from_start:
                reconstruct_path(came_from_start, curr_e, draw)
                reconstruct_path(came_from_end, curr_e, draw)
                return True

            for neighbor in curr_e.neighbors:
                if neighbor not in came_from_end:
                    came_from_end[neighbor] = curr_e
                    q_end.append(neighbor)
                    neighbor.make_open()
            
            if curr_e != end: curr_e.make_closed()

        draw()
        
    return False