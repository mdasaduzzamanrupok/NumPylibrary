#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Splitting Array 

import numpy as np 

arr = np.array([1,2,3,4,5,6]) #Split the array in 3 parts:

newarr = np.array_split(arr, 3)


print(newarr)


# In[2]:


#Split the array in 4 parts:

arr1 = np.array([1,2,3,4,5,6])

newarr1 = np.array_split(arr1,4)

print(newarr1)


# In[3]:


#Access the splitted arrays:

arr2 = np.array([1,2,3,4,5,6])

newarr2 = np.array_split(arr2,3)

print(newarr2[0])
print(newarr2[1])
print(newarr2[2])


# In[4]:


#Split the 2-D array into three 2-D arrays: 


arr3 = np.array([[1,2], [2,3], [4,5], [6,7], [8,9], [10,11]])

newarr3 = np.array_split(arr3, 3)

print(newarr3)


# In[6]:


#Split the 2-D array into three 2-D arrays along rows: 

arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr4 = np.array_split(arr4, 3, axis=1)

print(newarr4)


# In[7]:


#Use the hsplit() method to split the 2-D array into three 2-D arrays along rows: 

arr5 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr5 = np.hsplit(arr5, 3)

print(newarr5)


# In[ ]:




