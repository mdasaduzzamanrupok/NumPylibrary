#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Numpy vertical Stacking 

import numpy as np 


# In[4]:


#horizontal stacking

a = np.arange(1,10).reshape(3,3)


# In[18]:


a


# In[6]:


b = 2*a


# In[7]:


b


# In[8]:


#hstack
np.hstack((a,b))


# In[12]:


#column_stack
np.column_stack((a,b))


# In[11]:


#concatenate
np.concatenate((a,b), axis = 1)


# In[13]:


#vertical stacking 

#vstack
np.vstack((a,b))


# In[14]:


#row_stack
np.row_stack((a,b))


# In[15]:


np.concatenate((a,b))


# In[16]:


#depth stack

#dstack
np.dstack((a,b))


# In[ ]:




