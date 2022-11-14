import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy import special
from scipy.stats import poisson

π = np.pi

h = 1
m = 1
ω = 1

N = 6
E = h * ω * (N+1/2)
A = np.sqrt(2*E/(m*ω**2))

print(A)

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
ln0, = ax.plot(x, U(x))
ln = [ax.plot([], []) for _ in range(5)]

def Psi(N,x,t,E):
	return sum([np.exp(1j*ω*(n+1/2)*t)*poisson.pmf(n,h*ω*(E+1/2))*psi(n,x) for n in range(N)])

def init():
    ax.set_xlim(-A, A)
    ax.set_ylim(-0.1, 3)
    return ln0,ln,

# def update(frame):
#     ydata = np.abs(Psi(10,x,frame))**2
#     ln.set_data(x, ydata)
#     return ln,


T = 2*np.pi*ω
times = np.arange(0, T, 1/60)
Y = [[] for _ in range(len(ln))]
for n in range(len(ln)):
    for t in times:
        Y[n].append(3*np.abs(Psi(10,x,t,n))**2)

def update(frame):
    for n in range(len(ln)):
        l = ln[n][0]
        l.set_data(x, Y[n][frame])
    return ln0,ln,

# for n in range(N):
# 	# ω = 2*h*(n+1/2) / (m*A**2)
# 	# plt.plot(x,psi(n,x)+h*ω*(n+1/2))
# 	plt.plot(x,psi(n,x)**2)

ani = FuncAnimation(fig, update, init_func=init, frames=len(times), interval=16.7, repeat=True) 

plt.show()
