import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from ee_state import ee_state


N=0
states = [ee_state(1,3,n) for n in range(N,N+4)]
A = max([s.A for s in states])

Δx = 0.005
x = np.arange(-A,A,Δx)

plt.plot(x,states[0].U(x))

# for s in states:
# 	y = np.abs(s.psi(x,0))**2+s.E
# 	plt.plot(x,y)

y = np.abs(sum([poisson.pmf(s.n,1)*s.psi(x,0) for s in states]))**2
plt.plot(x,y)
plt.plot(x,np.abs(states[0].psi(x,0))**2)

plt.show()
