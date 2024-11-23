#Numpy Getting Started

import numpy as np

#arr1: This is a NumPy array object created using the np.array function. It contains the elements [1, 2, 3, 4, 5].
#np: This is the NumPy module, which is imported at the beginning of the code using import numpy as np.

"""arr1 = np.array({1,2,3,4,5}); #using only one digit then use  arr1 = np.array(1) 
print(arr1)
"""

"""
#np.__version__: This is a string object representing the version of the NumPy module that is currently being used.
print(np.__version__)

#Create a NumPy ndarray Object
#NumPy is used to work with arrays. The array object in NumPy is called ndarray.
#We can create a NumPy ndarray object by using the array() function.
#type(): This built-in Python function tells us the type of the object passed to it. Like in above code
it shows that arr is numpy.ndarray type.
print(type(arr1))
"""

"""arr2 = np.array(12)  #0-D Arrays
arr3 = np.array([1, 2, 3, 4, 5]) #1-D Arrays
arr4 = np.array([[1, 2, 3], [4, 5, 6]]) #2-D Arrays
arr5 = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])#3-D Arrays
print(arr2, "dimensions is", arr2.ndim)
print(arr3, "dimensions is", arr3.ndim)
print(arr4, "dimensions is", arr4.ndim)
print(arr5, "dimensions is", arr5.ndim)
"""

#Higher Dimensional Arrays
"""arr6 = np.array([12, 13, 14, 15],ndmin=2)
print(arr6)
"""
                                       #NumPy Array Indexing

#Access Arrays Element
"""arr7 = [1,2,3,4,5]
print(arr7[2])
print(arr7[1] + arr7[4])
"""
#Access 2-D Arrays
"""arr8 = np.array([[1,2,3,4], [5,6,7,8]])
print(arr8[0,1])
c"""
#Access 3-D Arrays

"""arr9 = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print(arr9[1,1,1])
"""

#Negative Indexing
"""arr10 = np.array([[1,2,3],[4,5,6]])
print(arr10[0,1])
"""

                            #NumPy Array Slicing


"""arr11 = np.array([1,2,3,4,5,6,7])
print(arr11[1])
print(arr11[-1])
print(arr11[1:])
print(arr11[:1])
print(arr11[-1:])
print(arr11[:-1])
print(arr11[1:3])
print(arr11[-3:-1])
print(arr11[1:5:2])
print(arr11[::2])
"""
#Slicing 2-D Arrays

"""arr12 = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])
print(arr12[1, 1:4])
print(arr12[1:2, 1])
print(arr12[1:3])
"""

#Array Copy vs View

"""arr14 = np.array([1,2,3,4,5])
x = arr14.copy()
arr14[0] = 0
print(arr14,arr14.base)  #copy
print(x,x.base)          #orignal

print()
"""

"""arr15 = np.array([6,7,8,9,10])
y = arr15.view()
arr15[0] = 0
print(arr15,arr15.base)  #view
print(y,y.base)      #orignal
"""









                                          #Array Shape

"""arr16 = np.array([[1,2,3,4,5],
                  [1,2,3,4,5]])
print(arr16.shape)
"""







                                            #Array Reshaping
#Reshape From 1-D to 2-D
"""arr18 = np.array([1,2,3,4,5,6,7,8,9])
x = arr18.reshape(3,3)
print(x)
"""

#Reshape From 1-D to 3-D
"""arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
newarr = arr.reshape(3, 3, 2)
print(newarr)
"""

#Returns Copy or View?
"""arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)
"""

#Unknown Dimension
"""arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -2)
print(newarr)
"""

#Flattening the arrays
"""arr = np.array([[1, 2, 3, 4, 4], [4, 5, 6, 7, 4]])
newarr = arr.reshape(-1)
print(newarr)
"""

                    #NumPy Array Iterating

#Iterating 1-D Arrays
""""arr23 = np.array([1,2,3,4,5])
for x in arr23:
    print(x)
"""

#Iterating 2-D Arrays
"""arr24 = np.array([1,2,3,4,5])
for x in arr24:
    print(x)
"""

#To return the actual values
"""arr25 = np.array([[1,2,3,4],[5,6,7,8]])
for x in arr25:
    for y in x:
        print(y)
"""

#Iterating 3-D Arrays
"""arr26 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr26:
    print(x)
"""

#To return the actual values
"""arr27 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr27:
    for y in x:
        for z in y :
         print(z)
"""

