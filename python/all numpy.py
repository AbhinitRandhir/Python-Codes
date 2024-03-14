# import numpy as ny
# arr=([1,2,3,4])
# print(arr)
# print(type(arr))

# import numpy as np
# #zero dimensional array
# a=np.array(10)
# print(a)

# import numpy as np
# #one dimensional array
# a= np.array([12,14,16])
# print ( a)

# import numpy as np
# # one dimensional array
# a= np.array([12,14,16],dtype='complex')
# print ( a)

# import numpy as np
# #two dimensinal array
# a=np.array([[1,2,3],[4,5,6]])
# print(a)



# import numpy as np
# # ndarray from list
# x = [10,20,30]
# a = np.asarray(x)
# print (a)

# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# print("Array 1: ",arr1)
# print("Array 2: ",arr2)
# np.copyto(arr2, arr1)
# print("After copying the array ")
# print("Array 1: ",arr1,)
# print("Array 2: ",arr2)

# import numpy as np
# # three dimensional array
# a= np.array([[[11,20],[30,40]],[[50,60],[70,80]]])
# print (a)

# import numpy as np
# arr=np.array([1,2,3,4])
# print(arr)
 
#2 numpy.shape
# import numpy as np
# arr=np.array([[1,2,3,4],[5,6,7,8]])
# print(arr.shape)

#3
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# arr1 = arr.reshape(2, 3, 2)
# arr2 = arr.reshape(4,3)
# print(arr1)
# print(arr2)

# arr2 = arr.reshape(-1)

#4
# import numpy as np
# a = np.array([[1,2], [3,4]])
# print(a.flatten())

#5
# import numpy as np
# x = np.array([[1.,2.],[3.,4.]])
# print(x)
# print("the transposed array is ")
# print(x.T)

#6
# import numpy as np
# x = np.array([[1, 2], [3, 4]])
# m = np.asmatrix(x)
# x[0,0] = 5
# print(m)

#7
# import numpy as np
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6]])
# c=np.concatenate((a, b), axis=0)
# print(c)
#8
# import ctypes
# import numpy as np
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# c=np.vstack((a,b))
# print(c)
#9
# import numpy as np
# a = np.array([1, 3, 4])
# b = np.array([2, 5, 6])
# c=np.hstack((a,b))
# print(c)

import numpy as np
x1 = np.arange(9.0).reshape((3, 3))
x2 = np.arange(3.0)
np.add(x1, x2)
