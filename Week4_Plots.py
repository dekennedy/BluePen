#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# %%
# use the 'seaborn-colorblind' style
plt.style.use('seaborn-colorblind')
# %%
np.random.seed(123)

df = pd.DataFrame({'A': np.random.randn(365).cumsum(0), 
                   'B': np.random.randn(365).cumsum(0) + 20,
                   'C': np.random.randn(365).cumsum(0) - 20}, 
                  index=pd.date_range('1/1/2017', periods=365))
df.head()
# %%
df.plot(); # add a semi-colon to the end of the plotting call to suppress unwanted output
# %%
# create a scatter plot of columns 'A' and 'C', with changing color (c) and size (s) based on column 'B'
df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis')
# %%
df.plot.scatter('A', 'C', c='B', s=df['B'])
# %%
