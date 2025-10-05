import os

import matplotlib.pyplot as plt

from random_walk import RandomWalk

counter = 1
while True:
    # Make a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fix, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values,
               rw.y_values,
               c=point_numbers,
               cmap=plt.cm.Blues,
               edgecolors='none',
               s=1)
    ax.set_aspect('equal')

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1],
               rw.y_values[-1],
               c='red',
               edgecolors='none',
               s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # plt.show()
    file_name = f"random_walk_{counter}.png"
    if os.path.exists(file_name):
        os.remove(file_name)
    plt.savefig(file_name, bbox_inches='tight')

    keep_running = input(f"Walk Total: {counter} - Make another walk?(y/n): ")
    if keep_running == 'n':
        break
    counter += 1
