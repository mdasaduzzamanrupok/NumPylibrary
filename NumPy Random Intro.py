#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Generate a random integer from 0 to 100:

from numpy import random 

x = random.randint(100)

print(x)


# In[22]:


#Generate Random Float

x1 = random.rand()

print(x1)


# In[13]:


#Generate a 1-D array containing 5 random integers from 0 to 100:

from numpy import random

y = random.randint(100, size=(7))

print(y)


# In[16]:


#Generate a 2-D array with 4 rows, each row containing 6 random integers from 0 to 100:

t = random.randint(100, size = (4,6))

print(t)


# In[17]:


#Generate a 1-D array containing 5 random floats:

e = random.rand(5)

print(e)


# In[18]:


#Generate a 2-D array with 3 rows, each row containing 5 random numbers: 


w = random.rand(3,5)

print(w)


# In[19]:


#Return one of the values in an array: 

b = random.choice([3,5,6,3,10])

print(b)


# In[20]:


#Generate a 2-D array that consists of the values in the array parameter (3, 5, 6, and 10):
    
k = random.choice([3,5,6,3,10], size = (3,5))

print(k)


# In[ ]:




