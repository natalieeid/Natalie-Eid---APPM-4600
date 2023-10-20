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
    for i in range(50):
      [xstar,ier,its,j] =  SlackerNewton(x0,tol,Nmax)
    elapsed = time.time()-t
    print(xstar)
    print('SlackerNewton: the error message reads:',ier) 
    print('SlackerNewton: took this many seconds:',elapsed/50)
    print('SlackerNetwon: number of iterations is:',its)
    print('SlackerNetwon: number of Jacobian Inverses calculated is:',j)
     
     
def evalF(x): 

    F = np.zeros(2)
    
    F[0] = (4*x[0]**2)+(x[1]**2)-4
    F[1] = x[0]+x[1]-np.sin(x[0]-x[1])
    return F
    
def evalJ(x): 

    
    J = np.array([[8*x[0], 2**x[1]], [1-np.cos(x[0]-x[1]),1+np.cos(x[0]-x[1])]])
    return J


def SlackerNewton(x0,tol,Nmax):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its, j = number of Jacobians computed '''
    ''' Outputs: xstar= approx root, ier = error message, its = num its, j = numer of iterations'''

    j=0
    J = evalJ(x0)
    Jinv = inv(J)
    F = evalF(x0)

    x1 = x0 - Jinv.dot(F)

    for its in range(Nmax):

       F = evalF(x1)
       x2 = x1 - Jinv.dot(F)
       
       if (norm(x2-x1) < tol):
           xstar = x2
           ier =0
           return[xstar, ier,its,j]
           
      
       if (0.07*norm(x0-x1) < norm(x1-x2)):
          J = evalJ(x2)
          Jinv = inv(J)
          F = evalF(x2)
          j += 1 
          x0=x1
          x1=x2
       
    
    xstar = x1
    ier = 1
    return[xstar,ier,its,j]

driver()


