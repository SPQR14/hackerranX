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

archivo = open("files/TXT/manejo_de_archivos.txt", encoding='UTF-8')
texto = archivo.readlines()
print(texto)
archivo.close()

with open("files/TXT/manejo_de_archivos.txt", "r", encoding='UTF-8') as archivo:
    texto = archivo.readlines()
    print(texto)

with open("files/TXT/manejo_de_archivos.txt", "a", encoding='UTF-8') as archivo:
    archivo.write("Juan Pérez López 18")
    archivo.write("\n")
    archivo.write("María García Lozano 22")
    archivo.write("\n")

print(f"fuera del bloque with {texto}")
"""
"""
########################################################################################################################
                                            Manejo de CSV como archivo                        
########################################################################################################################
"""
"""
Estación,Enero ,Febrero,Marzo
Zócalo,100,200,300
Bellas Artes,400,500,600
Juárez,700,800,900
Hidalgo,100,1100,1200
"""

pasajeros = {}

with open('files/TXT/datos_metro.csv', 'r', encoding='UTF-8') as archivo:
    archivo.readline() # Quitar el encabezado
    estaciones = archivo.readlines() # Información relevante
    for estacion in estaciones:
        lista = estacion.strip().split(",")
        pasajeros[lista[0]] = list(map(int, lista[1:]))

print(pasajeros)

print(sum(pasajeros["Zócalo"]))