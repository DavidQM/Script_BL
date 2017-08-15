#!/usr/bin/env python
#  Importar librerias
# --------------------
import numpy as np
import matplotlib.pylab as plb
from pylab import *
import os, sys


#  Funcion "wavenumber"
# d --> depth
# f --> frecuencia
# ----------------------
def wavenumber(f, d, mode="hunt"):
	"""
	mode = "exact"
    Calculo del numero de onda usando la relacion de dispersion de la teoria
    lineal resuelta con un metodo iterativo (punto fijo) sin tener en cuenta
    el efecto doppler de las corrientes en la frecuencia de las olas.
            2
          w    =   g * k * tanh(k*h)    --->    w  = 2*pi*f
    
	mode = "hunt"  (default)
    Calculo del numero de onda usando la aproximacion empirica propuesta por Hunt 1979
              2        2             y
          (kh)    =   y   +  --------------------
                                   6
                                 ----      n
                             1 + \    d   y
                                 /     n
                                 ----
                                 n = 1
               2
          y = w  h  / g
          
          d0 = [0.666, 0.355, 0.161, 0.0632, 0.0218, 0.0065]
	"""
	
	if d < 0:
		raise ValueError("La profundidad debe ser mayor que cero (d > 0)")
	
	# checkear el argumento mode
	if mode == "exact":
		#
		tol = 1e-9
		maxiter = 1000000
		g = 9.8
		w = 2.* np.pi * f
		k0 = (w**2.)/g
		for cnt in xrange(maxiter):
			k = (w**2)/(g*np.tanh(k0*d))
			k0 = k
			if all(abs(k - k0) >= tol):
				return k0
		return k
	#
	elif mode == "hunt":
		#
		d0 = [0.666, 0.355, 0.161, 0.0632, 0.0218, 0.0065]
		g = 9.8
		w = 2.* np.pi * f
		y = (w**2)*d/g
		#
		poly = np.zeros_like(f)
		for n, dn in enumerate(d0):
			poly += dn*y**(n+1)
		#
		k = np.sqrt(y**2 + y/(1 + poly))/d

		return k
	#
	else:
		raise ValueError("mode debe ser 'hunt' o 'exact'")


#  Funcion "transfer_funcion"
# ----------------------------
def transfer_funcion(k, d, zp):
    """
    La funcion de transferencia se aplica para pasar el espectro de presion
    al espectro de superficie libre. Esta basada en la teoria lineal (Airy)
    
                    cosh(k*d)
            Kp = ----------------
                   cosh(k*zp)
    """
    
    Kp = np.cosh(k*d)/np.cosh(k*zp);
    Kp[Kp > 10] = 10;
    
    return Kp
