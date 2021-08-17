salario = None
vendas = None
funcionario = None

def read_string():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()

def read_numeric():
  try:
    # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())


funcionario = read_string()
salario = read_numeric()
vendas = read_numeric()
print(str("TOTAL = R$ ") + str("{:0.2f}".format((vendas * 0.15 + salario))))
