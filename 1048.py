PORCENTAGEM = None
SALARIO = None
AU = None

def read_numeric():
  try:
    # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())


SALARIO = read_numeric()
if SALARIO <= 400:
  PORCENTAGEM = 0.15
  AU = SALARIO * PORCENTAGEM + SALARIO
elif SALARIO <= 800:
  PORCENTAGEM = 0.12
  AU = SALARIO * PORCENTAGEM + SALARIO
elif SALARIO <= 1200:
  PORCENTAGEM = 0.1
  AU = SALARIO * PORCENTAGEM + SALARIO
elif SALARIO <= 2000:
  PORCENTAGEM = 0.07
  AU = SALARIO * PORCENTAGEM + SALARIO
else:
  PORCENTAGEM = 0.04
  AU = SALARIO * PORCENTAGEM + SALARIO
print(str("Novo salario: ") + str("{:0.2f}".format(AU)))
print(str("Reajuste ganho: ") + str("{:0.2f}".format((PORCENTAGEM * SALARIO))))
print(str("Em percentual: ") + str(str("{:0.0f}".format((PORCENTAGEM * 100))) + str(" %")))
