#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Feb 16 13:05:39 2022

@author: sqpr14_
"""

"""
###############################################################################
                            Alcance de variables.
###############################################################################
"""

externa = "EXTERNA"

def funcion(parametro):
    interna = "INTERNA"
    print(f"Dentro de la función: {externa} {parametro} {interna}")

funcion("PARAMETRO")

print(f"Fuera de la función: {externa}, es la única variable disponible fuera de la función funcion")
