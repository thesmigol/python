my_10_conto = None
cem = None
cincao_pra_comprar_alimento = None
enrtada = None
galo = None
jujubinha = None
troco_do_pao = None
vintao = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())


enrtada = read_integer()
cem = enrtada % 100
galo = cem % 50
vintao = galo % 20
my_10_conto = vintao % 10
cincao_pra_comprar_alimento = my_10_conto % 5
troco_do_pao = cincao_pra_comprar_alimento % 2
jujubinha = cincao_pra_comprar_alimento % 1
print(enrtada)
print(str(enrtada / 100) + str(" nota(s) de R$ 100,00"))
print(str(cem / 50) + str(" nota(s) de R$ 50,00"))
print(str(galo / 20) + str(" nota(s) de R$ 20,00"))
print(str(vintao / 10) + str(" nota(s) de R$ 10,00"))
print(str(my_10_conto / 5) + str(" nota(s) de R$ 5,00"))
print(str(cincao_pra_comprar_alimento / 2) + str(" nota(s) de R$ 2,00"))
print(str(troco_do_pao / 1) + str(" nota(s) de R$ 1,00"))
