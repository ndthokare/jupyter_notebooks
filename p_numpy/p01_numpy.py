"""
>>> import numpy as np

>>> a = np.array([[1,2],[3,4]])
>>> b = np.array([[5,6],[7,8]])
>>> a*b # element wise operation
>>> b/2 # element wise operation
>>> 10/b # element wise operation
>>> a.dot(b) # matrix multiplication

>>>a = np.array([[1,2],[3,4]])
>>> b = np.array([[5,6],[7,8]])
>>> a.dtype
>>> np.concatenate((a,b))
>>> np.append(a,b,axis=0)
>>> np.append(a,b,axis=1)
>>> np.vstack((a,b))
>>> np.hstack((a,b))
>>> np.dstack((a,b))

>>> c = np.array([[1,2,3,4],[5,6,7,8]])
>>> c.reshape(2,2,2)

"""
