import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

size = 5
global_grid = np.eye(size, dtype=int) + np.eye(size, dtype=int)[::-1]
global_grid[size // 2, size // 2] = 1

def update(grid):
    new_grid = np.zeros([size, size], dtype=int)
    for x in range(size):
        for y in range(size):
            if x == 0 or y == 0 or x == size - 1 or y == size - 1:
                new_grid[x, y] = 0 
            else:
                neighbour_count = grid[x - 1, y - 1] + grid[x - 1, y] + grid[x - 1, y + 1] + grid[x, y - 1] +\
                grid[x, y + 1] + grid[x + 1, y - 1] + grid[x + 1, y] + grid[x + 1, y + 1]
                if grid[x, y] == 1:
                    if neighbour_count == 2 or neighbour_count == 3:
                        new_grid[x, y] = 1
                else:
                    if neighbour_count == 3:
                        new_grid[x, y] = 1

    global global_grid
    global_grid = new_grid

fig, ax = plt.subplots()
im = ax.imshow(global_grid, cmap=colors.ListedColormap(["black","white"]))
fig.canvas.draw()
plt.pause(0.5)
while True:
    update(global_grid)
    im.set_data(global_grid)
    fig.canvas.draw()
    plt.pause(0.1)
