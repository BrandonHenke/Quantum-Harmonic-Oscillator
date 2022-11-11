import numpy as np
import matplotlib.pyplot as plt
from scipy import special

π = np.pi

h = 1
m = 100
ω = 1

N = 4
E = h * ω * (N+1/2)
A = np.sqrt(2*E/(m*ω**2))

# A = 1
# ω = 2*h*(n+1/2) / (m*A**2)


Δx = 0.01

def U(x):
	return m*ω**2*x**2/2



x = np.arange(-A,A,Δx)
plt.plot(x,U(x))

def psi(n : int,x):
	f1 = 1/np.sqrt(2**n * np.math.factorial(n))
	f2 = (m*ω/(π*h))**(1/4)
	f3 = np.exp(-m*ω*x**2/(2*h))
	Hn = special.hermite(n,monic=True)
	f4 = Hn(np.sqrt(m*ω/h)*x)
	return f1*f2*f3*f4

for n in range(N):
	# ω = 2*h*(n+1/2) / (m*A**2)
	# plt.plot(x,psi(n,x)+h*ω*(n+1/2))
	plt.plot(x,psi(n,x)**2+h*ω*(n+1/2))

plt.show()