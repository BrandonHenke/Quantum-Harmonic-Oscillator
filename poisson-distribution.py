import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson


π = np.pi

h = 1
m = 1
ω = 3

N = 6
E = h * ω * (N+1/2)

n = np.arange(20)
P = poisson.pmf(n,N)

plt.scatter(n,P)
plt.show()