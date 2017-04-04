import random


class Jugador(object):
    __nomJugador = 'unamedJugador'

    def __init__(self, nom):
        self.__nomJugador = nom

    def jugar_una_ma(self):
        valors = ('pedra', 'paper', 'tisora')
        una_ma = random.randint(0, 2)
        return valors[una_ma]

    def get_nom(self):
        return self.__nomJugador