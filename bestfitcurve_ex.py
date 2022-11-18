# Importing the necessary libraries
from matplotlib import pyplot as plt
import numpy as np

# Preparing the data to be computed and plotted
dt = np.array([
          [0.5, 0.28],
          [0.5, 0.29],
          [0.5, 0.33],
          [0.7, 0.21],
          [0.7, 0.23],
          [0.7, 0.26],
          [0.8, 0.24],
          [0.8, 0.25],
          [0.8, 0.29],
          [0.9, 0.28],
          [0.9, 0.30],
          [0.9, 0.31],
          [1.0, 0.30],
          [1.0, 0.33],
          [1.0, 0.35]
])

# Preparing X and y from the given data
X = dt[:, 0]
y = dt[:, 1]

# Calculating parameters (theta0, theta1 and theta2)
# of the 2nd degree curve using the numpy.polyfit() function
theta = np.polyfit(X, y, 2)

print(f'The parameters of the curve: {theta}')

# Now, calculating the y-axis values against x-values according to
# the parameters theta0, theta1 and theta2
y_line = theta[2] + theta[1] * pow(X, 1) + theta[0] * pow(X, 2)

# Plotting the data points and the best fit 2nd degree curve
plt.scatter(X, y)
plt.plot(X, y_line, 'r')
plt.title('2nd degree best fit curve using numpy.polyfit()')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()