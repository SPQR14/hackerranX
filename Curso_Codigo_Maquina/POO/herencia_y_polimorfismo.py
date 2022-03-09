#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Feb 21 13:25:39 2022

@author: sqpr14_
"""


class Producto:
    """
     ###################################################################################################################
                                            Herencia y polimorfismo/supermercado.
     ###################################################################################################################
    """
    def __init__(self, id, descripcion, costo):
        self.id = id
        self.descripcion = descripcion
        self.costo = costo

    def __str__(self):
        return "Producto genérico"

    def __lt__(self, other):
        return self.costo < other.costo

    def __gt__(self, other):
        return self.costo > other.costo

    def crear_etiqueta(self):
        return "%s\n%s\n%0.2f\n" % (self.id, self.descripcion, self.costo)


class Perecedero(Producto):

    def __init__(self, id, descripcion, costo, fecha_cad):
        super().__init__(id, descripcion, costo)
        self.fecha_cad = fecha_cad

    def __str__(self):
        return "Perecedero"

    def crear_etiqueta(self):
        return super().crear_etiqueta() + '%s\n' % self.fecha_cad


class Electronico(Producto):

    def __init__(self, id, descripcion, costo, marca):
        super().__init__(id, descripcion, costo)
        self.marca = marca

    def __str__(self):
        return "Electrónico"

    def crear_etiqueta(self):
        return super().crear_etiqueta() + '%s\n' % self.marca


producto = Producto('g', 'Genérico', 100)
perecedero = Perecedero('p', 'Jitomate', 200.32, '12-25')
electronico = Electronico('e', 'Television', 25902.23, 'Sony')

"""
print(producto.crear_etiqueta())
print(perecedero.crear_etiqueta())
print(electronico.crear_etiqueta())
"""

objetos = (producto, perecedero, electronico)

for o in objetos:
    print(o.crear_etiqueta(), o)

if isinstance(producto, Producto):
    print("producto sí es producto we")

print('Es más grande la tele que los jitomates?', electronico > perecedero)

########################################################################################################################
