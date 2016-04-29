# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 16:46:59 2016

@author: Nick
"""

import scipy as sp, numpy as np,matplotlib.pyplot as plt
import scipy.fftpack as ft
n=5000
T=0.01
x=np.linspace(0,n*T,num=n)
'''
f=np.sin(2*np.pi*10*x)
f[:2400]=np.zeros((2400))
f[2600:]=np.zeros((2400))
'''
f=
F=ft.fft(f)
X=np.linspace(0,1/(2.0*T),num=n/2)
fig1=plt.figure()
plt.plot(x,f)
fig2= plt.figure()
ax1=fig2.add_subplot('111')
ax1.plot(X,2.0/n*np.absolute(F)[:n/2])
'''
ax2=ax1.twinx()
ax2.plot(X,np.angle(F)[:n/2]/np.pi,color='g')
ax2.set_ylabel('pi')
'''
ax1.set_xlabel('Hz')
plt.show()

