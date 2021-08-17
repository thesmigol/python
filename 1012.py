from numbers import Number
import math

A = None
B = None
C = None
ENTRADA = None
LISTA_CONVERT = None
PI = None

def read_line():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()


ENTRADA = read_line()
LISTA_CONVERT = ENTRADA.split(" ")
A = LISTA_CONVERT[0]
B = LISTA_CONVERT[1]
C = LISTA_CONVERT[2]
PI = 3.14159
A = (A if isinstance(A, Number) else 0) + (float(A))
B = (B if isinstance(B, Number) else 0) + (float(B))
C = (C if isinstance(C, Number) else 0) + (float(C))
print(str("TRIANGULO: ") + str("{:0.3f}".format(((A * C) / 2))))
print(str("CIRCULO: ") + str("{:0.3f}".format((PI * (math.pow(C, 2))))))
print(str("TRAPEZIO: ") + str("{:0.3f}".format((((A + B) * C) / 2))))
print(str("QUADRADO: ") + str("{:0.3f}".format((math.pow(B, 2)))))
print(str("RETANGULO: ") + str("{:0.3f}".format((A * B))))
