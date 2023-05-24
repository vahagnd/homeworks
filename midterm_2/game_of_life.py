import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

global_grid = np.eye(5, dtype=int) + np.eye(5, dtype=int)[::-1]
global_grid[2, 2] = 1
global_grid = np.pad(global_grid, (15, 15))

size = global_grid.shape[0]

def update(grid):
    new_grid = np.zeros([size, size], dtype=int)
    temp_grid = np.pad(grid, (1, 1))
    for x in range(1, size + 1):
        for y in range(1, size + 1):
            neighbour_count = temp_grid[x - 1, y - 1] + temp_grid[x - 1, y] + temp_grid[x - 1, y + 1] + temp_grid[x, y - 1] +\
            temp_grid[x, y + 1] + temp_grid[x + 1, y - 1] + temp_grid[x + 1, y] + temp_grid[x + 1, y + 1]
            if grid[x - 1, y - 1] == 1:
                if neighbour_count == 2 or neighbour_count == 3:
                    new_grid[x - 1, y - 1] = 1
            else:
                if neighbour_count == 3:
                    new_grid[x - 1, y - 1] = 1
    global global_grid
    global_grid = new_grid


fig, ax = plt.subplots()
im = ax.imshow(global_grid, cmap=colors.ListedColormap(["black","white"]))
fig.canvas.draw()
plt.pause(1)
while True:
    update(global_grid)
    im.set_data(global_grid)
    fig.canvas.draw()
    plt.pause(1)
