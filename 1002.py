area = None
n = None
raio = None

def read_numeric():
  try:
    # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())


raio = read_numeric()
n = 3.14159
area = n * (raio * raio)
print(str("A=") + str("{:0.4f}".format(area)))