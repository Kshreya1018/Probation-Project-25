import numpy as np
import pandas as pd
b=np.random.randint(1,100,size=10)
arr=pd.Series(b)
print(arr)
print(arr.head(5))
print(arr.tail(5))
print(arr.max())
print(arr.min())
print(arr.mean())
a=arr.tolist()
print(a)

