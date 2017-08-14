#!/usr/bin/env python
"""
------------------------------
 Autor  : Daniel S. Pelaez Z.
 e-mail : dspelaez@unal.edu.co
 Fecha  : Marzo, 2014
 Lugar  : Medellin
------------------------------
"""
#  Importar librerias
# --------------------
import numpy as np
import matplotlib.pylab as plb
from pylab import *
import transfer_funcion as TransFun
import os, sys

#  Funcion "zero_crossing"
# -------------------------
def zero_crossing(t, x, d, zp):
    # Calculos de los puntos
    # ----------------------
    # Re-muestro del vector
    tt = np.linspace(t[0], t[-1], len(t)*100)
    xx = np.interp(tt, t, x)
    
    # Encontrar el indice con los ceros
    ix     = np.diff(np.sign(xx))
    ix_up, = np.where(ix > 0)

    # Encontrar la altura y el periodo de cada ola
    H, T = np.zeros(len(ix_up)-1), np.zeros(len(ix_up)-1)
    for i in range(len(ix_up) - 1):
        a = ix_up[i]
        b = ix_up[i+1]
        H[i] = xx[a:b].max() - xx[a:b].min()
        T[i] = tt[b] - tt[a]
    
    # Calculos de los parametros
    # --------------------------
    #H0 = np.sort(H)#daniel santiago
    f=1.0/T
    K=TransFun.wavenumber(f,d,"hunt")
    Kp=TransFun.transfer_funcion(K,d,zp)
    Hc=H*Kp;
    H0 = np.sort(Hc)#victor & david 14 de agosto 2016
    Hz = H0[2*len(H)/3:].mean()

    Tz = np.mean(T)

    return Hz, Tz
