#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Feb 21 13:25:39 2022

@author: sqpr14_
"""

"""
########################################################################################################################
                                            Clases y objetos/Casino.
########################################################################################################################
"""
from random import randint

class Tragamonedas:
    
    def __init__(self, id = '', premio = 0.0):  # obligatorio
        self.id = id
        self.premio = premio
        self.monedas = 0
        self.jackpots = 0

    def __str__(self):  # Representación en texto del objeto
        return 'ID: ' + str(self.id) + ' - Premio: ' + str(self.premio)
    
    def __eq__(self, other):  # 
        return self.monedas == other.monedas

    def __lt__(self, other):
        return self.monedas < other.monedas

    def __gt__(self, other):
        return self.monedas > other.monedas

    def jugar(self):
        self.monedas += 1
        numeros = randint(0, 9), randint(0, 9), randint(0, 9)
        mensaje = ''
        if numeros[0] == numeros[1] == numeros[2]:
            self.jackpots += 1
            mensaje = 'Felicidades, ganaste %0.2f' %self.premio
        else:
            mensaje = 'Suerte para la otra'
        return numeros, mensaje

tragamonedas_a = Tragamonedas(1, 10000.00)
tragamonedas_b = Tragamonedas(2, 700.00)

for i in range(100):
    print(tragamonedas_a.jugar())
    print(tragamonedas_b.jugar())

print('A: ', tragamonedas_a.monedas, tragamonedas_a.jackpots)
print('B: ', tragamonedas_b.monedas, tragamonedas_b.jackpots)

print(tragamonedas_a)
print(tragamonedas_b)

print(tragamonedas_a == tragamonedas_b)
