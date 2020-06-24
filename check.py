class Check:
    """
    Verificar todos los parametros y arrojarlos a main()
    """
    def __init__(self, ai):
        self.rows = list("ABCDEFGH")
        self.columns = list("12345678")
        self.tablero = ai.Tablero
        self.check = False
        self.escape = False

    def input_(self, respuesta):
        """Verifica coordenadas tanto de origen como de destino, no hace cambios en los datos, solo los checkea.

           Primero se encarga del input, seguido lo ingresa a un bucle y no sale hasta que cumpla los parametros:
        1) Verifica si el tamaño del input es 3
        2) Verifica si el row esta entre los valores permitidos
        3) Verifica si la column esta entre los valores permitidos
        4) Verifica si la pieza existe"""
        valor = respuesta
        if len(valor) == 3:  # 1)
            if valor[1] not in self.rows:  # 2)
                print("Row incorrecta")
            elif valor[2] not in self.columns:  # 3)
                    print("columna incorrecta")
            elif valor[0] not in "KQRBNP":
                print("pieza no valida")          # 4)
            else:
                self.check = True
                return valor
        else:
            print("Debes ingresar un valor igual a 3")

    def check_get_(self, origen):
        """Funcion que verifica si existe pieza en el destino y ademas si existe pieza en el origen.
        """
        self.get1 = self.tablero.GET(origen)
        if self.get1:
            return True
        elif not self.get1:
            print("No existe pieza en el origen")
            return False

    def check_p(self, valor, get):
        if valor[0] == get[1]:
            return True
        else:
            print("La pieza no coincide con la del tablero")
            return False

    def run(self):
        while True:
            self.origen = self.sub_run_("Que pieza desea mover?", True)
            if self.escape:
                return self.origen, None
            self.destino = self.sub_run_("Hacia donde desea moverla?")
            if self.check_get_(self.origen):
                return self.origen, self.destino

    def sub_run_(self, mensaje, enroque = False):
        while not self.check:
            valor = input(f"{mensaje}\n").upper()
            if enroque:
                if valor in ("**", "*"):
                    self.escape = True
                    return valor
            self.input_(valor)
        self.check = False
        return valor[0], self.rows.index(valor[1]), self.columns.index(valor[2])








