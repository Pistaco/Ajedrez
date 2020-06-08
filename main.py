from piezas import Pieza, Peon
from tablero import Tablero


class Ajedres:
    def __init__(self):
        self.tablero = Tablero()
        self.turnoactual = "W"

    def __switchturn(self):
        if self.turnoactual == "W":
            self.turnoactual = "B"
        if self.turnoactual == "B":
            self.turnoactual = "W"

    def _info_(self, pregunta):
        while True:
            input_ = input(pregunta)
            keys = tuple("ABCDEFGH")
            if len(input_) == 3:
                a, b, c = input_
                a, b, c = a.upper() ,b.upper(), int(c)
                if a not in "KQRBNP":
                    print("no ingresaste una pieza valida")
                elif b not in keys:
                    print("ingresaste un valor incorrecto")
                elif c not in tuple(range(1, 8)):
                    print("ingresaste un valor incorrecto")
                else:
                    tupla = (a, keys.index(b), c - 1)
                    return tupla
            else:
                print("Valor demasiado largo")

    def turno(self):
        while True:
            coo = self._info_("Que pieza desea mover?\n")
            plz = self._info_("Hacia donde quiere moverla?\n")
            if self._Seleccionador_(coo):
                if self.pactual.mover(coo, plz):
                    break

    def _Seleccionador_(self, coo):
        PD = {"P": Peon}
        seleccionada = PD.get(coo[0])
        get = self.tablero.GET(coo)[1]
        if coo[0] == get:
            self.pactual = seleccionada(self.tablero)
            return True
        print("La pieza que escribiste no coincide con la que esta en el tablero")
        return False
         

    def run(self):
        while True:
            self.tablero.display()
            self.turno()


test = Ajedres()
test.run()
