#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Numpy Searching Arrays 


import numpy as np 


arr = np.array([1, 2, 3, 4, 5, 6])

newarr=np.where( arr==3 )

print(newarr)


# In[6]:


#Find the indexes where the values are even:

arr2 = np.array([1,2,3,4,5,6,7,8,9])

newarr1 = np.where(arr2%2==0)

print(newarr1)


# In[11]:


#Find the indexes where the value 7 should be inserted:

arr3 = np.array([6, 7, 8, 9])

x = np.searchsorted(arr3,7)

print(x)


# In[12]:


#Find the indexes where the value 7 should be inserted, starting from the right:

arr4 = np.array([6, 7, 8, 9])

x = np.searchsorted(arr4, 7, side='right')

print(x)


# In[13]:


#Find the indexes where the values 2, 4, and 6 should be inserted:

arr5 = np.array([1, 3, 5, 7])

x = np.searchsorted(arr5, [2, 4, 6])

print(x)


# In[ ]:




