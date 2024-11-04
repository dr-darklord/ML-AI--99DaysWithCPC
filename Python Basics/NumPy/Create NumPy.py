'''#create a numPy array 

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))'''

#Another way to create an array


import numpy as np
my_list = [1,2,3,4,5,6,7,8,9]
arr = np.array(my_list)
print(my_list)

my_mat = [[1,2,3],[4,5,6],[7,8,9]]
np.array(my_mat)
print(my_mat)

h = np.arange(0,11,2)
print(h)