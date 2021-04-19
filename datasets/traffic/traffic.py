# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 19:52:25 2021

@author: chris
"""
import numpy as np
import pandas as pd
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(rc={'figure.figsize':(12,9)})

path = Path(__file__).parent.absolute()


df = pd.read_csv(path / 'traffic.csv')

#print(df.groupby('Junction').describe()['Vehicles'])
print("min time: ", df['DateTime'].min())
print("max time: ", df['DateTime'].max())

print(df.count())

df.set_index('DateTime',inplace=True)
df.index = pd.to_datetime(df.index)


sns.lineplot(x="DateTime", y="Vehicles",
             hue="Junction", data=df)
plt.show()

sns.lineplot(x="DateTime", y="Vehicles",
             hue="Junction", data=df[df.index > '2017-05-01'])
