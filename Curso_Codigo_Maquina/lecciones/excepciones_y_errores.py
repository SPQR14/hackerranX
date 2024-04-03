#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Feb 17 10:51:39 2022

@author: sqpr14_
"""

"""
########################################################################################################################
                                                    Manejo de errores.
########################################################################################################################
"""
#ZeroDivisionError
#ValueError
#ETC
a = True
count = 0
while a and count < 5:
    try:
        monto = float(input("Indica el monto que deseas para el crédito: "))
        num_pagos = int(input("Indica el número de pagos: "))
        if num_pagos < 0:
            raise Exception("No pueden ingresarse cantidades negativas")  # Excepción personalizada
        elif num_pagos > 18:
            raise Exception("El plazo máximo para pagar el crédito es de 12 meses")
        elif num_pagos > monto:
            raise Exception("El número de pagos no puede ser mayor al monto solicitado")
        pago_mensual = monto / num_pagos
        print(f"El pago mensual será de: {round(pago_mensual, 2)}")
    except ValueError as error:
        print(f"Hubo un error de conversión de tipos de dato {error.args}")
    except ZeroDivisionError as error:
        print(f"Hubo un error de división entre 0 (cero) {error.args}")
    except Exception as error:
        print(f"Hubo un error {error.args} inténtalo nuevamente, porfavor")
    else:
        # Este bloque se ejecuta cuando no ocurre ninguna excepción.
        a = False
        print("La solicitud se ha realizado con éxito.")
    finally:
        # Este bloque se ejecuta siempre. Se ejecuta cuando ocurren excepciones y cuando no.
        count += 1
    if count >= 5:
        print(f"Intentos exceidos. Total de intentos: {count}. Vuelve a intentarlo en una hora.")
