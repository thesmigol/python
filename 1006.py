c = None
b = None
a = None

def read_numeric():
  try:
    # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())


a = read_numeric()
b = read_numeric()
c = read_numeric()
print(str("MEDIA = ") + str("{:0.1f}".format((((a * 2 + b * 3) + c * 5) / 10))))