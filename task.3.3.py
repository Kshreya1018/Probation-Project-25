import numpy as np
a=np.random.randint(1,20,size=(10))
b=np.random.randint(1,20,size=(10))
print(a)
print(b)
add=a+b
sub=a-b
mul=a*b
div=a//b
sq=a**2
d=np.dot(a,b)
sorted=np.sort(b)
print("element wise addition:",add)
print("element wise addition:",sub)
print("element wise addition:",mul)
print("element wise addition:",div)
print("square pf every element of first array:",sq)
print("dot product of two arrays:",d)
print("sorted second array:",sorted)