#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Feb 21 13:25:39 2022

@author: sqpr14_
"""


class Cuenta:

    """
    ####################################################################################################################
                                                Encapsulamiento/cuentas bancarias.
    ####################################################################################################################
    """

    def __init__(self, nombre = '', direccion = '' ):
        self.nombre = nombre
        self.direccion = direccion
        self.__balance = 0.0

    def retirar(self, monto):
        if monto <= self.__balance:
            self.__balance -= monto

    def depostitar(self, monto):
        if monto > 0:
            self.__balance += monto

    # el decorador property
    # es para métodos getter
    @property
    def balance(self):
        print("getter method called")
        return self.__balance

    # así se define un método setter
    @balance.setter
    def balance(self, valor):
        print("setter method called")
        self.__balance = valor

    # Otra forma de definir un método getter
    def get_balance(self):
        return self.__balance

    # Otra forma de definir un método setter
    def set_balance(self, valor):
        self.__balance = valor


cuenta = Cuenta("Juan", "Reforma 100")
print(cuenta.nombre, cuenta.direccion)
cuenta.depostitar(200)
cuenta.retirar(500)
# Así se llama a los métodos getter y setter definidos mediante decoradores
cuenta.balance = 1234.98
print(cuenta.balance)

# Así se llama a los métodos getter y setter definidos de manera "clásica"
cuenta.set_balance(1123.89)
print(cuenta.get_balance())
