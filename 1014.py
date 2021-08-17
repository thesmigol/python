distancia = None
gasosa_kkkkkkkkk = None

def read_numeric():
  try:
    # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())


distancia = read_numeric()
gasosa_kkkkkkkkk = read_numeric()
print(str("{:0.3f}".format((distancia / gasosa_kkkkkkkkk))) + str(" km/l"))
