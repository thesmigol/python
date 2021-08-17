A = None
B = None
C = None
ENTRADA = None
i = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())


ENTRADA = read_integer()
A = 1
B = 2
C = 3
i = 4
for count in range(int(ENTRADA)):
  print(str(A) + str(str(" ") + str(str(B) + str(str(" ") + str(str(C) + str(" PUM"))))))
  A = A + i
  B = B + i
  C = C + i
