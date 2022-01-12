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
