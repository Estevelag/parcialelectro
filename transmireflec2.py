# -*- coding: utf-8 -*-
"""
Created on Sun May  3 17:21:26 2020

@author: User
"""
import numpy as np
from math import exp
import scipy.constants as sc
from matplotlib import pyplot as plt
#Main variables
Npts=1001
pc=100
Ez=np.zeros((1,Npts),dtype=float)####hacerlo mas grande,el 1, y hacer un videito
Hy=np.zeros((1,Npts),dtype=float)
ei=np.zeros((1,Npts),dtype=float)
ei[0,0:200]=sc.epsilon_0
ei[0,200:700]=sc.epsilon_0*12
ei[0,700:1001]=sc.epsilon_0
dt= 8.46666666666666667e-14
dx=0.0000254#0.0000254 Para que multiplicando por la cantidad de puntos me de al ancho del parcial mas un poco
E0=1.0
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 17:21:26 2020

@author: User
"""
import numpy as np
from math import exp
import scipy.constants as sc
from matplotlib import pyplot as plt
#Main variables
Npts=1001
pc=300
Ez=np.zeros((1,Npts),dtype=float)####hacerlo mas grande,el 1, y hacer un videito
Hy=np.zeros((1,Npts),dtype=float)
ei=np.zeros((1,Npts),dtype=float)
ei[0,0:200]=sc.epsilon_0
ei[0,200:700]=sc.epsilon_0*12
ei[0,700:1001]=sc.epsilon_0
dt= 8.46666666666666667e-14
dx=0.0000254#0.0000254 Para que multiplicando por la cantidad de puntos me de al ancho del parcial mas un poco
E0=1.0
Ttotal=1# 180ns after
a=0
b=0
f=1e11
#########Proceso de animación

x=np.linspace(0,1000,num=1001)*dx
Ez=np.zeros((1,Npts),dtype=float)
Hy=np.zeros((1,Npts),dtype=float)
Ez[0,pc]=E0*np.sin(0)##acá estoy ploteando el primer valor nada mas
y=Ez[0,:]

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'r-')
ax.axvline(x=200*dx)
ax.axvline(x=700*dx)
ax.set_xlim(0,0.0256)
ax.set_ylim(-1,2)
ax.set_ylabel('Electric Field(V/m)')
ax.set_xlabel('Posición x(m)')
for i in range(0, 500):
    ####Calculate the magnetic field
    for j in range(0,(Npts-1)):
        Hy[0,j]=Hy[0,j]+(dt/(sc.mu_0*dx))*(Ez[0,j+1]-Ez[0,j])
    #Update the electric field
    a=Ez[0,Npts-2]
    b=Ez[0,1]
    for k in range(0,Npts):
        Ez[0,k]=Ez[0,k]+(dt/(ei[0,k]*dx))*(Hy[0,k]-Hy[0,k-1])
    #Electric source
    if (i<200) and (f*dt*i<1):
        Ez[0,pc]=E0*np.sin(2*np.pi*f*dt*i)
    elif (i<200) and (f*dt*i>=1):
        Ez[0,pc]=E0*np.sin(2*np.pi*f*dt*i)*0.00000000000002
    Ez[0,0]=b
    Ez[0,Npts-1]=a
    line1.set_ydata(Ez[0,:])
    fig.canvas.draw()#####actualizacion de la grafica
    fig.canvas.flush_events()
print("reflectancia y transmitancia =",-Ez[0,218],-Ez[0,138])