from piezas import Pieza, Peon
from tablero import Tablero
from check import Check

class Ajedres:
    def __init__(self):
        self.tablero = Tablero()
        self.turnoactual = "W"
        self.check = Check(self)

    def __switchturn(self):
        if self.turnoactual == "W":
            self.turnoactual = "B"
        elif self.turnoactual == "B":
            self.turnoactual = "W"

    def turno(self):
        while True:
            coo, plz = self.check.run(self.turnoactual)
            self.seleccionador_(coo)
            if self.pactual(self.tablero, coo, plz).accion():
                break

    def seleccionador_(self, coo):
        PD = {"P": Peon}
        seleccionada = PD.get(coo[0])
        self.pactual = seleccionada

    def run(self):
        while True:
            self.tablero.display()
            self.turno()
            self.__switchturn()


test = Ajedres()
test.run()
