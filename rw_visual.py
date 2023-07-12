import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
 # Make a random walk.   
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig,ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    #ax.scatter(rw.x_vals, rw.y_vals, s=1, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none')
    ax.plot(rw.x_vals, rw.y_vals, linewidth=1 )

    # Emphasize the first and last points.
    ax.scatter(0,0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_vals[-1], rw.y_vals[-1], c='red', edgecolors='none', s=100)

    # Remove the axes.
    ax.xaxis.set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break


