#Array এর ধরণ
import numpy as np
a = np.array([1,2,3]) #1D Array
b = np.array([[1,2],[3,4]]) #2D Array
c = np.array([[[1],[2]],[[3],[4]]]) #3D Array

print(b.ndim) # will shows the dimension of the array
print(a)
print(b)
print(c)