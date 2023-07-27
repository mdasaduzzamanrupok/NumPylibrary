#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Reshape

import numpy as np 

arr1 = np.array([[1,2,3,4],
        [4,5,6,7]]
       )

arr1


# In[11]:


arr1.shape


# In[21]:


arr1_reshaped = np.reshape(arr1, (4,2)) 


# In[22]:


arr1_reshaped


# In[23]:


arr_reshaped2 = np.reshape(arr1, (3,3))  #value error 


# In[24]:


# Resize 


arr1


# In[25]:


arr1_resized = np.resize(arr1, (3,3))


# In[26]:


arr1_resized


# In[27]:


arr1_resized2 = np.resize(arr1, (4,2))


# In[28]:


arr1_resized2


# In[ ]:




