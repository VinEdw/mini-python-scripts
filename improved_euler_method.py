import numpy as np
import pandas as pd

# Set the initial conditions, final x, number of steps
x_0 = 0.0
y_0 = 1.0
x_f = 1.0
N = 10
# Calculate delta_x, the amount to nudge x each iteration
delta_x = (x_f - x_0) / N

# Set the first order differential equation f(x, y)
def f(x, y):
    return y - x**2 + 2*x

# Create an array for the x values
x = np.linspace(x_0, x_f, N+1)
# Create an empty array for the y values
y = np.zeros(N+1)
# Add the initial y value
y[0] = y_0

# Populate the y array recursively
# Formula: y_{i+1} = y_i + \Delta x * f(x_i, y_i)
for i in range(N):
    slope_1 = f(x[i], y[i])
    slope_2 = f(x[i+1], y[i] + delta_x*slope_1)
    slope_avg = (slope_1 + slope_2)/2
    y[i+1] = y[i] + slope_avg * delta_x

# Create a dataframe
df = pd.DataFrame({"x": x, "y": y})
# Calculate the theoretical values and the global truncation error
df["y_th"] = np.exp(df.x) + df.x**2
df["GTE"] = df.y_th - df.y
# Print the data
print(df)
