#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Feb 21 13:25:39 2022

@author: sqpr14_
"""


class Vehiculo:
    """
    ####################################################################################################################
                                                Atributos/Vehículos.
    ####################################################################################################################
    """
    # Por convención los atributos de instancia se definen en la parte de arriba y son válidos para todas las intancias
    # que se creen de los objetos, tienen persistencia mientras esté en ejecución el programa.
    folio = 0
    COLORES = (
        'BLANCO',
        'ROJO',
        'VERDE'
    )

    def __init__(self, color):
        Vehiculo.folio += 1
        self.serie = Vehiculo.folio
        self.__set_color(color)

    def __str__(self):
        return str(self.serie) + ' ' + self.color

    def __eq__(self, other):
        return self.serie == other.serie

    def __lt__(self, other):
        return self.serie < other.serie

    def __gt__(self, other):
        return self.serie > other.serie

    def __set_color(self, color):
        color = color.upper().strip()
        if color in Vehiculo.COLORES:
            self.color = color.capitalize()
        else:
            self.color = Vehiculo.COLORES[0].capitalize()  # Valor por defecto


vehiculo_a = Vehiculo("Rojo")
vehiculo_b = Vehiculo("verde    ")
vehiculo_c = Vehiculo("\nRosa")

print(vehiculo_a.serie, vehiculo_a.color)
print(vehiculo_b.serie, vehiculo_b.color)
print(vehiculo_c.serie, vehiculo_c.color)
print(vehiculo_c, vehiculo_b, vehiculo_a)
print(vehiculo_c.folio)

print("Color del puro vehículo c ", vehiculo_c.color)
