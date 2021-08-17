anos = None
dias = None
dias_totais = None
meses = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())


dias_totais = read_integer()
anos = dias_totais / 365
meses = (dias_totais % 365) / 30
dias = (dias_totais % 365) % 30
print(str(anos) + str(" ano(s)"))
print(str(meses) + str(" mes(es)"))
print(str(dias) + str(" dia(s)"))
