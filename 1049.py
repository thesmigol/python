STRING_1 = None
STRING_2 = None
STRING_3 = None

def read_string():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()


STRING_1 = read_string()
STRING_2 = read_string()
STRING_3 = read_string()
if STRING_1 == "vertebrado":
  if STRING_2 == "ave":
    if STRING_3 == "carnivoro":
      print("aguia")
    else:
      print("pomba")
  else:
    if STRING_3 == "onivoro":
      print("homem")
    else:
      print("vaca")
else:
  if STRING_2 == "inseto":
    if STRING_3 == "hematofago":
      print("pulga")
    else:
      print("lagarta")
  else:
    if STRING_3 == "hematofago":
      print("sanguessuga")
    else:
      print("minhoca")
