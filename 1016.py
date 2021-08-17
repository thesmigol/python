entrada = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())


entrada = read_integer()
print(str(entrada * 2) + str(" minutos"))
