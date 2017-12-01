# -*- coding: utf-8 -*-

from jugador import *
from moderador import *
from comptador import *

if __name__ == "__main__":
    comptador1 = Comptador()
    comptador2 = Comptador()
    comptador_intern = Comptador()

    jugador1 = Jugador("Pere")
    jugador2 = Jugador("Anna")
    jutge = Moderador()

    while comptador1.GetCount() < 3 and comptador2.GetCount() < 3 and comptador_intern.GetCount() < 10:
        ma_j1 = jugador1.jugar_una_ma()
        ma_j2 = jugador2.jugar_una_ma()
        ma_guanyadora = jutge.modera(ma_j1, ma_j2)
        if ma_guanyadora == ma_j1:
            comptador1.incrementa()
            print jugador1.get_nom() + " té avantatge, " + ma_j1 + " guanya a " + ma_j2
        elif ma_guanyadora == ma_j2:
            comptador2.incrementa()
            print jugador2.get_nom() + " té avantatge, " + ma_j2 + " guanya a " + ma_j1
        else:
            print "Es produeix empat"
        comptador_intern.incrementa()
    if comptador1.GetCount() > comptador2.GetCount():
        print jugador1.get_nom() + " ha guanyat"
    elif comptador2 > comptador1.GetCount():
        print jugador2.get_nom() + " ha guanyat"
    else:
        print "Els dos jugadors han empatat"
