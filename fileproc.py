#!/usr/bin/env python3
#%%
import numpy as np
import matplotlib.pyplot as plt
import csv
# %matplotlib qt

dado = np.zeros(2001)
data = np.zeros(2001)
with open('profile_demo.txt', 'r+') as f:
    r = csv.reader(f, delimiter='\t')
    r = list(r)
    for i in range(len(r)):
        data[i] = float(r[i][11])
        dado[i] = float(r[i][9])


#%%
plt.plot(data+dado)
plt.plot(-data+dado)
plt.plot(dado)
plt.show()
#%%
np.save('fresneltop', data+dado)
np.save('fresnelbot', -data+dado)
np.save('los', dado)