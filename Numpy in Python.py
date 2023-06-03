import numpy as np
"""
This file illustrates basic functions of numpy.
"""

array = np.array([1,2,3,4,5,6,7,8])
print(array)

list = [1,2,3,4,'u',False]
print(list)

array1 = np.array([1,2,3,4,'u',False])
print(array1)

list1 = list*3
print(list1)

array2 = array*3
print(array2)


# Create a Matrix

a = [[1,2,3],
    [4,5,6],
    [7,8,9]]

print(a)

a = np.array(a)
print(a)

np.random.seed(0)
rand = np.random.randint(0,10,(3,4))
print(rand)

id = np.identity(5, dtype=int)
print(id)

full = np.full((2,3), 7)
print(full)



