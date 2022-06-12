# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 17:32:07 2022

@author: azade
"""

import math
import io
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as pp
import scipy.stats
import scipy.optimize
import scipy.spatial


pop = pd.read_excel("bootstrapping.xlsx")
#in console
pop.head()

pop.hist(histtype='step')

#in console
pop.describe()

pop.sample(100,replace=True).describe()
bootstrap = pd.DataFrame({'resamplemean': [pop.sample(100,replace=True).H_TLS.mean() for i in range(1000)]})

#in console
bootstrap.resamplemean.hist(histtype='step')
pp.axvline(pop.H_TLS.mean(),color='C1')

print(bootstrap.resamplemean.quantile(0.025), bootstrap.resamplemean.quantile(0.975))

n1 = scipy.stats.norm(7.5,1)
n2 = scipy.stats.norm(4,1)

#in console
x = np.linspace(0,10,100)
pp.plot(x,0.5*n1.pdf(x) + 0.5*n2.pdf(x))

def draw():
    while True:
        v = n1.rvs() if np.random.rand() < 0.5 else n2.rvs()
        if 0 <= v <= 10:
            return v
print(draw())


def dataset(n=100):
    return pd.DataFrame({'H_TLS': [draw() for i in range(n)]})
#in console
for i in range(5):
    dataset(100).H_TLS.hist(histtype='step',density=True)


means = pd.DataFrame({'resamplemean': [dataset(100).H_TLS.mean() for i in range(1000)]})

#in console
means.resamplemean.hist(histtype='step')
bootstrap.resamplemean.hist(histtype='step')


