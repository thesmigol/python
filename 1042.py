LISTA2 = None
LISTA = None
ENTRADA = None

def read_line():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()

def lists_sort(my_list, type, reverse):
  def try_float(s):
    try:
      return float(s)
    except:
      return 0
  key_funcs = {
    "NUMERIC": try_float,
    "TEXT": str,
    "IGNORE_CASE": lambda s: str(s).lower()
  }
  key_func = key_funcs[type]
  list_cpy = list(my_list)
  return sorted(list_cpy, key=key_func, reverse=reverse)


ENTRADA = read_line()
LISTA2 = ENTRADA.split(" ")
LISTA = lists_sort(ENTRADA.split(" "), "NUMERIC", False)
print(int((LISTA[0])))
print(int((LISTA[1])))
print(str(int((LISTA[2]))) + str("\n"))
print(int((LISTA2[0])))
print(int((LISTA2[1])))
print(int((LISTA2[2])))
