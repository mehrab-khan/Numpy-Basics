#Indexing এবং Slicing
import numpy as np
arr = np.array([10,20,30,40,50])
print(arr[0])     # 10
print(arr[1:4])   # [20 30 40]

#2D Array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b[0, 1])  # প্রথম row, দ্বিতীয় column = 2 Output will be "2"