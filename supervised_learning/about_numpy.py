import numpy as np
import time

# NumPy routines which allocate memory and fill arrays with value
a = np.zeros(4);                print(f"np.zeros(4) :   a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
a = np.zeros((4,));             print(f"np.zeros(4,) :  a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
a = np.random.random_sample(4); print(f"np.random.random_sample(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

# NumPy routines which allocate memory and fill arrays with value
# but do not accept shape as input argument
a = np.arange(4.);              print(f"np.arange(4.):     a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
a = np.random.rand(4);          print(f"np.random.rand(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

# NumPy routines which allocate memory and fill with user specified values
a = np.array([5,4,3,2]);  
print(f"np.array([5,4,3,2]):  a = {a},     a shape = {a.shape}, a data type = {a.dtype}") # int64

a = np.array([5.,4,3,2]);
print(f"np.array([5.,4,3,2]): a = {a}, a shape = {a.shape}, a data type = {a.dtype}") # float64


# vector indexing operations on 1-D vectors
a = np.arange(10)
print(a)

# access an element
print(f"a[2].shape: {a[2].shape} a[2]  = {a[2]}, Accessing an element returns a scalar")

# access the last element, negative indexes count from the end
print(f"a[-1] = {a[-1]}")

# indexs must be within the range of the vector or they will produce and error
try:
    c = a[10]
except Exception as e:
    print("The error message you'll see is:")
    print(e) # out of bounds

# vector slicing operations
a = np.arange(10)
print(f"a         = {a}") # [0 1 2 3 4 5 6 7 8 9]

# access 5 consecutive elements (start:stop:step)
c = a[2:7:1];
print("a[2:7:1] = ", c) # [2 3 4 5 6]

# access 3 elements separated by two 
c = a[2:7:2];
print("a[2:7:2] = ", c) # [2 4 6]

# access all elements index 3 and above
c = a[3:];   
print("a[3:]    = ", c) # [3 4 5 6 7 8 9]

# access all elements below index 3
c = a[:3];   
print("a[:3]    = ", c) # [0 1 2]

# access all elements
c = a[:];    
print("a[:]     = ", c) # [0 1 2 3 4 5 6 7 8 9]


# Vector Operations
a = np.array([1,2,3,4])
print(f"a             : {a}") # [1 2 3 4]

# negate elements of a
b = -a 
print(f"b = -a        : {b}") # [-1 -2 -3 -4]

# sum all elements of a, returns a scalar
b = np.sum(a) 
print(f"b = np.sum(a) : {b}") # 10

b = np.mean(a)
print(f"b = np.mean(a): {b}") # 2.5

b = a**2
print(f"b = a**2      : {b}") # [1  4  9 16]

a = np.array([ 1, 2, 3, 4])
b = np.array([-1,-2, 3, 4])
print(f"Binary operators work element wise: {a + b}") # [0 0 6 8]

#try a mismatched vector operation
c = np.array([1, 2])
try:
    d = a + c
except Exception as e:
    print("The error message you'll see is:")
    print(e) # operands could not be broadcast together with shapes (4,) (2,)

a = np.array([1, 2, 3, 4])

# multiply a by a scalar
b = 5 * a 
print(f"b = 5 * a : {b}") # [5 10 15 20]
