#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from time import perf_counter as perf


# In[23]:


altura_y_pesos = np.array([[ 1.74, 91.40 ],
                           [ 1.80, 88.70 ],
                           [ 1.78, 87.30 ],
                           [ 1.68, 62.70 ],
                           [ 1.78, 81.60 ]])


# In[24]:


print("Mínimo", altura_y_pesos.min())
print("Máximo", altura_y_pesos.max())
print("Posición del mínimo", altura_y_pesos.argmin())
print("Pocisión del máximo", altura_y_pesos.argmax())
print("Suma de todo", altura_y_pesos.sum())
print("Media de todo", altura_y_pesos.mean())


# In[25]:


altura_y_pesos.ndim


# In[26]:


altura_y_pesos.shape  # Vertical, Horizontal


# In[22]:


print("Mínimo de la columna estatura", altura_y_pesos.min(axis = 0))
print("Máximo de la columna estatura", altura_y_pesos.max(axis = 0))
print("Posición del mínimo en la columna estatura", altura_y_pesos.argmin(axis = 0))
print("Pocisión del máximo en la columna estatura", altura_y_pesos.argmax(axis = 0))
print("Suma de la columna estatura", altura_y_pesos.sum(axis = 0))
print("Media de la columna estatura", altura_y_pesos.mean(axis = 0))


# In[ ]:





# In[ ]:





# In[ ]:




