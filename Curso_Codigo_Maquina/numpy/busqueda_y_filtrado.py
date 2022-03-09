#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from time import perf_counter as perf


# In[2]:


arreglo = np.array([i for i in range(1,16)])


# arreglo

# In[3]:


np.where(arreglo >= 10)


# In[4]:


arreglo = np.array([1.1, 1.2, 1.3, 1.4, 1.5], dtype='f2')


# In[5]:


arreglo.dtype


# In[6]:


class Busquedas:
    
    def __init__(self, array):
        self.array = array
        pass
    
    def __str__(self):
        return "Busquedas con numpy"
    
    def realiza_busqueda(self, busqueda = 0, signo = ''):
        if busqueda > max(self.array) or busqueda < min(self.array):
            return "out of range"
        elif signo == "==":
            return list(np.where(self.array == busqueda))
        elif signo == ">=":
            return list(np.where(self.array >= busqueda))
        elif signo == "<":
            return list(np.where(self.array < busqueda))
        elif signo == ">":
            return list(np.where(self.array > busqueda))
        elif signo == "<=":
            return list(np.where(self.array <= busqueda))
        else:
            return "invalid search"


# In[7]:


b = Busquedas(arreglo)


# In[8]:


b.realiza_busqueda(busqueda=10, signo='==')


# In[9]:


arreglo = np.arange(1,161)


# In[10]:


arreglo


# In[11]:


arreglo = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# In[12]:


filtro = [True, False, True, True, True, True, False, False, True, True]


# In[13]:


arreglo[filtro]


# In[16]:


alturas = np.array([1.74, 1.8, 1.78, 1.68, 1.78, 1.7, 1.74, 1.74, 1.73, 1.79,
           1.78, 1.72, 1.65, 1.78, 1.7, 1.68, 1.79, 1.68, 1.82, 1.72,
           1.75, 1.66, 1.67, 1.79, 1.75, 1.65, 1.78, 1.73, 1.71, 1.81,
           1.73, 1.71, 1.68, 1.74, 1.75, 1.68, 1.74, 1.81, 1.73, 1.82,
           1.8, 1.67, 1.73, 1.7, 1.73, 1.7, 1.81, 1.81, 1.76, 1.82, 1.68,
           1.74, 1.65, 1.8, 1.78, 1.7, 1.68, 1.78, 1.79, 1.73, 1.64, 1.67,
           1.69, 1.74, 1.76, 1.66, 1.66, 1.73, 1.79, 1.81, 1.78, 1.63,
           1.76, 1.72, 1.71, 1.7, 1.62, 1.8, 1.75, 1.8, 1.78, 1.78, 1.76,
           1.65, 1.65, 1.68, 1.74, 1.75, 1.69, 1.75, 1.7, 1.83, 1.64, 1.7,
           1.69, 1.69, 1.64, 1.69, 1.77, 1.8, 1.78, 1.69, 1.7, 1.7, 1.7,
           1.63, 1.73, 1.84, 1.66, 1.78, 1.8, 1.79, 1.78, 1.74, 1.77,
           1.73, 1.77, 1.76, 1.75, 1.8, 1.75,  1.8, 1.79, 1.71, 1.73,
           1.59, 1.76, 1.75, 1.71, 1.76, 1.8, 1.68, 1.74, 1.77, 1.73,
           1.68, 1.63, 1.67])

