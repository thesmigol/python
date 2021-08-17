entrada = None
i = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())

def upRange(start, stop, step):
  while start <= stop:
    yield start
    start += abs(step)

def downRange(start, stop, step):
  while start >= stop:
    yield start
    start -= abs(step)


entrada = read_integer()
for i in (1 <= float(entrada)) and upRange(1, float(entrada), 1) or downRange(1, float(entrada), 1):
  if (entrada % i) == 0:
    print(i)
