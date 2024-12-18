import matplotlib.pyplot as plt
from random_walk import RandomWalk
#from matplotlib import colormaps
#print(colormaps)


# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    ax.set_aspect('equal')
    plt.show()

    keep_running = input("Make another walk? [y/n]: ")
    if keep_running == 'n':
        break