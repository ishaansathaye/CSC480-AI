import tkinter as tk
import random
from collections import deque
import heapq
import argparse
import time

class TownMap:
    def __init__(self, master, size=10, block_density=0.2):
        self.master = master
        self.size = size
        self.block_density = block_density

        self.canvas = tk.Canvas(master, width=500, height=500, bg="white")
        self.canvas.pack()

        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        self.start = (0, 0)  # Start position is always top left
        self.goal = (size - 1, size - 1)  # Goal position is always bottom right
        self.generate_random_map()

        self.draw_map()

    def generate_random_map(self):
        for i in range(self.size):
            for j in range(self.size):
                if random.random() < self.block_density:
                    self.grid[i][j] = 1  # 1 represents a blocked cell

    def draw_map(self):
        cell_width = 500 / self.size
        cell_height = 500 / self.size

        for i in range(self.size):
            for j in range(self.size):
                x0, y0 = i * cell_width, j * cell_height
                x1, y1 = (i + 1) * cell_width, (j + 1) * cell_height

                if self.grid[j][i] == 1:  # Corrected indexing here
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="black", outline="black")
                else:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="black")

        # Draw start and goal positions
        for pos in [self.start, self.goal]:
            x0, y0 = pos[1] * cell_width, pos[0] * cell_height
            x1, y1 = (pos[1] + 1) * cell_width, (pos[0] + 1) * cell_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="red" if pos == self.goal else "green")

    def bfs(self):
        start_time = time.time()
        queue = deque([(self.start, [])])
        visited = set()
        expanded_nodes = 0

        while queue:
            current, path = queue.popleft()
            expanded_nodes += 1
            if current == self.goal:
                execution_time = time.time() - start_time
                return path + [current], expanded_nodes, execution_time

            if current not in visited:
                visited.add(current)
                neighbors = self.get_neighbors(current)
                for neighbor in neighbors:
                    queue.append((neighbor, path + [current]))

        return None, expanded_nodes, time.time() - start_time

    def dfs(self):
        start_time = time.time()
        stack = [(self.start, [])]
        visited = set()
        expanded_nodes = 0

        while stack:
            current, path = stack.pop()
            expanded_nodes += 1
            if current == self.goal:
                execution_time = time.time() - start_time
                return path + [current], expanded_nodes, execution_time

            if current not in visited:
                visited.add(current)
                neighbors = self.get_neighbors(current)
                for neighbor in neighbors:
                    stack.append((neighbor, path + [current]))

        return None, expanded_nodes, time.time() - start_time

    def uniform_cost_search(self):
        start_time = time.time()
        heap = [(0, self.start, [])]
        heapq.heapify(heap)
        visited = set()
        expanded_nodes = 0

        while heap:
            cost, current, path = heapq.heappop(heap)
            expanded_nodes += 1
            if current == self.goal:
                execution_time = time.time() - start_time
                return path + [current], expanded_nodes, execution_time

            if current not in visited:
                visited.add(current)
                neighbors = self.get_neighbors(current)
                for neighbor in neighbors:
                    heapq.heappush(heap, (cost + 1, neighbor, path + [current]))

        return None, expanded_nodes, time.time() - start_time

    def get_neighbors(self, cell):
        neighbors = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in directions:
            new_x, new_y = cell[0] + dx, cell[1] + dy
            if 0 <= new_x < self.size and 0 <= new_y < self.size and self.grid[new_x][new_y] != 1:
                neighbors.append((new_x, new_y))

        return neighbors

    def mark_path(self, path):
        cell_width = 500 / self.size
        cell_height = 500 / self.size

        for cell in path[1:-1]:  # Exclude start and end positions
            x0, y0 = cell[1] * cell_width, cell[0] * cell_height
            x1, y1 = (cell[1] + 1) * cell_width, (cell[0] + 1) * cell_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="yellow")

def main():
    parser = argparse.ArgumentParser(description="Run search algorithms on a town map.")
    parser.add_argument("--bfs", action="store_true", help="Run BFS algorithm")
    parser.add_argument("--dfs", action="store_true", help="Run DFS algorithm")
    parser.add_argument("--ucs", action="store_true", help="Run Uniform Cost Search algorithm")

    args = parser.parse_args()

    root = tk.Tk()
    root.title("Town Map")
    town_map = TownMap(root)
    
    if args.bfs:
        path, expanded_nodes, execution_time = town_map.bfs()
        if path:
            town_map.mark_path(path)
            print("BFS Path:", path)
            print("BFS Expanded Nodes:", expanded_nodes)
            print("BFS Execution Time:", execution_time)
        else:
            print("No path found.")

    if args.dfs:
        path, expanded_nodes, execution_time = town_map.dfs()
        if path:
            town_map.mark_path(path)
            print("DFS Path:", path)
            print("DFS Expanded Nodes:", expanded_nodes)
            print("DFS Execution Time:", execution_time)
        else:
            print("No path found.")

    if args.ucs:
        path, expanded_nodes, execution_time = town_map.uniform_cost_search()
        if path:
            town_map.mark_path(path)
            print("Uniform Cost Search Path:", path)
            print("Uniform Cost Search Expanded Nodes:", expanded_nodes)
            print("Uniform Cost Search Execution Time:", execution_time)
        else:
            print("No path found.")

    root.mainloop()

if __name__ == "__main__":
    main()
