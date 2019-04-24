#!/usr/bin/env python3
#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#%%
ddata = np.load('dist_igatemi_farol.npy')
hdata = np.load('alturas_igatemi_farol.npy')
fresnel1 = np.load('fresneltop.npy')
fresnel2 = np.load('fresnelbot.npy')
los = np.load('los.npy')
#%%
with plt.style.context('ggplot', True):
    plt.figure('perfil-topografico')
    plt.title('Perfil Toporáfico')
    plt.xlabel('Distância [km]')
    plt.ylabel('Altitude [m]')
    plt.plot(ddata, hdata)
    plt.plot(ddata, fresnel1, '-.')
    plt.plot(ddata, fresnel2, '-.')
    plt.plot(ddata, los)
    plt.savefig('perfil-topografico.png')
    plt.show()

#%%
df = pd.read_csv('tabela_radio.csv')

k = 1.333316759
f = 1e9

htx, hrx = 38, 38


x = np.array(df['x(km)'])
y = np.array(df['h(m)'])

hmax = max(y)
hmin = min(y)
print(hmax, hmin)
dist = x[-1] - x[0]
print(dist)
R = k * 6371e3
dx = x[-1]/(len(x) - 1)

# dm 10%
dh = int(0.1*hmax)
print(dh)

#%%
