LEITURA = None
STRING_1 = None
STRING_2 = None

def read_line():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()


LEITURA = read_line()
STRING_1 = int((LEITURA.split(" ")[0]))
STRING_2 = int((LEITURA.split(" ")[1]))
if STRING_1 >= STRING_2:
  print(str("O JOGO DUROU ") + str(str((24 - STRING_1) + STRING_2) + str(" HORA(S)")))
else:
  print(str("O JOGO DUROU ") + str(str(STRING_2 - STRING_1) + str(" HORA(S)")))
