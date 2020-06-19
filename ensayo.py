import numpy as num

array1 = num.zeros([8, 8])
array1[6, 4] = 1  # COLISION
array1[6, 2] = 1  # PIEZA
# TORRES
A = [6, 2]  # INICI0
B = [2, 2]  # VERTICAL
C = [6, 6]  # HORIZONTAL + COLISION
D = [2, 6]  # DIAGONAL
E = [6, 0]  # HORIZONTAL

#ARRAY
print(array1)
# MOVIMIENTO

#INICIO (A) CON DESTINO (B)
def ayuda(origen, destino):
   print(origen, destino)
   rows = [origen[0], destino[0]]
   columns = [origen[1], destino[1]]
   print(rows, columns)

   def direccion(rows, columns):

       if len(set(rows)) == 1:
           return "H"

       elif len(set(columns)) == 1:
           return "B"

       else:
           print("Error, algo paso")
           raise

   def sentido(variables):
       if variables[0] < variables[1]:
           return 1
       else:
           return -1

   if direccion(rows, columns) == "H":
       valor = sentido(columns)
       lista = array1[rows[0], columns[0]:columns[1]:valor]
   else:
       valor = sentido(rows)
       lista = array1[rows[0]:rows[1]:valor, columns[0]]
   return lista
        
def torre(origen, destino):
   rowA, columnA = origen
   rowB, columnB = destino
   if rowA == rowB or columnB == columnB:
       return True
   else:
       print("MOVIMIENTO NO PERMITIDO")


def colisiontorre(origen, destino):
   lista = ayuda(origen, destino)
   print(lista)
   contador = 0
   for x in lista:
       if x:
           contador += 1
   if contador == 1:
       return True
   else:
       print("Colision")


def run():
   Check1 = torre(A, E)
   Check2 = colisiontorre(A, E)
   if Check1 and Check2:
       print("OK")

run()