#Iterating Arrays Using nditer()






#Iterating Array With Different Data Types




#Iterating With Different Step Size


#Enumerated Iteration Using ndenumerate()



                          #NumPy Joining Array

"""arr33 = np.array([1, 2, 3])
arr34= np.array([4, 5, 6])
arr35 = np.concatenate((arr33, arr34))
print(arr35)
"""
#Join two 2-D arrays along rows (axis=1):

"""arr35 = np.array([[1,2],[3,4]])
arr36 = np.array([[5,6],[7,8]])
arr37 = np.concatenate((arr35, arr36), axis=1)
print(arr37) 
"""

"""arr35 = np.array([[1,2],[3,4]])
arr36 = np.array([[5,6],[7,8]])
arr37 = np.concatenate((arr35, arr36), axis=1)
print("2D array:")
print(arr37)
# Convert to 1D array
arr37_1d = arr37.flatten()
print("\n1D array:")
print(arr37_1d)
"""
#Stacking Along Rows

"""arr41 = np.array([1,2,3,4,5])
arr42 = np.array([6,7,8,9,10])
arr43 = np.hstack((arr41, arr42))
print(arr43)
"""

#Stacking Along Columns
"""arr44 = np.array([1,2,3,4,5])
arr45 = np.array([6,7,8,9,10])
arr46 = np.vstack((arr44, arr45))
print(arr46)
"""

#Joining Arrays Using Stack Functions
"""arr38 = np.array([1, 2, 3])
arr39 = np.array([4, 5, 6])
arr40 = np.stack((arr38, arr39), axis=1)
print(arr40)
"""

#Stacking Along Height (depth)
"""arr47 = np.array([[1,2],[3,4]])
arr48 = np.array([[5,6],[7,8]])
arr50 = np.dstack((arr47, arr48))
print(arr50)
"""

                                   #NumPy Splitting Array

"""arr48 = np.array([1, 2, 3, 4, 5, 6])
newarr49 = np.array_split(arr48, 4)
print(newarr49)
#Split Into Arrays
print(newarr49[0])
print(newarr49[1])
print(newarr49[2])
"""

#Splitting 2-D Arrays
"""arr50 = np.array([[1,2,0],[3,4,0],[5,6,0],[7,8,0],[9,10,0],[11,12,0]])
arr51 = np.array_split(arr50, 2)
print(arr51)
print(arr51[0])
print(arr51[1])
"""

#Split the 2-D array into three 2-D arrays along rows.
"""arr51 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
arr52 = np.array_split(arr51, 2, axis=1)
print(arr52)
"""

#in above code An alternate solution is using hsplit()
"""arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr)
"""

"""arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.vsplit(arr,3)
print(newarr)
"""

                         #Searching Arrays


"""arr57 = np.array([1,3,6,3,8,9,5])
arr58 = np.where(arr57 == 0)
print(arr58)
"""

"""arr59 = np.array([1,2,3,4,5,6,7,8,9,10])
arr60 = np.where(arr59%2 == 0)
arr61 = np.where(arr59%1 == 0)
print(arr60,"\n", arr61)
"""

#Search Sorted







































                                  # Sorting Arrays

"""arr68 = np.array([1,3,5,7,9,2,4,6,8,10])
print(np.sort(arr68))

arr69 = np.array(['banana', 'fruits', 'cherry', 'apple'])
print(np.sort(arr69))

arr70 = np.array(['True', 'False', 'True', 'False'])
print(np.sort(arr70))
"""
#Sorting a 2-D Array

"""arr71 = np.array([[1,9,6,4,7],[3,5,8,2,10]])
print(np.sort(arr71))
"""

                                    #NumPy Filter Array
#Filtering Arrays
"""arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
jia = arr[x]
print(jia)
"""

"""arr = np.array([1,2,3,4,5,6,7,8,9,10])
Filter_Array = []
for x in arr:
  if x > 5:
    Filter_Array.append(True)
  else:
    Filter_Array.append(False)

newarray = arr[Filter_Array]
print(Filter_Array)
print(newarray)
"""

"""arr = np.array([1,2,3,4,5,6,7,8,9,10])
Filter_Array = []
for x in arr:
  if x % 2 == 0:
    Filter_Array.append(True)
  else:
    Filter_Array.append(False)

newarray = arr[Filter_Array]
print(Filter_Array)
print(newarray)

"""