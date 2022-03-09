#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np


# In[16]:


altura = np.array([1.74, 1.8, 1.78, 1.68, 1.78], dtype='f2')
peso = np.array([81.4, 88.7, 87.3, 62.7, 81.6], dtype='f2')


# In[17]:


matriz = np.stack((altura, peso), axis = 1)


# In[18]:


matriz


# In[19]:


matrix = np.concatenate((altura,peso))


# In[20]:


matrix


# In[21]:


matrix.dtype


# In[29]:


right_in_two = np.stack((altura, peso), axis = 1)


# In[30]:


print(right_in_two, type(right_in_two))


# In[32]:


separated = np.split(right_in_two, 5)


# In[33]:


print(separated, type(separated))


# In[ ]:





# In[ ]:




