A = None
B = None
C = None
ENTRADA = None
LISTA = None

def read_line():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()


ENTRADA = read_line()
LISTA = ENTRADA.split(" ")
A = float((LISTA[0]))
B = float((LISTA[1]))
C = float((LISTA[2]))
if A + B > C and C + B > A and C + C > B:
  print(str("Perimetro = ") + str(A + (B + C)))
else:
  print(str("Area = ") + str((0.5 * (A + B)) * C))
