entrada = None
leitura = None
produtro = None
quantidade = None
total = None
valor = None

def read_line():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()


entrada = read_line()
leitura = entrada.split(" ")
produtro = int((leitura[0]))
quantidade = int((leitura[1]))
if produtro == 1:
  total = "{:0.2f}".format((4 * quantidade))
elif produtro == 2:
  total = "{:0.2f}".format((4.5 * quantidade))
elif produtro == 3:
  total = "{:0.2f}".format((5 * quantidade))
elif produtro == 4:
  total = "{:0.2f}".format((2 * quantidade))
elif produtro == 5:
  total = "{:0.2f}".format((1.5 * quantidade))
print(str("Total: R$ ") + str(total))
