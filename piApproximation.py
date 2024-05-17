import numpy as mp

x = []
y = []
for i in range (0,10000):
  x.append(np.random.uniform(-1,1))
  y.append(np.random.uniform(-1,1))

inside = (x**2 + y**2) < 1
in_x = x[inside]
in_y = y[inside]

pi_val = 4*(inside.sum/1000)

print(pi_val)
