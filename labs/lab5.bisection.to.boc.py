# import libraries
import numpy as np

def driver():

# use routines    
    f = lambda x: x**3 +x-4
    fder= lambda x: 
    a = 1
    b = 4

    c = 0 

    [astar,ier] = bisection(f,fder,a,b)
    print('a value in the basin of convergence is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', f(astar))
    print('iterations=',c)




# define routines
def bisection(f,a,b,tol):
    
#    Inputs:
#     f,fd,a,b       - function, function derivative, and endpoints of initial interval
#      tol  - bisection stops when interval length < tol

#    Returns:
#      astar - root 
#      int   - basin of convergence 
#      ier   - error message
#            - ier = 1 => Failed
#            - ier = 0 == success


#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier]

# make sure that initial guesses are not already in the basin of convergence

   fdera = fder(a)
   fderb = fder(b)
   if (fdera<1) : 
      astar = a
      ier = 0 
      return [astar, ier]
   if (fderb<1) : 
      astar = b
      ier = 0 
      return [astar, ier]
  

#iterate to find value inside the basin of convergence 
    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, ier]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
#      print('abs(d-a) = ', abs(d-a))
      
    astar = d
    ier = 0
    c = count 
    return [astar, ier]
     
#append newtons method 
(p,pstar,info,it) = newton(f,fp,p0,tol, Nmax)
  print('the approximate root is', '%16.16e' % pstar)
  print('the error message reads:', '%d' % info)
  print('Number of iterations:', '%d' % it)


def newton(f,fp,astar,tol,Nmax):
 
  
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

