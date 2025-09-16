# numpy array
import numpy as np 
arr1=np.array([4,24,23,56,63])
arr2=np.array([21,32,34,54,65])
print(arr1)
print(type(arr1))
 
#slicing in simple array
print(arr1[0:2],arr2[4])
#slicing in nested array 
arr3=np.array([23,43,46,56],[45,52,78])
print(arr3[0:1 , 1:2])

