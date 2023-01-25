# Plots m realizations of the Brownian motion with n steps following Roberts algorithm 1.1 p.3. We choose to vectorize the code after Roberts' approach, following the dogma that loops are expensive.

import numpy as np
import matplotlib.pyplot as plt
import sys

m=5 # number of realizations you wish to plot
n=300 # number of time steps we sample

# Create vector of sample times
time=np.linspace(0.,1., n)

# Prescribe step lengths
h= np.diff(time)

# Create matrix of increments: each row is one of the realizations
dw = np.sqrt(h)*np.random.randn(m,n-1)

# Initialize matrix of positions
w = np.zeros([m,n])

# Do random walk
w[:,1:n] = np.cumsum(dw, axis=1)

# Plot results
plt.figure()

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

for k in np.arange(0, m):
    plt.plot(time,np.reshape(w[k, :], n))

plt.xlabel(r'$\mathrm{time} \ t$', fontsize=18)
plt.ylabel(r'$\mathrm{position} \ W(t)$', fontsize=18)

plt.xlim([0.,1.])

plt.tick_params(axis="x", labelsize=14)
plt.tick_params(axis="y", labelsize=14)

plt.tight_layout()

"""
fignamepng = 'brownian_motion'+'.png'
plt.savefig(fignamepng, dpi=300)
"""

plt.show()
