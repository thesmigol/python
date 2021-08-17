Y = None
X = None
lista = None

def read_line():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()


Y = 0
X = 2
while not X == Y:
  lista = read_line().split(" ")
  X = float((lista[0]))
  Y = float((lista[1]))
  if X < Y:
    print("Crescente")
  elif X > Y:
    print("Decrescente")
