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
from scipy.optimize import curve_fit
popt, pcov = curve_fit(sigmoid, xdata, ydata)
print(f"beta_1 is : {popt[0]} and beta_2 is : {popt[1]}")
x = np.linspace(1960, 2015, 55)
x = x / max(x)
plt.figure(figsize = (8, 5))
y = sigmoid(x, *popt)
plt.plot(xdata, ydata , 'ro', label = 'data')
plt.plot(x,y, linewidth = 3, label = 'fit')
plt.legend(loc = 'best')
plt.ylabel('GDP')
plt.xlabel('Year')
plt.show()


