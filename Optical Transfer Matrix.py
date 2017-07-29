# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 12:11:42 2016

@author: nick anthony
"""

from __future__ import division
import numpy as np, matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
'''
Using the wave transfer matrix formalism form chapter 7 of Saleh and Teich
Fundamentals of Photonics, this script calculates the reflectance of a
multilayer dielectric.
'''

def inter(n1,n2):
    #Returns a matrix representing the interface between two dielectrics with indices n1 on the left and n2 on the right.
    #Actually the order of terms does not appear to matter.
    return 1/(2*n2)*np.matrix([[n2+n1,n2-n1],[n2-n1,n2+n1]])
def prop(lamb,n,d):
    #Returns a matrix representing the propagation of light with wavelength, "lamb", through homogenous material wth index, "n",
    #for a distance of "d". d and lamb must use the same units.
    phi=n*2*np.pi/lamb*d
    return np.matrix([[np.exp(-phi*1j),0],[0,np.exp(1j*phi)]])
def calc(m):
    #calculates reflected power given a transfer matrix, "m".
    def m_to_scatter(m):
        return (1/m[1,1])*np.matrix([[m[0,0]*m[1,1]-m[0,1]*m[1,0],m[0,1]],[-m[1,0],1]])
    scatter=m_to_scatter(m)
    Reflect=np.real(scatter[1,0]*np.conj(scatter[1,0]))
    return Reflect


'''
m is the final transfer matrix. It should be made by multiplying the matrices
representing each element of the system. If the transmitted light is considered
to be propagating from left to right then the matrices should be in multiplied
in reverse, from right to left.
'''



param=np.array([1,2,3,10])

R=np.zeros((5000,len(param)))
High_lambda=12000
Low_lambda=500
lp=7.5e3
lb=lp*3/2


for l in np.linspace(Low_lambda,High_lambda,num=R.shape[0]):
    print('%d'%((l-Low_lambda)/(High_lambda-Low_lambda)*100)+'%')
   
    for p in param:
        n3=1
        n2=n3+p
        '''
        Here is the series of multiplied matrices
        '''
        m=(prop(l,n3,lb/(4*n3))*inter(n3,n2)*prop(l,n2,lb/(4*n2))*inter(n2,n3))**10
        
        
        
        R[np.where(np.linspace(Low_lambda,High_lambda,num=R.shape[0])==l)[0][0],np.where(param==p)[0][0]]=(calc(m))
hf=plt.figure()
ha=hf.add_subplot(111,projection='3d')
X,Y=np.meshgrid(param,np.linspace(Low_lambda,High_lambda,num=R.shape[0]))
ha.plot_surface (X,Y,R,cstride=1,rstride=10)
ha.set_ylabel('Wavelength (nm)')
ha.set_xlabel('Parameter')
ha.set_zlabel('Reflectance')
plt.figure()
plt.xlabel('Wavelength (nm)')
plt.ylabel('Reflectance')
for i in range(R.shape[1]):
    plt.plot(np.linspace(Low_lambda,High_lambda,num=R.shape[0]),R[:,i],label=str(param[i]))
plt.legend()
plt.show()
