#!/usr/bin/env python
# coding: utf-8

# # Array indexing and slicing 
# 
# 

# In[2]:


#indexing

import numpy as np

arr1= np.array([1,2,3,4,5])

print(arr1)


# In[3]:


arr1[0]


# In[4]:


arr1[1]


# In[5]:


arr1[-1]


# In[7]:


arr2 = np.random.randint(1,10, size = (3,3))

print(arr2)


# In[8]:


arr2[0][0]


# In[11]:


arr2[1,1]


# In[12]:


arr3 = np.random.randint(1,10, size = (2,3,3))

print(arr3)


# In[13]:


arr3[0][1][1]


# In[16]:


arr3[0,1,1]


# In[19]:


arr3[1,2,1]


# In[20]:


#slicing

print(arr1)


# In[21]:


print(arr1[0:2])


# In[24]:


print(arr1[2:])


# In[23]:


print(arr2)


# In[26]:


arr2[0:2,0:2]


# In[27]:


arr2[1: ,1:]


# In[ ]:




