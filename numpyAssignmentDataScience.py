# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:05:06 2023

@author: yuvra_d0x8avj
"""
###############################################################################

# Write Numpy Version
import numpy as np
print(np.__version__)

###############################################################################

# write numpy program to check whether none of the element of array is zero

                              # all

import numpy as np

arr=np.array([1,2,3,4])
print('Original Array:',arr)
print('Is array is not containing zero?',np.all(arr)) 

arr2=np.array([1,2,3,4,0])
print('Original Array:',arr2)
print('Is array is not containing zeros?',np.all(arr2)) 


###############################################################################

# write numpy program to test if any of the element of array is non zero

                                # any

import numpy as np
arr3=np.array([1,2,3,0])
print(np.any(arr3))

import numpy as np
arr4=np.array([0,0,0,0,0])
print(np.any(arr4))

###############################################################################

# write numpy program to test given array element-wise for finiteness
# not infinity or not a number

                            # isfinite()

import numpy as np
arr1=np.array([1,0,np.nan,np.inf])
print('Test a given array element-wise for finiteness')
print(np.isfinite(arr1))

###############################################################################

# Write a numpy program to test element-wise NaN for a givena rray

                            # .isnan()
                            
import numpy as np

a=np.array([1,0,np.nan,np.inf])
print(np.isnan(a))


###############################################################################

# Write Numpy program to create an element-wise comparision
# (greater, greater_equal,less and less_equal)
 
                            #greater()
                            #greater_equal()
                            #less()
                            #less_equal()

x=np.array([3,5])
y=np.array([2,5])
print('Original numbers: ')
print(x)
print(y)
print('For Greater:')
print(np.greater(x,y))
print('For Greater_equal:')
print(np.greater_equal(x,y))
print('Less:')
print(np.less(x,y))
print('For Less_equal: ')
print(np.less_equal(x,y))

###############################################################################

# Write Numpy program to create 3X3 Identity matrix

                            # .identity(size like 3)

import numpy as np
arr1=np.identity(3)
print(arr1)


###############################################################################

# write Numpy program to generate a random number

# .random.normal(loc:mean,scale:standard deviation,size )
                            
import numpy as np
rand_num=np.random.normal(0,1,2)
print(rand_num)

###############################################################################

# write Numpy program to create a
# 3X4 array and iterate over it.

                      # nditer(array)
                      # arrange(start,end) and reshape(row,column)

import numpy as np

a=np.arange(10,22).reshape((3,4))
print('Original Array')
print(a)

for x in np.nditer(a):
    print(x,end=" ")
    print()

###############################################################################

# write Numpy program to create vector of length 5
#a whose values is distributed between 10 and 50
 
              # linspace(start pt,end pt,total no in vector)

import numpy as np
v=np.linspace(10,49,5)
print(v)

###############################################################################
# write Numpy program to create 3X3 matrix 
# with values ranging from 2 to 10

import numpy as np
x=np.arange(2,11).reshape(3,3)
print(x)

###############################################################################

# write Numpy program to reverse an array
# (the first element becomes last)

                                  # [::-1] 

import numpy as np
arr=np.array([1,2,3,4,5,6])
x=arr[::-1]
print(x)

###############################################################################

# write Numpy program to compute the multiplication of two given matric

                                  # dot(matrix1,matrix2)      

import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
x=np.dot(p, q)
print(x) # multiplication of matrix by .dot

###############################################################################

# write Numpy program to compute cross product of two matrix

import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
z=np.cross(p, q)
print(z)

###############################################################################

# write Numpy program to compute determinent of given square array

                                    #linalg
                                    #linalg.det(single argument)
                                    #to find determinent

import numpy as np
from numpy import linalg as LA 

p=[[1,0],[1,2]]
q=[[1,2],[3,4]]

x=np.linalg.det(p)
print(x)

###############################################################################

# write Numpy program to compute eigenvalues and right eigenvectors of given square array
  

                                #np.linalg.eig(matrix)

import numpy as np
from numpy import linalg 
a=np.mat("3 -2;1 0")
print('Original Matrix: ',a)
w,v=np.linalg.eig(a)
print('Eigen values: ',w)
print('Eigen Vector: ',v)

###############################################################################

# write Numpy program to compute the inverse of given array

                                 # np.linalg.inv(matrix)
                                 


import numpy as np
from  numpy import linalg
a=np.mat("1,2;3,4")
a=np.linalg.inv(a)
print(a)


###############################################################################

# write Numpy program to compute 



