import numpy as np
import random
a=np.random.randint(1, 20, size=(3,3))
print("array:",a)
print("first row:",a[0, :])
print("second column:",a[:, 1])
print("elemwnt at 2,2 position:",a[1, 1])
print("sub array:",a[0:2, 0:2])
a[1, 1]=99
print("modified array:",a)