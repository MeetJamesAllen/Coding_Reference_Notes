import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

data = pd.read_csv("president_heights.csv")

heights = data['height(cm)']
print(heights)


print("Mean height: ", int(heights.mean()))
print("Standard deviation: ", heights.std())
print("Minimum height: ", heights.min())
print("Maximum height: ", heights.max())


print("25th percentile: ", np.percentile(heights, 25))
print("Median: ", np.median(heights))
print("75th persentile: ", np.percentile(heights, 75))


plt.hist(heights)
plt.title("Height Distribution Of US Presidents")
plt.xlabel("Height (cm)")
plt.ylabel("Number");