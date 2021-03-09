import numpy as np
import matplotlib.pyplot as plt
import seaborn; seaborn.set()



m = np.random.rand(10, 2) # Create random array
plt.scatter(m[:, 0], m[:, 1], s=100) # Show scatter plot

# Compute differences between plots (sum of squared differences for each axis)
dist_sq = np.sum((m[:, np.newaxis, :] - m[np.newaxis, :, :]) ** 2, axis=-1)


# Differences between plots (long method)
differences = m[:, np.newaxis, :] - m[np.newaxis, :, :] # Find the difference between each axis
sq_difference = differences ** 2 # Square the differences


# Sum the coordinate differences to get the squared distance
dist_sq = sq_difference.sum(-1)


# Shows index postion of nearest neighbours (smallest value resulting
# from the sum of the previous step)
nearest  = np.argsort(dist_sq, axis=1)

# Previous step is a full sort but unnecessary as we're only interested
# in nearest neighbours. We can run partition sort instead.
K = 2
nearest_partition = np.argpartition(dist_sq, K + 1, axis = 1)

# Draw lines between the nearest location
plt.scatter (m[:, 0], m[:, 1], s=100)

K = 2

for i in range (m.shape[0]):
    for j in nearest_partition[i, :K+1]:
        # Plot a line from m[i] to m[j]
        # use zip 
        plt.plot(*zip(m[j], m[i]), color='black')
