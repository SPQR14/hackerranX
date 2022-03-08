#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 3 de marzo 2022

@author: Alberto I. Pico Lara
"""

"""
Tech Challenge:
Escribe un código en ***Python*** que aplane un arreglo de enteros o arreglos de enteros (que puede estar anidado arbitrariamente) a un arreglo plano de enteros.
"""

# l = [1, [2, [3, [4, 5]]]]
# l = [8, 2, [3, 10, [11, 12]], [1, 2, [3, 4]], 5, 6]
# l = [13, 2,[5, [7, [1, 2, 3, 4, [6, 4, 3]]]],8,[9]]
l = [13, 2, [5, [7, [1, 2, 3, 4, [6, 4, 3]]]], 8, [9], [13, 2, [5, [7, [1, 2, 3, 4, [6, 4, 3]]]], 8, [9]],
     [8, 2, [3, 10, [11, 12]], [1, 2, [3, 4]], 5, 6]]


def list_flatener(nest):
    """
    :param nest:
    :return: Lista "aplanada"
    """

    if len(nest) == 0:
        print("Menos que cero", nest)
        return nest
    elif isinstance(nest[0], list):
        print("Es lista")
        return list_flatener(nest[0] + list_flatener(nest[1:]))
    print("Ningún casito", nest)
    return nest[:1] + list_flatener(nest[1:])


print("vaya, terminó", list_flatener(l))