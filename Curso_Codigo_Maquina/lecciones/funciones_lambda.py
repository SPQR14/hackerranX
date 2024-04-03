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

decompose = lambda x: x.strip().lstrip().split()
concat = lambda x: ' '.join(x)

print(sumar(2,2), multiplicar(7, 9), constante())

personas = [('Juan', 82, 5), ("Luisa", 41, 10), ("Arnulfo", 75, 20), ("Zuleima", 30, 15)]

print("En desorden", personas)

personas.sort()

print('Ordenadas por nombre', personas)

personas.sort(reverse=True)

print("Por nombre de Z - A", personas)

personas.sort(key=lambda x:x[1]) #Por primer elemento de la tupla

print("Por edad", personas)

personas.sort(key=lambda x:x[1]+x[2]) #Sumar los dos elementos enteros de las tuplas

print("Antes es peor", personas)

