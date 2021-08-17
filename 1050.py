entrada = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())


entrada = read_integer()
if entrada == 61:
  print("Brasilia")
elif entrada == 71:
  print("Salvador")
elif entrada == 11:
  print("Sao Paulo")
elif entrada == 21:
  print("Rio de Janeiro")
elif entrada == 32:
  print("Juiz de Fora")
elif entrada == 19:
  print("Campinas")
elif entrada == 27:
  print("Vitoria")
elif entrada == 31:
  print("Belo Horizonte")
else:
  print("DDD nao cadastrado")
