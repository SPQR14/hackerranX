#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Feb 21 13:25:39 2022

@author: sqpr14_
"""

"""
########################################################################################################################
                                            Recursividad/Búsqueda binaria.
########################################################################################################################
"""

lista = [11, 12, 13, 14, 15, 16, 17]


def busqueda_iterartiva(lista, dato):
    bajo = 0
    alto = len(lista) - 1
    centro = (bajo + alto) // 2
    while bajo <= alto:
        if lista[centro] == dato:
            return centro
        elif lista[centro] < dato:
            bajo = centro + 1
        else:
            alto = centro - 1
        centro = (bajo + alto) // 2
    return -1  # No existe en la lista


def busqueda_recursiva(lista, bajo, alto, dato):
    if bajo > alto:  # caso base
        return -1
    centro = (bajo + alto) // 2  # caso recursivo
    if lista[centro] == dato:
        return centro
    elif lista[centro] < dato:
        return busqueda_recursiva(lista, centro + 1, alto, dato)
    else:
       return busqueda_recursiva(lista, bajo, centro - 1, dato)


for i in range(10, 19):
    print(i, busqueda_iterartiva(lista, i))
    print(i, busqueda_recursiva(lista, 0, (len(lista) + 1), i))

