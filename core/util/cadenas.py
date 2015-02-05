#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append('./')

EXCLUIDOS_WIN = ('/', '\\', ':', '*', '?', '"', '<', '>', '|')

def limpiarCaracteres(cadena, lstExcluidos=EXCLUIDOS_WIN, reemplazo='_'):
    for car in lstExcluidos:
        cadena = cadena.replace(car, reemplazo)
    return cadena

#cadena = "Hola:yo/>\\"
#print cadena
#cadenaLimpiada = limpiarCaracteres(cadena)
#print cadenaLimpiada

