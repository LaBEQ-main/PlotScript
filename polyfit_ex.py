import numpy as np
import matplotlib.pyplot as plt

plt.figure()
poly = np.polyfit(list_x,list_y,5)
poly_y = np.poly1d(poly)(list_x)
plt.plot(list_x,poly_y)
plt.plot(list_x,list_y)
plt.show()