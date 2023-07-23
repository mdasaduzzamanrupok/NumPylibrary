#!/usr/bin/env python
# coding: utf-8

# # Array creation 

# In[2]:


import numpy as np 

array1 = np.array([1,2,3,4], dtype = 'int')

array1


# In[6]:


#zeros

zeros = np.zeros((2,2) , dtype = 'float')

zeros


# In[10]:


#ones

ones = np.ones((3,3), dtype = 'int')

ones


# In[14]:


#full


full = np.full((2,3), 8)

full


# In[15]:


#identity 

identity= np.identity(3, dtype = 'int')

identity


# In[20]:


#eye

eye = np.eye(3,3, -1)

eye


# In[24]:


#arange 

arange = np.arange(1,100,5)

arange


# In[32]:


#linespace 

linspace = np.linspace(1,100,50, dtype='int')


linspace


# In[29]:


#empty

empty = np.empty((1,5))
empty


# In[30]:


for i in range(5):
    empty[:,i] = i
empty


# In[ ]:




