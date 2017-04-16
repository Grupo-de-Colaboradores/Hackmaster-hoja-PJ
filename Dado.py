!# /usr/bin/python

"""
 Este programa simula la tirada de un dado.
 Utiliza una función, aunque más adelante posiblemente sea una clase.
"""

import random

#Función dado
def Dado(min = 1, max):
    #Calcula un valor aleatorio entre min y max. Normalmente es necesario
    #sólo dar el valor máximo, pero también puedes dar el valor mínimo.
    #Ejemplos: Dado(20), un dado de 20 caras
    return random.randint(min, max);
