#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import random


# In[7]:


def create_matrix_random(m,n, start, end):
    lst = []
    for i in range(m):
        lst_sub = []
        for j in range(n):
            x = random.randint(start, end+1)
            lst_sub.append(x)
        lst.append(lst_sub)    
    return np.array(lst)   

