A = None
A_LISTA = None
B = None
B_LISTA = None
QNT_A = None
QNT_B = None
VALOR_A = None
VALOR_B = None

def read_line():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()


A = read_line()
B = read_line()
A_LISTA = A.split(" ")
B_LISTA = B.split(" ")
QNT_A = A_LISTA[1]
QNT_B = B_LISTA[1]
VALOR_A = A_LISTA[2]
VALOR_B = B_LISTA[2]
print(str("VALOR A PAGAR: R$ ") + str("{:0.2f}".format(((float(VALOR_A)) * (float(QNT_A)) + (float(VALOR_B)) * (float(QNT_B))))))
