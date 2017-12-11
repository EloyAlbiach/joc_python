import random


class Jugador(object):

    def __init__(self, nom="unnamedPlayer"):
        self.__nomJugador = nom

    def jugar_una_ma(self):
        valors = ('pedra', 'paper', 'tisora')
        una_ma = random.choice(valors)
        return una_ma

    def get_nom(self):
        return self.__nomJugador