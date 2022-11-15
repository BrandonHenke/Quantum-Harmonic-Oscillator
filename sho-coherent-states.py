import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation,ImageMagickWriter
from ch_state import ch_state
from datetime import datetime


plt.rcParams['text.usetex'] = True

π = np.pi

h = 1
m = 1
ω = 3

TotalEnergyLevels = 15

N=15
states = [ch_state(m,ω,E,TotalEnergyLevels) for E in range(N)]

# print(A)

A = 1.75*max([s.A for s in states])
# ω = 2*h*(n+1/2) / (m*A**2)


Δx = 0.005
x = np.arange(-A,A,Δx)


fig, ax = plt.subplots()
ln0, = ax.plot(x, states[0].U(x))
ln = [ax.plot([], []) for _ in range(len(states))]

def init():
	# ax.set_xlim(-A, A)
	ax.set_ylim(-0.1, states[N-1].E*(1+0.2))
	return ln0,ln,


T = 2*2*π/ω
spf = 1/30
times = np.arange(0, T, spf)
Y = [[] for _ in range(len(states))]
for n in range(len(states)):
	n_start = 1
	for t in times:
		Y[n].append((2*n+1)*np.abs(states[n].psi(x,t))**2+states[n].E)

def update(frame):
	for n in range(len(ln)):
		l = ln[n][0]
		l.set_data(x, Y[n][frame])
	return ln0,ln,

ax.set_title("Coherent States for a System With "+str(TotalEnergyLevels)+" Energy Levels.")
ax.set_xlabel("Position")
ax.set_ylabel("Energy Level and Probability Density")

# for n in range(N):
# 	# ω = 2*h*(n+1/2) / (m*A**2)
# 	# plt.plot(x,psi(n,x)+h*ω*(n+1/2))
# 	plt.plot(x,psi(n,x)**2)

ani = FuncAnimation(fig, update, init_func=init, frames=len(times), interval=spf*1000, repeat=True) 

file_name = str(datetime.now())+'-coherent_Sim.gif'

ani.save(file_name,"MovieWriter", fps=int(1/spf),dpi=500)

