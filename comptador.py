class Comptador(object):

    def __init__(self):
        self.__count = 0

    def incrementa(self):
        self.__count += 1

    def GetCount(self):
        return self.__count
