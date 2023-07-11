import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

GRID_SIZE = int(input("Size of grid: "))

NUM_GENERATIONS = int(input("Duration: "))

def make_grid(size):
    grid = np.random.choice([0, 1], size=(size, size), p=[0.5, 0.5])
    return grid


def neighbors(grid, i, j):
    neighbors = grid[max(0, i - 1):i + 2, max(0, j - 1):j + 2]
    count = int(np.sum(neighbors)) - int(grid[i, j])
    return count


def update_grid(grid):
    new_grid = np.copy(grid)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            count = neighbors(grid, i, j)
            if grid[i, j] == 1:
                if count < 2 or count > 3:
                    new_grid[i, j] = 0
            elif count == 3:
                new_grid[i, j] = 1
    return new_grid


def animate(grid):
    fig, ax = plt.subplots()
    ax.set_xticks([])
    ax.set_yticks([])
    img = ax.imshow(grid, cmap='binary')

    def update(frame):
        nonlocal grid
        grid = update_grid(grid)
        img.set_array(grid)
        return img,

    ani = animation.FuncAnimation(fig, update, frames=NUM_GENERATIONS, interval=200, blit=True)
    plt.show()


def main():
    grid = make_grid(GRID_SIZE)
    animate(grid)

if __name__ == "__main__":
    main()

