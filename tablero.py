class Tablero:
    """Clase cuya unica funcion es manejar los datos del tablero.
    """
    def __init__(self):
        """Crear el diccionario de datos.

        Letras: row
        Numeros: column
        """

        self.data = {
            "A": {1: "BR", 2: "BB", 3: "BN", 4: "BK", 5: "BQ", 6: "BN", 7: "BB", 8: "BR"},
            "B": {1: "BP", 2: "BP", 3: "BP", 4: "BP", 5: "BP", 6: "BP", 7: "BP", 8: "BP"},
            "C": {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: ""},
            "D": {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: ""},
            "E": {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: ""},
            "F": {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: ""},
            "G": {1: "WP", 2: "WP", 3: "WP", 4: "WP", 5: "WP", 6: "WP", 7: "WP", 8: "WP"},
            "H": {1: "WR", 2: "WB", 3: "WN", 4: "WK", 5: "WQ", 6: "WN", 7: "WB", 8: "WR"},
        }

    def display(self):
        """
        Mostrar el tablero en pantalla.
        """

        print("     (#1) (#2) (#3) (#4) (#5) (#6) (#7) (#8)")
        for k, v in self.data.items():
            valores = ""
            for V in v.values():
                if V:
                    valores = f"{valores} [{V}]"
                else:
                    valores = f"{valores} [  ]"
            print(f"({k}) {valores}")

    def MD(self, origen: "PG1", objeto: "WP"):
        """Funcion que te permite modificar el diccionario del tablero.

        El primer parametro debe estar en el formato de coordenadas (P: Pieza, G: Row, 1: Column) y ademas tener
        siempre una longitud de 3, de lo contrario arrojara error 
        El segundo parametro  debe ser lo que desees sobrescribir

        """  
        Pieza, row, columna= tuple(origen)
        self.data[row.upper()][int(columna)] = objeto 
    
    def GET(self, origen: "PG1", bol: bool=False):
        """Funcion que te permite obtener una valor del tablero.
        origen = coordenadas
        bol = el valor lo puedes tener en bool
        """
        Pieza, row, columna = tuple(origen)
        data = self.data[row][int(columna)]
        if bol:
            return bool(data)
        return data