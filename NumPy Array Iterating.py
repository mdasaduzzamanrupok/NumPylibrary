#!/usr/bin/env python
# coding: utf-8

# In[3]:


#NumPy Array Iterating

import numpy as np 

arr= np.array([1,2,3,4,5])   #Iterate on the elements of the following 1-D array

for x in arr:
    print(x)


# In[5]:


#In a 2-D array it will go through all the rows
arr1= np.array([[1,2,3], [4,5,6]])

for x in arr1:
    print(x)


# In[7]:


#Iterate on each scalar element of the 2-D array:
arr2 = np.array([[1,2,3,4],[5,6,7,8]])

for x in arr2:
    for y in x:
        print(y)


# In[14]:


#Iterate on the elements of the following 3-D array:

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr3:
    print("x represents the 2-D array:")
    print(x)


# In[15]:


#Iterate down to the scalars:

arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr4:
  for y in x:
    for z in y:
      print(z)


# In[16]:


#Iterate through the array as a string:

arr5 = np.array([1, 2, 3])

for x in np.nditer(arr5, flags=['buffered'], op_dtypes=['S']):
  print(x)


# In[18]:


#Iterate through every scalar element of the 2D array skipping 1 element:
arr6 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr6[:, ::2]):
  print(x)


# In[ ]:




