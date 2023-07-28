#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Ravel
import numpy as np 

arr1 = np.random.randint(1,10, (2,3)) #return a view of the array 

arr1


# In[2]:


arr1_raveled = np.ravel(arr1)   


# In[4]:


arr1_raveled


# In[5]:


arr1_raveled.shape


# In[8]:


arr1_raveled[0]= 100


# In[9]:


arr1


# In[10]:


#flatten

arr1


# In[11]:


arr1_flattened = arr1.flatten()  #return a copy of the array , always allocates a new array 


# In[12]:


arr1_flattened


# In[13]:


arr1_flattened[0]= 0


# In[15]:


arr1_flattened


# In[16]:


arr1       


# In[17]:


#defining an array shape 

arr1


# In[18]:


arr1.shape 


# In[19]:


arr1.shape = (3,2)


# In[20]:


arr1


# In[21]:


arr1.shape = (5,2) #cannot reshape array of size 6 into shape (5,2)


# In[ ]:




