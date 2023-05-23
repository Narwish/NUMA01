#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 17:06:23 2021

@author: Björn Follin, Lukas Early
Homework group 46
"""

from numpy import *
from matplotlib.pyplot import *
def a(k,x):
    if k == 0:
        return (1+x)/2
    else:
        return (a(k-1,x)+g(k-1,x))/2
def g(k,x):
    if k == 0:
        return sqrt (x)
    else:
        return sqrt(a(k-1,x)*g(k-1,x))


def approx_ln(x,n):
    return ((x-1)/a(n,x))

#%% Task 2
x_lin=linspace(1, 10, 200)
ln_x=[log(x) for x in x_lin]

for n in [1, 2, 4, 8]:
    L_approx_ln=[]
    L_diff1=[]
    
    for x in x_lin:
        L_approx_ln.append(approx_ln(x,n))
    for e in range(0, len(x_lin)):
        L_diff1.append((ln_x[e])-L_approx_ln[e])
        
    figure(0)
    plot(x_lin, L_approx_ln, label=f'n={n}')
    
    figure(1)
    plot(x_lin,L_diff1, label=f'n={n}') 

figure(0)
plot(x_lin, ln_x, label='ln(x)')
legend()
title('Approximation of ln(x) after n iterations')

figure(1)
semilogy()
legend()
title('Difference between the approximation and ln(x)')
    
#%% Task 3
Error_val = []
x_val = []
for j in range (1,6):
    Error_val.append(abs(approx_ln(1.41,j)-log(1.41)))
    x_val.append(j)
figure(2)
title('Absolute value of error versus n')
plot(x_val, Error_val)
axis([1, 5, 0.0008379377801034371 ,0.0008425571469886095])


#%% Task 4
def dki (i,k,x):
    if k == 0:
        return a(i,x)
    else:  
        return (dki(i,k-1,x) -4**(-k) * dki(i-1,k-1,x))/ (1-4**(-k))

    
def fast_approx_ln(n,x):
    return ((x-1)/ dki(n,n,x))

# %%Task 5
for n in [1, 2, 3, 4, 5]:
    L_diff2 = []
    
    for x in x_lin:
        L_diff2.append(abs(log(x)-fast_approx_ln(n,x)))
    
    figure(3)
    plot(x_lin, L_diff2, label=f'n={n}')

figure(3)
semilogy()
legend()
xlabel('x')
ylabel('Error')
title('Error behavior of the accelerated Carlsson Method for the log')