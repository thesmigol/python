total = None
sapo = None
rato = None
coelho = None
quantidade = None
tipo = None
leitura = None
n_de_caso = None

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


coelho = 0
rato = 0
sapo = 0
n_de_caso = read_integer()
for count in range(int(n_de_caso)):
  leitura = read_line().split(" ")
  quantidade = leitura[0]
  tipo = leitura[1]
  quantidade = float(quantidade)
  if tipo == "S":
    sapo = sapo + quantidade
  elif tipo == "R":
    rato = rato + quantidade
  elif tipo == "C":
    coelho = coelho + quantidade
total = sapo + (coelho + rato)
print(str("Total: ") + str(str("{:0.0f}".format(total)) + str(" cobaias")))
print(str("Total de coelhos: ") + str("{:0.0f}".format(coelho)))
print(str("Total de ratos: ") + str("{:0.0f}".format(rato)))
print(str("Total de sapos: ") + str("{:0.0f}".format(sapo)))
print(str("Percentual de coelhos: ") + str(str("{:0.2f}".format(((coelho / total) * 100))) + str(" %")))
print(str("Percentual de ratos: ") + str(str("{:0.2f}".format(((rato / total) * 100))) + str(" %")))
print(str("Percentual de sapos: ") + str(str("{:0.2f}".format(((sapo / total) * 100))) + str(" %")))
