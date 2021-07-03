import pandas as pd
import matplotlib.pyplot as plt

#import the CSV
top20_deathtoll = pd.read_csv('top20_deathtoll.csv')

#subplots initialize
fig, ax = plt.subplots(figsize=(4.5, 6))

#actual plot, height of the barh and color of the bar
ax.barh(top20_deathtoll['Country_Other'],
        top20_deathtoll['Total_Deaths'],
        height=0.45, color='#1d9ac9')

#pick the xtickmarks you want
ax.set_xticks([0, 150000, 300000])
#set a custom label if need be
ax.set_xticklabels(['0', '150,000', '300,000'])
#position of the xaxis
ax.xaxis.tick_top()
#color of the xaxis
ax.tick_params(axis='x', colors='grey')
#Remove the tick marks from the axes 
ax.tick_params(top=False, left=False)

#removing all ticks from the y-axis
ax.set_yticklabels([]) # an empty list removes the labels

#Left-indend the horizontal labels.
country_names = top20_deathtoll['Country_Other']
for i, country in zip(range(20), country_names):
    ax.text(x=-80000, y=i-0.15, s=country)

#Titles and subtitles for the graph
ax.text(x=-80000, y=23.5,
        s='The Death Toll Worldwide Is 1.5M+',
        weight='bold', size=17)
ax.text(x=-80000, y=22.5,
        s='Top 20 countries by death toll (December 2020)',
        size=12)

#removing the spines 
for location in ['left', 'right', 'top', 'bottom']:
    ax.spines[location].set_visible(False)

#Add a vertical line to better reference the mid point
ax.axvline(x=150000, ymin=0.045, c='grey', alpha=0.5)

#plot the graph
plt.show()