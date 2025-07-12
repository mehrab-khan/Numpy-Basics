#Array থেকে নির্দিষ্ট কিছু মান বের করার শর্টকাট পদ্ধতি
import numpy as np

a = np.array([10, 20, 30, 40, 50])
print(a[[1, 3, 4]])  
# Output: [20 40 50]
