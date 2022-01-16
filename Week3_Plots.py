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

## add expo to the first plot
plt.subplot(1,2,1)
plt.plot(exponential_data, '-x')


# %%

##Lock Y axis
plt.figure()
ax1 = plt.subplot(1, 2, 1)
plt.plot(linear_data, '-o')
# pass sharey=ax1 to ensure the two subplots share the same y axis
ax2 = plt.subplot(1, 2, 2, sharey=ax1)
plt.plot(exponential_data, '-x')

# %%

##Histogram

import matplotlib.pyplot as plt
import numpy as np

# repeat with number of bins set to 100
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True)
axs = [ax1,ax2,ax3,ax4]

for n in range(0,len(axs)):
    sample_size = 10**(n+1)
    sample = np.random.normal(loc=0.0, scale=1.0, size=sample_size)
    axs[n].hist(sample, bins=100)
    axs[n].set_title('n={}'.format(sample_size))








# %%

##Box plot

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



normal_sample = np.random.normal(loc=0.0, scale=1.0, size=10000)
random_sample = np.random.random(size=10000)
gamma_sample = np.random.gamma(2, size=10000)

df = pd.DataFrame({'normal': normal_sample, 
                   'random': random_sample, 
                   'gamma': gamma_sample})



df.describe()                  





# %%

plt.figure()
# create a boxplot of the normal data, assign the output to a variable to supress output
_ = plt.boxplot(df['normal'])



# %%

plt.figure()
plt.hist(df['gamma'], bins=100)

plt.show

# %%
