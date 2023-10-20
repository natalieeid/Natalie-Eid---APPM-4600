import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm 

def driver():

    x0 = np.array([1,0])
    
    Nmax = 100
    tol = 1e-10
    
    t = time.time()
    for j in range(50):
      [xstar,ier,its] =  Newton(x0,tol,Nmax)
    elapsed = time.time()-t
    print(xstar)
    print('Newton: the error message reads:',ier) 
    print('Newton: took this many seconds:',elapsed/50)
    print('Netwon: number of iterations is:',its)
     
    
def evalF(x): 

    F = np.zeros(2)
    
    F[0] = (4*x[0]**2)+(x[1]**2)-4
    F[1] = x[0]+x[1]-np.sin(x[0]-x[1])
    return F
    
def evalJ(x): 

    h=1*10**(-3)
    F = F = evalF(x)
    FH1 = F = evalF(x+[h,0])
    FH2 = F = evalF(x+[0,h])
    FnH1 = F = evalF(x-[h,0])
    FnH2 = F = evalF(x-[0,h])
    J = np.array([[(FH1[0]-FnH1[0])/h,(FH2[0]-FnH2[0])/h],[(FH1[1]-FnH1[1])/h,(FH2[1]-FnH2[1])/h]])
    return J



def Newton(x0,tol,Nmax):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    for its in range(Nmax):
       J = evalJ(x0)
       Jinv = inv(J)
       F = evalF(x0)
       
       x1 = x0 - Jinv.dot(F)
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier, its]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]
           

driver()       
