# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 19:52:25 2021

@author: chris
"""
import numpy as np
import pandas as pd
from pathlib import Path
import seaborn as sns

path = Path(__file__).parent.absolute()


df = pd.read_csv(path / 'traffic.csv')

#print(df.groupby('Junction').describe()['Vehicles'])
print("min time: ", df['DateTime'].min())
print("max time: ", df['DateTime'].max())

print(df.count())

df.set_index('DateTime',inplace=True)
df.index = pd.to_datetime(df.index)

df_week = df.resample('W').sum()

sns.histplot(df_week,x='DateTime',y='Vehicles')
