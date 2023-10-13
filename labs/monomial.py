import numpy as np
import numpy.linalg as la

def driver(): 


    f = lambda x: 1 / (1 + (10*x)**2)

    N = 4
    a = -1
    b = 1
   
   
    ''' create equispaced interpolation nodes'''
    xint = np.linspace(a,b,N+1)
    
    ''' create interpolation data'''
    yint = f(xint)


    ''' create points for evaluating the monomoal interpolating polynomial'''
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    yeval_mono = np.zeros(Neval+1)
    yexact = np.zeros(Neval+1)
    a_s = monom(xint, yint)
  
 
    ''' evaluate monomial poly '''
    for z in range(Neval+1):
       yexact[z] = f(xeval[z])
       for w in range(N+1) : 
          yeval_mono[z] += a_s[w]*xeval[z]**w


    '''plot the functions'''
    fex = f(xeval)
       

    plt.figure()    
    plt.plot(xeval,fex,'ro-')
    plt.plot(xeval,yeval_mono,'bs--') 
    plt.legend()
    plt.figure() 
    plt.show()




    ''' create vandermonde matrix '''
def Vandermonde(x, n):
 Van = np.zeros((n+1,n+1))
 for i in range(n+1):
   for j in range(n+1):
        Van[j][i] = x[j]**i
                               
   return Van;

 ''' evaluate the polynomial terms'''
def monom(x,y):
  N = len(x)-1
  V = Vandermonde(x, N)
  Vinv = la.inv(V)
  a = Vinv * y
  return a 


driver()        
