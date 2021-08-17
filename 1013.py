a = None
b = None
c = None
ganhou = None
kkkkkkkkk_eh_maior_po = None
lista = None
valores_de_entrada = None

def read_line():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()


valores_de_entrada = read_line()
lista = valores_de_entrada.split(" ")
a = int((lista[0]))
c = int((lista[2]))
b = int((lista[1]))
kkkkkkkkk_eh_maior_po = ((a + b) + (abs((a - b)))) / 2
ganhou = ((kkkkkkkkk_eh_maior_po + c) + (abs((kkkkkkkkk_eh_maior_po - c)))) / 2
print(str(ganhou) + str(" eh o maior"))
