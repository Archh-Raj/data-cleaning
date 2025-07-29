import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def bar_plot_in_pandas(data, sources, groups):
    df = pd.DataFrame(zip(*data), index=sources, columns=groups)

    return df

young_people = [10, 12, 96, 40]
old_people = [90, 20,55,15]

sources = ['tv','Newspaper','Internet','Word of mouth']
groups = ['20-40','50-70']

df = bar_plot_in_pandas(data=[young_people, old_people], sources=sources, groups=groups)

#df.plot.bar() #normal bar plot

df.T.plot.bar() #Transposed bar plot
plt.show()
