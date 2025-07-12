'''
copy() করলে নতুন Array তৈরি হয়।

view() করলে মূল Array-এর reference তৈরি হয়।

python
Copy
Edit

'''

import numpy as np
arr = np.array([1, 2, 3])
x = arr.copy()
y = arr.view()

arr[0] = 100
print(x)  # Copy unaffected
print(y)  # View changes with arr
