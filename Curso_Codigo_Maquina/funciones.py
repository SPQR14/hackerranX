#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 13:05:39 2022

@author: sqpr14_
"""

"""
###############################################################################
                                        Funciones.
###############################################################################
"""

def suma_dos_numeros(a, b):
    return a + b

def sumar(*numeros):
    suma = 0
    for numero in numeros:
       suma += numero 
    return suma

#print(sumar(5, 8, 8, 9, 4, 5))

# Caso de aplicación a impresión de credenciales 


nombre = "AlbertO IsAAC"
paterno = "PICO"
materno = "LARA"

def formatea_nombres(nombre = "", paterno = "", materno = ""):
    return nombre.upper() + ' ' + paterno.capitalize() + ' ' + materno.capitalize()

def crea_clave_poblacional(nombre = "", fecha_nac = ""):
    clave = ""
    for palabra in nombre.split(" "):
        clave += palabra[0]
    clave += fecha_nac[-2:]
    return clave
    
nombre = formatea_nombres(nombre = "lilia Alejandra", materno = "Basaldúa", paterno = "PIco")
print(nombre)
fecha = "1993"
print(f"La clave es {crea_clave_poblacional(nombre, fecha)}")


"""
###############################################################################
                        Paso por valor y por referencia.
###############################################################################
"""

def doblar(referencia, valor):
    referencia *= 2
    valor *= 2

estructura = ['a', 'b', 'c']
primitiva  = 'abc'

print("ANTES", estructura, primitiva)