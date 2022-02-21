#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Feb 21 13:25:39 2022

@author: sqpr14_
"""

"""
########################################################################################################################
                                            Recursividad.
########################################################################################################################
"""

"""
    CASO BASE: Caso más simple o el último caso.

    CASO RECURSIVO: Donde la función se manda a llamar a sí misma, pero resolviendo un problema menor.
"""

"""
######    Imprimir del 5 al 0    ######
    -> Imprimir 5 + Imprimir del 4 al 0
    -> Imprimir 4 + Imprimir del 3 al 0
    -> Imprimir 3 + Imprimir del 2 al 0
    -> Imprimir 2 + Imprimir del 1 al 0
    -> Imprimir 1 + Imprimir 0
"""


from time import perf_counter


def recursiva(n = 0):
    if n == 0:      # caso base
        print(n)
    else:           # caso recursivo
        print(n)
        recursiva(n - 1)

recursiva(5)

def factorial_iterativo(num = 0):
    if num == 0 or num == 1:
        return 1
    resultado = 1
    for i in range(2, num + 1):
        resultado *= i
    return resultado


def factorial_recursiva(num = 0):
    if num == 0 or num == 1:                   # caso base
        return 1
    return num * factorial_recursiva(num - 1)  # caso recursivo


inicio = perf_counter()
for i in range(1000000):
    factorial_iterativo(100)
fin = perf_counter()
print("Iterativo %0.4f" %(fin - inicio))

inicio = perf_counter()
for i in range(1000000):
    factorial_recursiva(100)
fin = perf_counter()
print("Recursivo %0.4f" %(fin - inicio))

