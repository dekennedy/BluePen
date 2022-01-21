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

plt.boxplot(df['normal'])

# plt.show(block=True)



# %%

plt.figure()

Y = np.random.normal(loc=0.0, scale=1.0, size=10000)
X = np.random.random(size=10000)
plt.hist2d(X, Y, bins=25)
plt.colorbar()
plt.show()



# %%



plt.figure()
data = np.random.rand(10)
plt.plot(data)

def onclick(event):
    plt.cla()
    plt.plot(data)
    plt.gca().set_title('Event at pixels {},{} \nand data {},{}'.format(event.x, event.y, event.xdata, event.ydata))

# tell mpl_connect we want to pass a 'button_press_event' into onclick when the event is detected
plt.gcf().canvas.mpl_connect('button_press_event', onclick)


# %%


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
%matplotlib notebook





# generate 4 random variables from the random, gamma, exponential, and uniform distributions
x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000)+7
x4 = np.random.uniform(14,20, 10000)
x = [x1, x2, x3, x4]

# generate 4 subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharey = True)
ax = [ax1, ax2, ax3, ax4]

# generate 4 axises(xmin, xmax, ymin, ymax) for each graph
axis1 = [-7.5, 2.5, 0, 0.6]
axis2 = [0, 10, 0, 0.6]
axis3 = [7, 17, 0, 0.6]
axis4 = [14, 20, 0, 0.6]
axis = [axis1, axis2, axis3, axis4]

# generate 4 bins for each graph
bins1 = np.arange(-7.5, 2.5, 0.2)
bins2 = np.arange(0, 10, 0.2)
bins3 = np.arange(7, 17, 0.2)
bins4 = np.arange(12, 22, 0.2)
bins = [bins1, bins2, bins3, bins4]

# annotation positions
anno_x = [-1, 6.5, 13.5, 18]

# generate titles
titles = ["Normal", "Gamma", "Exponential", "Uniform"]


# create the function that will do the plotting, where curr is the current frame
def update(curr):

    # check if animation is at the last frame, and if so, stop the animation
    if curr == n:
        a.event_source.stop()
       
    # plot the histograms
    for i in range(len(ax)):
        ax[i].cla()
        ax[i].hist(x[i][:100*curr], normed = True, bins = bins[i])
        ax[i].axis(axis[i])
        ax[i].set_title(titles[i])
#         ax[i].set_ylabel('Probability')
#         ax[i].set_xlabel('Value')
        ax[i].annotate('n = {}'.format(100*curr), [anno_x[i], 0.5])
    plt.tight_layout()
   

a = animation.FuncAnimation(fig, update, interval=100)



# %%
