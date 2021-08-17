A = None
B = None
C = None
criar_lista = None
lista = None
NA = None
NB = None
NC = None
quantidade = None
sim = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())

def read_line():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()


quantidade = read_integer()
for count in range(int(quantidade)):
  criar_lista = read_line()
  lista = criar_lista.split(" ")
  A = float((lista[0]))
  B = float((lista[1]))
  C = float((lista[2]))
  sim = ((A * 2 + B * 3) + C * 5) / (2 + (3 + 5))
  print("{:0.1f}".format(sim))
