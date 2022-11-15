import numpy as np
from scipy import special

π = np.pi
h = 1

class ee_state:
	def __init__(self,m,ω,n):
		self.m  = m
		self.ω  = ω
		self.n = n
		self.E = self.ω*h*(self.n+1/2)
		self.A = np.sqrt(2*self.E/(self.m*self.ω**2))
	
	def psi(self, x,t):
		ut = np.exp(-1j*self.E*t/h)
		f1 = 1/np.sqrt(2**self.n * np.math.factorial(self.n))
		f2 = (self.m*self.ω/(π*h))**(1/4)
		f3 = np.exp(-self.m*self.ω*x**2/(2*h))
		Hn = special.hermite(self.n)
		f4 = Hn(np.sqrt(self.m*self.ω/h)*x)
		return ut*f1*f2*f3*f4
	
	def U(self,x):
		return 0.5*self.m*self.ω**2*x**2