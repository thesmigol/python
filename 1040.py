kkkkkk_recuperacao = None
nota_exame = None
soma_doida = None
nota_4 = None
nota_3 = None
nota_2 = None
nota_1 = None
notas_formadas = None
lista_notas = None

def read_line():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()

def read_numeric():
  try:
    # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())


lista_notas = read_line()
notas_formadas = lista_notas.split(" ")
nota_1 = float((notas_formadas[0]))
nota_2 = float((notas_formadas[1]))
nota_3 = float((notas_formadas[2]))
nota_4 = float((notas_formadas[3]))
soma_doida = ((nota_1 * 2 + nota_2 * 3) + (nota_3 * 4 + nota_4 * 1)) / 10
print(str("Media: ") + str("{:0.1f}".format(soma_doida)))
if soma_doida >= 7:
  print("Aluno aprovado.")
elif soma_doida < 5:
  print("Aluno reprovado.")
else:
  print("Aluno em exame.")
  nota_exame = read_numeric()
  print(str("Nota do exame: ") + str("{:0.1f}".format(nota_exame)))
  kkkkkk_recuperacao = (soma_doida + nota_exame) / 2
  if kkkkkk_recuperacao >= 5:
    print("Aluno aprovado.")
  else:
    print("Aluno reprovado.")
  print(str("Media final: ") + str("{:0.1f}".format(kkkkkk_recuperacao)))
