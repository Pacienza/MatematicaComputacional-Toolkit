from scipy.interpolate import *



x = [0, 15, 17]

y = [-50000, 30000, 28000]

p = lagrange(x, y)

print(p)
