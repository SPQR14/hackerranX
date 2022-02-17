#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Feb 17 15:34:39 2022

@author: sqpr14_
"""
"""
########################################################################################################################
#                                        Manejo de archivos                                                            #
########################################################################################################################
"""

archivo = open("files\\TXT\\manejo_de_archivos.txt", encoding='UTF-8')
texto = archivo.read() #TODO EL ARCHIVO
print(texto)
print(type(texto))
archivo.close()

archivo = open("files\\TXT\\manejo_de_archivos.txt", encoding='UTF-8')
texto = archivo.readline() #UNA SOLA LINEA
print(texto)
texto = archivo.readline() #UNA SOLA LINEA
print(texto)
texto = archivo.readline() #UNA SOLA LINEA
print(texto)
texto = archivo.readline() #UNA SOLA LINEA
print(texto)
archivo.close()

archivo = open("files\\TXT\\manejo_de_archivos.txt", encoding='UTF-8')
texto = archivo.readlines()
print(texto)
archivo.close()

with open("files\\TXT\\manejo_de_archivos.txt", "r", encoding='UTF-8') as archivo:
    texto = archivo.readlines()
    print(texto)

print(f"fuera del bloque with {texto}")