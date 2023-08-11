#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Filtering Arrays

import numpy as np  

arr = np.array([11,23,54,34])  #Create an array from the elements on index 0 and 2:

x = [True, False, True, False]

newarr= arr[x]

print(newarr)


# In[11]:


#Create a filter array that will return only values higher than 42:

import numpy as np 
arr1 = np.array([11,23,54,34])


filter_arr = []  #Create an empty list


for element in arr1:
    if element >42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
     
        
newarr1 = arr1[filter_arr]
print(filter_arr)
print(newarr1)



# In[13]:


#Create a filter array that will return only even elements from the original array:

import numpy as np

arr2 = np.array([1,2,3,4,4,6,7,8])

filter_arr1 = []

for element in arr2:
    if element % 2 == 0:
        filter_arr1.append(True)
    else:
        filter_arr1.append(False)
newarr2 = arr2[filter_arr1] 

print(filter_arr1)
print(newarr2)


# In[ ]:




