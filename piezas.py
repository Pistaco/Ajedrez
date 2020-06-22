def colisionator(lista):
    values = 0
    for x in lista:
        if x:
            values += 1
    if values == 1:
        return True
    else:
        return False


def lista(partida, destino):
    if partida == destino:
        return partida
    else:
        if partida < destino:
            return range(partida, destino)
        else:
            return range(partida, destino, -1)


class Pieza:
    """
    Clase que encarga de manejar las piezas y las funciones asociadas a ellas.
    """
    def __init__(self, ai):
        self.tablero = ai.tablero
        self.data = self.tablero.data
        self.check = True
        self.origen = ai.coo
        self.destino = ai.plz
        self.ta = ai.turnoactual
        self.get1 = self.tablero.GET(self.origen)
        self.get2 = self.tablero.GET(self.destino)
        self.roworigen, self.columnorigen = self.origen[1:]
        self.rowdestino, self.columndestino = self.destino[1:]

    def mover(self):
        """Funcion que se encarga de mover la pieza.

        esta funcion modifica la matriz y reeplaza los valores correspndientes
        """
        if self.check:
            self.tablero.MD(self.destino, self.get1)
            self.tablero.MD(self.origen, "")

    def capturar(self):
        if self.get2:
            turno = self.get2[0]
            if self.ta != turno:
                return True
            else:
                print("Ya existe una pieza en el destino")
                self.check = False
    
    def accion(self):
        self.turno()
        self.movimiento_permitido()
        self._colision_detector()
        self.capturar()
        self.mover()
        return self.check

    def turno(self):
        if self.get1[0] == self.ta:
            self.check = True
        else:
            print("No puedes mover esta pieza en este turno")
            self.check = False

    def movimiento_permitido(self):
        return True

    def _colision_detector(self):
        rows = lista(self.origen[1], self.destino[1])
        columns = lista(self.origen[2], self.destino[2])
        lista1 = self.data[rows, columns]
        if not colisionator(lista1):
            print("Hay una pieza estorbando")
            self.check = False


class Peon(Pieza):

    def help_(self):
        if "W" == self.ta:
            if self.roworigen == 6:
                valor = (-1 ,-2)
            else:
                valor = (-1,)
        elif "B" == self.ta:
            if self.roworigen == 1:
                valor = (1, 2)
            else:
                valor = (1,)
        return valor

    def movimiento_permitido(self):

        def movimiento_(valor):
            check = 0
            if (self.rowdestino - self.roworigen) not in valor:
                print("row no permitida para el peon")
                check += 1
            if self.columnorigen != self.columndestino:
                print("columna no permitida para el peon")
                check += 1
            if check > 0:
                self.check = False

        movimiento_(self.valor)

    def _colision_detector(self):
        if self.get2:
            self.check = False
            print("Ya existe una pieza en el destino")

    def capturar(self):
        if self.get2 and self.get2[0] != self.ta:
            if self.roworigen + self.valor[0] == self.rowdestino and abs(self.columnorigen - self.columndestino) == 1:
                return True
        return False

    def accion(self):
        self.turno()
        self.valor = self.help_()
        if not self.capturar():
            self.movimiento_permitido()
            self._colision_detector()
        self.mover()
        return self.check



class Torre(Pieza):
    def movimiento_permitido(self):
        if self.roworigen == self.rowdestino or self.columnorigen == self.columndestino:
            return True
        else:
            print("Solo movimiento horizontal permitido para la Torre")
            self.check = False


class Alfil(Pieza):
    def movimiento_permitido(self):
        if self.roworigen != self.rowdestino and self.columnorigen != self.columndestino:
            return True
        else:
            print("Solo movimiento vertical permitido para el Alfil")
            self.check = False


class Caballo(Pieza):
    def movimiento_permitido(self):
        print(self.origen, self.destino)
        rows = abs(self.roworigen - self.rowdestino)
        colums = abs(self.columnorigen - self.columndestino)
        print(rows, colums)
        if (rows + colums) != 3:
            print("Movimiento no valido para el caballo")
            self.check = False

    def _colision_detector(self):
        return True

class Reina(Pieza):
    def movimiento_permitido(self):
        True

class Rey(Pieza):
    def _colision_detector(self):
        pass
    def movimiento_permitido(self):
        rows = abs(self.roworigen - self.rowdestino)
        colums = abs(self.columnorigen - self.columndestino)
        if (rows == 1 or rows == 0) and (colums == 1 or colums == 0):
            return True
        else:
            print("Movimiento no permitido para el rey")
            self.check = False