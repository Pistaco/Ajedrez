from piezas import Pieza, Peon
from tablero import Tablero

def opciones_(evaluar, opciones, mensaje, operador = "negacion"):
    if operador == "negacion":
        if evaluar not in opciones:
            print(mensaje)
            return False
        return True
    if operador == "==":
        if evaluar == opciones:
            return True
        else:
            print(mensaje)
            return False


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
            if opciones_(len(input_), 3, "Ingresaste un valor demasiado largo", "=="):
                a, b, c = input_
                a, b, c = a.upper() ,b.upper(), int(c)
                if opciones_(a, "KQRBNP", "no ingresaste una pieza valida"):
                    if opciones_(b, keys, "ingresaste una row incorrecta"):
                        if opciones_(c, tuple(range(1,8)), "ingresaste una columna incorrecta"):
                            tupla = (a, keys.index(b), c - 1)
                            return tupla

    def turno(self):
        while True:
            coo = self._info_("Que pieza desea mover?\n")
            if self.tablero.GET(coo, bol=True) is False:
                print("No existe pieza donde seleccionaste")
            elif self._Seleccionador_(coo):
                plz = self._info_("Hacia donde quiere moverla?\n")
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
