from piezas import Pieza, Peon
from tablero import Tablero


def opciones_(evaluar, opciones, mensaje, operador="negacion"):
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
        self.check = True

    def __switchturn(self):
        if self.turnoactual == "W":
            self.turnoactual = "B"
        elif self.turnoactual == "B":
            self.turnoactual = "W"

    def _info_(self, pregunta):

        def check_len(origen):
            orige = len(origen)
            if not opciones_(orige, 3, "Valor demasidado largo", "=="):
                self.check = False

        def check_column(origen):
            try:
                orige = int(origen[2])
            except:
                print("columna invalida")
                self.check = False
                return False
            if not opciones_(orige, range(1, 9), "Columna invalida"):
                self.check = False
            return orige - 1

        def check_row(origen):
            orige = origen[1].upper()
            keys = tuple("ABCDEFGH")
            if not opciones_(orige, "ABCDEFGH", "Row invalida"):
                self.check = False
                return False
            return keys.index(orige)

        def check_pieza(origen):
            orige = origen[0].upper()
            if not opciones_(orige, "KQRBNP", "Pieza no valida"):
                self.check = False
            return orige

        while True:
            self.check = True
            _input = input(pregunta)
            check_len(_input)
            R = check_row(_input)
            C = check_column(_input)
            P = check_pieza(_input)
            if self.check:
                break
        return P, R, C

    def turno(self):
        while True:
            coo = self._info_("Que pieza desea mover?\n")
            self.Seleccionador_(coo)
            self.check_turno(coo)
            print(self.check)
            if self.check:
                plz = self._info_("Hacia donde desea moverla?\n")
                a = self.pactual.accion(coo, plz)
                print(a)
                if a:
                    break

    def check_turno(self, origen):
        get = self.tablero.GET(origen)
        if get[0] != self.turnoactual:
            print("Solo puedes seleccionar piezas de tu bando")
            self.check = False

    def Seleccionador_(self, coo):
        PD = {"P": Peon}
        seleccionada = PD.get(coo[0])
        get = self.tablero.GET(coo)[1]
        if coo[0] == get:
            self.pactual = seleccionada(self.tablero)
        else:
            print("La pieza que escribiste no coincide con la que esta en el tablero")
            self.check = False

    def run(self):
        while True:
            print(self.turnoactual)
            self.tablero.display()
            self.turno()
            self.__switchturn()


test = Ajedres()
test.run()
