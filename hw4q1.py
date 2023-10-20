import numpy as np
import math 
import matplotlib.pyplot as plt 
import random
import scipy.special as scipy

#import packages 

def driver() : 

#create vector for theta values 

	X = np.linspace(0,10,100)

#define the variables 

	Ti=20
	Ts=-15
	a=0.138*10**-6

#evaluate for T

	T=(Ti-Ts)*scipy.erf(X/(2*np.sqrt(a*86400)

#plot the curve
	plt.plot(X,T)
	plt.show()