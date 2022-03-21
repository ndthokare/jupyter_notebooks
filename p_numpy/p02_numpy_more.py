"""
>>> import numpy as np
>>> a = np.array([5,6,9])
>>> a = np.array([[1,2],[3,4],[5,6]])
>>> a.ndim
>>> a.itemsize
>>> a.dtype
>>> a = np.array([[1,2],[3,4],[5,6]], dtype=np.float)
>>> a.dtype
>>> a.size
>>> a.shape
>>> a
>>> a = np.array([[1,2],[3,4],[5,6]], dtype=np.complex_)
>>> b = np.zeros((3,4))
>>> b
>>> c = np.ones((3,4))
>>> c
>>> l = range(5)
>>> l[2]
>>> np.arange(1,5) # similar to range in python
>>> np.arange(1,10,3) # similar to range in python
>>> np.linspace(1,2,10) # creates array of 10 elements equispaced between 1 & 2

>>> a = np.array([[1,2],[3,4],[5,6]])
>>> a.shape
>>> b = a.reshape(2,3)
>>> b.shape
>>> a.reshape(6,1)
>>> a.ravel() # flattens array. Creates one dimensional array
>>> a.min()
>>> a.max()
>>> a.sum()

>>>import numpy as np a.sum(axis=0) # return sum along axis (dimension) 0 - [column-axis=0, row-axis=1]
>>> a.sum(axis=1)
>>> np.sqrt(a)
>>> np.std(a) # standard deviation

>>> a = np.array([[1,2],[3,4]])
>>> b = np.array([[5,6],[7,8]])
>>> a+b # element wise operation
>>> a*b # element wise operation
>>> b/a # element wise operation
>>> b/2 # element wise operation
>>> 10/b # element wise operation
>>> a.dot(b) # matrix multiplication

>>>import numpy as np a = np.array([[1,2],[3,4]])
>>> b = np.array([[5,6],[7,8]])
>>> a.dtype
>>> np.concatenate((a,b))
>>> np.append(a,b,axis=0)
>>> np.append(a,b,axis=1)


"""
