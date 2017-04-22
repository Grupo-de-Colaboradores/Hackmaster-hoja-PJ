"""
Comienza el proceso de la creación de personaje. Utilizaremos la \"chuleta\" del libro del manual del jugador, pag 341 como pseudocódigo
"""

#Hacemos una pequeña intro al usuario o usuaria y le explicamos el proceso interactivamente
print ("\n"*2, "\t"*2, "Bienvenido o bienvenida al programa de creación de personajes de Hackmaster,\n\t te voy a hacer unas preguntas y vamos definiendo características ... ¿preparad@ para la acción?\n")
input ("")
print ("\n"*2, "\t"*2, "Lo primero es elegir las características básicas de personaje, y para ello tiraremos varios dados... \n\t ¿listos tus dados virtuales?")
input ("")

#Creamos un dado virtual
import random
def Dado (max, min = 1):
    """Calcula un valor aleatorio entre min y max. Normalmente es necesario
    sólo dar el valor máximo, pero también puedes dar el valor mínimo.
    Ejemplos: Dado(20), un dado de 20 caras; Dado(7,2), un dado entre 2 y 7"""
    return random.randint(min, max);

#seguimos interaccionando mientras definimos características, que quedan asignadas a variables
print ("\n"*2, "\t"*2, "Un dado de 6 se tira así: teclea Dado(6) y después presiona intro... ¿practicamos?")
input ("")
print ("\n"*2, "\t"*2, "Ahora teclea Dado(6) una vez, y después presiona intro")
input ("")
print ("\n"*2, "\t"*2, Dado(6))
print("\n"*2, "\t"*2,)
input ("(presiona intro... )")
print ("\n"*2, "\t"*2, "¡Excelente!, ahora tiraremos 3 dados de 6 para determinar cada una de las características básicas de tu personaje,", "\n"*2, "\t"*2, "¡Que los dados queden donde caigan!", "\n"*2, "\t"*2, "¿Empezamos?")
