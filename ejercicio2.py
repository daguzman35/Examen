# Ejercicio 2 (20 puntos)
# Resuelva la ecuación de advección lineal d_t u + c d_x u = 0. 
# La condición inicial es una función gaussiana centrada en 0.0 y de sigma 0.1.
# La ecuación debe ser resuelta hasta un tiempo final T=0.5 y una velocidad c=-1.0.
# El programa debe hacer una gráfica (adveccion.png) con la condición incial y el resultado final.

import numpy as np

tfin=0.5
c=-1.0

miT=np.linspace(0,tfin)
miX=np.linspace(-10,10)

def miecu(dt,dx,u,c):
    return dt*u+c*dx
  
#Son las 3:59pm
