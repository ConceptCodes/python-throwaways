import matplotlib.pyplot as plt
import numpy as np
import random
import time

def randomwalk(N):
    x, y, bigness = np.zeros((N)), np.zeros((N)), np.zeros((N))
    for n in range(0,N):
        angle = random.random() * 2*np.pi
        jump = np.random.normal(0, 50)

        x[n] = x[n-1] + (np.cos(angle) * jump)
        y[n] = y[n-1] + (np.sin(angle) * jump)
        bigness[n] = abs(jump)      
    return x, y, bigness

def random_color(bigness):
    return plt.cm.gist_ncar(bigness/100)

x, y, bigness = randomwalk(100)

xy = zip(x,y)
fig, ax = plt.subplots()
for start, stop, b in zip(xy[:-1], xy[1:], bigness):
    x, y = zip(start, stop)
    ax.plot(x, y, color=random_color(b))

plt.show()