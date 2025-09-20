import numpy as np
import random
a=np.random.randint(1,100,10)
print("maximum element:",np.max(a))
print("maximum element:",np.min(a))
print("mean of the array:",np.mean(a))
print("sum of elements:",np.sum(a))
print("index of maximum element:",np.argmax(a))
print("index of minimum element:",np.argmin(a))
print("sorted array:",np.sort(a))