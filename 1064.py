entrada = None
idades = None
quantos_positivos = None

def read_numeric():
  try:
    # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())


idades = 0
quantos_positivos = 0
for count in range(6):
  entrada = read_numeric()
  if entrada > 0:
    quantos_positivos = 1 + quantos_positivos
    idades = idades + entrada
print(str(quantos_positivos) + str(" valores positivos"))
print("{:0.1f}".format((idades / quantos_positivos)))
