#!/usr/bin/env python3
#%%
import numpy as np
import matplotlib.pyplot as plt

#%%
ddata = np.load('dist_igatemi_farol.npy')
hdata = np.load('alturas_igatemi_farol.npy')
fresnel1 =  np.load('fresneltop.npy')
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
