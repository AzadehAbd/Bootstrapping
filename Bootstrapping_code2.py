# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 17:43:27 2022

@author: azade
"""


import numpy as np
import pandas as pd
import statistics
import matplotlib
import matplotlib.pyplot as plt

df= pd.read_excel("bootstrapping.xlsx")
print(df.head(3))


#here the name should change too
df.CS_F.hist(histtype="step")

print(df.describe())

#df.sample(1000,replace=True).describe()

Nboot= 10000
#below line should be adjusted 
factor=df[["CS_F"]]

def booststrap(x, Nboot, statfun):
    "calculate the bootstrap statistics for sample x"
    x=np.array(x)
    resampled_stat=[]

    for k in range (Nboot):
        index= np.random.randint(0, len(x), len(x))
        sample=x[index]
        bstatistic =  statfun(sample)
        resampled_stat.append(bstatistic)
    return np.array(resampled_stat)

testbootsrap= booststrap(factor, Nboot, np.mean)
plt.hist(testbootsrap, histtype="step")

plt.hist(testbootsrap, histtype="step")
#below line should be adjusted 
plt.axvline(df.CS_F.mean(), color="C1")


print(factor.mean())
print(np.mean(testbootsrap))
print(np.std(testbootsrap))
print(np.median(testbootsrap))
print(np.quantile(testbootsrap, 0.025))
print(np.quantile(testbootsrap, 0.975))
print(np.min(testbootsrap))
print(np.max(testbootsrap))


