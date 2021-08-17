import math

raio = None
SDASDASDAS = None

def read_numeric():
  try:
    # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())


raio = read_numeric()
SDASDASDAS = 4.0 / 3.0
print(str("VOLUME = ") + str("{:0.3f}".format(((SDASDASDAS * 3.14159) * (math.pow(raio, 3))))))
