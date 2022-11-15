import numpy as np
from scipy.stats import poisson
from ee_state import ee_state

π = np.pi
h = 1

class ch_state:
	def __init__(self,m,ω,N,n:int=6):
		self.m=m
		self.ω=ω
		self.N=N
		self.E = h*self.ω*(self.N+1/2)
		self.A = np.sqrt(2*self.E/(self.m*self.ω**2))
		self.states = [ee_state(self.m,self.ω,En) for En in range(n)]
	
	def psi(self,x,t):
		return sum([poisson.pmf(s.n,self.N)*s.psi(x,t) for s in self.states])

	def U(self,x):
		return 0.5*self.m*self.ω**2*x**2