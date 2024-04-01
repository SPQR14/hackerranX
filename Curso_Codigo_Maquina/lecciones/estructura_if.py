#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 18:00:18 2021

@author: sqpr14_
"""

"""
Sistema de orientación vocacional
artes -> teatro
deportes -> medicina del deporte
matemáticas -> Ingeniería
"""

artes = True
deportes = False
matematicas = True


if deportes and matematicas and artes:
    print("Estudia teatro o medicina deportiva o ingeniería")
elif deportes and matematicas:
    print("Estudia medicina deportiva o ingeniería")
elif artes and matematicas:
    print("Arquitectura")
elif artes and deportes:
    print("Estudia teatro o medicina del deporte")
elif deportes:
    print("Estudia medicina deportiva")
elif matematicas:
    print("Estudia ingeniería")
elif artes:
    print("Estudia teatro")
else:
    print("Consulta a un asesor vocacional")