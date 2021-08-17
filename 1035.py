A = None
B = None
C = None
D = None
entrada = None
lista = None
listar_lista = None

def read_line():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()


entrada = read_line()
lista = entrada.split(" ")
A = float((lista[0]))
B = float((lista[1]))
C = float((lista[2]))
D = float((lista[3]))
if B > C and D > A and (C + D > A + B) == (C > 0 and D > 0 and (A % 2) == 0):
  print("Valores aceitos")
else:
  print("Valores nao aceitos")
