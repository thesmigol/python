ALCOOL = None
DISEL = None
ENTRADA = None
GASOLINA = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())


ALCOOL = 0
DISEL = 0
GASOLINA = 0
while ENTRADA != 4:
  ENTRADA = read_integer()
  if ENTRADA == 1:
    ALCOOL = ALCOOL + 1
  elif ENTRADA == 2:
    GASOLINA = GASOLINA + 1
  elif ENTRADA == 3:
    DISEL = DISEL + 1
print("MUITO OBRIGADO")
print(str("Alcool: ") + str(ALCOOL))
print(str("Gasolina: ") + str(GASOLINA))
print(str("Diesel: ") + str(DISEL))
