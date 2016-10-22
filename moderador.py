class Moderador(object):

    def modera(self, manoA, manoB):
        guanyador = "empate"
        if manoA == "paper" and manoB == "pedra":
            guanyador = "paper"

        if manoA == "pedra" and manoB == "paper":
            guanyador = "paper"

        if manoA == "tisora" and manoB == "pedra":
            guanyador = "pedra"

        if manoA == "pedra" and manoB == "tisora":
            guanyador = "pedra"

        if manoA == "paper" and manoB == "tisora":
            guanyador = "tisora"

        if manoA == "tisora" and manoB == "paper":
            guanyador = "tisora"
        return guanyador

