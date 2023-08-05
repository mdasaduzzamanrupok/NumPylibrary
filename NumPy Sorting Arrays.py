#!/usr/bin/env python
# coding: utf-8

# In[4]:


#NumPy Sorting Arrays

import numpy as np 

arr = np.array([3,1,2,5,4,0])

sort1 = np.sort(arr)

print(sort1)


# In[6]:


#Sort the array alphabetically:

arr1 = np.array(['Apple','Jackfood','Banana', 'Pineapple'])

sort2 = np.sort(arr1)

print(sort2)


# In[3]:


#Sort a boolean array:
import numpy as np

arr2 = np.array([True, False, True])

print(np.sort(arr2))


# In[5]:


#Sort a 2-D array:

arr3 = np.array([[2,1,0,3], [6,4,8,7]])

print(np.sort(arr3))


# In[ ]:




