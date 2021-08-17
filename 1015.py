import math

enrtada = None
entrada = None
jfghjhgjhg = None
kkkkkkkkkkk = None
x1 = None
x2 = None
y1 = None
y2 = None

def read_line():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()


enrtada = read_line().split(" ")
x1 = float((enrtada[0]))
y1 = float((enrtada[1]))
entrada = read_line().split(" ")
x2 = float((entrada[0]))
y2 = float((entrada[1]))
jfghjhgjhg = x2 - x1
kkkkkkkkkkk = y2 - y1
print("{:0.4f}".format((math.sqrt(((math.pow(jfghjhgjhg, 2)) + (math.pow(kkkkkkkkkkk, 2)))))))
