import numpy as np 

h = 0.01 * (1/2**(np.arange(0, 10)))
s=np.pi/2

fds1 = (-np.sin(s+h)+np.sin(s))/h

fds2 = (-np.sin(s+h)+np.sin(s-h))/2*h

print(fds1)
print(fds2)