pesos = np.array([81.4, 88.7, 87.3, 62.7, 81.6, 80.9, 74.6, 84.7, 76.7, 88.3,
         84.6, 74, 57.7, 84.1, 79.7, 63.8, 88.4, 71.2, 87.1, 67, 80.7,
         74.7, 60.5, 85.9, 72.4, 59.7, 87.3, 85.7, 64.1, 91.9, 82.8, 75.7,
         60.2, 73.1, 74.7, 65.9, 80.9, 91.3, 76, 86.8, 80.7, 74.2, 83.1,
         77.8, 84.5, 58.8, 89.5, 87, 84, 89.9, 56.5, 80.2, 61.8, 86.3,
         82.6, 69.4, 65.8, 79.3, 88.1, 78.5, 69.1, 62.5, 74, 74.4, 87.6,
         59.6, 61.4, 83.2, 89.2, 89.2, 103.7, 67.9, 85.4, 69.5, 75.7,
         83.9, 59.5, 87.9, 82.6, 88.1, 86.2, 88.9, 84.4, 58.4, 61.5, 69.2,
         84.2, 78, 81.1, 81.5, 74.7, 90.4, 59.2, 79.3, 65.1, 93, 60.5,
         76.4, 98.8, 89.1, 88.9, 61.1, 76.6, 86, 75.5, 66.9, 79.4, 87.9,
         72.3, 93.8, 89, 90.7, 86.7, 77.6, 85.1, 91.8, 103.2, 91.1, 67,
         86.9, 78.7, 87.1, 85.5, 69.8, 75, 53.9, 99, 93.7, 88, 79.4, 87.6,
         60.4, 82.7, 90.6, 79.8, 61.2, 62.5, 59.7])


# In[17]:


paises = np.array(["Albania", "Alemania", "Andorra", "Angola",
                "Antigua y Barbuda", "Arabia Saudita", "Argelia",
                "Argentina", "Armenia", "Australia", "Austria",
                "Bahrein", "Bangladesh", "Belarús", "Belice", "Benín",
                "Bermudas", "Bolivia", "Bosnia y Hercegovina", "Botsuana",
                "Brasil", "Brunéi", "Burundi", "Bélgica", "Cabo Verde",
                "Cambodia", "Canadá", "Catar", "Chad", "Chequia", "Chile",
                "Colombia", "Congo (Rep. Democr.)", "Corea del Norte",
                "Corea del Sur", "Costa de Marfil", "Costa Rica", "Croacia",
                "Cuba", "Dinamarca", "Dominica", "Ecuador", "Egipto",
                "El Salvador", "Emiratos Árabes", "Eritrea", "Eslovaquia",
                "Eslovenia", "España", "Estonia", "Etiopía", "Fiji",
                "Filipinas", "Finlandia", "Francia", "Gabón", "Gambia",
                "Granada", "Grecia", "Groenlandia", "Guatemala",
                "Guinea Ecuatorial", "Honduras", "Hong Kong", "Hungría",
                "India", "Indonesia", "Iraq", "Irlanda", "Islandia",
                "Islas Cook", "Islas Salomón", "Israel", "Japón",
                "Kirguistán", "Kiribati", "Laos", "Letonia", "Libia",
                "Lituania", "Luxemburgo", "Líbano", "Macedonia",
                "Madagascar", "Malaui", "Maldivas", "Malta", "Marruecos",
                "Micronesia", "Moldavia", "Mongolia", "Montenegro",
                "Mozambique", "México", "Namibia", "Nauru", "Nepal",
                "Nicaragua", "Niue", "Noruega", "Nueva Zelandia", "Níger",
                "Omán", "Palaos", "Panamá", "Papúa Nueva Guinea", "Paraguay",
                "Países Bajos", "Perú", "Polinesia Francesa", "Polonia",
                "Puerto Rico", "Reino Unido", "República Dominicana",
                "Rumania", "Samoa", "Samoa Americana", "Santa Lucía",
                "Senegal", "Serbia", "Seychelles", "Suecia", "Suiza",
                "Tailandia", "Taiwán", "Timor Oriental", "Tokelau", "Tonga",
                "Tuvalu", "Túnez", "Ucrania", "Uganda", "Uruguay", "USA",
                "Venezuela", "Vietnam", "Yemen", "Zambia"])


# In[27]:


print(paises[pesos > 90], paises[pesos > 90].size)
      
print(paises[alturas > 1.8], paises[alturas > 1.8].size)


# In[36]:


print(paises[(pesos > 90) & (alturas > 1.8)])  # Para los vectores de numpy, la operación lógica "Y" se define como & no como and.


# In[38]:


print(paises[(pesos > 90) | (alturas > 1.8)], paises[(pesos > 90) | (alturas > 1.8)].size)  # Para el caso de la unión se usa el pipeline, operador lógico "O"


# In[ ]:




