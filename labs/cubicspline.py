import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 


def driver():
    
    f = lambda x: 1 / (1 + (10*x)**2)
    a = -1
    b = 1
    
    ''' create points you want to evaluate at'''
    Neval = 100
    xeval =  np.linspace(a,b,Neval)
    
    ''' number of intervals'''
    Nint = 10
    
    '''evaluate the cubic spline'''
    yeval = eval_cubic_spline(xeval,Neval,a,b,f,Nint)
    
    ''' evaluate f at the evaluation points'''
    fex = np.zeros(Neval)
    for j in range(Neval):
      fex[j] = f(xeval[j]) 
    
    
    plt.figure()
    plt.plot(xeval,fex,'ro-')
    plt.plot(xeval,yeval,'bs-')
    plt.legend(["Line spine"], fontsize="x-large")
    plt.show()
     
    err = abs(yeval-fex)
    plt.figure()
    plt.plot(xeval,err,'ro-')
    plt.show()
    
    

    
    
def  eval_cubic_spline(xeval,Neval,a,b,f,Nint):

    '''create the intervals for piecewise approximations'''
    xint = np.linspace(a,b,Nint+1)

    '''evaluate the function at the interpolation nodes'''
    yint = f(xint)
   
    '''create vector to store the evaluation of the linear splines'''
    y = np.zeros(Neval) 

    '''find the step length'''
    h = xint[1] - xint[0]
    
    '''initialize and empty matrix'''
    A = np.zeros((Nint-1,Nint-1))
    '''insert values into matrix'''
    for i in range(Nint-1) : 
        for j in range(Nint-1) : 
             if (i==j) : 
                A[i][j] = 1/3

             elif (abs(i-j)==1) : 
                A[i][j] = 1/12
            
    '''create vector b for Ax=b'''
    b = np.zeros(Nint)
    for i in range(Nint) : 
        b[i] = (yint[i+1] -2*yint[i] + yint[i-1])/2*h
        return b

        '''solve the linear system'''
    A_inv = np.linalg.inv(A)
    M = A_inv@b 
      

    
    
    for jint in range(Nint):
        '''find indices of xeval in interval (xint(jint),xint(jint+1))'''
        '''let ind denote the indices in the intervals'''
        '''let n denote the length of ind''' 
        ind = np.where(np.logical_and((xeval <= xint[jint+1]), (xeval >= xint[jint])))
        n = len(ind)
        
        
        '''temporarily store your info for creating a line in the interval of 
         interest'''
        a1= xint[jint]
        fa1 = f(a1)
        b1 = xint[jint+1]
        fb1 = f(b1)
        c1= xint[jint-1]
        fc1= f(c1)

        
        for kk in range(n):
           '''use your cubic evaluator to evaluate the lines at each of the points 
           in the interval'''
           C = fa1/h - h*M[kk]/6
           D = fb1/h - h*M[kk+1]/6
           y[jint[kk]] = M[kk]*(b1 - xeval[jint[kk]])**3/(6*h) + M[kk+1]*(xeval[jint[kk]]-a1)/(6*h) + C*(c1-1) + D*(xeval[jint[kk]]-a1)
         
           return y
           
           
if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()               
