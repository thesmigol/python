nota2 = None
nota1 = None

def read_numeric():
  try:
    # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())


nota1 = read_numeric()
nota2 = read_numeric()
print(str("MEDIA = ") + str("{:0.5f}".format(((nota1 * 3.5 + nota2 * 7.5) / 11))))
