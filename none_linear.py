import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
read = pd.read_csv("china_gdp.csv")
plt.figure(figsize = (8,5))
x_data, y_data = (read['Year'].values, read['Value'].values)
draw = plt.plot(x_data, y_data, 'bo')
plt.xlabel('Year')
plt.ylabel('GDP')
plt.show()
def sigmoid (x, beta_1, beta_2):
    y = 1 / (1 + np.exp(-beta_1 * (x - beta_2)))
    return y
xdata = x_data / max(x_data)
ydata = y_data / max(y_data)
print(xdata)
