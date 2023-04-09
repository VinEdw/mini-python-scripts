import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set the intial conditions, final x, number of steps
x_0 = 0
y_0 = 0.5
x_f = 0.5
N = 10
# Calculate delta_x, the amount to nudge x each iteration
delta_x = (x_f - x_0) / N

# Set the first order differential equation f(x, y)
def f(x, y):
    return (x - y)**2

# Create an array for the x values
x = np.linspace(x_0, x_f, N+1)
# Create an empty array for the y values
y = np.zeros(N+1)
# Add the inital y value
y[0] = y_0

# Populate the y array recursively
# Formula: y_{i+1} = y_i + \Delta x * f(x_i, y_i)
for i in range(N):
    slope = f(x[i], y[i])
    y[i+1] = y[i] + slope * delta_x

# Plot the result
fig, ax = plt.subplots(1, 1)
ax.plot(x, y)
ax.set_xlabel("x")
ax.set_ylabel("y")
fig.show()

# Print the points
df = pd.DataFrame({"x": x, "y": y})
print(df)
