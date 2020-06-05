from piezas import Pieza
from tablero import Tablero


class Ajedres:
    def __init__(self):
        self.tablero = Tablero()
        self.piezas = Pieza(self.tablero)
        self.turnoactual = "W"

    def __switchturn(self):
        if self.turnoactual == "W":
            self.turnoactual = "B"
        if self.turnoactual == "B":
            self.turnoactual = "W"

    def _info_(self, pregunta):
        while True:
            input_ = input(pregunta)
            if len(input_) == 3:
                a, b, c = input_
                b, c = b.upper(), int(c)
                if b not in tuple("ABCDEFGH"):
                    print("ingresaste un valor incorrecto")
                elif c not in tuple(range(1, 8)):
                    print("ingresaste un valor incorrecto")
                else:
                    tupla = (a, b, c)
                    return tupla
            else:
                print("Valor demasiado largo")

    def turno(self):
        while True:
            coo = self._info_("Que pieza desea mover?\n")
            plz = self._info_("Hacia donde quiere moverla?\n")
            if self.piezas.colision_detector(plz):
                self.piezas.mover(coo, plz)
                break
            else:
                print("ya hay una pieza aqui")

    def run(self):
        while True:
            self.tablero.display()
            self.turno()


test = Ajedres()
test.run()
