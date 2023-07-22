#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np 

#array attributes

a = np.array([1,3,4])  #1-d A One-Dimensional Array 


# In[10]:


a 


# In[7]:


type(a)


# In[11]:


a.shape


# In[12]:


a.ndim  


# In[13]:


b = np.array([[1,2,3,4],      
             [2,4,5,9]])             #2-d A Two-Dimensional Array 


# In[16]:


type(b), b.shape, b.ndim


# In[20]:


c = np.array([[[1,3,4,5],
              [5,6,6,3],
              [4.0,3,5,6,]]])  #3-d Three dimensional array


# In[21]:


type(c), c.shape, c.ndim


# In[22]:


#check data type 


a.dtype, b.dtype , c.dtype


# In[23]:


a.size, b.size, c.size  #Determine how many element one there in an array 


# In[24]:


a.nbytes , b.nbytes, c.nbytes   #Determine how many bytes consumed by an array 


# In[ ]:




