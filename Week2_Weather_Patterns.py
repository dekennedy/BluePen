#%%

##Example Chart Modifications. 


from matplotlib.axis import YAxis
import matplotlib.pyplot as plt
import numpy as np

plt.figure()

languages =['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]

# change the bar color to be less bright blue
bars = plt.bar(pos, popularity, align='center', linewidth=0, color='lightslategrey')

# make one bar, the python bar, a contrasting color
bars[0].set_color('#1F77B4')

# soften all labels by turning grey
plt.xticks(pos, languages, alpha=0.8)

# remove the Y label since bars are directly labeled
# plt.ylabel('% Popularity', alpha=0.8)

#Add title
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)

# # remove all the ticks (both axes), and tick labels on the Y axis
# plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')


plt.tick_params(
    axis='y',          # changes apply to the x-axis or y-axis
    which='both',      # both major and minor ticks are affected
    left=False,      # ticks along the bottom/Left edge are off
    right=False,         # ticks along the top/Right edge are off
    labelleft=False) # labels along the bottom edge are off


# remove the frame of the chart
for spine in plt.gca().spines.values():
    spine.set_visible(False)

    
# direct label each bar with Y axis values
for bar in bars:
    plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5, str(int(bar.get_height())) + '%', 
                 ha='center', color='w', fontsize=11)





plt.show()



# %%
