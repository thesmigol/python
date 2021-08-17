idades = None
oi = None
quantos_anos_vc_tem = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())


quantos_anos_vc_tem = float((read_integer()))
idades = 0
oi = 0
while quantos_anos_vc_tem > 0:
  idades = idades + quantos_anos_vc_tem
  oi = oi + 1
  quantos_anos_vc_tem = read_integer()
print("{:0.2f}".format((float((idades / oi)))))
