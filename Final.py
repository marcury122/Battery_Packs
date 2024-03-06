import matplotlib.pyplot as plt

# Define constants
gen = [0, 0, 0, 2, 5, 6, 10, 4, 3, 0, 0, 0]
con = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 6]
maxBh = 5

# Initialize lists
bat = [0]*12
grid = [0]*12

# Calculate BH
BH = 0
for i in range(12):
    BH += gen[i] - con[i]
    if BH < 0:
        grid[i] = -BH
        BH = 0
    elif BH > maxBh:
        grid[i] = maxBh - BH
        BH = maxBh
    else:
        grid[i] = 0
    bat[i] = con[i] - gen[i] - grid[i]

# Plot bat and grid lists
plt.plot(bat, label="bat")
plt.plot(grid, label="grid")
plt.legend()
plt.xlabel("Time step")
plt.ylabel("Value")
plt.show()