import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy import special
from scipy.stats import poisson

π = np.pi

h = 1
m = 1
ω = 1

N = 4
E = h * ω * (N+1/2)
A = np.sqrt(2*E/(m*ω**2))

# A = 1
# ω = 2*h*(n+1/2) / (m*A**2)


Δx = 0.005

def U(x):
	return m*ω**2*x**2/2

x = np.arange(-A,A,Δx)

def psi(n : int,x):
	f1 = 1/np.sqrt(2**n * np.math.factorial(n))
	f2 = (m*ω/(π*h))**(1/4)
	f3 = np.exp(-m*ω*x**2/(2*h))
	Hn = special.hermite(n)
	f4 = Hn(np.sqrt(m*ω/h)*x)
	return f1*f2*f3*f4


fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [])

def Psi(N,x,t):
	return sum([np.exp(1j*h*ω*(n+1/2)*t/h)*poisson.pmf(n,h*ω*(1+1/2))*psi(n,x) for n in range(N)])

def init():
    ax.set_xlim(-A, A)
    ax.set_ylim(-0.1, 1)
    return ln,

def update(frame):
    ydata = np.real(np.abs(Psi(10,x,frame))**2)
    ln.set_data(x, ydata)
    return ln,

# for n in range(N):
# 	# ω = 2*h*(n+1/2) / (m*A**2)
# 	# plt.plot(x,psi(n,x)+h*ω*(n+1/2))
# 	plt.plot(x,psi(n,x)**2)

T = 10
ani = FuncAnimation(fig, update, frames=np.arange(0, T, T/60),
                    init_func=init, blit=False)
plt.show()
