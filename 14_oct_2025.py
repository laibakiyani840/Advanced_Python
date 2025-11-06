import numpy as np
print(np.random.rand(2,3))
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr.shape)
print(arr.ndim)
print(arr.dtype)
print(arr.size)
print(arr.itemsize)
print(arr.nbytes)
print(arr.shape,arr.ndim,arr.dtype)
# Indexing and slicing numPy array
arr=np.array([[10,20,30],[40,50,60]])
print(arr)
#basic indexing
print(arr[0,1])
print(arr[0][1])
print(arr[1][2])
# slicing array
print(arr[0,0:2])
print(arr[0,:2])
print(arr[:,1:])
# Negative indexing
print(arr[-1,-2])
# 1D vs 2D Behavior
a=np.arange(10)
print(a)
print(a[2:7:2])
# Element wise arithmetic operations
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)
print(a-b)  
print(a*b)
print(a/b)
print(a*10)
print(a-1)
# Comparison operations
print(a>2)
print(a<=2)
print(a==2)
print(a!=2)
print(a>=2)

# Mathematical functions
print(np.sqrt(a))   
print(np.exp(a))
print(np.log(a))
# Trigonometric functions
print(np.sin(a))
print(np.cos(a))
print(np.tan(a))
print(np.sinh(a))
print(np.cosh(a))
print(np.tanh(a))
print(np.sin(np.pi/2))
print(np.cos(0))
# Aggregate functions
print(np.sum(a))
print(np.mean(a))
print(np.median(a))
print(np.std(a))
print(np.var(a))
print(np.min(a))
print(np.max(a))    
# Apply universal functions to multi-dimensional arrays
b=np.array([[1,2,3],[4,5,6]])
print(b)
print(np.sum(b,axis=0)) # column-wise sum
print(np.sum(b,axis=1)) # row-wise sum
print(np.mean(b,axis=0)) # column-wise mean
print(np.mean(b,axis=1)) # row-wise mean
print(np.std(b,axis=0)) # column-wise std
print(np.std(b,axis=1)) # row-wise std
print(np.var(b,axis=0)) # column-wise variance
print(np.var(b,axis=1)) # row-wise variance
print(np.min(b,axis=0)) # column-wise min
print(np.min(b,axis=1)) # row-wise min  
print(np.max(b,axis=0)) # column-wise max
print(np.max(b,axis=1)) # row-wise max

# Reshaping and Manipulating Arrays
c=np.arange(12)
print(c)
reshaped_c=c.reshape(3,4)
print(reshaped_c)
flattened_c=reshaped_c.flatten()
print(flattened_c)

# Transpose of an array
b=np.array([[1,2],[3,4]])
print(b)
print(b.T)