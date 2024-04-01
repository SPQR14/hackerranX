#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Feb 21 11:02:39 2022

@author: sqpr14_
"""

"""
########################################################################################################################
                                            Creación e importación de módulos.
########################################################################################################################
"""
"""
# import math as m
from math import ceil, floor
import manejo_archivos
# help(math)
f = 1.5
print(ceil(f))
print(floor(f))
"""

from manejo_archivos import leer, escribir

escribir('files/TXT/prueba_modulos.txt', "Texto pasado por módulos, qué loco no?")
print(leer('files/TXT/prueba_modulos.txt'))