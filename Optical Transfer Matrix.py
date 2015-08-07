from __future__ import division
import numpy as np, matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
'''
Using the wave transfer matrix formalism form chapter 7 of Saleh and Teich
Fundamentals of Photonics, this script calculates the reflectance of a
multilayer dielectric.
'''

def inter(n1,n2):
    #Returns a matrix representing the interface between two dielectrics with indices n1 on the left and n2 on the right
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
param=np.array([4/6,4/7,4/5])

R=np.zeros((500,len(param)))
High_lambda=3000
Low_lambda=300

for l in np.linspace(Low_lambda,High_lambda,num=R.shape[0]):
    print '%d'%((l-Low_lambda)/(High_lambda-Low_lambda)*100)+'%'
   
    for p in param:
        
        '''
        Here is the series of multiplied matrices
        '''
        m=prop(l,1,1000)*np.linalg.matrix_power(inter(1,2)*prop(l,2,633/(2*p))*inter(2,1)*prop(l,1,633/p),10)
        
        
        
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