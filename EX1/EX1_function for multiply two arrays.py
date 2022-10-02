#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Shymaa Ali Fathi.
#Applications of accelerators exercise solution.
#EX1.
#Write a function in Python code that multiples two 3x3 Matrices (ndarray) and returns the result.
#Call this function using two randomly generated 3 by 3 matrices and print the results.


# In[2]:


import numpy as np


# In[24]:


#creating a function to multiply two 3x3 arrays, function with arguments
def multiples_arrays(arr1,arr2):
    task=np.multiply(arr1, arr2)
    return task
#Define the generator needed to randomly generate numbers
rng = np.random.default_rng()
#Generating 3x3 array of random numbers
arr1=rng.random((3,3))
print ("array1",arr1)
arr2=rng.random((3,3))
print ("array2",arr2)
#call the multiples_arrays function
result=multiples_arrays(arr1,arr2)
print ("result of multiplication",result)
print ("End of EX1")


# In[ ]:




