# Ejercicio 1 (10 puntos)
# Calcule integral de exp(x) entre 0 y 1 con el método de trapecio y de Simpson.
# Haga una grafica (error.png) del error fraccional entre la solución numérica y 
# analítica como funcion del numero de puntos (desde N=10 hasta N=10^8). 
# Tanto el error como el numero de puntos deben variar en escala logaritmica.


# David Guzman
# 2018-06-18

import numpy as np

def areatrapecio(base,h1,h2):
    promh=(h1+h2)/2.0
    return base*promh

def integralTrapecio(N):
    liminf=0
    limsup=1
    #N=10  #pasos entran por parametro
    
    N=int(N)  #aseguro que N sea un entero

    mivec=np.linspace(liminf,limsup,N)  #coordenadas x, entre 0 y 1, con N pasos
    mivecsup=mivec[1:]  #del segundo al ultimo
    mivecinf=mivec[0:-1] #del primero al penultimo

    basevec=mivecsup-mivecinf
    hvec=np.exp(mivec)            #alturas


    #print(basevec)

    h1vec=hvec[0:-1]    #del primero al penultimo
    h2vec=hvec[1:]      #del segundo al ultimo

    #print(areatrapecio(basevec,h1vec,h2vec))

    laintegral=areatrapecio(basevec,h1vec,h2vec)

    laintegral=np.sum(laintegral)
    #print("la integral es:",laintegral)
    return laintegral



###ATENCION No lo hice con expmax=8 porque el sistema no pudo calcularlo: dice 'killed'.
expmax=7    #deberia ser 8 segun enunciado...
tamvecN=expmax-1   #tamano del vector N

Nvariable=np.logspace(1,expmax,tamvecN)  #el numero de pasos debe ser entero
#print(Nvariable)
    

#print(Nvariable)
integralTrapecio(10)
resTrapecio=np.zeros(tamvecN)   #inicio vector vacio
i=0
for n in Nvariable:
    resTrapecio[i]=integralTrapecio(n)
    i+=1
    


###ERROR:

resReal=np.exp(1)-np.exp(0)

mierror= (resTrapecio - resReal)/resReal
print("Calculo por metodo de trapecio.")
print("Uso los siguientes valores de N:")
print(Nvariable)
print("Los resultados de la integral para cada N son:")
print(resTrapecio)
print("Los errores obtenidos son:\n",mierror)



import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.plot(Nvariable,mierror)
plt.xlabel("Numero de pasos, N")
plt.ylabel("Error en calculo de la integral de exp(x) entre 0 y 1.")
#No se como exportar esto a un archivo desde aqui.


print("Son las 3:50pm")
##SON LAS 3:50pm!!!!




