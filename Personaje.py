#! /usr/bin/python

"""
Este script crea la clase Personaje, que tendrá los atributos
y características básicas comunes a todos los personajes
"""
print("Hola")

class Personaje(object):
    """Este script crea la clase Personaje, que tendrá los atributos
    y características básicas comunes a todos los personajes."""
    def __init__(self, nombre, clase, nivel, alineamiento, raza, sexo, edad, altura, peso, pelo, ojos, diox, manobuena, jugador, fue, des, con, intl, sab, car, asp, hon):
        #super(Personaje, self).__init__()
        self.nombre = nombre
        self.clase = clase
        self.nivel = nivel
        self.alineamiento = alineamiento
        self.raza = raza
        self.sexo = sexo
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.pelo = pelo
        self.ojos = ojos
        self.diox = diox
        self.manobuena = manobuena
        self.jugador = jugador
        self.fue = fue
        self.des = des
        self.con = con
        self.intl = intl
        self.sab = sab
        self.car = car
        self.asp = asp
        self.hon = hon

caract = {}
print (caract)
caract[nombre]=input("Ponle nombre: ")
