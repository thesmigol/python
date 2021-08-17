horas_de_trabalho = None
numero = None
salario_amem = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())

def read_numeric():
  try:
    # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())


numero = read_integer()
horas_de_trabalho = read_integer()
salario_amem = read_numeric()
print(str("NUMBER = ") + str(numero))
print(str("SALARY = U$ ") + str("{:0.2f}".format((horas_de_trabalho * salario_amem))))