#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Alberto
"""

def sumar_dos_numeros(a, b):
    return a+b

def suma_numeros(*numeros):
    suma = 0
    for num in numeros:
        suma += num
    return suma

print("El resultado de sumar del 1 al 20 es igual a", suma_numeros(1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))

def formatear_nombre(nombre='', apellido_p='', apellido_m=''):
    return nombre.upper() + ' ' + apellido_p.capitalize() + ' ' + apellido_m.capitalize()

print("Nombre completo:", formatear_nombre(apellido_p='sandoval', nombre='alejandra'))

def generar_clave(nombre='', fechanac=''):
    clave= ''
    for token in nombre.split():
        clave+=token[0]
    return clave+fechanac[-2:]

print(generar_clave('Alberto Isaac Pico Lara', '1994'))
