import math

A = None
B = None
C = None
ENTRADA = None
LISTA = None
PRIMEIRO = None
SEGUNDO = None
TERCEIRO = None

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
if A >= B and A >= C:
  PRIMEIRO = A
  if B >= C:
    SEGUNDO = B
    TERCEIRO = C
  else:
    TERCEIRO = B
    SEGUNDO = C
if B >= A and B >= C:
  PRIMEIRO = B
  if A >= C:
    SEGUNDO = A
    TERCEIRO = C
  else:
    TERCEIRO = A
    SEGUNDO = C
if C >= A and C >= B:
  PRIMEIRO = C
  if A >= B:
    SEGUNDO = A
    TERCEIRO = B
  else:
    TERCEIRO = A
    SEGUNDO = B
if A == B and B == C:
  PRIMEIRO = A
  SEGUNDO = B
  TERCEIRO = C
A = PRIMEIRO
B = SEGUNDO
C = TERCEIRO
if A >= B + C:
  print("NAO FORMA TRIANGULO")
else:
  if (math.pow(A, 2)) == (math.pow(B, 2)) + (math.pow(C, 2)):
    print("TRIANGULO RETANGULO")
  if (math.pow(A, 2)) > (math.pow(B, 2)) + (math.pow(C, 2)):
    print("TRIANGULO OBTUSANGULO")
  if (math.pow(A, 2)) < (math.pow(B, 2)) + (math.pow(C, 2)):
    print("TRIANGULO ACUTANGULO")
  if A == C and A == B:
    print("TRIANGULO EQUILATERO")
  if A == B and A != C or B == C and B != A or A == C and A != B:
    print("TRIANGULO ISOSCELES")
