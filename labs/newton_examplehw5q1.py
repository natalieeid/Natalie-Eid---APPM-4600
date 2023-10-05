# import libraries
import numpy as np
import math 
import scipy.special as scipy
        


def driver():


  a =(0.138*10**(-6))
  t = 5184000
  Ti = 20
  Ts = -15
  c= 2*np.sqrt(a*t)
  q = 2/np.sqrt(np.pi)

  f = lambda x: (Ti-Ts)*scipy.erf(x/c)+Ts
  fp = lambda x: (Ti-Ts)*q*math.exp(-(x/c)**2)
  p0 = 1

  Nmax = 100
  tol = 1.e-14

  (p,pstar,info,it) = newton(f,fp,p0,tol, Nmax)
  print('the approximate root is', '%16.16e' % pstar)
  print('the error message reads:', '%d' % info)
  print('Number of iterations:', '%d' % it)


def newton(f,fp,p0,tol,Nmax):
  """
  Newton iteration.
  
  Inputs:
    f,fp - function and derivative
    p0   - initial guess for root
    tol  - iteration stops when p_n,p_{n+1} are within tol
    Nmax - max number of iterations
  Returns:
    p     - an array of the iterates
    pstar - the last iterate
    info  - success message
          - 0 if we met tol
          - 1 if we hit Nmax iterations (fail)
     
  """
  p = np.zeros(Nmax+1);
  p[0] = p0
  for it in range(Nmax):
      p1 = p0-f(p0)/fp(p0)
      p[it+1] = p1
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it]
      p0 = p1
  pstar = p1
  info = 1
  return [p,pstar,info,it]
        
driver()



