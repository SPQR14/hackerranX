#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 19:38:08 2021

@author: sqpr14_
"""
import time
from random import randint

def ordenamiento_burbuja(lista):
    t = len(lista)
    for i in range(0, t):
        for j in range(t - 1, i, -1):
            if lista[j] < lista[j - 1]:
                temp = lista[j]
                lista[j] = lista[j -1]
                lista[j - 1] = temp 
    
    return lista

t0 = time.time()
l = [randint(-10000,10000) for x in range(100000)]
print("--- %s segundos ---" % (time.time() - t0))
t1 = time.time()
ordenamiento_burbuja(l)
print("--- %s segundos ---" % (time.time() - t1))
    
