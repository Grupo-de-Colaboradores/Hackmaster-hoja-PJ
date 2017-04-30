"""
Añadimos los valores fraccionales a las características
"""

#Tirar las características básicas con los valores fraccionales

#Creamos un dado virtual
import random
def Dado (max, min = 1):
    """Calcula un valor aleatorio entre min y max. Normalmente es necesario
    sólo dar el valor máximo, pero también puedes dar el valor mínimo.
    Ejemplos: Dado(20), un dado de 20 caras; Dado(7,2), un dado entre 2 y 7"""
    return random.randint(min, max);

#Primero, agrupamos las características en un tuple
características = ("Fue", "Des", "Con", "Int", "Sab", "Car", "Asp")
caract_nomb = características # Trabajaremos con una copia de la lista

def tirada_fraccional():
    """Devuelve el valor fraccional en percentiles de cada característica"""
    lanzamientosD100 = [] #inicializamos una lista vacía
    for i in zip(caract_nomb): #iteramos en un bucle 6 veces,  1 por cada característica
        lanzamientosD100.append(Dado(100)) #en cada iteración, lanzamos 1D100, y lo añadimos a la lista
    return lanzamientosD100  #devuelve una lista con 6 tiradas de D100

val_fraccionales = tirada_fraccional()

# #Tiramos el D100 una vez por cada característica
# for caract in caract_nomb:
#     val_fraccionales.append(tirada_fraccional())

#Creamos un diccionario con las características y sus valores fraccionales
caracteristicas_fracc = dict((x, y) for (x, y) in zip(caract_nomb, val_fraccionales))
