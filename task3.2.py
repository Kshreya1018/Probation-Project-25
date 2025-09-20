import numpy as np
import random
a=np.random.randint(1, 20, size=(3,3))
print(a)
print(a[0, :])
print(a[:, 0])
print(a[1, 1])
print(a[0:2, 0:2])
a[1, 1]=99
print(a)