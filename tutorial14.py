#বড় array আর ছোট array এর মাঝে গণনা
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([1, 2, 3])

print(a + b)
#দুইটার shape ঠিক match না করলেও NumPy নিজে থেকেই মান adjust করে নেয়।