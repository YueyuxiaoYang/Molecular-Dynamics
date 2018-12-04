#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:38:39 2018

@author: lestradavi
"""

import numpy as np
import matplotlib as plt

mass_O = 15.999*10**(-3) #kg/mol
d0 = 0.1016 #nm
k = 251208 
dt= 5*10**(-16)
n_steps = 1000
Ndf=1
T=300

#V calculated by 300K

di=0.001

vi=np.sqrt((Ndf*k*T)/mass_O)

vi_a1=np.zeros(n_steps+1)
pi_a1=np.zeros(n_steps+1)
vi_a2=np.zeros(n_steps+1)
vi_a2[0]=vi
pi_a2=np.zeros(n_steps+1)
pi_a2[0]=di

di_list = []

for i in range(n_steps):
    F=-1*k*abs(pi_a2[i]-pi_a1[i])
    a=F/mass_O
    di = pi_a2[i]-pi_a1[i]
    if(di>0):
        a_a1 = -1*a
        a_a2 = a
    else:
        a_a1 = a
        a_a2 = -1*a
    vi_a1[i+1]=(vi_a1[i]+dt*a_a1)
    vi_a2[i+1]=(vi_a2[i]+dt*a_a2)
    pi_a1[i+1]=(pi_a1[i]+vi_a1[i+1]*dt)
    pi_a2[i+1]=(pi_a2[i]+vi_a2[i+1]*dt)

di_list = pi_a2-pi_a1
print(di_list)
plt.pyplot.plot(di_list)
    
