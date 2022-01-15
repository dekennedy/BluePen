#%%

#imports

import imp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



plt.figure()

# subplot with 1 row, 2 columns, and current axis is 1st subplot axes
plt.subplot(1, 2, 1)

linear_data = np.array([1,2,3,4,5,6,7,8])

plt.plot(linear_data, '-o')

#define Exponential_data
exponential_data = linear_data**2

#Rows, Columns, Plot number

# Plot number 2
plt.subplot(1,2,2)
plt.plot(exponential_data, '-o')







# %%
