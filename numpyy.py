from array import array
import numpy as np

arr = np.array([1,2,3,4,5])

print(arr)
print(type(arr))

#o-D array
arr = np.array(43)
print(arr)

#1-D array
list = [1,2,3,5]
arr = np.array(list)
print(arr)

#2-D array
arr = np.array([[1,2,3,4],[1,2,3,4]])
print(arr)

#3-D array
arr = np.array([[[1,2,3],[1,2,3,4]],[[1,2,3],[4,5,6]]])
print(arr)

#checking for dimensions ndim
arr = np.array(34)
print(arr.ndim)