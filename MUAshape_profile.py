from numpy import *
import matplotlib.pyplot as plt

y = [ 0, 0, 1 ,1, 1, 1, 0, 0, 0, 0]
x = range(10)

fig = plt.figure( figsize=(8, 1.5))
plt.plot(x,y)
ax = fig.add_subplot(111)
ax.set_xticks([1,2,3.5,5,6])
ax.set_xticklabels(["$z_0n - a_n/2 - b_n$", "$z_0n - a_n/2$", "$z_0n$", "$z_0n + a_n/2$", "$z_0n + a_n/2 + b_n$"], fontsize = 8)
plt.savefig('MUAshape.png', bbox_inches='tight')
