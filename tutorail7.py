#Reshape এবং Flatten
import numpy as np
a = np.array([[1,2],[3,4],[5,6]])
print(a.reshape(2,3)) ## 2 rows, 3 columns kore ekta array retun korbe like
#[[1 2 3]
#[4 5 6]]
print(a.flatten()) #এক লাইনে সব elements ba ek array te sob elements