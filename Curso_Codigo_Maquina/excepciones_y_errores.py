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
            raise Exception("No pueden ingresarse cantidades negativas")
        elif num_pagos > 12:
            raise Exception("No se puede exceder un año como plazo de pago")
        pago_mensual = monto / num_pagos
        print(f"El pago mensual será de: {round(pago_mensual, 2)}")
    except ValueError as error:
        print(f"Hubo un error de conversión de tipos de dato {error.args}")
    except ZeroDivisionError as error:
        print(f"Hubo un error de división entre 0 (cero) {error.args}")
    except Exception as error:
        print(f"Hubo un error {error.args} inténtalo nuevamente, porfavor")
    else:
        a = False
        print("La solicitud se ha realizado con éxito.")
    finally:
        count += 1

print(f"Intentos exceidos. Total de intentos: {count}. Vuelve a intentarlo en una hora.")