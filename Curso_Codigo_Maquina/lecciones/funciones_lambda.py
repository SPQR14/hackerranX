#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Feb 16 13:05:39 2022

@author: sqpr14_
"""

"""
###############################################################################
                            Funciones lambda.
###############################################################################
"""

sumar = lambda a, b : a + b
multiplicar = lambda a, b, c = 1 : a * b * c
constante = lambda : 10     

print(sumar(2,2), multiplicar(7, 9), constante())

personas = [('Juan', 82, 5), ("Luisa", 41, 10), ("Arnulfo", 75, 20)]

print(personas)

personas.sort(key = lambda x : x[1]) # accede al elemento 1 de las tuplas.

print(personas)

personas.sort(key = lambda x : x[1] + x[2], reverse = True)
print(f"(antes es peor) {personas}")
