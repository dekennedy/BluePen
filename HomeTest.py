#%%

print('Hello')

import pandas as pd

df = pd.read_csv(r'/Users/davidkennedy/Downloads/Development_Plans.csv')

print(df)
# %%

#packages
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


linear_data = np.array([1,2,3,4,5,6,7,8])
exponential_data = linear_data**2


plt.figure()
observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')

##map to_datatime
observation_dates = list(map(pd.to_datetime, observation_dates)) # convert the map to a list to get rid of the error
plt.plot(observation_dates, linear_data, '-o',  observation_dates, exponential_data, '-o')


x = plt.gca().xaxis

# rotate the tick labels for the x axis
for item in x.get_ticklabels():
    item.set_rotation(45)




# %%

#Bar Charts

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


linear_data = np.array([1,2,3,4,5,6,7,8])
exponential_data = linear_data**2

plt.figure()
xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width=0.3)


#add new Bars

new_xvals = []

for v in xvals:
    new_xvals.append(v+0.3)

plt.bar(new_xvals, exponential_data, width= 0.3, color = 'red')




# %%


#add new Bars

new_xvals = []

for v in xvals:
    new_xvals.append(v+.03)

plt.bar(new_xvals, exponential_data, width= 0.3, color = 'red')




# %%


# stacked bar charts are also possible
plt.figure()
xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width = 0.3, color='b')
plt.bar(xvals, exponential_data, width = 0.3, bottom=linear_data, color='r')

# %%

# or use barh for horizontal bar charts
plt.figure()
xvals = range(len(linear_data))
plt.barh(xvals, linear_data, height = 0.3, color='b')
plt.barh(xvals, exponential_data, height = 0.3, left=linear_data, color='r')


## testing update


# %%


plt.figure()
xvals = range(len(linear_data))
plt.barh(xvals, linear_data, height = 0.3, color='b')

new_xvals = []

for v in xvals:
    new_xvals.append(v+0.3)


plt.barh(new_xvals, exponential_data, height = 0.3, color='r')





# %%
