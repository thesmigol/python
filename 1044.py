A = None
B = None
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
A = int((LISTA[0]))
B = int((LISTA[1]))
if A > B:
  if (A % B) == 0:
    print("Sao Multiplos")
  else:
    print("Nao sao Multiplos")
if A < B:
  if (B % A) == 0:
    print("Sao Multiplos")
  else:
    print("Nao sao Multiplos")
if A == B:
  print("Sao Multiplos")
