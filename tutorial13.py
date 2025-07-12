#Axis Concept ভালোভাবে
import numpy as np
a = np.array([[1, 2], [3, 4]])

print(np.sum(a, axis=0))  # Column-wise যোগফল
print(np.sum(a, axis=1))  # Row-wise যোগফল
