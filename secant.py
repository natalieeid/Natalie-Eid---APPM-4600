import numpy as np
import math

def driver():

  f = lambda x: (x**6)-x-1
  p0 = 1
  p1 = 1.5

  Nmax = 100
  tol = 1.e-14

  (itvals,pstar,info,c) = secant(f,p0,p1,tol, Nmax)
  print('the approximate root is', '%16.16e' % pstar)
  print('the error message reads:', '%d' % info)
  print('Number of iterations:', '%d' % c)

def secant(f,p0,p1,tol,Nmax):
   """
     Inputs:
    f    - function
    p0,p1- initial guesses for root
    tol  - iteration stops when p_n,p_{n+1} are within tol
    Nmax - max number of iterations
  Returns:
    p     - an array of the iterates
    pstar - the last iterate
    info  - success message
          - 0 if we met tol
          - 1 if we hit Nmax iterations (fail)
 
   """

   itvals = []
  
   c = 0 

#check that inital points are not roots 

   if (f(p0)==0) : 
     pstar=p0
     info = 0 
     itvals.append[p0]

   if (f(p1)==0) : 
     pstar=p1
     info = 0 
     itvals.append[p1]
   

   fp1=f(p1)
   fp0=f(p0)
     
#do the iteration  
   while c < Nmax :

#check that no divide by zero error 
       if (abs(fp0-fp1)==0):
          info = 1 
          pstar = p1
          return [itvals,pstar,info,c]

#find the next iterate
       p_next = p0 - (fp1*(p1-p0))/(fp1-fp0)
  

#see if iterate convergeres 
       if (abs(p_next-p1) < tol):
           pstar = p1
           info = 0
           return [itvals,pstar,info,c]
       p0 = p1
       p1 = p_next
       fpo = f(p1)
       fp1 = f(p_next)
       itvals.append(p1)
       c +=1

#stop iterating if c gets to big 
       pstar = p1
       info = 1
       return [itvals,pstar,info,c]
         
driver()