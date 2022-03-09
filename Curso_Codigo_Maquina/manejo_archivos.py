#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Feb 21 11:02:39 2022

@author: sqpr14_
"""

"""
########################################################################################################################
                                            Modulo 1 para manejo de archivos.
########################################################################################################################
"""

def escribir(nombre, texto):
    with open(nombre, "w", encoding='utf-8') as archivo:
        archivo.write(texto)

def leer(nombre):
    texto = ""
    with open(nombre, "r", encoding='utf-8') as archivo:
        texto = archivo.read()
    return texto

if __name__ == "__main__":
    escribir('files/TXT/prueba_1.txt', "Texto de prueba, lol\nLuego qué sigue?")
    print(leer('files/TXT/prueba_1.txt'))
