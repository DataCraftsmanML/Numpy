import numpy as np
#NumPy ufuncs

"""x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []
for i, j in zip(x, y):
  z.append(i + j)
print(z)
"""

"""x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x,y)
print(z)"""

#Create Your Own ufunc

"""def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 4,  1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
"""













#Simple Arithmetic
"""arr1 = np.array([10,15,20,30])
arr2 = np.array([5,8,7,4])
newarr1 = np.add(arr1, arr2)
newarr2 = np.subtract(arr1, arr2)
newarr3 = np.multiply(arr1, arr2)
newarr4 = np.divide(arr1, arr2)
newarr5 = np.power(arr1, arr2)
newarr6 = np.remainder(arr1, arr2)
newarr7 = np.mod(arr1, arr2)
newarr8 = np.divmod(arr1, arr2)
print(newarr1, "\n", newarr2, "\n", newarr3, "\n", newarr4, "\n", newarr5, "\n", newarr6, "\n", newarr7, "\n", newarr8)
"""
"""arr3 = np.array([1, -2, -4, 5])
newarr9 = np.absolute(arr3)
print(newarr9)
"""

                             #Rounding Decimals

"""Rounding Decimals
   There are primarily five ways of rounding off decimals in NumPy:

"""

#Truncation and fix

"""arr1 = np.trunc([-3.1666, 3.6667])
arr2 = np.fix([-3.1666, 3.6667])
print(arr1, "\n", arr2)
"""

#   rounding
"""arr = np.around(3.1666, 2)
print(arr)
"""

#Floor




#Ceil




                                                  #NumPy Logs


"""arr = np.arange(1, 10)
print(np.log(arr))
print(np.log2(arr))
print(np.log10(arr))
"""

#Log at Any Base





                                                #NumPy Summations
#Summations
"""np.add(arr1, arr2):
- Adds two arrays element-wise
- Takes two separate arguments

np.sum([arr1, arr2]):
- Sums multiple arrays
- Takes a single argument (a list of arrays)
"""

"""arr1 = np.array([1,2,3])
arr2 = np.array([1,2,3])
newarr1 = np.add(arr1,arr2)
newarr2 = np.sum()
print(newarr)
"""

#Summation Over an Axis
"""arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr1 = np.sum([arr1, arr2], axis=0)
newarr2 = np.sum([arr1, arr2], axis=1)
print(newarr1)
print(newarr2)
"""

#Cummulative Sum

"""arr1 = np.array([2,5,7])
newarr = np.cumsum(arr1)
print(newarr)
"""

                                        #NumPy Products

"""newarr1 = np.prod(arr1):
This calculates the product of all elements in arr1.
Result: 1 * 5 * 4 * 3 = 60
It doesn't print [] because it's a single scalar value.

newarr2 = np.prod([arr1, arr2]):
This creates a list of two arrays: [arr1, arr2]
NumPy interprets this as a 2D array:
[[1, 5, 4, 3],
[1, 4, 3, 2]]
"""

"""arr1 = np.array([1,5,4,3])
arr2 = np.array([1,4,3,2])
newarr1 = np.prod(arr1)
newarr2 = np.prod([arr1, arr2])
print(newarr1, "\n", newarr2)
"""

#Product Over an Axis
"""arr1 = np.array([1,3,5,2])
arr2 = np.array([5,4,2,1])
newarr = np.prod([arr1,arr2],axis=1)
print(newarr)
"""

#Cummulative Product
"""arr1 = np.array([1,2,3,4,5])
newarr = np.cumprod(arr1)
print(newarr)
"""

#NumPy Differences

#Differences
#A discrete difference means subtracting two successive elements.
"""arr1 = np.array([1,3,5,3])
newarr = np.diff(arr1)
print(newarr)
"""

"""arr1 = np.array([10, 15, 25, 5])
newarr0 = np.diff(arr1, n=0)
newarr1 = np.diff(arr1, n=1)
newarr2 = np.diff(arr1, n=2)
newarr3 = np.diff(arr1, n=3)
print(newarr0,"\n",newarr1,"\n",newarr2,"\n",newarr3)
"""

                                 #NumPy LCM Lowest Common Multiple

"""num1 = 12
num2 = 4

x = np.lcm(num1, num2)
print(x)
"""

"""arr1 = np.array([1,2,3])
x = np.lcm.reduce(arr1)
print(x)
"""

#arr1 = np.arange(1,11)
#x = np.lcm.reduce(arr1)
#print(x)

                              #NumPy GCD Greatest Common Denominator

"""num1 = 5
num2 = 10
x = np.gcd(num1, num2)
print(x)
"""

#Finding GCD in Arrays
"""arr1 = np.array([5,10,15])
x = np.gcd.reduce(arr1)
print(x)
"""


                               #NumPy Trigonometric Functions

#Find sine value of PI/2:
"""x = np.sin(np.pi/2)
y = np.sin(np.pi/3)
print(x, "\t", y)
"""
"""z = np.array([np.pi/2, np.pi/3, np.pi/4])
a = np.sin(z)
print(a)
"""

#Convert Degrees Into Radians
#Note: radians values are pi/180 * degree_values.
"""arr1 = np.array([3,5,7,9])
x = np.deg2rad(arr1)
print(x)
"""

#Radians to Degrees
#multiply the number of radians by 180/π.
"""arr1 = np.array([3,5,7,9])
x = np.rad2deg(arr1)
print(x)
"""

#Finding Angles
#sin inverse
"""x = np.arcsin(1)
print(x)"""

#Angles of Each Value in Arrays
"""arr1 = np.array([1,-1,0.1])
x = np.arcsin(arr1)
print(x)"""

#Hypotenues

"""base = 4
perp = 5
x = np.hypot(base, perp)
print(x)
"""


                                #NumPy Hyperbolic Functions

#Hyperbolic Functions

"""x = np.sinh(np.pi/2)
print(x)
"""


                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                         
                                         #NumPy Set Operations

#Create Sets in NumPy
"""arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)
"""

#Finding Union

"""arr1 = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
arr2 = np.array([2,4,6,4,2])
x = np.union1d(arr1, arr2)
print(x)
"""

#Finding Intersection
"""arr1 = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
arr2 = np.array([2,4,6,4,2])
x = np.intersect1d(arr1, arr2)
print(x)
"""

#Finding Difference

"""set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setdiff1d(set1, set2, assume_unique=True)
print(newarr)
"""

#Finding Symmetric Difference

"""set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setdiff1d(set1, set2, assume_unique=True)
print(newarr)
"""