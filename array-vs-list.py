import numpy as np
a = np.ones((9,9))
print(a[2,2])

# cannot assign objects to array element
a[2,2] = [9,8,7]

# can assign objects to list element
# note the change in indexing
a = a.tolist()
a[2][2] = [9,8,7]
